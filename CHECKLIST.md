# Outreach uplift checklist (one page)

## Before the campaign
- [ ] Eligible list frozen and dated
- [ ] Primary outcome and window chosen (e.g. applications within 60 days)
- [ ] 3–6 segments defined **in advance**
- [ ] Sample size checked: can this test detect the lift worth acting on? ([spreadsheet](spreadsheet/uplift-calculator.xlsx), "Sample size" tab)
- [ ] Randomized with `RAND()` pasted as values; assignment file saved
- [ ] Holdout excludes nothing time-critical to a borrower's welfare
- [ ] [Test plan](templates/test-plan-template.md) written and signed off

## During
- [ ] Contacts made as assigned; every override recorded
- [ ] No changes to the list or the outcome definition

## After the window closes
- [ ] Overall lift with 95% interval (analysed by *assigned* group)
- [ ] Cost per **incremental** outcome, with its range, next to the naive cost
- [ ] Lift by segment, with intervals and shrinkage
- [ ] Any segment with a negative estimate flagged for review
- [ ] Reach report: target-market / LMI / existing-customer share of contacts vs list
- [ ] [Results](templates/campaign-results-template.md) written up

## Next campaign
- [ ] Contacts allocated by shrunk lift (or lift per dollar); no contacts to zero- or negative-lift segments
- [ ] Target-market floor checked; its cost recorded
- [ ] 10–20% holdout kept within the targeted group; 5–10% of contacts spent exploring lower-ranked segments
- [ ] Targeting kept separate from eligibility and underwriting

## When outcomes mature
- [ ] Approval rate and early delinquency: contacted vs holdout, overall and by segment
- [ ] Pooled holdouts updated; segment table refreshed annually

## Before building an uplift model
- [ ] At least ~20,000 pooled randomized prospects
- [ ] Pre-outreach inputs only; no protected characteristics or obvious proxies
- [ ] Beats the segment table on a randomized hold-out, with intervals
