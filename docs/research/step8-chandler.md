# Step 8: Chandler, AZ (2026-11-14, America/Denver)

**Rows:** 3 (three Post Offices). Fifth and last city of the approved Arizona batch (Phoenix, Tucson, Mesa, Gilbert, Chandler; one city at a time). Chandler is an incorporated city in Maricopa County (Census "Chandler city", GEOID 0412000; county Maricopa County, GEOID 04013), not a consolidated city-county. Only addresses inside Chandler city whose official printed city is Chandler are listed. No businesses were contacted. Brands in scope for non-Colorado states: USPS and Walmart Supercenters only. This PR is USPS only; Walmart rows are omitted because the official walmart.com store locator was unavailable.

**Counts:** 3 locations; 3 money order; 0 check cashing; 0 bill pay; 0 prepaid reload. Labels on the hub: 0 Open evenings, 3 Open weekends. The money-orders page lists 3. The after-hours page lists 3 (Andersen Springs, Chandler, and Ocotillo, all Saturday hours). None of the three listed offices has a weekday close after 17:00. No check-cashing or bill-pay page (zero listings). Holds: none. In-city, not listed: none. The Ocotillo office is in ZIP 85248, which is also an official Sun Lakes ZIP; the address and official map point geocode in Chandler city, not the Sun Lakes CDP, so it is included.

Hours are copied as published and are local Chandler time (Arizona Time, Mountain Standard Time; Arizona does not observe daylight saving). `last_verified` is 2026-11-14 on every row. `verification_status` is `verified_official_locator` on every row.

## Method

- **USPS:** official USPS Location Finder API (`tools.usps.com`, `requestType` po), queried with curl the same way as the earlier Arizona cities. Pass 1: 5 and 15 miles around every official Chandler ZIP (8 codes listed for Chandler, AZ by ZIP-Codes.com from USPS data last updated 2026-11-01) and nearby official ZIPs for Gilbert, Mesa, Tempe, Phoenix-edge, Queen Creek, and Maricopa (23 ZIPs, 46 queries, 48 unique records). Pass 2: 1, 2, 3, 10, and 20 mile widenings on edge Chandler and fringe ZIPs (30 queries, 4 added records). Total 52 records (`step8-browser/chandler-usps-locator-2026-11-14.jsonl`). Official location pages and both-file geocodes for all 52 were already on file from earlier Valley research (all HTTP 200, page `poDetail` matched the API). Retail hours means the BUSINESS block only. Full notes: `step8-browser/chandler-usps-2026-11-14.md`.
- **Walmart:** not collected. The official walmart.com store locator was unavailable, so no Walmart rows are in this PR.
- **City limits:** U.S. Census Bureau Geocoder, address endpoint and coordinates endpoint, Public_AR_Current / Current_Current and Public_AR_Census2020 / Census2020_Census2020, Incorporated Places + CDPs + Counties. All 52 addresses and all 52 official locator map points on both benchmarks (`step8-browser/chandler-usps-geocoder-2026-11-14.jsonl`). OpenStreetMap was not used.
- Fees reuse existing rows in `data/providers/fees.csv`. No new fee rows or brands. Coordinates for USPS rows are in the notes column (lat/lng columns stay blank, as in every city CSV).

## USPS (3 listed)

All three offices have printed city Chandler and address plus official map point in Chandler city on both Census files. All three list Domestic and Inquiry Money Orders.

Holds: none. In-city exclusions: none.

## Walmart Supercenters

Not collected in this PR. The official walmart.com store locator was unavailable. No Walmart rows, no Walmart fee citations, and no Neighborhood Markets.

## Site changes in this PR

- New `data/locations/chandler.csv` and `/chandler/`, `/chandler/money-orders/`, and `/chandler/after-hours/` pages.
- Chandler added under the existing Arizona heading on the home "Start here" list and on `/cities/`, after Gilbert. Home and `/cities/` meta descriptions now say "Phoenix, Tucson, Mesa, Gilbert, and Chandler, Arizona". No other city CSV or page changed except those meta and list lines. Colorado order is unchanged.
