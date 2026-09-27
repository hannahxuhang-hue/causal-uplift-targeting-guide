# 7. Mission, reach, and fair lending

> Analytical guidance, not legal advice. Confirm with counsel what applies to your institution and products.

Targeting changes **who hears from you**. For a community lender, that is a mission question and a compliance
question as well as an efficiency one.

## 7.1 Check who your targeting reaches

For every campaign, compare the contacted group with the whole eligible list on:

- the share in your **target market** (for a certified CDFI, the target markets in your certification);
- the share in **low- and moderate-income census tracts** and in majority-minority tracts;
- the share of **existing customers** vs businesses new to you;
- any other groups central to your mission (women-owned, rural, immigrant-owned), where you hold that information lawfully.

`reach_report()` produces these shares.

**Why it matters for CDFIs.** A certified CDFI must direct at least **60% of both the number and the dollar volume** of
its arm's-length, on-balance-sheet financial products to its target markets (a single-year shortfall can be offset by
meeting the benchmark over three years). Outreach that drifts toward already-connected, higher-income businesses erodes
that share one campaign at a time, even when no one intends it.

## 7.2 Response models tend to drift toward the already-served

A response model contacts whoever is most likely to apply, and those are often existing customers and the
best-connected businesses. In the worked example, 33% of the response model's contacts were past borrowers, against 1%
for the segment rule. Targeting on **incremental** effect tends to move outreach toward businesses that are eligible but
not yet connected, which is often the population a community lender exists to serve.

That alignment is common but **not guaranteed**. Check it every campaign.

## 7.3 Setting a floor

If a targeting rule would push target-market reach below the level you need, set a **floor**: a minimum share of
contacts that must go to target-market prospects. `select_with_floor()` fills the floor from the highest-scoring
target-market prospects first, then fills the rest by score. The "Next campaign" tab of the spreadsheet checks the
floor.

Record the cost: how many incremental applications the floor gave up, if any. In the worked example a 65% floor cost
nothing. When it does cost something, that is the explicit, documented price of a mission commitment.

## 7.4 Fair-lending considerations

- **Don't use protected characteristics, or obvious proxies for them, as targeting inputs.** Race, ethnicity, national
  origin, sex, religion, marital status, age (with limited exceptions), and receipt of public assistance should not
  drive who is contacted. Geography, including LMI-tract status, can be a legitimate mission criterion. Review with
  counsel how you use it.
- **Regulation B, 2026.** The CFPB's April 2026 amendments (effective July 21, 2026) narrowed "discouragement" to oral or
  written statements that would lead a reasonable person to believe the creditor would deny or offer worse terms. They
  state that encouraging statements directed at one group do not discourage others who were not the intended recipients,
  and that decisions about advertising footprint and community engagement fall outside the prohibition. Disparate treatment
  remains prohibited, and state laws and the Fair Housing Act (for housing-related credit) continue to apply. Treat this as
  background, not as a conclusion about your programs.
- **Keep targeting and underwriting separate** ([chapter 6.5](06-choosing-who-to-contact.md)). Outreach order must never
  change the credit decision.
- **Watch what outreach produces.** If contacted applicants in one group are approved at much lower rates, or their loans
  go bad early, outreach may be drawing people into applications that don't serve them. The companion
  [monitoring guide](https://github.com/hannahxuhang-hue/lending-model-monitoring-guide) (chapter 5) covers approval-rate
  checks by group.

## 7.5 Record it

For each campaign, keep: the targeting rule, the reach report against the list, any floor and its cost, and the
approval and early-performance comparison once outcomes mature. Use
[`templates/campaign-results-template.md`](../templates/campaign-results-template.md).
