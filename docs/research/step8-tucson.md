# Step 8: Tucson, AZ (2026-11-14, America/Denver)

**Rows:** 8 (eight Post Offices). Second city of the approved Arizona batch (Phoenix, Tucson, Mesa, Gilbert, Chandler; one city at a time). Tucson is an incorporated city in Pima County (Census "Tucson city", GEOID 0477000; county Pima County, GEOID 04019), not a consolidated city-county. Only addresses inside Tucson city whose official printed city is Tucson are listed, except Davis Monthan AFB, which had an address no-match and is listed on its official map point inside Tucson city. No businesses were contacted. Brands in scope for non-Colorado states: USPS and Walmart Supercenters only. This PR is USPS only; Walmart rows are omitted because the official walmart.com store locator was unavailable.

**Counts:** 8 locations; 8 money order; 0 check cashing; 0 bill pay; 0 prepaid reload. Labels on the hub: 0 Open evenings, 4 Open weekends. The money-orders page lists 8. The after-hours page lists 4 (Coronado, Fort Lowell, Mission, and Rincon, all Saturday hours). None of the eight listed offices has a weekday close after 17:00. The Tucson Post Office on Cherrybell Stravenue publishes hours until 18:30 and Saturday hours, but it has no money-order tags, so it is not listed and does not appear on after-hours. No check-cashing or bill-pay page (zero listings). Holds: Casas Adobes, Mountain View, Oro Valley, San Xavier, South Tucson, and Vail Annex. In-city, not listed (no money-order tags): Downtown Tucson, Kino Retail Unit, Rincon Plaza Retail, and Tucson / Cherrybell.

Hours are copied as published and are local Tucson time (Arizona Time, Mountain Standard Time; Arizona does not observe daylight saving). `last_verified` is 2026-11-14 on every row. `verification_status` is `verified_official_locator` on every row.

## Method

- **USPS:** official USPS Location Finder API (`tools.usps.com`, `requestType` po), queried with curl the same way as Phoenix. Pass 1: 5 and 15 miles around every Tucson ZIP (55 USPS-city codes listed for Tucson, AZ by ZIP-Codes.com from USPS data last updated 2026-11-01) and nearby official ZIPs for Marana, Sahuarita, Green Valley, Mount Lemmon, Ajo, Cortaro, Rillito, Benson, and Sierra Vista (70 ZIPs, 140 queries, 41 unique records). Pass 2: additional fringe official ZIPs plus 1, 2, 3, 10, 20, and (on sparse edges) 50 mile widenings (117 queries, 31 added records, all far from Tucson city). Total 72 records (`step8-browser/tucson-usps-locator-2026-11-14.jsonl`). Official location pages were fetched for all 72 records (all HTTP 200 on the first try); each page's embedded `poDetail` matched the API record. Retail hours means the BUSINESS block only. Full notes: `step8-browser/tucson-usps-2026-11-14.md`.
- **Walmart:** not collected. The official walmart.com store locator was unavailable, so no Walmart rows are in this PR.
- **City limits:** U.S. Census Bureau Geocoder, address endpoint and coordinates endpoint, Public_AR_Current / Current_Current and Public_AR_Census2020 / Census2020_Census2020, Incorporated Places + CDPs + Counties. All 72 addresses and all 72 official locator map points on both benchmarks (`step8-browser/tucson-usps-geocoder-2026-11-14.jsonl`). OpenStreetMap was not used.
- Fees reuse existing rows in `data/providers/fees.csv`. No new fee rows or brands. Coordinates for USPS rows are in the notes column (lat/lng columns stay blank, as in every city CSV).

## USPS (8 listed)

Seven offices have printed city Tucson and address plus official map point in Tucson city on both Census files. Davis Monthan AFB Post Office (1439478) prints Tucson; the address had no Census match after retries and is listed on the official map point, which is in Tucson city on both files. Coronado and Mission list MONEYORDERSDOM only; the others list Domestic and Inquiry Money Orders except Davis Monthan, which is also Domestic only.

Holds and in-city exclusions are listed in the city-page "not listed" section and in `tucson-usps-2026-11-14.md`.

## Walmart Supercenters

Not collected in this PR. The official walmart.com store locator was unavailable. No Walmart rows, no Walmart fee citations, and no Neighborhood Markets.

## Site changes in this PR

- New `data/locations/tucson.csv` and `/tucson/`, `/tucson/money-orders/`, and `/tucson/after-hours/` pages.
- Tucson added under the existing Arizona heading on the home "Start here" list and on `/cities/`, after Phoenix. Home and `/cities/` meta descriptions now say "Phoenix and Tucson, Arizona". No other city CSV or page changed except those meta and list lines. Colorado order is unchanged.
