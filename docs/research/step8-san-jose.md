# Step 8: San Jose, CA (2026-11-15, America/Denver)

**Rows:** 9 (nine Post Offices). Third city of the California batch (Los Angeles, San Diego, San Jose, San Francisco, Fresno; one city at a time). San Jose is an incorporated city in Santa Clara County (Census "San Jose city", GEOID 0668000; county Santa Clara County, GEOID 06085), not a consolidated city-county. Only addresses inside San Jose city whose official printed city is San Jose are listed. No businesses were contacted. This PR is USPS only; Walmart rows are omitted because the official walmart.com store locator was unavailable.

**Counts:** 9 locations; 9 money order; 0 check cashing; 0 bill pay; 0 prepaid reload. Labels on the hub: 1 Open evenings, 7 Open weekends. The money-orders page lists 9. The after-hours page lists 7 (1 evening and 7 weekends, with overlap). No check-cashing or bill-pay page (zero listings). Holds: New Almaden (prints San Jose; address and official point in unincorporated Santa Clara County) and Alviso (prints Alviso; address and official point in San Jose city). In-city, not listed: 9 San Jose-printed records without money-order tags.

Hours are copied as published and are local San Jose time (Pacific Time). `last_verified` is 2026-11-15 on every row. `verification_status` is `verified_official_locator` on every row.

## Method

- **USPS:** official USPS Location Finder API (`tools.usps.com`, `requestType` po). Official San Jose ZIPs came from ZIP-Codes.com search.asp, because the `ca-san-jose` city-page slug is a collision (Alviso). Pass 1: 5 and 15 miles around 111 ZIPs (222 queries, 119 unique records). Pass 2 added 1, 2, 3, 10, and 20 mile widenings around 57 core and edge ZIPs (285 queries, 2 added records far from San Jose city, no new printed-San-Jose offices). Total 121 records (`step8-browser/san-jose-usps-locator-2026-11-15.jsonl`). Official location pages were fetched for all 121 records (all HTTP 200 on the first try); each page's embedded `poDetail` matched the API record. Full notes: `step8-browser/san-jose-usps-2026-11-15.md`.
- **Walmart:** not collected.
- **City limits:** U.S. Census Bureau Geocoder, address and coordinates endpoints, Public_AR_Current / Current_Current and Public_AR_Census2020 / Census2020_Census2020, Incorporated Places + CDPs + Counties, matching San Jose city GEOID 0668000 only. All 121 addresses and official locator map points on both benchmarks (`step8-browser/san-jose-usps-geocoder-2026-11-15.jsonl`). OpenStreetMap was not used. No listed office used the map-point fallback.
- Fees reuse existing rows in `data/providers/fees.csv`. Coordinates for USPS rows are in the notes column (lat/lng columns stay blank).

## Site changes in this PR

- New `data/locations/san-jose.csv` and `/san-jose/`, `/san-jose/money-orders/`, and `/san-jose/after-hours/` pages.
- San Jose added under the existing California heading on the home "Start here" list and on `/cities/`, after San Diego. Home and `/cities/` meta descriptions now say "Los Angeles, San Diego, and San Jose, California". No other city CSV or page changed except those meta and list lines. Colorado order is unchanged.
