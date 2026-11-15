# Step 8: San Francisco, CA (2026-11-15, America/Denver)

**Rows:** 31 (31 Post Offices). Fourth city of the California batch (Los Angeles, San Diego, San Jose, San Francisco, Fresno; one city at a time). San Francisco is a consolidated city-county (Census "San Francisco city", GEOID 0667000; county San Francisco County, GEOID 06075, coextensive). Only addresses inside San Francisco city whose official printed city is San Francisco are listed. South San Francisco is a separate incorporated city in San Mateo County and is not listed here. No businesses were contacted. This PR is USPS only; Walmart rows are omitted because the official walmart.com store locator was unavailable.

**Counts:** 31 locations; 31 money order; 0 check cashing; 0 bill pay; 0 prepaid reload. Labels on the hub: 7 Open evenings, 22 Open weekends. The money-orders page lists 31. The after-hours page lists 22 (7 evening and 22 weekends, with all seven evening offices also having Saturday hours). No check-cashing or bill-pay page (zero listings). No printed-city holds. In-city, not listed: 9 San Francisco-printed records without money-order tags, including West Portal (Saturday hours) and San Francisco Gen Del.

Hours are copied as published and are local San Francisco time (Pacific Time). `last_verified` is 2026-11-15 on every row. `verification_status` is `verified_official_locator` on every row.

## Method

- **USPS:** official USPS Location Finder API (`tools.usps.com`, `requestType` po). Official San Francisco ZIPs came from ZIP-Codes.com search.asp (the `ca-san-francisco` city-page slug is not a collision). Pass 1: 5 and 15 miles around 151 ZIPs (302 queries, 211 unique records). Pass 2 added 1, 2, 3, 10, and 20 mile widenings around 67 official and edge ZIPs (335 queries, 2 added records far from San Francisco city, no new printed-San-Francisco offices). Total 213 records (`step8-browser/san-francisco-usps-locator-2026-11-15.jsonl`). Official location pages were fetched for all 213 records (all HTTP 200 on the first try); each page's embedded `poDetail` matched the API record. Full notes: `step8-browser/san-francisco-usps-2026-11-15.md`.
- **Walmart:** not collected.
- **City limits:** U.S. Census Bureau Geocoder, address and coordinates endpoints, Public_AR_Current / Current_Current and Public_AR_Census2020 / Census2020_Census2020, Incorporated Places + CDPs + Counties, matching San Francisco city GEOID 0667000 only. All 213 addresses and official locator map points on both benchmarks (`step8-browser/san-francisco-usps-geocoder-2026-11-15.jsonl`). OpenStreetMap was not used. Five listed offices used the documented map-point fallback after street-name retries: Diamond Heights, Lakeshore Plaza, Marina, Bryant Street, and Presidio.
- Fees reuse existing rows in `data/providers/fees.csv`. Coordinates for USPS rows are in the notes column (lat/lng columns stay blank).

## Site changes in this PR

- New `data/locations/san-francisco.csv` and `/san-francisco/`, `/san-francisco/money-orders/`, and `/san-francisco/after-hours/` pages.
- San Francisco added under the existing California heading on the home "Start here" list and on `/cities/`, after San Jose. Home and `/cities/` meta descriptions now say "Los Angeles, San Diego, San Jose, and San Francisco, California". No other city CSV or page changed except those meta and list lines. Colorado order is unchanged.
