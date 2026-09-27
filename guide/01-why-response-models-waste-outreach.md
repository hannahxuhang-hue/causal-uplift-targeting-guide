# 1. Why "who responds" is the wrong question

A lender with limited staff time has to choose whom to contact about a loan product, a refinance, a
technical-assistance program, or a payment-assistance option. The usual approach is to contact the people
most likely to respond: past borrowers, recent inquiries, businesses that opened last month's email. A
**response model** formalises this. It predicts who applies after being contacted, and you contact the top of
the list.

The trouble is that many of those people **would have applied anyway**. Contacting them produces applications,
but not *extra* applications. The staff time is spent, the campaign report looks good, and very little changed.

## The four kinds of prospect

For any outreach, each prospect falls roughly into one of four groups:

| | **Applies if not contacted** | **Doesn't apply if not contacted** |
|---|---|---|
| **Applies if contacted** | *Sure thing*: outreach is wasted | ***Persuadable***: outreach creates the application |
| **Doesn't apply if contacted** | *Do-not-disturb*: outreach backfires | *Lost cause*: outreach is wasted |

Only **persuadables** make outreach worthwhile. A response model cannot tell them apart from sure things,
because both apply when contacted. That is exactly why it ranks sure things at the top: they have the highest
response rate.

In lending, sure things are often businesses that **already have a relationship** with the lender. Persuadables
are often businesses that are eligible and would benefit, but face a barrier outreach can remove: they don't know
the product exists, don't think they would qualify, or haven't found the time. For a community lender, persuadables
are frequently the businesses its mission is about.

## What "uplift" means

**Uplift** (also called incremental effect, or treatment effect) is the *difference outreach makes*:

```
uplift = P(applies | contacted) − P(applies | not contacted)
```

You can never observe both for the same prospect. You either contacted them or you didn't. So uplift can only
be measured by comparing **similar groups that were and weren't contacted**, and the only reliable way to get
such groups is to decide at random who gets contacted. That is the subject of [chapter 2](02-designing-the-test.md).

## The approach in this guide

A ladder, where each rung needs more data than the last:

1. **Randomize** part of your outreach and keep a holdout ([chapter 2](02-designing-the-test.md)).
2. **Measure** whether outreach works at all, with an interval ([chapter 3](03-measuring-incremental-effect.md)).
3. **Segment**: measure lift for a few pre-defined groups ([chapter 4](04-segment-lift.md)).
   *For most community lenders, this is where to stop.*
4. **Model** individual uplift, once pooled tests reach tens of thousands of prospects ([chapter 5](05-uplift-models.md)).

Then: spend the budget where lift is highest ([chapter 6](06-choosing-who-to-contact.md)), check who that reaches
([chapter 7](07-mission-reach-and-fair-lending.md)), and keep measuring ([chapter 8](08-keep-a-holdout.md)).
[Chapter 9](09-other-uses.md) applies the same method to payment-assistance outreach and program referrals.

## Why this matters more for small lenders

Large lenders can afford to waste some outreach. A lender with three loan officers cannot. In the
[worked example](../examples/walkthrough.ipynb), the same 1,000 contacts produce about **three times as many extra
applications** when chosen by measured lift as when chosen at random, and **about twice as many** as when chosen
by a response model.
