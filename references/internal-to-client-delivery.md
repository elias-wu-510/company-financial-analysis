# Internal → Client Delivery Workflow

Use this reference when a company-analysis task should go through an internal review version first, then be converted into a clean customer-facing deliverable.

## Goal

Separate:
1. **internal working version** for validation and review
2. **client delivery version** for external presentation

This prevents internal QA language, reviewer notes, or iteration traces from leaking into the customer-facing report.

## Two-stage workflow

### Stage 1 — Internal version

Purpose:
- test methodology
- catch period / comparability / evidence issues
- surface reviewer-sensitive weaknesses
- attach checklist status honestly

Internal version may include:
- checklist artifacts
- pass / partial / fail summaries
- wording such as "still partial" or "needs reviewer-proofing"
- notes about source gaps or unresolved verification items
- explicit references to revision goals

### Stage 2 — Client delivery version

Purpose:
- provide a polished report to the client
- remove internal process traces
- preserve conclusions, evidence, and caution where needed
- present in a calm, professional, externally readable style

Client delivery version should remove:
- version-comparison language
- "this round" / "this version" / "improved from prior version" wording
- checklist language
- pass / partial / fail language
- internal QA notes
- reviewer-facing meta commentary

Client delivery version should keep:
- company and period scope
- executive summary
- business-model explanation
- core evidence-based findings
- risks, caveats, and limitations phrased naturally
- references

## Writing rules for client delivery

- Write as if the client only sees the final report.
- Do not mention prior drafts unless the user explicitly wants revision history.
- Replace internal correction language with clean analytical language.
- Keep caution, but phrase it as a professional limitation note rather than internal uncertainty tracking.

## Recommended sequence

1. Generate internal version
2. Run checklist / pass-partial-fail review
3. Fix high-priority issues
4. Freeze analytical conclusions
5. Produce a separate client delivery version
6. If charts are present, run `scripts/chart_sanity_scan.py` on the client-delivery HTML and review any warnings before export / sending
7. Export / send only the client version unless the user also wants the internal package

## Delivery package rule

Default external package:
- client report HTML / PDF

Optional internal package:
- internal report
- checklist
- pass / partial / fail summary

## Style note

The client delivery version should also follow the light-theme guidance unless the user explicitly requests another style.
