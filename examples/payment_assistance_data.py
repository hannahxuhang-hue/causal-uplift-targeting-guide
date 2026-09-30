"""
Synthetic data for the payment-assistance worked example (guide chapter 9.1).

Everything here is simulated. No real lender or borrower is represented.

Scenario: over two quarters, 800 small-business borrowers miss a payment.
Every borrower receives the lender's standard help (reminder letter and
a hardship-options notice). Loan officers can also make a limited number of
proactive calls offering to talk through a short-term payment plan. Which
borrowers get the call was randomized, so the test measures what the
*extra* call adds; no one was denied help.

Outcome: loan brought current (cured) within 60 days of the missed payment.
"""

from __future__ import annotations

import numpy as np
import pandas as pd

SEGMENTS = {
    # segment: (share, cure rate without call, true effect of call)
    "First missed payment, seasonal business": (0.22, 0.55, 0.17),
    "First missed payment, other": (0.38, 0.62, 0.07),
    "Repeat late (2+ missed in 12 months)": (0.28, 0.31, 0.03),
    "Already on a hardship plan": (0.12, 0.22, 0.00),
}


def generate(n: int = 800, call_share: float = 0.5, seed: int = 21) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    names = list(SEGMENTS)
    shares = np.array([SEGMENTS[s][0] for s in names])
    seg = rng.choice(names, size=n, p=shares / shares.sum())
    base = np.array([SEGMENTS[s][1] for s in seg])
    effect = np.array([SEGMENTS[s][2] for s in seg])
    called = rng.binomial(1, call_share, n)
    cured = rng.binomial(1, np.clip(base + called * effect, 0, 1))
    return pd.DataFrame({"segment": seg, "called": called, "cured_60d": cured, "true_effect": effect})


def next_quarter(n: int = 420, seed: int = 22) -> pd.DataFrame:
    """Borrowers who miss a payment next quarter (no one called yet)."""
    rng = np.random.default_rng(seed)
    names = list(SEGMENTS)
    shares = np.array([SEGMENTS[s][0] for s in names])
    seg = rng.choice(names, size=n, p=shares / shares.sum())
    return pd.DataFrame({"segment": seg, "true_effect": [SEGMENTS[s][2] for s in seg]})
