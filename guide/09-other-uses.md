# 9. The same method beyond marketing

The question "does contacting this person make a difference, and for whom?" comes up throughout a community lender's
work. The method in chapters 2–8 applies unchanged. Only the outcome and the ethics of the holdout differ.

## 9.1 Early-delinquency and payment-assistance outreach

**Question:** which borrowers does a proactive call (a reminder, an offer to restructure, a referral to counselling) help
stay current?

- **Outcome:** 30+ days past due at 90 days after the call; or cured within 60 days for those already late.
- **Sure things** here are borrowers who would have paid anyway. **Persuadables** are borrowers for whom a timely
  conversation prevents a missed payment.
- **Holdout ethics.** Do not withhold help from borrowers already in distress. Test **timing or type** instead: a call at
  the first missed payment vs the standard schedule; a call vs a text; with vs without a restructuring offer. Everyone gets
  help, and the test tells you which help works best for whom.
- **Link to monitoring.** Early-delinquency signals from the companion
  [monitoring guide](https://github.com/hannahxuhang-hue/lending-model-monitoring-guide) (chapter 3) identify *who is at
  risk*. Uplift tells you *who a call will help*. They are different lists. The highest-risk borrowers may not be the ones
  a call changes.

**Worked example.** [`examples/payment_assistance_walkthrough.ipynb`](../examples/payment_assistance_walkthrough.ipynb)
follows 800 small-business borrowers who missed a payment (synthetic data). Everyone gets the standard reminder and
hardship notice; which borrowers also get a proactive call is randomized. The overall effect of the call is not
distinguishable from zero, but the segment table shows a large effect for seasonal businesses on their first missed
payment and none for repeat-late borrowers, the highest-risk group. Directing next quarter's 120 calls by measured lift
cures about twice as many loans as calling at random, and several times more than calling the highest-risk borrowers
first.

## 9.2 Technical-assistance and program referrals

**Question:** which clients, when referred to a TA program or financial-coaching session, go on to enrol, complete it, or
become loan-ready?

- **Outcome:** enrolment, completion, or an application within 6 months.
- **Holdout:** with a waiting list, randomizing the *order* of invitation is a natural and fair design.

## 9.3 Renewal and repeat-borrower outreach

**Question:** which borrowers near the end of a loan benefit from a proactive renewal conversation?

- Existing borrowers are often sure things. Measure before spending loan-officer time on them.

## 9.4 What stays the same

In every case: randomize, measure overall lift with an interval, measure a few pre-defined segments with shrinkage,
allocate by lift, check reach, and keep a holdout.
