# Step 8: Fresno, CA (2026-11-15, America/Denver)

**Rows:** 8 (eight Post Offices). Fifth city of the California batch (Los Angeles, San Diego, San Jose, San Francisco, Fresno; one city at a time). Fresno is an incorporated city in Fresno County (Census "Fresno city", GEOID 0627000; county Fresno County, GEOID 06019), not a consolidated city-county. Only addresses inside Fresno city whose official printed city is Fresno are listed. Clovis is a separate incorporated city and is not listed here. No businesses were contacted. This PR is USPS only; Walmart rows are omitted because the official walmart.com store locator was unavailable.

**Counts:** 8 locations; 8 money order; 0 check cashing; 0 bill pay; 0 prepaid reload. Labels on the hub: 0 Open evenings, 5 Open weekends. The money-orders page lists 8. The after-hours page lists 5 (0 evening and 5 weekends). No check-cashing or bill-pay page (zero listings). Holds: Barton and Calwa (both print Fresno; address and official point in Calwa CDP). In-city, not listed: Civic Center Fresno (BUSINESS hours, no money-order tags).

Hours are copied as published and are local Fresno time (Pacific Time). `last_verified` is 2026-11-15 on every row. `verification_status` is `verified_official_locator` on every row.

## Method

- **USPS:** official USPS Location Finder API (`tools.usps.com`, `requestType` po). Official Fresno ZIPs came from ZIP-Codes.com search.asp (the `ca-fresno` city-page slug is not a collision). The `ca-pinedale` slug collided with the Fresno city page; 93650 is an official Fresno ZIP. Pass 1: 5 and 15 miles around 99 ZIPs (198 queries, 72 unique records). Pass 2 added 1, 2, 3, 10, and 20 mile widenings around 71 official and edge ZIPs (355 queries, 2 added records far from Fresno city, no new printed-Fresno offices). Total 74 records (`step8-browser/fresno-usps-locator-2026-11-15.jsonl`). Official location pages were fetched for all 74 records (all HTTP 200 on the first try); each page's embedded `poDetail` matched the API record. Full notes: `step8-browser/fresno-usps-2026-11-15.md`.
- **Walmart:** not collected.
- **City limits:** U.S. Census Bureau Geocoder, address and coordinates endpoints, Public_AR_Current / Current_Current and Public_AR_Census2020 / Census2020_Census2020, Incorporated Places + CDPs + Counties, matching Fresno city GEOID 0627000 only. All 74 addresses and official locator map points on both benchmarks (`step8-browser/fresno-usps-geocoder-2026-11-15.jsonl`). OpenStreetMap was not used. One listed office used the documented map-point fallback after street-name retries: Clinter.
- Fees reuse existing rows in `data/providers/fees.csv`. Coordinates for USPS rows are in the notes column (lat/lng columns stay blank).

## Site changes in this PR

- New `data/locations/fresno.csv` and `/fresno/`, `/fresno/money-orders/`, and `/fresno/after-hours/` pages.
- Fresno added under the existing California heading on the home "Start here" list and on `/cities/`, after San Francisco. Home and `/cities/` meta descriptions now say "Los Angeles, San Diego, San Jose, San Francisco, and Fresno, California". No other city CSV or page changed except those meta and list lines. Colorado order is unchanged.
