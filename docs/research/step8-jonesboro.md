# Step 8: Jonesboro, AR (2026-11-15, America/Denver)

**Rows:** 3 (three Post Offices). Fifth city of the approved Arkansas batch (Little Rock, Fayetteville, Fort Smith, Springdale, Jonesboro; one city at a time). Jonesboro is an incorporated city in Craighead County (Census "Jonesboro city", GEOID 0535710; county Craighead County, GEOID 05031), not a consolidated city-county. Only addresses inside Jonesboro city whose official printed city is Jonesboro are listed. No businesses were contacted. Brands in scope for non-Colorado states: USPS and Walmart Supercenters only. This PR is USPS only; Walmart rows are omitted because the official walmart.com store locator was unavailable.

**Counts:** 3 locations; 3 money order; 0 check cashing; 0 bill pay; 0 prepaid reload. Labels on the hub: 0 Open evenings, 1 Open weekends. The money-orders page lists 3. The after-hours page lists 1 (Caraway Jonesboro, Saturday 09:00-12:00). The weekday close at that office is 17:00, which does not count as Open evenings. No check-cashing or bill-pay page (zero listings). Hold: State University. In-city, not listed: Jonesboro (1368525) at 2404 Race St, and Northeast Arkansas (1473451) and Jonesboro AR SDC (1599137) at 3405 Moore Rd.

Hours are copied as published and are local Jonesboro time (Central Time). Nettleton’s weekday midday split is stored with commas (`09:00-13:00,14:00-16:00`). `last_verified` is 2026-11-15 on every row. `verification_status` is `verified_official_locator` on every row.

## Method

- **USPS:** official USPS Location Finder API (`tools.usps.com`, `requestType` po), queried with curl the same way as the earlier Arkansas cities. Pass 1: 5 and 15 miles around every official Jonesboro ZIP (5 codes listed for Jonesboro, AR by ZIP-Codes.com from USPS data last updated 2026-11-01) and nearby official ZIPs for Bono, Brookland, Bay, Cash, Monette, Lake City, Trumann, Marked Tree, Paragould, Walnut Ridge, Hoxie, Pocahontas, Harrisburg, Weiner, Egypt, Caraway, Black Oak, Leachville, Manila, Blytheville, Osceola, Newport, Alicia, Minturn, Sedgwick, Swifton, and State University (35 ZIPs, 70 queries, 86 unique records). Pass 2 added official Bay ZIP 71651 and official State University Unique ZIP 71999 (both listed on those city pages) and 1, 2, 3, 10, and 20 mile widenings (54 queries, 25 added records, all far from Jonesboro city). Total 111 records (`step8-browser/jonesboro-usps-locator-2026-11-15.jsonl`). Official location pages were fetched for all 111 records (all HTTP 200 on the first try); each page's embedded `poDetail` matched the API record. Retail hours means the BUSINESS block only. Full notes: `step8-browser/jonesboro-usps-2026-11-15.md`.
- **Walmart:** not collected. The official walmart.com store locator was unavailable, so no Walmart rows are in this PR.
- **City limits:** U.S. Census Bureau Geocoder, address endpoint and coordinates endpoint, Public_AR_Current / Current_Current and Public_AR_Census2020 / Census2020_Census2020, Incorporated Places + CDPs + Counties. All 111 addresses and all 111 official locator map points on both benchmarks (`step8-browser/jonesboro-usps-geocoder-2026-11-15.jsonl`). OpenStreetMap was not used.
- Fees reuse existing rows in `data/providers/fees.csv`. No new fee rows or brands. Coordinates for USPS rows are in the notes column (lat/lng columns stay blank, as in every city CSV).

## USPS (3 listed)

All three offices have printed city Jonesboro and address plus official map point in Jonesboro city on both Census files. All three list Domestic and Inquiry Money Orders.

Hold: State University, documented in the city-page "not listed" section and in `jonesboro-usps-2026-11-15.md`.

## Walmart Supercenters

Not collected in this PR. The official walmart.com store locator was unavailable. No Walmart rows, no Walmart fee citations, and no Neighborhood Markets.

## Site changes in this PR

- New `data/locations/jonesboro.csv` and `/jonesboro/`, `/jonesboro/money-orders/`, and `/jonesboro/after-hours/` pages.
- Jonesboro added under the existing Arkansas heading on the home "Start here" list and on `/cities/`, after Springdale. Home and `/cities/` meta descriptions now say "Little Rock, Fayetteville, Fort Smith, Springdale, and Jonesboro, Arkansas". No other city CSV or page changed except those meta and list lines. Colorado order is unchanged.
