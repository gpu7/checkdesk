# Step 8: Mesa, AZ (2026-11-14, America/Denver)

**Rows:** 8 (eight Post Offices). Third city of the approved Arizona batch (Phoenix, Tucson, Mesa, Gilbert, Chandler; one city at a time). Mesa is an incorporated city in Maricopa County (Census "Mesa city", GEOID 0446000; county Maricopa County, GEOID 04013), not a consolidated city-county. Only addresses inside Mesa city whose official printed city is Mesa are listed. No businesses were contacted. Brands in scope for non-Colorado states: USPS and Walmart Supercenters only. This PR is USPS only; Walmart rows are omitted because the official walmart.com store locator was unavailable.

**Counts:** 8 locations; 8 money order; 0 check cashing; 0 bill pay; 0 prepaid reload. Labels on the hub: 0 Open evenings, 5 Open weekends. The money-orders page lists 8. The after-hours page lists 5 (Mesa, Mesa Desert, Mesa Dobson, Mesa Mountain View, and Mesa Superstition Springs, all Saturday hours). None of the eight listed offices has a weekday close after 17:00. No check-cashing or bill-pay page (zero listings). Holds: none. In-city, not listed: none.

Hours are copied as published and are local Mesa time (Arizona Time, Mountain Standard Time; Arizona does not observe daylight saving). `last_verified` is 2026-11-14 on every row. `verification_status` is `verified_official_locator` on every row.

## Method

- **USPS:** official USPS Location Finder API (`tools.usps.com`, `requestType` po), queried with curl the same way as Phoenix and Tucson. Pass 1: 5 and 15 miles around every official Mesa Valley ZIP (19 of the 23 codes listed for Mesa, AZ by ZIP-Codes.com from USPS data last updated 2026-11-01; the four far Navajo/Hopi codes on that page were not queried as Mesa nearby ZIPs) and nearby official ZIPs for Chandler, Gilbert, Tempe, Apache Junction, Queen Creek, Higley, and Phoenix-edge ZIPs (35 ZIPs, 70 queries, 54 unique records). Pass 2: 1, 2, 3, 10, and 20 mile widenings on edge Mesa and fringe ZIPs (40 queries, 1 added record: Coolidge). Total 55 records (`step8-browser/mesa-usps-locator-2026-11-14.jsonl`). Official location pages and both-file geocodes for all 55 were already on file from the Phoenix and Tucson research (all HTTP 200, page `poDetail` matched the API). Retail hours means the BUSINESS block only. Full notes: `step8-browser/mesa-usps-2026-11-14.md`.
- **Walmart:** not collected. The official walmart.com store locator was unavailable, so no Walmart rows are in this PR.
- **City limits:** U.S. Census Bureau Geocoder, address endpoint and coordinates endpoint, Public_AR_Current / Current_Current and Public_AR_Census2020 / Census2020_Census2020, Incorporated Places + CDPs + Counties. All 55 addresses and all 55 official locator map points on both benchmarks (`step8-browser/mesa-usps-geocoder-2026-11-14.jsonl`). OpenStreetMap was not used.
- Fees reuse existing rows in `data/providers/fees.csv`. No new fee rows or brands. Coordinates for USPS rows are in the notes column (lat/lng columns stay blank, as in every city CSV).

## USPS (8 listed)

All eight offices have printed city Mesa and address plus official map point in Mesa city on both Census files. All eight list Domestic and Inquiry Money Orders.

Holds: none. In-city exclusions: none.

## Walmart Supercenters

Not collected in this PR. The official walmart.com store locator was unavailable. No Walmart rows, no Walmart fee citations, and no Neighborhood Markets.

## Site changes in this PR

- New `data/locations/mesa.csv` and `/mesa/`, `/mesa/money-orders/`, and `/mesa/after-hours/` pages.
- Mesa added under the existing Arizona heading on the home "Start here" list and on `/cities/`, after Tucson. Home and `/cities/` meta descriptions now say "Phoenix, Tucson, and Mesa, Arizona". No other city CSV or page changed except those meta and list lines. Colorado order is unchanged.
