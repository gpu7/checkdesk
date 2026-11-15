# Bridgeport, CT USPS research — 2026-11-15 (America/Denver)

Post Offices only. Official USPS Location Finder API (`POST https://tools.usps.com/UspsToolsRestServices/rest/POLocator/findLocations`, `requestType` po) and official location pages (`https://tools.usps.com/locations/details/<id>`). Retail hours are the BUSINESS block only. Money-order flags are taken only from that office's own `poDetail.services` tags (`MONEYORDERSDOM`, `MONEYORDERSINQ`). Hours on the city pages are Eastern Time. No businesses were contacted. Walmart was not collected (official walmart.com store locator unavailable).

Census place used for listing: **Bridgeport city**, GEOID **0908000**, Greater Bridgeport Planning Region GEOID **09120**. Classification matches that exact name and GEOID only. Bridgeport is coextensive with Bridgeport town. Stratford, Fairfield, Trumbull, and other nearby municipalities are not folded in.

## ZIP inventory

ZIP-Codes.com slug `https://www.zip-codes.com/city/ct-bridgeport.asp` is not a collision: the page title is Bridgeport, CT, last updated November 1, 2026. Official Bridgeport ZIPs were taken from `search.asp?fld-city=Bridgeport&fld-state=CT`. The search title says "10 ZIP Codes in Bridgeport, CT". The city page and the search results table have the same 10 unique codes, all listed as Bridgeport in Greater Bridgeport: 06601, 06602, 06604, 06605, 06606, 06607, 06608, 06610, 06673, 06699 (6 Standard, 2 P.O. Box, 2 Unique). Official unique total: 10. Nearby city and town ZIPs were added and filtered to prefixes 066, 064, and 068 (51 ZIPs in pass 1). The `ct-seymour` slug collided with Oxford (search.asp fallback, 2 ZIPs). The `ct-huntington` slug collided with Shelton (search.asp, 1 ZIP). The `ct-hamden` slug collided with New Haven (065xx dropped by the in-area filter).

## Locator sweep

- Pass 1: 51 ZIPs, 102 queries at 5 and 15 miles, 179 unique records, 0 failed queries, 4 printed Bridgeport.
- Pass 2: 110 widening queries (1, 2, 3, 10, and 20 miles) around 22 official and edge ZIPs (official 10 plus Stratford 06614/06615, Trumbull 06611, Fairfield 06824/06825, Easton 06612, Milford 06460/06461, Shelton 06484, Monroe 06468, Westport 06880, Southport 06890), 0 fails, 11 added records, all far Long Island offices (Port Jefferson, Stony Brook, Setauket, and similar), no new printed-Bridgeport offices.
- Total unique records: **190**. Raw locator dump: `bridgeport-usps-locator-2026-11-15.jsonl`.

## Official pages

All 190 official location pages returned HTTP 200 on the first try. Each page's embedded `poDetail` matched the API record on address, phone, and BUSINESS hours (`match_api` on all 190). Raw parse: `/workspace/step8bdr/pages.json`.

Four records print Bridgeport:

| locatorID | Official name | Address | ZIP | MONEYORDERS tags | BUSINESS hours |
|---|---|---|---|---|---|
| 1375148 | NOBLE | 934 E MAIN ST | 06608 | DOM + INQ | Weekdays 08:30-13:00,14:00-16:30; Saturday and Sunday closed |
| 1354281 | BAYVIEW | 115 BOSTON AVE | 06610 | DOM + INQ | Weekdays 08:30-17:00; Saturday 09:00-12:00; Sunday closed |
| 1434081 | BRIDGEPORT | 120 MIDDLE ST | 06602 | none | No BUSINESS block (lobby, PO-box access, pickup, and bulk-mail-accept blocks only) |
| 1579655 | BRIDGEPORT CT S&DC | 120 MIDDLE ST | 06602 | none | Weekdays 08:30-17:00; Saturday 08:30-13:30; Sunday closed |

## Geocoder

U.S. Census Bureau Geocoder, address and coordinates, Public_AR_Current / Current_Current and Public_AR_Census2020 / Census2020_Census2020, layers Incorporated Places + Census Designated Places + Counties. OpenStreetMap was not used. All 190 records were geocoded with no request errors. Raw: `bridgeport-usps-geocoder-2026-11-15.jsonl`.

All four printed-Bridgeport records have an address match and an official map point in Bridgeport city (GEOID 0908000) on both files. No address no-matches among them, so no street-name retries and no map-point fallbacks. The 2020 address file matches 120 Middle St to ZIP 06604 rather than the official printed ZIP 06602; both matches are still in Bridgeport city (06602 is a P.O. Box ZIP). No record that prints another city has any geocode leg in Bridgeport city. No printed-Bridgeport record falls outside the city.

## Classification

- **Listed (2):** Noble and Bayview. Both print Bridgeport, have money-order tags, and have address and official map point in Bridgeport city on both files. Neither is labeled Open evenings (Bayview's 17:00 weekday close does not count). Bayview is labeled Open weekends. Noble has a weekday midday split, stored as `08:30-13:00,14:00-16:30`.
- **HOLD, printed Bridgeport, not in the city:** none.
- **HOLD, other printed city, any geocode leg in Bridgeport city:** none.
- **In-city, not listed (2):** Bridgeport (1434081) and Bridgeport CT S&DC (1579655), both at 120 Middle St. Both print Bridgeport and sit in the city; neither official page lists money orders. The S&DC record does publish BUSINESS hours, including Saturday.

4 records print Bridgeport (2 listed + 2 not listed + 0 holds).
