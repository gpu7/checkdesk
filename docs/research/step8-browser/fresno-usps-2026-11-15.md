# Fresno, CA USPS research — 2026-11-15 (America/Denver)

Post Offices only. Official USPS Location Finder API (`POST https://tools.usps.com/UspsToolsRestServices/rest/POLocator/findLocations`, `requestType` po) and official location pages (`https://tools.usps.com/locations/details/<id>`). Retail hours are the BUSINESS block only. Money-order flags are taken only from that office's own `poDetail.services` tags (`MONEYORDERSDOM`, `MONEYORDERSINQ`). Hours on the city pages are Pacific Time. No businesses were contacted. Walmart was not collected (official walmart.com store locator unavailable).

Census place used for listing: **Fresno city**, GEOID **0627000**, Fresno County GEOID **06019**. Classification matches that exact name and GEOID only. Fresno is not a consolidated city-county. Clovis city (GEOID 0614218) is a separate incorporated city and is not folded in.

## ZIP inventory

ZIP-Codes.com slug `https://www.zip-codes.com/city/ca-fresno.asp` is not a collision: the page title is Fresno, CA, last updated November 1, 2026. Official Fresno ZIPs were taken from `search.asp?fld-city=Fresno&fld-state=CA`. The search title says "58 ZIP Codes in Fresno, CA"; the results table has 50 unique codes, all listed as Fresno. The official city page adds eight ZIPs not in search.asp (93786, 93790–93794, 93844, 93888). Official unique total: 58, all listed as Fresno. Nearby incorporated-city and neighborhood ZIPs were added and filtered to 936/937 (99 ZIPs in pass 1). The `ca-pinedale` slug collided with the Fresno city page; official ZIP 93650 is listed as Fresno (Standard, Fresno County) and also appeared in the Pinedale search.asp result.

## Locator sweep

- Pass 1: 99 ZIPs, 198 queries at 5 and 15 miles, 72 unique records, 0 failed queries, 11 printed Fresno.
- Pass 2: 355 widening queries (1, 2, 3, 10, and 20 miles) around 71 official and edge ZIPs, 0 fails, 2 added records far from the city (Coarsegold and Santa Rita Park), no new printed-Fresno offices.
- Total unique records: **74**. Raw locator dump: `fresno-usps-locator-2026-11-15.jsonl`.

All 74 official pages returned HTTP 200 on the first try. Embedded `poDetail` matched the API record on all 74 (`match_api`).

## Geocoding

U.S. Census Bureau Geocoder, address endpoint and coordinates endpoint, Public_AR_Current / Current_Current and Public_AR_Census2020 / Census2020_Census2020, layers Incorporated Places, Census Designated Places, and Counties. All 74 addresses and all 74 official locator map points were geocoded on both files (`fresno-usps-geocoder-2026-11-15.jsonl`). The geocoder used each office's printed state (CA). OpenStreetMap was not used.

Address retries were run for the printed-Fresno office with a no-match on either file:

- Clinter (1358393), 2601 E Olive Ave: 2020 file matches 2601 E OLIVE AVE, FRESNO, CA, 93701 in Fresno city; current file still no-match after street-name retries (OLIVE AVENUE, EAST OLIVE AVE, and similar). A retry that dropped the leading E snapped the geocoder to 2601 W OLIVE AVE, FRESNO, CA, 93728 (the opposite side of Olive Avenue), which is not treated as a match for the official East Olive Avenue address. Has money-order tags. Official point (36.758131, -119.779874) in Fresno city on both files.

## Classification (74 records)

- **8 listed.** Printed city Fresno; money-order tags present. 7 have address and official map point in Fresno city on both Census files. 1 listed under map-point fallback, as documented above (Clinter). All 8 are in Fresno County. 0 Open evenings. 5 Open weekends (Saturday retail; no Sunday hours): Clinter, Cardwell, Hughes, Woodward Park, and East Fresno. Pinedale, the Fresno Post Office, and Tower have no weekend hours. Official names kept, including Pinedale, Clinter, Woodward Park, East Fresno, and Tower. Pinedale prints FRESNO and is listed. Tower has a weekday midday split (09:00-12:30,13:00-16:00).
- **1 in-city, not listed.** Printed Fresno; all four geocode legs in Fresno city; no money-order tags. Civic Center Fresno (1532916) at 855 M St Ste 190 (BUSINESS hours 09:00-16:00 weekdays, no Saturday).
- **2 HOLD, printed Fresno, not in Fresno city.** Barton (1490835), 2382 S Cedar Ave 93725, and Calwa (1356686), 4026 E Jensen Ave 93725: both print Fresno; the address and official map point are in Calwa CDP (Fresno County, GEOID 06019), with no incorporated place, on both files. Both have money orders. Calwa has a weekday midday split. Map-point fallback does not apply because the official points are not in Fresno city.
- **0 HOLD, other printed city, in Fresno city.**
- **63 left off.** Other printed cities fully outside Fresno city, including the two Clovis records at 655 Minnewawa Ave (Clovis city, GEOID 0614218), plus Madera, Sanger, Fowler, Selma, Kerman, and others.

11 records print Fresno (8 listed + 1 in-city not listed + 2 Calwa-CDP holds).

No Walmart rows. IDs are `usps-fresno-<locatorID>`. `last_verified` 2026-11-15. `verification_status` `verified_official_locator`. One listed office used the map-point fallback, as documented above.
