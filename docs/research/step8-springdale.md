# Step 8: Springdale, AR (2026-11-15, America/Denver)

**Rows:** 2 (two Post Offices). Fourth city of the approved Arkansas batch (Little Rock, Fayetteville, Fort Smith, Springdale, Jonesboro; one city at a time). Springdale is one incorporated Census place spanning Washington and Benton counties (Census "Springdale city", GEOID 0566080), not a consolidated city-county. Ranking and city-limits checks use the whole-place boundary. Only addresses inside Springdale city whose official printed city is Springdale are listed. Both listed offices geocode in the Washington County part (GEOID 05143) of that place. No businesses were contacted. Brands in scope for non-Colorado states: USPS and Walmart Supercenters only. This PR is USPS only; Walmart rows are omitted because the official walmart.com store locator was unavailable.

**Counts:** 2 locations; 2 money order; 0 check cashing; 0 bill pay; 0 prepaid reload. Labels on the hub: 0 Open evenings, 1 Open weekends. The money-orders page lists 2. The after-hours page lists 1 (the Springdale Post Office on Springdale Avenue, Saturday 09:00-12:00). The weekday close at that office is 17:00, which does not count as Open evenings. No check-cashing or bill-pay page (zero listings). Holds: none. In-city, not listed: none.

Hours are copied as published and are local Springdale time (Central Time). `last_verified` is 2026-11-15 on every row. `verification_status` is `verified_official_locator` on every row.

## Method

- **USPS:** official USPS Location Finder API (`tools.usps.com`, `requestType` po), queried with curl the same way as the earlier Arkansas cities. Pass 1: 5 and 15 miles around every official Springdale ZIP (4 codes listed for Springdale, AR by ZIP-Codes.com from USPS data last updated 2026-11-01) and nearby official ZIPs for Fayetteville, Tontitown, Johnson, Elm Springs, Lowell, Cave Springs, Rogers, Bentonville, Elkins, Goshen, Prairie Grove, Centerton, Pea Ridge, Bella Vista, Siloam Springs, West Fork, Greenland, Gentry, Avoca, Garfield, and Gateway (34 ZIPs, 68 queries, 54 unique records). Pass 2 added official Hindsville ZIP 72738 (the city-page slug hit a lookup limit; search.asp returned 72738) and 1, 2, 3, 10, and 20 mile widenings (57 queries, 1 added record, Witter). Total 55 records (`step8-browser/springdale-usps-locator-2026-11-15.jsonl`). Official location pages were fetched for all 55 records (all HTTP 200 on the first try); each page's embedded `poDetail` matched the API record. Retail hours means the BUSINESS block only. Full notes: `step8-browser/springdale-usps-2026-11-15.md`.
- **Walmart:** not collected. The official walmart.com store locator was unavailable, so no Walmart rows are in this PR.
- **City limits:** U.S. Census Bureau Geocoder, address endpoint and coordinates endpoint, Public_AR_Current / Current_Current and Public_AR_Census2020 / Census2020_Census2020, Incorporated Places + CDPs + Counties. All 55 addresses and all 55 official locator map points on both benchmarks (`step8-browser/springdale-usps-geocoder-2026-11-15.jsonl`). OpenStreetMap was not used.
- Fees reuse existing rows in `data/providers/fees.csv`. No new fee rows or brands. Coordinates for USPS rows are in the notes column (lat/lng columns stay blank, as in every city CSV).

## USPS (2 listed)

Both offices have printed city Springdale and address plus official map point in Springdale city on both Census files. Both list Domestic and Inquiry Money Orders.

## Walmart Supercenters

Not collected in this PR. The official walmart.com store locator was unavailable. No Walmart rows, no Walmart fee citations, and no Neighborhood Markets.

## Site changes in this PR

- New `data/locations/springdale.csv` and `/springdale/`, `/springdale/money-orders/`, and `/springdale/after-hours/` pages.
- Springdale added under the existing Arkansas heading on the home "Start here" list and on `/cities/`, after Fort Smith. Home and `/cities/` meta descriptions now say "Little Rock, Fayetteville, Fort Smith, and Springdale, Arkansas". No other city CSV or page changed except those meta and list lines. Colorado order is unchanged.
