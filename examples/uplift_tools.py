"""
Tools for measuring and targeting the incremental effect of outreach.

Plain functions over pandas/numpy/scikit-learn. Each maps to a chapter of the
guide (see ../guide/). Written for randomized tests of a few thousand
prospects, which is the scale of a small lender's campaign.
"""

from __future__ import annotations

import numpy as np
import pandas as pd
from scipy import stats


# ---------------------------------------------------------------------------
# Chapter 2: designing the test
# ---------------------------------------------------------------------------

def sample_size_per_group(p_control: float, lift: float, alpha: float = 0.05, power: float = 0.80,
                          holdout_share: float = 0.5) -> dict:
    """Prospects needed to detect an absolute lift in application rate.

    Two-sided test of two proportions. `holdout_share` is the share of the list
    left uncontacted; smaller holdouts need a larger total list.
    """
    p1 = p_control + lift
    z_a, z_b = stats.norm.ppf(1 - alpha / 2), stats.norm.ppf(power)
    k = (1 - holdout_share) / holdout_share          # contacted per holdout prospect
    var = p_control * (1 - p_control) + p1 * (1 - p1) / k
    n_holdout = int(np.ceil((z_a + z_b) ** 2 * var / lift ** 2))
    n_contacted = int(np.ceil(n_holdout * k))
    return {"holdout": n_holdout, "contacted": n_contacted, "total": n_holdout + n_contacted}


def minimum_detectable_lift(n_total: int, p_control: float, alpha: float = 0.05, power: float = 0.80,
                            holdout_share: float = 0.5) -> float:
    """Smallest absolute lift a test of this size can reliably detect."""
    n0, n1 = n_total * holdout_share, n_total * (1 - holdout_share)
    z = stats.norm.ppf(1 - alpha / 2) + stats.norm.ppf(power)
    lift = 0.01
    for _ in range(50):                               # fixed-point on the variance
        p1 = p_control + lift
        lift = z * np.sqrt(p_control * (1 - p_control) / n0 + p1 * (1 - p1) / n1)
    return float(lift)


# ---------------------------------------------------------------------------
# Chapter 3: measuring the incremental effect
# ---------------------------------------------------------------------------

def lift_with_ci(df: pd.DataFrame, treat_col: str, outcome_col: str, level: float = 0.95) -> dict:
    """Difference in outcome rate between contacted and holdout, with a Wald interval."""
    t, c = df[df[treat_col] == 1][outcome_col], df[df[treat_col] == 0][outcome_col]
    p1, p0, n1, n0 = t.mean(), c.mean(), len(t), len(c)
    diff = p1 - p0
    se = np.sqrt(p1 * (1 - p1) / n1 + p0 * (1 - p0) / n0)
    z = stats.norm.ppf(0.5 + level / 2)
    pval = 2 * stats.norm.sf(abs(diff) / se) if se > 0 else np.nan
    return {"n_contacted": n1, "n_holdout": n0, "rate_contacted": p1, "rate_holdout": p0,
            "lift": diff, "ci_low": diff - z * se, "ci_high": diff + z * se,
            "relative_lift": diff / p0 if p0 > 0 else np.nan, "p_value": pval,
            "incremental_per_1000": 1000 * diff}


def cost_per_incremental(lift: float, ci_low: float, ci_high: float, cost_per_contact: float) -> dict:
    """Outreach cost per extra application (or funded loan) the outreach caused."""
    f = lambda x: cost_per_contact / x if x > 0 else np.inf
    return {"point": f(lift), "best_case": f(ci_high), "worst_case": f(ci_low)}


# ---------------------------------------------------------------------------
# Chapter 4: segment-level lift (the small-lender workhorse)
# ---------------------------------------------------------------------------

def segment_lift(df: pd.DataFrame, segment_col: str, treat_col: str, outcome_col: str,
                 shrink: bool = True) -> pd.DataFrame:
    """Lift by pre-defined segment, with intervals and optional shrinkage.

    Shrinkage (empirical Bayes) pulls noisy segment estimates toward the overall
    lift in proportion to their uncertainty, so a small segment with a lucky
    result is not ranked first on luck alone.
    """
    overall = lift_with_ci(df, treat_col, outcome_col)["lift"]
    rows = []
    for seg, g in df.groupby(segment_col, observed=True):
        r = lift_with_ci(g, treat_col, outcome_col)
        se = (r["ci_high"] - r["ci_low"]) / (2 * 1.96)
        rows.append({"segment": seg, "prospects": len(g), "rate_holdout": r["rate_holdout"],
                     "rate_contacted": r["rate_contacted"], "lift": r["lift"],
                     "ci_low": r["ci_low"], "ci_high": r["ci_high"], "se": se})
    out = pd.DataFrame(rows)
    if shrink and len(out) > 1:
        # Method-of-moments estimate of true between-segment variance.
        tau2 = max(np.var(out["lift"], ddof=1) - np.mean(out["se"] ** 2), 0.0)
        w = tau2 / (tau2 + out["se"] ** 2) if tau2 > 0 else 0.0
        out["lift_shrunk"] = overall + w * (out["lift"] - overall)
    return out.drop(columns="se")


# ---------------------------------------------------------------------------
# Chapter 5: uplift models
# ---------------------------------------------------------------------------

def _base_model(seed: int = 0):
    from sklearn.ensemble import HistGradientBoostingClassifier
    return HistGradientBoostingClassifier(max_depth=3, learning_rate=0.05, max_iter=150,
                                          min_samples_leaf=40, l2_regularization=1.0, random_state=seed)


def fit_t_learner(train: pd.DataFrame, features: list[str], treat_col: str, outcome_col: str, seed: int = 0):
    """Two-model approach: one model for contacted, one for holdout.
    Uplift = P(outcome | contacted) - P(outcome | not contacted)."""
    m1 = _base_model(seed).fit(train.loc[train[treat_col] == 1, features], train.loc[train[treat_col] == 1, outcome_col])
    m0 = _base_model(seed).fit(train.loc[train[treat_col] == 0, features], train.loc[train[treat_col] == 0, outcome_col])
    return lambda X: m1.predict_proba(X[features])[:, 1] - m0.predict_proba(X[features])[:, 1]


def fit_transformed_outcome(train: pd.DataFrame, features: list[str], treat_col: str, outcome_col: str,
                            seed: int = 0):
    """Class-transformation approach (Jaskowski & Jaroszewicz, 2012), for 50/50 randomization.
    Z = 1 if (contacted and applied) or (not contacted and did not apply). Then uplift = 2 P(Z=1) - 1."""
    z = (train[treat_col] == train[outcome_col]).astype(int)
    m = _base_model(seed).fit(train[features], z)
    return lambda X: 2 * m.predict_proba(X[features])[:, 1] - 1


def fit_response_model(train: pd.DataFrame, features: list[str], treat_col: str, outcome_col: str, seed: int = 0):
    """The conventional approach, for comparison: who applies when contacted?"""
    m = _base_model(seed).fit(train.loc[train[treat_col] == 1, features], train.loc[train[treat_col] == 1, outcome_col])
    return lambda X: m.predict_proba(X[features])[:, 1]


def qini_curve(y: np.ndarray, t: np.ndarray, score: np.ndarray, n_points: int = 20) -> pd.DataFrame:
    """Qini curve on randomized hold-out data (Radcliffe, 2007).

    For the top x% by score: incremental outcomes = Y_contacted - Y_holdout * (N_contacted / N_holdout).
    A good targeting score rises steeply at first. A random order gives a straight line.
    """
    order = np.argsort(-score)
    y, t = np.asarray(y)[order], np.asarray(t)[order]
    n = len(y)
    rows = [{"share_targeted": 0.0, "incremental": 0.0}]
    for k in np.linspace(n / n_points, n, n_points).astype(int):
        yt, tt = y[:k], t[:k]
        n_t, n_c = tt.sum(), (1 - tt).sum()
        inc = yt[tt == 1].sum() - (yt[tt == 0].sum() * n_t / n_c if n_c > 0 else 0)
        rows.append({"share_targeted": k / n, "incremental": inc})
    return pd.DataFrame(rows)


def qini_coefficient(curve: pd.DataFrame) -> float:
    """Area between the Qini curve and the random-targeting line, as a share of total incremental outcomes."""
    x, y = curve["share_targeted"].values, curve["incremental"].values
    random_line = x * y[-1]
    return float(np.trapezoid(y - random_line, x) / abs(y[-1])) if y[-1] != 0 else np.nan


def policy_value(df: pd.DataFrame, score: np.ndarray, share: float, treat_col: str, outcome_col: str,
                 n_boot: int = 500, seed: int = 0) -> dict:
    """Estimated extra outcomes per 1,000 contacts if you contact the top `share` by score.

    Estimated on randomized hold-out data: within the top `share`, compare
    contacted vs holdout. Bootstrapped interval, because with a few hundred
    prospects in the top slice the estimate is noisy.
    """
    rng = np.random.default_rng(seed)
    top = df.assign(_s=score).nlargest(int(len(df) * share), "_s")

    def est(d):
        a, b = d[d[treat_col] == 1][outcome_col], d[d[treat_col] == 0][outcome_col]
        return 1000 * (a.mean() - b.mean())

    point = est(top)
    boots = [est(top.sample(len(top), replace=True, random_state=int(rng.integers(1e9)))) for _ in range(n_boot)]
    return {"incremental_per_1000_contacts": point,
            "ci_low": float(np.percentile(boots, 2.5)), "ci_high": float(np.percentile(boots, 97.5))}


# ---------------------------------------------------------------------------
# Chapter 6: choosing who to contact
# ---------------------------------------------------------------------------

def select_with_floor(df: pd.DataFrame, score: np.ndarray, budget: int, flag_col: str, floor: float) -> np.ndarray:
    """Pick `budget` prospects by score, while making sure at least `floor`
    of them have `flag_col` == 1 (e.g. target-market or LMI-tract businesses).

    Fills the floor with the highest-scoring flagged prospects first, then
    fills the rest by score from everyone left.
    """
    d = df.assign(_s=score, _i=np.arange(len(df)))
    need = int(np.ceil(budget * floor))
    flagged = d[d[flag_col] == 1].nlargest(need, "_s")["_i"].values
    rest = d[~d["_i"].isin(flagged)].nlargest(budget - len(flagged), "_s")["_i"].values
    chosen = np.zeros(len(df), dtype=bool)
    chosen[np.concatenate([flagged, rest])] = True
    return chosen


def reach_report(df: pd.DataFrame, chosen: np.ndarray, flag_cols: list[str]) -> dict:
    """Share of contacts with each flag, vs the share on the whole list."""
    out = {"contacts": int(chosen.sum())}
    for c in flag_cols:
        out[f"{c}_share_of_contacts"] = float(df.loc[chosen, c].mean())
        out[f"{c}_share_of_list"] = float(df[c].mean())
    return out
