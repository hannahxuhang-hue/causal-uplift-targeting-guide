# 6. Choosing who to contact

With segment lifts (or model scores) in hand, the next campaign is an allocation problem: **a fixed contact budget,
spent where it creates the most additional applications or funded loans.**

## 6.1 The basic rule

1. Rank segments (or prospects) by **shrunk lift**, highest first.
2. Allocate contacts down the ranking until the budget runs out.
3. **Don't contact segments with zero or negative lift**, even if budget remains. Unspent outreach capacity can go to
   something else: servicing, technical assistance, follow-up on applications.

The "Next campaign" tab of the [spreadsheet](../spreadsheet/uplift-calculator.xlsx) does this and reports expected
incremental applications.

## 6.2 When contacts cost different amounts

If some prospects are more expensive to reach (an in-person visit vs a call, or a translated mailing), rank by
**lift per dollar** instead of lift:

```
priority = shrunk lift ÷ cost per contact
```

A segment with half the lift at a quarter of the cost comes first.

## 6.3 When the value of an outcome differs

If what matters is funded loans rather than applications, or dollar volume, use lift on that outcome. It is usually
noisier, so you may need to pool campaigns first. A reasonable compromise: rank on application lift (more data), then
check the funded-loan lift by segment once outcomes are in ([chapter 3.3](03-measuring-incremental-effect.md)).

## 6.4 Results from the worked example

The next campaign has 4,000 prospects and capacity for 1,000 contacts at $30 each. True incremental applications are
known because the data is simulated:

| Method used to choose the 1,000 | True incremental applications | Outreach cost per incremental application | Past borrowers among contacts |
|---|---|---|---|
| Segment rule (shrunk lift) | **64** | **$465** | 1% |
| T-learner | 47 | $637 | 20% |
| Response model | 32 | $951 | 33% |
| Random | 22 | $1,385 | 19% |

Same budget, three times the effect of random outreach, and about twice that of a response model. The response model
spends a third of its contacts on past borrowers, who were mostly applying anyway.

## 6.5 Keep eligibility and credit decisions separate

Outreach targeting decides **whom you contact first**. It must not decide **who may apply** or **how an application is
underwritten**. Every applicant, contacted or not, goes through the same credit process. Keeping the two separate matters
for fairness and for the regulatory reasons in [chapter 7](07-mission-reach-and-fair-lending.md). It also keeps the
measurement honest.
