# 4. Segment lift: the small lender's main tool

Once you know outreach works overall, the question is **for whom**. With a few thousand prospects, the most reliable
answer comes from a small number of **segments defined in advance**, not from a machine-learning model.

## 4.1 Choosing segments

Use what your staff already know about why people do or don't apply. Good segments:

- are defined **before** you look at the results (write them in the test plan);
- are **few**: 3 to 6, so each has a few hundred prospects;
- separate plausible **sure things** from plausible **persuadables**.

Typical segments for a small-business lender:

| Segment | Why it might differ |
|---|---|
| Already engaged (recent inquiry, past or current borrower) | Likely to apply anyway: sure things |
| Technical-assistance alumni without a loan | Know the lender, may not know they qualify: likely persuadable |
| Referral-partner lists | Varies by partner |
| Recently declined applicants | Outreach may read as pressure, or raise false hopes |
| Everyone else | Baseline |

## 4.2 Measuring lift by segment

For each segment, the same comparison as [chapter 3](03-measuring-incremental-effect.md): contacted vs holdout, with an
interval. The [spreadsheet](../spreadsheet/uplift-calculator.xlsx) ("Segment lift" tab) and `segment_lift()` do it.

From the worked example (outcome: applications within 60 days):

| Segment | Prospects | Rate, holdout | Rate, contacted | Lift | 95% interval | Shrunk lift |
|---|---|---|---|---|---|---|
| TA alumni, no loan | 957 | 3.1% | 11.7% | **+8.6** | +5.3 to +11.9 | +7.9 |
| Already engaged | 1,144 | 17.5% | 18.7% | +1.1 | −3.3 to +5.6 | +1.3 |
| Other | 1,648 | 3.7% | 4.1% | +0.4 | −1.5 to +2.3 | +0.5 |
| Recently declined | 251 | 8.4% | 4.5% | −3.9 | −10.0 to +2.3 | −2.0 |

The already-engaged segment has the **highest application rate** and would top any response-based ranking.
Its **lift** is close to zero. The TA-alumni segment has one of the lowest application rates without outreach,
and by far the largest lift.

## 4.3 Shrinkage: don't rank on luck

Small segments produce noisy estimates. The segment that looks best is often the one that got lucky. **Shrinkage**
(empirical Bayes) pulls each segment's lift toward the overall lift, by more when the segment's estimate is less
certain:

```
shrunk lift = overall lift + w × (segment lift − overall lift)
w = τ² / (τ² + se²)
```

where τ² is the estimated true variation between segments (the variance of segment lifts minus their average sampling
variance) and se is the segment's standard error. If segments don't genuinely differ, τ² is zero and every segment
shrinks to the overall lift. That is the honest answer in that case.

Rank and allocate on **shrunk lift**, and show the unshrunk lift and interval alongside so readers can see the evidence.

## 4.4 How far to trust a segment table

- A segment whose interval **excludes zero** has a demonstrated effect.
- A segment whose interval **includes zero** may still be worth contacting if its shrunk lift is positive and the
  cost is low. But treat it as unproven and keep testing it.
- A segment with a **negative** point estimate deserves attention even if the interval includes zero. Contacting
  it may be doing harm. Hold it out of the next campaign, or change the message, and test again.

## 4.5 Why not just add more segments?

Each extra split halves the data per segment. With 4,000 prospects and a 50/50 split, eight segments leave about
250 per arm per segment, and intervals of ±5 points or wider. At that point you are ranking noise. If you need finer
targeting than a handful of segments can give, you need either more data (pool campaigns) or a model
([chapter 5](05-uplift-models.md)), and a model needs even more data.
