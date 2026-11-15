# San Francisco, CA USPS research — 2026-11-15 (America/Denver)

Post Offices only. Official USPS Location Finder API (`POST https://tools.usps.com/UspsToolsRestServices/rest/POLocator/findLocations`, `requestType` po) and official location pages (`https://tools.usps.com/locations/details/<id>`). Retail hours are the BUSINESS block only. Money-order flags are taken only from that office's own `poDetail.services` tags (`MONEYORDERSDOM`, `MONEYORDERSINQ`). Hours on the city pages are Pacific Time. No businesses were contacted. Walmart was not collected (official walmart.com store locator unavailable).

Census place used for listing: **San Francisco city**, GEOID **0667000**, a consolidated city-county coextensive with San Francisco County GEOID **06075** (FUNCSTAT C). Classification matches that exact place name and GEOID only (SUMLEV 162). South San Francisco city (GEOID 0673262, San Mateo County) is a separate incorporated city and is not folded in. Do not confuse with San Jose GEOID 0668000 or San Diego GEOID 0666000.

## ZIP inventory

ZIP-Codes.com slug `https://www.zip-codes.com/city/ca-san-francisco.asp` is not a collision: the page title is San Francisco, CA, last updated November 1, 2026. Official San Francisco ZIPs were taken from `search.asp?fld-city=San Francisco&fld-state=CA`. The search title says "53 ZIP Codes in San Francisco, CA". The results table has 53 unique codes: 51 listed as San Francisco and 2 listed as South San Francisco (94080 and 94083, San Mateo County). 94128 is listed as San Francisco but in San Mateo County (SFO). The official city page adds three ZIPs not in search.asp (94172, 94177, 94188). Official unique total: 53. Nearby incorporated-city and neighborhood ZIPs were added from city pages and search.asp and filtered to 940/941/945/946/947/948/949, plus five San Mateo 944xx peninsula ZIPs included in the pass 1 file (151 ZIPs in pass 1).

## Locator sweep

- Pass 1: 151 ZIPs, 302 queries at 5 and 15 miles, 211 unique records, 0 failed queries, 40 printed San Francisco. Two South San Francisco offices appeared (Chestnut 1357881 and Linden 1370530).
- Pass 2: 335 widening queries (1, 2, 3, 10, and 20 miles) around 67 official and edge ZIPs (official 53 plus Daly City, Brisbane, San Bruno, Pacifica, Oakland waterfront, Alameda, Sausalito, Tiburon, and San Mateo edge ZIPs), 0 fails, 2 added records far from the city (Casa Correo in Concord and Clayton in Clayton), no new printed-San-Francisco offices.
- Total unique records: **213**. Raw locator dump: `san-francisco-usps-locator-2026-11-15.jsonl`.

All 213 official pages returned HTTP 200 on the first try. Embedded `poDetail` matched the API record on all 213 (`match_api`).

## Geocoding

U.S. Census Bureau Geocoder, address endpoint and coordinates endpoint, Public_AR_Current / Current_Current and Public_AR_Census2020 / Census2020_Census2020, layers Incorporated Places, Census Designated Places, and Counties. All 213 addresses and all 213 official locator map points were geocoded on both files (`san-francisco-usps-geocoder-2026-11-15.jsonl`). The geocoder used each office's printed state (CA). OpenStreetMap was not used.

Address retries were run for printed-San-Francisco offices with a no-match on either file:

- Diamond Heights (1360815), 5262 Diamond Heights Blvd: current file matches in San Francisco city; 2020 file still no-match after street-name retries (DIAMOND HEIGHTS BOULEVARD and DIAMOND HEIGHTS BLVD.). Has money-order tags. Official point in San Francisco city on both files.
- Lakeshore Plaza (1369681), 1543 Sloat Blvd: current file matches in San Francisco city; 2020 file still no-match after street-name retries (SLOAT BOULEVARD and SLOAT BLVD.). Has money-order tags. Official point in San Francisco city on both files.
- Marina (1371854), 2055 Lombard St: 2020 file matches in San Francisco city; current file still no-match after street-name retries (LOMBARD STREET, LOMBARD ST., and LOMBARD). Has money-order tags. Official point in San Francisco city on both files.
- Bryant Street (1454203), 1600 Bryant St 94141: 2020 file matches 1600 BRYANT ST, SAN FRANCISCO, CA, 94103 in San Francisco city; current file still no-match after street-name retries and a retry that used the 2020 matched ZIP 94103. Has money-order tags. Official point in San Francisco city on both files.
- Presidio (1486545), 558 Presidio Blvd Ste B: official street no-match on both files. Retries that dropped the unit STE B made the geocoder snap to 558 PRESIDIO AVE, SAN FRANCISCO, CA, 94115 (a different street name and ZIP), which is not treated as a match for the official Presidio Boulevard address. Has money-order tags (Domestic Money Orders only). Official point (37.798539, -122.451416) in San Francisco city on both files.
- San Francisco Gen Del (1492402), 391 Ellis St: 2020 file matches in San Francisco city; current file still no-match after street-name retries. No money-order tags and no BUSINESS hours. Official point in San Francisco city on both files.

## Classification (213 records)

- **31 listed.** Printed city San Francisco; money-order tags present. 26 have address and official map point in San Francisco city on both Census files. 5 listed under map-point fallback, as documented above (Diamond Heights, Lakeshore Plaza, Marina, Bryant Street, and Presidio). All 31 are in San Francisco County. 7 Open evenings: Pine Street (weekday close 18:00); Clayton Street, Golden Gate, Geary, Lakeshore Plaza, and Bryant Street (weekday close 17:30); and San Francisco P&DC Finance (weekday close 20:30). 22 Open weekends (Saturday retail; no Sunday hours). The nine listed offices with no weekend hours are Federal Building San Fran, Fox Plaza, Sutter Street, Brannan Street, Bernal Heights, Gateway San Francisco, Bayview, Presidio, and McLaren. Official names kept, including Federal Building San Fran, North Beach PRS, San Francisco P&DC Finance, Gateway San Francisco, Mission San Francisco, and Presidio. The Presidio office prints SAN FRANCISCO and is listed. Four listed offices have a weekday midday split: Federal Building San Fran, Presidio, McLaren, and Visitacion.
- **9 in-city, not listed.** Printed San Francisco; geography in San Francisco city (including one map-point-fallback geography); no money-order tags. West Portal (1387159, Saturday BUSINESS hours); San Francisco (1440671) and San Francisco Coll Unit (1489618) at 1300 Evans Ave (no BUSINESS; same building as the listed P&DC Finance office); Townsend Carrier Annex (1450964) and San Francisco CA Townsd SDC (1613877) at 550 Townsend St (no BUSINESS); North Beach Annex (1440884, no BUSINESS); Mendell Carrier Annex (1451583, no BUSINESS); Napoleon Street Carrier Cplx (1451705, no BUSINESS); San Francisco Gen Del (1492402, no BUSINESS; current address no-match after retries, official point in the city).
- **0 HOLD, printed San Francisco, not in San Francisco city.**
- **0 HOLD, other printed city, in San Francisco city.** The map-point fallback was not needed for a printed-city disagreement, because none occurred.
- **173 left off.** Other printed cities fully outside San Francisco city, including Oakland (14), Berkeley (8), Fremont (6), Daly City (4), and the two South San Francisco offices (Chestnut 1357881 and Linden 1370530), whose addresses and official map points are in South San Francisco city (GEOID 0673262) on both files.

40 records print San Francisco (31 listed + 9 in-city not listed).

No Walmart rows. IDs are `usps-san-francisco-<locatorID>`. `last_verified` 2026-11-15. `verification_status` `verified_official_locator`. Five listed offices used the map-point fallback, as documented above.
