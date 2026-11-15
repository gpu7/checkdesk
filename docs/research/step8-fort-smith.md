# Step 8: Fort Smith, AR (2026-11-15, America/Denver)

**Rows:** 4 (four Post Offices). Third city of the approved Arkansas batch (Little Rock, Fayetteville, Fort Smith, Springdale, Jonesboro; one city at a time). Fort Smith is an incorporated city in Sebastian County (Census "Fort Smith city", GEOID 0524550; county Sebastian County, GEOID 05131), not a consolidated city-county. Only addresses inside Fort Smith city whose official printed city is Fort Smith are listed. No businesses were contacted. Brands in scope for non-Colorado states: USPS and Walmart Supercenters only. This PR is USPS only; Walmart rows are omitted because the official walmart.com store locator was unavailable.

**Counts:** 4 locations; 4 money order; 0 check cashing; 0 bill pay; 0 prepaid reload. Labels on the hub: 1 Open evenings, 1 Open weekends. The money-orders page lists 4. The after-hours page lists 1 (GMF Fort Smith, weekday close 18:00 and Saturday hours). No check-cashing or bill-pay page (zero listings). Holds: none. In-city, not listed: two Fort Smith-printed records at 3318 S 74th St (1363843 and 1473448) that lack money-order tags and a BUSINESS hours block.

Hours are copied as published and are local Fort Smith time (Central Time). `last_verified` is 2026-11-15 on every row. `verification_status` is `verified_official_locator` on every row.

## Method

- **USPS:** official USPS Location Finder API (`tools.usps.com`, `requestType` po), queried with curl the same way as Little Rock and Fayetteville. Pass 1: 5 and 15 miles around every official Fort Smith ZIP (13 codes listed for Fort Smith, AR by ZIP-Codes.com from USPS data last updated 2026-11-01) and nearby official ZIPs for Van Buren, Barling, Alma, Greenwood, Lavaca, Charleston, Mulberry, Hackett, Mansfield, Huntington, Midland, Hartford, Waldron, Paris, Ozark, Booneville, Magazine, Cedarville, Rudy, Mountainburg, Uniontown, Natural Dam, Dyer, and the Oklahoma-border cities Arkoma, Pocola, Roland, Moffett, Spiro, Sallisaw, and Poteau (44 ZIPs, 88 queries, 67 unique records). Pass 2: 1, 2, 3, 10, and 20 mile widenings around core and edge ZIPs (50 queries, 0 added records). Total 67 records (`step8-browser/fort-smith-usps-locator-2026-11-15.jsonl`). Official location pages were fetched for all 67 records (all HTTP 200 on the first try); each page's embedded `poDetail` matched the API record. Retail hours means the BUSINESS block only. Full notes: `step8-browser/fort-smith-usps-2026-11-15.md`.
- **Walmart:** not collected. The official walmart.com store locator was unavailable, so no Walmart rows are in this PR.
- **City limits:** U.S. Census Bureau Geocoder, address endpoint and coordinates endpoint, Public_AR_Current / Current_Current and Public_AR_Census2020 / Census2020_Census2020, Incorporated Places + CDPs + Counties. All 67 addresses and all 67 official locator map points on both benchmarks (`step8-browser/fort-smith-usps-geocoder-2026-11-15.jsonl`). Address geocoding used the office's printed state (AR or OK), not a hardcoded AR. OpenStreetMap was not used.
- Fees reuse existing rows in `data/providers/fees.csv`. No new fee rows or brands. Coordinates for USPS rows are in the notes column (lat/lng columns stay blank, as in every city CSV).

## USPS (4 listed)

All four offices have printed city Fort Smith and address plus official map point in Fort Smith city on both Census files. All four list Domestic and Inquiry Money Orders. The GMF Fort Smith Post Office is listed because it prints Fort Smith, geocodes in Fort Smith city, lists money orders, and publishes retail BUSINESS hours (including evenings and Saturday). Two other records at the same 3318 S 74th St address are in-city, not listed, as documented in the city-page "not listed" section and in `fort-smith-usps-2026-11-15.md`.

## Walmart Supercenters

Not collected in this PR. The official walmart.com store locator was unavailable. No Walmart rows, no Walmart fee citations, and no Neighborhood Markets.

## Site changes in this PR

- New `data/locations/fort-smith.csv` and `/fort-smith/`, `/fort-smith/money-orders/`, and `/fort-smith/after-hours/` pages.
- Fort Smith added under the existing Arkansas heading on the home "Start here" list and on `/cities/`, after Fayetteville. Home and `/cities/` meta descriptions now say "Little Rock, Fayetteville, and Fort Smith, Arkansas". No other city CSV or page changed except those meta and list lines. Colorado order is unchanged.
