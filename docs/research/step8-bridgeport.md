# Step 8: Bridgeport, CT (2026-11-15, America/Denver)

**Rows:** 2 (two Post Offices). First city of the Connecticut batch (Bridgeport, Stamford, New Haven, Hartford, Waterbury; one city at a time). Bridgeport is an incorporated city, coextensive with Bridgeport town, in the Greater Bridgeport Planning Region (Census "Bridgeport city", GEOID 0908000; planning region GEOID 09120). Only addresses inside Bridgeport city whose official printed city is Bridgeport are listed. Stratford, Fairfield, Trumbull, and other nearby municipalities are not listed here. No businesses were contacted. This PR is USPS only; Walmart rows are omitted because the official walmart.com store locator was unavailable.

**Counts:** 2 locations; 2 money order; 0 check cashing; 0 bill pay; 0 prepaid reload. Labels on the hub: 0 Open evenings, 1 Open weekends (Bayview). The money-orders page lists 2. The after-hours page lists 1 (0 evening and 1 weekend). No check-cashing or bill-pay page (zero listings). Holds: none. In-city, not listed: the Bridgeport Post Office (1434081, 120 Middle St; no BUSINESS block, no money-order tags) and Bridgeport CT S&DC (1579655, same address; BUSINESS hours including Saturday, no money-order tags).

Hours are copied as published and are local Bridgeport time (Eastern Time). `last_verified` is 2026-11-15 on every row. `verification_status` is `verified_official_locator` on every row.

## Method

- **USPS:** official USPS Location Finder API (`tools.usps.com`, `requestType` po). Official Bridgeport ZIPs came from ZIP-Codes.com search.asp (the `ct-bridgeport` city-page slug is not a collision). City page and search.asp have the same 10 unique ZIPs, all listed Bridgeport. Pass 1: 5 and 15 miles around 51 ZIPs (102 queries, 179 unique records, 4 printed Bridgeport). Pass 2 added 1, 2, 3, 10, and 20 mile widenings around 22 official and edge ZIPs (110 queries, 11 added records, all far Long Island offices, no new printed-Bridgeport offices). Total 190 records (`step8-browser/bridgeport-usps-locator-2026-11-15.jsonl`). Official location pages were fetched for all 190 records (all HTTP 200 on the first try); each page's embedded `poDetail` matched the API record. Full notes: `step8-browser/bridgeport-usps-2026-11-15.md`.
- **Walmart:** not collected.
- **City limits:** U.S. Census Bureau Geocoder, address and coordinates endpoints, Public_AR_Current / Current_Current and Public_AR_Census2020 / Census2020_Census2020, Incorporated Places + CDPs + Counties, matching Bridgeport city GEOID 0908000 only. All 190 addresses and official locator map points on both benchmarks (`step8-browser/bridgeport-usps-geocoder-2026-11-15.jsonl`). OpenStreetMap was not used. No listed office needed the map-point fallback.
- Fees reuse existing rows in `data/providers/fees.csv`. Coordinates for USPS rows are in the notes column (lat/lng columns stay blank).

## Site changes in this PR

- New `data/locations/bridgeport.csv` and `/bridgeport/`, `/bridgeport/money-orders/`, and `/bridgeport/after-hours/` pages.
- A new Connecticut heading, after Colorado, on the home "Start here" list and on `/cities/`, with Bridgeport as the first city. Home and `/cities/` meta descriptions now include "Bridgeport, Connecticut". No other city CSV or page changed except those meta and list lines. Colorado pages are unchanged.
