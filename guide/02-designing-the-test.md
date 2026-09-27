# 2. Designing the test

Everything in this guide rests on one thing: **a randomized holdout**. Some prospects who would have been
contacted are, by chance, not contacted this time. Comparing them with those who were contacted is the only
reliable way to measure what outreach does.

## 2.1 Why randomize?

Any other comparison is biased. Businesses your staff *chose* to contact differ from those they didn't:
more engaged, closer to the office, better known. Comparing their application rates mixes the effect of
outreach with those differences. Comparing "this year's campaign" with "last year" mixes it with everything
else that changed.

Random assignment is what makes the two groups alike on everything, including things you can't measure.

## 2.2 How to randomize (in a spreadsheet)

1. Put the full eligible list in a sheet. Freeze it: no additions or removals after this point.
2. Add a column `=RAND()`, then copy and **paste as values** so it stops changing.
3. Sort by that column. The first *x*% are the holdout; the rest are contacted.
4. Save this assignment file with the date. It is your test record.

If staff are allowed to override the assignment ("I know this business, I'll call anyway"), record every override.
Analyse by *assigned* group, not by who was actually contacted. This is called intention-to-treat, and it keeps
the comparison fair.

## 2.3 What to measure

- **Primary outcome:** the one decision will rest on. Usually **applications** (quicker to observe) or
  **funded loans** (closer to what matters). Pick it before the campaign starts.
- **Window:** a fixed period after contact, e.g. 60 days, the same for both groups.
- **Secondary outcomes:** funded amount, early performance of funded loans (so a campaign that creates extra
  *bad* loans is noticed), and enrolment in technical assistance.

Match outcomes to prospects by a stable ID, not by name.

## 2.4 How big a test?

The test must be large enough to detect the effect you care about. Otherwise it produces noise, and noise gets
read as a finding.

Inputs: the application rate **without** outreach (from past campaigns, or a reasonable guess), and the
**smallest lift worth acting on**. The [spreadsheet](../spreadsheet/uplift-calculator.xlsx) ("Sample size" tab) and
`sample_size_per_group()` do the arithmetic. Typical numbers:

| Rate without outreach | Lift to detect | Holdout share | Total list needed |
|---|---|---|---|
| 4% | +2 points | 50% | ~3,700 |
| 4% | +2 points | 20% | ~5,200 |
| 4% | +4 points | 50% | ~1,100 |
| 10% | +3 points | 50% | ~3,500 |

(80% power, 5% significance.)

If your list is smaller than the table says:

- **pool** the test across two or three campaigns, keeping the same randomization rule;
- test a **bigger change** (a personal call vs no contact, rather than two versions of a letter);
- or accept that this test can only detect large effects, and say so in the results.

## 2.5 Holdout size

A 50/50 split is the most efficient. A smaller holdout (10–30%) contacts more people now but needs a larger list for
the same precision. For a **first** test, 30–50% is usually right. Once you know outreach works and are targeting it,
keep a smaller holdout in every campaign ([chapter 8](08-keep-a-holdout.md)).

## 2.6 Is a holdout fair to the people held out?

The holdout is not denied credit. They can still apply through every normal channel, and they are simply not
called or mailed *this round*. Outreach capacity is limited anyway, so someone is always not contacted. Randomizing
decides who fairly, and produces the evidence that later lets you reach *more* of the businesses outreach actually
helps.

Keep holdouts away from anything time-critical to a borrower's welfare. For example, don't withhold hardship or
payment-assistance outreach from borrowers already in distress ([chapter 9](09-other-uses.md) covers how to test there).

## 2.7 Write the plan down first

Before the campaign, record: the list and its date, the randomization, the primary outcome and window, the
segments you will look at, and the minimum lift the test can detect. Use
[`templates/test-plan-template.md`](../templates/test-plan-template.md). Fixing these in advance stops the results
from being re-cut until something looks significant.
