# San Jose, CA USPS research — 2026-11-15 (America/Denver)

Post Offices only. Official USPS Location Finder API (`POST https://tools.usps.com/UspsToolsRestServices/rest/POLocator/findLocations`, `requestType` po) and official location pages (`https://tools.usps.com/locations/details/<id>`). Retail hours are the BUSINESS block only. Money-order flags are taken only from that office's own `poDetail.services` tags (`MONEYORDERSDOM`, `MONEYORDERSINQ`). Hours on the city pages are Pacific Time. No businesses were contacted. Walmart was not collected (official walmart.com store locator unavailable).

Census place used for listing: **San Jose city**, GEOID **0668000**, Santa Clara County GEOID **06085**. Classification matches that exact name and GEOID only.

## ZIP inventory

ZIP-Codes.com slug `https://www.zip-codes.com/city/ca-san-jose.asp` is a collision: the page is Alviso, CA (last updated November 1, 2026), official ZIP 95002. Official San Jose ZIPs were taken from `search.asp?fld-city=San Jose&fld-state=CA`. The search title says "60 ZIP Codes in San Jose, CA"; the results table has 50 unique codes, including Alviso 95002, Mount Hamilton 95140, and 95025 listed as San Jose in San Benito County. Nearby incorporated-city and neighborhood ZIPs were added and filtered to 940/943/945/950/951 (111 ZIPs in pass 1). East Palo Alto's city-page slug collided with Palo Alto; search.asp returned 94303, already in the set.

## Locator sweep

- Pass 1: 111 ZIPs, 222 queries at 5 and 15 miles, 119 unique records, 0 failed queries, 19 printed San Jose.
- Pass 2: 285 widening queries (1, 2, 3, 10, and 20 miles) around 57 core and edge ZIPs, 0 fails, 2 added records (Davenport 95017 and Livermore CA SDC 94550), no new printed-San-Jose offices.
- Total unique records: **121**. Raw locator dump: `san-jose-usps-locator-2026-11-15.jsonl`.

All 121 official pages returned HTTP 200 on the first try. Embedded `poDetail` matched the API record on all 121 (`match_api`).

## Geocoding

U.S. Census Bureau Geocoder, address endpoint and coordinates endpoint, Public_AR_Current / Current_Current and Public_AR_Census2020 / Census2020_Census2020, layers Incorporated Places, Census Designated Places, and Counties. All 121 addresses and all 121 official locator map points were geocoded on both files (`san-jose-usps-geocoder-2026-11-15.jsonl`). The geocoder used each office's printed state (CA). OpenStreetMap was not used.

## Classification (121 records)

- **9 listed.** Printed city San Jose; money-order tags present; address and official map point in San Jose city on both Census files. 1 Open evenings (Willow Glen, weekday close 17:30). 7 Open weekends (Saturday retail; no Sunday hours). Saint James Park and Bayside have no weekend hours. Official names kept, including Saint James Park, Cambrian Park, and Willow Glen. Willow Glen prints SAN JOSE and is listed.
- **9 in-city, not listed.** Printed San Jose; all four geocode legs in San Jose city; no money-order tags. San Jose (1440673) and San Jose MO Finance (1448614) at 1750 Lundy Ave (no BUSINESS); Seven Trees Annex (1381245, no BUSINESS); Colonnade (1358734, midday BUSINESS); Eastridge (1361946, weekday close 19:00); Oakridge Mall (1375807, last weekday window ends 18:00); Garden (1364429); Parkmoor (1376852, Saturday hours); Foothill (1484522, Saturday hours).
- **1 HOLD, printed San Jose, not in San Jose city.** New Almaden (1374624), 21300 Almaden Rd 95120: the Census address match is 21300 ALMADEN RD, SAN JOSE, CA, 95120 on both files, but the address and official map point are in unincorporated Santa Clara County (GEOID 06085), with no incorporated place and no CDP, on both files. Has money orders. Map-point fallback does not apply because the official point is not in San Jose city.
- **1 HOLD, other printed city, in San Jose city.** Alviso (1440406), 1525 Gold St, prints Alviso; all four legs in San Jose city. Has money orders and a weekday midday split. The map-point fallback does not apply when the printed city already disagrees.
- **101 left off.** Other printed cities fully outside San Jose city, including Fremont (6), Sunnyvale (4), Santa Clara (4), Campbell (3), Milpitas, Cupertino, Los Gatos, Morgan Hill, and others.

19 records print San Jose (9 listed + 9 in-city not listed + 1 New Almaden hold).

No Walmart rows. IDs are `usps-san-jose-<locatorID>`. `last_verified` 2026-11-15. `verification_status` `verified_official_locator`. No map-point fallbacks were used for listed offices.
