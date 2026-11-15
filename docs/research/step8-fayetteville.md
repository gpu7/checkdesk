# Step 8: Fayetteville, AR (2026-11-15, America/Denver)

**Rows:** 2 (two Post Offices). Second city of the approved Arkansas batch (Little Rock, Fayetteville, Fort Smith, Springdale, Jonesboro; one city at a time). Fayetteville is an incorporated city in Washington County (Census "Fayetteville city", GEOID 0523290; county Washington County, GEOID 05143), not a consolidated city-county. Only addresses inside Fayetteville city whose official printed city is Fayetteville are listed. No businesses were contacted. Brands in scope for non-Colorado states: USPS and Walmart Supercenters only. This PR is USPS only; Walmart rows are omitted because the official walmart.com store locator was unavailable.

**Counts:** 2 locations; 2 money order; 0 check cashing; 0 bill pay; 0 prepaid reload. Labels on the hub: 1 Open evenings, 2 Open weekends. The money-orders page lists 2. The after-hours page lists 2 (Fayetteville and CB Craft, both Saturday hours). CB Craft is the evening office (weekday close 18:00). No check-cashing or bill-pay page (zero listings). Hold: Greenland. In-city, not listed: none.

Hours are copied as published and are local Fayetteville time (Central Time). `last_verified` is 2026-11-15 on every row. `verification_status` is `verified_official_locator` on every row.

## Method

- **USPS:** official USPS Location Finder API (`tools.usps.com`, `requestType` po), queried with curl the same way as Little Rock. Pass 1: 5 and 15 miles around every official Fayetteville ZIP (6 codes listed for Fayetteville, AR by ZIP-Codes.com from USPS data last updated 2026-11-01, including 72730 and 72764, which are also official Farmington and Springdale ZIPs) and nearby official ZIPs for Bentonville, Cave Springs, Centerton, Elkins, Greenland, Johnson, Lincoln, Lowell, Pea Ridge, Prairie Grove, Rogers, Siloam Springs, Springdale, West Fork, Winslow, and Gentry (28 ZIPs, 56 queries, 49 unique records). Pass 2 added official Tontitown ZIP 72770 and 1, 2, 3, 10, and 20 mile widenings (52 queries, 7 added records). Total 56 records (`step8-browser/fayetteville-usps-locator-2026-11-15.jsonl`). Official location pages were fetched for all 56 records (all HTTP 200 on the first try); each page's embedded `poDetail` matched the API record. Retail hours means the BUSINESS block only. Full notes: `step8-browser/fayetteville-usps-2026-11-15.md`.
- **Walmart:** not collected. The official walmart.com store locator was unavailable, so no Walmart rows are in this PR.
- **City limits:** U.S. Census Bureau Geocoder, address endpoint and coordinates endpoint, Public_AR_Current / Current_Current and Public_AR_Census2020 / Census2020_Census2020, Incorporated Places + CDPs + Counties. All 56 addresses and all 56 official locator map points on both benchmarks (`step8-browser/fayetteville-usps-geocoder-2026-11-15.jsonl`). OpenStreetMap was not used.
- Fees reuse existing rows in `data/providers/fees.csv`. No new fee rows or brands. Coordinates for USPS rows are in the notes column (lat/lng columns stay blank, as in every city CSV).

## USPS (2 listed)

Both offices have printed city Fayetteville and address plus official map point in Fayetteville city on both Census files. Both list Domestic and Inquiry Money Orders.

Hold: Greenland, documented in the city-page "not listed" section and in `fayetteville-usps-2026-11-15.md`.

## Walmart Supercenters

Not collected in this PR. The official walmart.com store locator was unavailable. No Walmart rows, no Walmart fee citations, and no Neighborhood Markets.

## Site changes in this PR

- New `data/locations/fayetteville.csv` and `/fayetteville/`, `/fayetteville/money-orders/`, and `/fayetteville/after-hours/` pages.
- Fayetteville added under the existing Arkansas heading on the home "Start here" list and on `/cities/`, after Little Rock. Home and `/cities/` meta descriptions now say "Little Rock and Fayetteville, Arkansas". No other city CSV or page changed except those meta and list lines. Colorado order is unchanged.
