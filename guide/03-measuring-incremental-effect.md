# 3. Did outreach work at all?

Before asking *whom* to target, ask whether outreach changes anything. Many campaigns never answer this.

## 3.1 The comparison

```
lift = outcome rate (contacted) − outcome rate (holdout)
```

with a 95% interval:

```
standard error = √( p₁(1−p₁)/n₁ + p₀(1−p₀)/n₀ )
interval       = lift ± 1.96 × standard error
```

The [spreadsheet](../spreadsheet/uplift-calculator.xlsx) ("Test result" tab) and `lift_with_ci()` compute both.

**Reading it:**

- **Interval entirely above zero:** outreach works. The point estimate is your best guess of how much.
- **Interval includes zero:** you have not shown an effect. That is not the same as showing *no* effect. Check the
  minimum detectable lift from [chapter 2](02-designing-the-test.md): if it was large, the test simply could not tell.
- **Interval entirely below zero:** outreach is reducing applications. Rare overall, but it happens in
  particular segments ([chapter 4](04-segment-lift.md)).

## 3.2 Cost per incremental outcome

Most campaign reports divide cost by outcomes among those contacted. That credits outreach with everything the
contacted group did, including what they would have done anyway.

The honest measure:

```
cost per incremental outcome = cost per contact ÷ lift
```

From the [worked example](../examples/walkthrough.ipynb), where each contact costs $30:

| | |
|---|---|
| Funded-loan rate, contacted | 6.35% |
| Funded-loan rate, holdout | 4.62% |
| Lift | +1.74 points (interval 0.33 to 3.14) |
| Naive cost per funded loan (contacted) | **$472** |
| Cost per **incremental** funded loan | **$1,729** (range $954 to $9,192) |
| Share of contacted-and-funded loans that would have happened anyway | **73%** |

Both numbers are "true". But only the second tells you what outreach bought. It is the number to compare with other
uses of loan-officer time, and to report to funders who pay for outreach.

Report the range, not just the point. With a lift interval that starts close to zero, the worst-case cost can be very
high. That is a reason to run a larger test, not to hide the range.

## 3.3 Check what kind of applications outreach created

An extra application is only good if it becomes a sound loan. Once outcomes mature, compare contacted vs holdout on:

- approval rate among applicants;
- early delinquency among funded loans (the early-warning check in the companion
  [monitoring guide](https://github.com/<your-username>/lending-model-monitoring-guide));
- loan size.

If outreach pulls in applications that are mostly declined, the cost per incremental *funded* loan will show it.
If it pulls in loans that go bad early, it is creating harm for borrowers as well as losses for the lender.
