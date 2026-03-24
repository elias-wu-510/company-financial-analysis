# Source Period Map

Use this reference when the task spans multiple years, mixed disclosure dates, or a combination of annual, interim, quarterly, and point-in-time balance-sheet data.

## Goal

Build a source map before analysis so the report does not confuse:
- financial year
- disclosure year
- interim versus full-year data
- flow metrics versus point-in-time balance-sheet metrics

## Minimum output fields

For each source, record:
- document name
- issuer
- disclosure date
- covered period
- period type: FY / H1 / Quarter / TTM / Point-in-time
- currency
- unit
- notes on what the document is safe to support

## Suggested workflow

1. List all official filings used for the task.
2. For each filing, record the covered period separately from the disclosure date.
3. Mark whether the filing supports income-statement analysis, balance-sheet analysis, financing commentary, or management outlook.
4. Reject any attempt to label a later disclosure date as if it were a later operating period.
5. Before charting, confirm that all series in the same exhibit share a compatible period type.

## Tooling note

Use `scripts/build_source_period_map.py` to create a first-pass JSON map from text or HTML files. Treat the script output as a draft to verify, not as final truth.
