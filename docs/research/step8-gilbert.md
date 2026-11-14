# Step 8: Gilbert, AZ (2026-11-14, America/Denver)

**Rows:** 2 (two Post Offices). Fourth city of the approved Arizona batch (Phoenix, Tucson, Mesa, Gilbert, Chandler; one city at a time). Gilbert is legally a town and an incorporated place in Maricopa County (Census "Gilbert town", GEOID 0427400; county Maricopa County, GEOID 04013; SUMLEV 162), not a consolidated city-county. Only addresses inside Gilbert town whose official printed city is Gilbert are listed. No businesses were contacted. Brands in scope for non-Colorado states: USPS and Walmart Supercenters only. This PR is USPS only; Walmart rows are omitted because the official walmart.com store locator was unavailable.

**Counts:** 2 locations; 2 money order; 0 check cashing; 0 bill pay; 0 prepaid reload. Labels on the hub: 0 Open evenings, 2 Open weekends. The money-orders page lists 2. The after-hours page lists 2 (Gilbert and Val Vista, both Saturday hours). Neither listed office has a weekday close after 17:00. No check-cashing or bill-pay page (zero listings). Hold: Higley. In-town, not listed (no money-order tags): Fiesta Annex and Gilbert Roadrunner Annex.

Hours are copied as published and are local Gilbert time (Arizona Time, Mountain Standard Time; Arizona does not observe daylight saving). `last_verified` is 2026-11-14 on every row. `verification_status` is `verified_official_locator` on every row.

## Method

- **USPS:** official USPS Location Finder API (`tools.usps.com`, `requestType` po), queried with curl the same way as Phoenix, Tucson, and Mesa. Pass 1: 5 and 15 miles around every official Gilbert ZIP (7 codes listed for Gilbert, AZ by ZIP-Codes.com from USPS data last updated 2026-11-01) and nearby official ZIPs for Mesa, Chandler, Higley, and Queen Creek (21 ZIPs, 42 queries, 40 unique records). Pass 2: 1, 2, 3, 10, and 20 mile widenings on edge Gilbert and fringe ZIPs (30 queries, 2 added records: Coolidge and a far Phoenix office). Total 42 records (`step8-browser/gilbert-usps-locator-2026-11-14.jsonl`). Official location pages and both-file geocodes for all 42 were already on file from earlier Valley research (all HTTP 200, page `poDetail` matched the API). Retail hours means the BUSINESS block only. Full notes: `step8-browser/gilbert-usps-2026-11-14.md`.
- **Walmart:** not collected. The official walmart.com store locator was unavailable, so no Walmart rows are in this PR.
- **Town limits:** U.S. Census Bureau Geocoder, address endpoint and coordinates endpoint, Public_AR_Current / Current_Current and Public_AR_Census2020 / Census2020_Census2020, Incorporated Places + CDPs + Counties. All 42 addresses and all 42 official locator map points on both benchmarks (`step8-browser/gilbert-usps-geocoder-2026-11-14.jsonl`). OpenStreetMap was not used.
- Fees reuse existing rows in `data/providers/fees.csv`. No new fee rows or brands. Coordinates for USPS rows are in the notes column (lat/lng columns stay blank, as in every city CSV).

## USPS (2 listed)

Both offices have printed city Gilbert and address plus official map point in Gilbert town on both Census files. Both list Domestic and Inquiry Money Orders.

Hold: Higley, documented in the city-page "not listed" section and in `gilbert-usps-2026-11-14.md`. In-town exclusions: Fiesta Annex and Gilbert Roadrunner Annex.

## Walmart Supercenters

Not collected in this PR. The official walmart.com store locator was unavailable. No Walmart rows, no Walmart fee citations, and no Neighborhood Markets.

## Site changes in this PR

- New `data/locations/gilbert.csv` and `/gilbert/`, `/gilbert/money-orders/`, and `/gilbert/after-hours/` pages.
- Gilbert added under the existing Arizona heading on the home "Start here" list and on `/cities/`, after Mesa. Home and `/cities/` meta descriptions now say "Phoenix, Tucson, Mesa, and Gilbert, Arizona". No other city CSV or page changed except those meta and list lines. Colorado order is unchanged.
