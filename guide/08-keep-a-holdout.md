# 8. Keep a holdout, and keep learning

A targeting rule measured once goes stale. Your list changes, your products change, the local economy changes, and a
segment that responded last year may not respond this year. The only way to know is to keep measuring.

## 8.1 A holdout in every campaign

Once you are targeting, hold back a **small random share (10–20%) of the prospects you would have contacted**. It costs
a little outreach each time, and in return you get:

- continuing proof that outreach still works for the targeted segments;
- an early signal when it stops working;
- evidence of impact to show funders and boards.

One campaign's holdout is small. **Pool holdouts across campaigns**, with the same randomization rule each time:

| Targeted prospects (pooled) | 15% holdout | Smallest detectable lift (base rate 5%) |
|---|---|---|
| 1,000 (one campaign) | 150 | ~5.8 points |
| 2,000 | 300 | ~4.0 points |
| 4,000 | 600 | ~2.8 points |

## 8.2 Explore as well as exploit

If you only ever contact the top segments, you never learn whether the others have changed. Put a small share of
contacts (e.g. 5–10%) into **randomly chosen prospects from lower-ranked segments**, and measure their lift too. This is
how a segment that was "lost causes" last year gets noticed when a new product makes it persuadable.

## 8.3 Refresh the segment table

- **Every campaign:** update lift for the targeted segments from the pooled holdout.
- **Every year** (or after a product, pricing, or eligibility change): re-estimate all segments from pooled randomized data,
  and review whether the segment definitions still make sense.
- **If a targeted segment's lift falls** so that its interval includes zero across two campaigns, treat it like a monitoring
  alert: investigate before continuing to spend on it.

## 8.4 Monitoring a targeting model

If you use an uplift model ([chapter 5](05-uplift-models.md)), monitor it like any other model. Data quality and input
stability checks from the companion
[Lending Model Monitoring Guide](https://github.com/<your-username>/lending-model-monitoring-guide) apply directly. The
**performance** check is the pooled holdout: does the model's top slice still show more lift than the segment table's?

## 8.5 Documentation

Keep, per campaign, the [test plan](../templates/test-plan-template.md) written before launch and the
[results](../templates/campaign-results-template.md) written after. Two pages each is plenty. Over a few years they
become an evidence base that few small lenders have: what outreach works, for whom, and at what cost.
