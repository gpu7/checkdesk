# Los Angeles, CA USPS research (2026-11-15, America/Denver; neighborhood-name release 2026-11-19)

## 2026-11-19 update

Richard approved listing Post Offices whose official printed city is a neighborhood or community name when both Census address files place the address inside the target incorporated city and money-order tags are present. Displayed addresses keep the official printed USPS city.

This update adds 35 such offices to the Los Angeles pages. All 35 have all four Census legs in Los Angeles city, GEOID 0644000, Los Angeles County GEOID 06037, and list money-order tags. They were geocoded in the 2026-11-15 sweep; `last_verified` on the new rows is 2026-11-19. The original 43 Los Angeles-printed rows are unchanged, including the three documented map-point fallbacks (Terminal Annex Finance, Sunset, and West Los Angeles Finance).

Printed names of the 35 added offices: North Hollywood 4, Canoga Park 2, Encino 2, San Pedro 2, and one each in Arleta, Chatsworth, Granada Hills, Harbor City, Marina del Rey, North Hills, Pacific Palisades, Pacoima, Panorama City, Playa del Rey, Porter Ranch, Reseda, Sherman Oaks, Studio City, Sun Valley, Sunland, Sylmar, Tarzana, Tujunga, Valley Village, Venice, West Hills, Wilmington, Winnetka, and Woodland Hills.

The Los Angeles list is now 78 Post Offices, all with money orders. Open evenings: 23. Open weekends: 57 (Saturday only; no Sunday). Hours labeled Pacific Time.

Holds that remain: 5 Los Angeles-printed geographic holds (Wagner Branch, Hazard, East Los Angeles, Airport Los Angeles, Barrington); 5 neighborhood-printed offices inside the city with no money-order tags (Civic Center Van Nuys, Van Nuys, Van Nuys CA SDC, Northridge, Toluca Lake New); 10 Los Angeles-printed in-city records with no money-order tags. OpenStreetMap was not used.

The rest of this memo is the original 2026-11-15 research, kept for the locator, geocode, and hold documentation. Listed and hold counts in the original sections below are superseded by this update.

---

# Step 8: Los Angeles, CA (2026-11-15, America/Denver)

**Rows:** 43 (43 Post Offices). First city of the California batch (Los Angeles, San Diego, San Jose, San Francisco, Fresno; one city at a time). Los Angeles is an incorporated city in Los Angeles County (Census "Los Angeles city", GEOID 0644000; county Los Angeles County, GEOID 06037), not a consolidated city-county. Long Beach is a separate incorporated city and is not listed here. Only addresses inside Los Angeles city whose official printed city is Los Angeles are listed. No businesses were contacted. Brands in scope for non-Colorado states: USPS and Walmart Supercenters only. This PR is USPS only; Walmart rows are omitted because the official walmart.com store locator was unavailable.

**Counts:** 43 locations; 43 money order; 0 check cashing; 0 bill pay; 0 prepaid reload. Labels on the hub: 13 Open evenings, 31 Open weekends. The money-orders page lists 43. The after-hours page lists 33 (13 evenings and 31 weekends, with overlap). No check-cashing or bill-pay page (zero listings). Holds: 5 printed-Los-Angeles geographic holds and 40 neighborhood-printed offices with a geocode leg in Los Angeles city. In-city, not listed: 10 Los Angeles-printed records without money-order tags.

Hours are copied as published and are local Los Angeles time (Pacific Time). Midday weekday splits are stored with commas (`08:00-13:30,14:30-16:30` and two others). `last_verified` is 2026-11-15 on every row. `verification_status` is `verified_official_locator` on every row.

## Method

- **USPS:** official USPS Location Finder API (`tools.usps.com`, `requestType` po), queried with curl the same way as the Arkansas cities. Pass 1: 5 and 15 miles around official Los Angeles ZIPs and nearby official or neighborhood ZIPs (435 ZIPs, 870 queries, 336 unique records). Pass 2 added 1, 2, 3, 10, and 20 mile widenings around core and edge ZIPs (130 queries, one added record in Piru, no new printed-Los-Angeles offices). Total 337 records (`step8-browser/los-angeles-usps-locator-2026-11-15.jsonl`). Official location pages were fetched for all 337 records (all HTTP 200 on the first try); each page's embedded `poDetail` matched the API record. Retail hours means the BUSINESS block only. Full notes: `step8-browser/los-angeles-usps-2026-11-15.md`.
- **Walmart:** not collected. The official walmart.com store locator was unavailable, so no Walmart rows are in this PR.
- **City limits:** U.S. Census Bureau Geocoder, address endpoint and coordinates endpoint, Public_AR_Current / Current_Current and Public_AR_Census2020 / Census2020_Census2020, Incorporated Places + CDPs + Counties, matching Los Angeles city GEOID 0644000 only. All 337 addresses and all 337 official locator map points on both benchmarks (`step8-browser/los-angeles-usps-geocoder-2026-11-15.jsonl`). OpenStreetMap was not used. Three offices are listed under the documented map-point fallback (printed city already Los Angeles; official map point in the city): Terminal Annex Finance, Sunset, and West Los Angeles Finance.
- Fees reuse existing rows in `data/providers/fees.csv`. No new fee rows or brands. Coordinates for USPS rows are in the notes column (lat/lng columns stay blank, as in every city CSV).

## USPS (43 listed)

Forty offices have printed city Los Angeles and address plus official map point in Los Angeles city on both Census files. Three more are listed under the map-point fallback documented in the long memo and in those CSV notes. All 43 list Domestic and Inquiry Money Orders.

Holds and in-city not-listed records are documented in the city-page "not listed" section and in `los-angeles-usps-2026-11-15.md`.

## Walmart Supercenters

Not collected in this PR. The official walmart.com store locator was unavailable. No Walmart rows, no Walmart fee citations, and no Neighborhood Markets.

## Site changes in this PR

- New `data/locations/los-angeles.csv` and `/los-angeles/`, `/los-angeles/money-orders/`, and `/los-angeles/after-hours/` pages.
- New California heading on the home "Start here" list and on `/cities/`, after Arkansas and before Colorado. Los Angeles is the first city under that heading. Home and `/cities/` meta descriptions now say "Little Rock, Fayetteville, Fort Smith, Springdale, and Jonesboro, Arkansas, and in Los Angeles, California" (home) / "… Jonesboro, Arkansas, and Los Angeles, California, and Denver …" (cities). No other city CSV or page changed except those meta and list lines. Colorado order is unchanged.
- California Census Vintage 2025 ranking memo copied to `docs/research/california-cities-census-2026-11-15.md`.
