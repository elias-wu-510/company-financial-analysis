# Delivery Loop

Use this reference when the task is a deliverable report rather than rough notes. Follow a self-check → revise → self-check → revise → deliver loop.

## Goal

Reduce reviewer rework by forcing at least two passes:
1. draft from official sources
2. structured self-review
3. targeted revision
4. final delivery with checklist status

## Recommended loop

### Step 0 — Lock scope

Record:
- company / ticker
- requested years and period types
- language
- output format
- whether peer comparison is required
- whether charts are required

### Step 1 — Pre-draft source check

Before drafting:
- build a source-period map
- extract page-based text where evidence chains matter
- normalize labels, units, and period notation
- identify known comparability traps

Suggested tools:
- `scripts/build_source_period_map.py`
- `scripts/extract_pdf_text_with_pages.py`
- `scripts/normalize_units_and_labels.py`
- `scripts/check_metric_comparability.py`

### Step 2 — Draft the report

Produce a full draft with:
- executive summary
- source and period scope
- operating model
- revenue / segment analysis
- profitability / driver analysis
- leverage / financing analysis
- references

### Step 3 — First self-review

Run the draft through:
- source / period map check
- comparability check
- driver-analysis check
- chart readability check
- language / unit consistency check
- reviewer-sensitive check

### Step 4 — First revision

Fix P0 issues first:
- wrong period labels
- mixed metrics used as direct comparisons
- unsupported judgment claims
- leverage explanations that ignore hybrid capital or equity-base effects
- inconsistent units / labels / language

### Step 5 — Second self-review

Check again after revision. Confirm that fixes did not introduce:
- new wording drift
- new unit inconsistency
- new chart confusion
- new unsupported strategic conclusions

### Step 6 — Final revision and delivery

Polish:
- plain-language explanations
- evidence blocks
- chart titles / notes / units
- peer comparison framing if included

Deliver:
1. final report
2. checklist status summary

## Delivery rule

Do not claim "all checked" unless the final report actually passes the checks. If an item remains incomplete, mark it as partial or not done and explain the limitation.
