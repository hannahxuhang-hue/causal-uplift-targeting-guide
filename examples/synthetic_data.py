"""
Synthetic outreach data for the worked example.

Everything here is simulated. No real lender, business, or campaign is
represented. The data are sized like a small community lender: a list of
4,000 small businesses (technical-assistance alumni, past inquiries,
referral-partner lists), half of which were contacted in a randomized pilot.

The simulation builds in the four kinds of prospect the guide describes:
  * "Sure things"  - already engaged (recent inquiry, past borrowers):
                     high application rate whether or not you call.
  * "Persuadables" - e.g. technical-assistance alumni without a loan yet:
                     low baseline, but outreach makes a real difference.
  * "Lost causes"  - low baseline and little response to outreach.
  * A small group whose application rate goes *down* when contacted
    (recently declined applicants who read outreach as pressure).
"""

from __future__ import annotations

import numpy as np
import pandas as pd

FEATURES = ["years_in_business", "annual_revenue_k", "prior_ta", "prior_borrower",
            "recent_inquiry", "recently_declined", "lmi_tract", "distance_miles"]


def _prospects(n: int, rng: np.random.Generator) -> pd.DataFrame:
    lmi = rng.binomial(1, 0.58, n)
    df = pd.DataFrame({
        "years_in_business": np.round(rng.gamma(2.2, 2.4, n), 1),
        "annual_revenue_k": np.round(np.exp(rng.normal(5.4 - 0.25 * lmi, 0.8, n))),
        "prior_ta": rng.binomial(1, 0.30 + 0.12 * lmi),          # technical-assistance alumni
        "prior_borrower": rng.binomial(1, 0.22 - 0.07 * lmi),
        "recent_inquiry": rng.binomial(1, 0.16, n),
        "recently_declined": rng.binomial(1, 0.06, n),
        "lmi_tract": lmi,                                         # target-market flag
        "distance_miles": np.round(rng.gamma(2.0, 4.0, n), 1),
    })
    return df


def _probabilities(df: pd.DataFrame) -> tuple[np.ndarray, np.ndarray]:
    """Return (P(apply | not contacted), true effect of contact on P(apply))."""
    z = (-3.4 + 1.9 * df["recent_inquiry"] + 1.2 * df["prior_borrower"] + 0.2 * df["prior_ta"]
         + 0.15 * np.log1p(df["years_in_business"]) - 0.03 * df["distance_miles"])
    p0 = 1 / (1 + np.exp(-z))
    young_ish = df["years_in_business"].between(1, 8)
    tau = (0.012
           + 0.070 * (df["prior_ta"] * (1 - df["prior_borrower"]) * young_ish)
           + 0.012 * df["lmi_tract"]
           - 0.010 * df["recent_inquiry"]
           - 0.004 * df["prior_borrower"]
           - 0.045 * df["recently_declined"]
           - 0.001 * df["distance_miles"])
    return p0.values, tau.values


def generate(n: int = 4000, treat_share: float = 0.5, seed: int = 11) -> pd.DataFrame:
    """A randomized pilot: `treat_share` of the list is contacted at random."""
    rng = np.random.default_rng(seed)
    df = _prospects(n, rng)
    p0, tau = _probabilities(df)
    df["contacted"] = rng.binomial(1, treat_share, n)
    p = np.clip(p0 + df["contacted"] * tau, 0.001, 0.99)
    df["applied"] = rng.binomial(1, p)
    approve_p = np.clip(0.45 + 0.03 * np.minimum(df["years_in_business"], 8) + 0.04 * df["prior_borrower"], 0, 0.95)
    df["funded"] = df["applied"] * rng.binomial(1, approve_p)
    df["true_effect"] = tau          # known only because the data are simulated
    return df


def generate_next_list(n: int = 4000, seed: int = 12) -> pd.DataFrame:
    """The next campaign's prospect list (no one contacted yet)."""
    rng = np.random.default_rng(seed)
    df = _prospects(n, rng)
    p0, tau = _probabilities(df)
    df["true_effect"] = tau
    df["p_apply_if_not_contacted"] = p0
    return df
