# External Retrieval Strategy

Use this reference when the analysis needs broader source coverage, such as official IR pages, results announcements, press releases, HKEX disclosures, or peer-company materials.

## Goal

Use external search to find the right sources faster without weakening source quality.

## Core rule

Use external search for discovery. Use official documents for evidence.

Do not treat a search snippet, media summary, or third-party article as the final basis for a key financial conclusion when an official filing or official IR source is available.

## Recommended source hierarchy

1. Company investor-relations hub
2. Official annual / interim / quarterly report PDFs
3. Official results announcements and press releases
4. Exchange disclosures (for example HKEX filings)
5. Official company presentations or transcripts
6. Third-party summaries only as a fallback discovery aid

## What external search is especially useful for

- Find the company IR hub quickly
- Find the latest annual or interim report PDF
- Find results announcements or press releases that explain changes in plain language
- Find peer-company IR pages for comparison work
- Confirm whether a filing or presentation exists before searching manually

## What must still be verified in official sources

- revenue, EBIT, EBITDA, profit, debt, cash, equity, leverage, and interest cover
- segment definitions and whether buckets are parent or child categories
- covered period versus disclosure date
- treatment of hybrid instruments such as perpetual capital securities
- management commentary that is used to support a conclusion

## Query patterns

Prefer targeted queries such as:

- `site:company-domain investor relations annual report 2024 pdf`
- `site:company-domain interim results 2025 pdf`
- `site:hkexnews.hk <company name> results announcement`
- `site:company-domain perpetual capital securities announcement`
- `site:company-domain investor presentation pdf`
- `site:peer-company-domain investor relations annual report pdf`

For MTR-like cases, useful examples include:
- `site:mtr.com.hk investor annual report 2024 pdf`
- `site:mtr.com.hk interim results 2025 pdf`
- `site:hkexnews.hk 港鐵 0066 業績公告`

## Peer comparison rule

When doing peer comparison:
1. use external search to find peer IR pages
2. pull metrics from official peer filings
3. normalize units, period labels, and metric definitions before comparing
4. do not compare peers on a mixed FY / H1 / TTM basis without an explicit warning

## Safety rule

If external search finds a useful third-party summary but the official filing cannot be located quickly, treat the third-party source as a pointer, not as the final citation for material claims.
