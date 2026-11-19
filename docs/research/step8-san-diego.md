# San Diego, CA — neighborhood-named offices added 2026-11-19

Three neighborhood-named Post Offices are now listed on the San Diego pages, under the rule approved 2026-11-19: the official page prints a community name, both the current and 2020 Census address files place the address inside San Diego city (GEOID 0666000), money-order tags are present, and the displayed city stays the official printed USPS city. All three also have official map points in San Diego city on both files, and all three are in San Diego County. The original twenty-seven San Diego-printed rows are unchanged, including the two documented map-point fallbacks.

Added offices (printed city in parentheses): La Jolla (La Jolla); La Jolla Village (La Jolla); and San Ysidro (San Ysidro). La Jolla and San Ysidro are communities inside San Diego city, not separate incorporated places.

The San Diego list is now 30 Post Offices, all with money orders (1 Open evenings, Carmel Mountain Postal Store; 26 Open weekends, Saturday only). Hours stay Pacific Time. La Jolla Village has no evening and no weekend retail hours, so it does not appear on the after-hours page.

Holds that remain: NAS North Island (prints San Diego; official map point in Coronado city); 11 San Diego-printed in-city records with no money-order tags (including La Jolla Annex UC, which prints San Diego).

The body below is the original 2026-11-15 memo and is superseded for listed and hold counts.

# Step 8: San Diego, CA (2026-11-15, America/Denver)

**Rows:** 27 (27 Post Offices). Second city of the California batch (Los Angeles, San Diego, San Jose, San Francisco, Fresno; one city at a time). San Diego is an incorporated city in San Diego County (Census "San Diego city", GEOID 0666000; county San Diego County, GEOID 06073), not a consolidated city-county. Only addresses inside San Diego city whose official printed city is San Diego are listed. No businesses were contacted. Brands in scope for non-Colorado states: USPS and Walmart Supercenters only. This PR is USPS only; Walmart rows are omitted because the official walmart.com store locator was unavailable.

**Counts:** 27 locations; 27 money order; 0 check cashing; 0 bill pay; 0 prepaid reload. Labels on the hub: 1 Open evenings, 24 Open weekends. The money-orders page lists 27. The after-hours page lists 24 (1 evening and 24 weekends, with overlap). No check-cashing or bill-pay page (zero listings). Holds: NAS North Island (prints San Diego; official point in Coronado city); La Jolla, La Jolla Village, and San Ysidro (printed-city mismatches inside San Diego city). In-city, not listed: 11 San Diego-printed records without money-order tags.

Hours are copied as published and are local San Diego time (Pacific Time). `last_verified` is 2026-11-15 on every row. `verification_status` is `verified_official_locator` on every row.

## Method

- **USPS:** official USPS Location Finder API (`tools.usps.com`, `requestType` po), queried with curl the same way as Los Angeles. Pass 1: 5 and 15 miles around official San Diego ZIPs and nearby official or neighborhood ZIPs (154 ZIPs, 308 queries, 107 unique records). Pass 2 added 1, 2, 3, 10, and 20 mile widenings around 60 core and edge ZIPs (300 queries, 0 added records). Total 107 records (`step8-browser/san-diego-usps-locator-2026-11-15.jsonl`). Official location pages were fetched for all 107 records (all HTTP 200 on the first try); each page's embedded `poDetail` matched the API record. Retail hours means the BUSINESS block only. Full notes: `step8-browser/san-diego-usps-2026-11-15.md`.
- **Walmart:** not collected. The official walmart.com store locator was unavailable, so no Walmart rows are in this PR.
- **City limits:** U.S. Census Bureau Geocoder, address endpoint and coordinates endpoint, Public_AR_Current / Current_Current and Public_AR_Census2020 / Census2020_Census2020, Incorporated Places + CDPs + Counties, matching San Diego city GEOID 0666000 only. All 107 addresses and all 107 official locator map points on both benchmarks (`step8-browser/san-diego-usps-geocoder-2026-11-15.jsonl`). OpenStreetMap was not used. Two offices are listed under the documented map-point fallback (printed city already San Diego; official map point in the city): Carmel Mountain Postal Store and MCAS Miramar.
- Fees reuse existing rows in `data/providers/fees.csv`. No new fee rows or brands. Coordinates for USPS rows are in the notes column (lat/lng columns stay blank, as in every city CSV).

## USPS (27 listed)

Twenty-five offices have printed city San Diego and address plus official map point in San Diego city on both Census files. Two more are listed under the map-point fallback documented in the long memo and in those CSV notes. All 27 list Domestic and Inquiry Money Orders.

Holds and in-city not-listed records are documented in the city-page "not listed" section and in `san-diego-usps-2026-11-15.md`.

## Walmart Supercenters

Not collected in this PR. The official walmart.com store locator was unavailable. No Walmart rows, no Walmart fee citations, and no Neighborhood Markets.

## Site changes in this PR

- New `data/locations/san-diego.csv` and `/san-diego/`, `/san-diego/money-orders/`, and `/san-diego/after-hours/` pages.
- San Diego added under the existing California heading on the home "Start here" list and on `/cities/`, after Los Angeles. Home and `/cities/` meta descriptions now say "Los Angeles and San Diego, California". No other city CSV or page changed except those meta and list lines. Colorado order is unchanged.
