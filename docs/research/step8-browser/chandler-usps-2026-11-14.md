# Chandler, AZ: USPS locator research (2026-11-14, America/Denver)

Research only until the city pages are shipped. No business was contacted. No browser was used. last_verified: 2026-11-14. Official detail pages that were fetched are marked verification_status `verified_official_locator`. Hours below are **Arizona Time** (Mountain Standard Time). Arizona does not observe daylight saving. City-limits wording: Chandler is an **incorporated city** in Maricopa County (Census "Chandler city" GEOID 0412000). The county is Maricopa County (GEOID 04013). Chandler is not a consolidated city-county. A USPS printed city of Chandler is treated as agreeing with that Census place name only when the address and official map point also fall inside Chandler city. Offices printed Chandler whose address or map point falls outside the city are holds. Offices printed with other place names are left off, or held if they geocode inside Chandler city. Map-point fallback applies only when the printed city already agrees and the official map point is in Chandler city.

## Method

- **Locator:** official USPS Location Finder API (`https://tools.usps.com/UspsToolsRestServices/rest/POLocator/findLocations`, `requestType` po), queried with curl the same way as the earlier Arizona cities. Official Chandler, AZ ZIP list: https://www.zip-codes.com/city/az-chandler.asp (USPS data last updated November 1, 2026). Eight official codes: 85224, 85225, 85226, 85248, 85249, and 85286 (Standard) and 85244 and 85246 (P.O. Box). 85248 also appears as an official Sun Lakes ZIP on that table. Nearby official ZIPs queried in pass 1: Gilbert 85233, 85234, 85295, 85296, 85297, and 85298; Mesa 85202 and 85210; Tempe 85281, 85282, and 85283; Phoenix-edge 85044 and 85048; Queen Creek 85142; and Maricopa 85139. Pass 1 (`sweep.py`): 23 ZIPs, 46 queries at 5 and 15 miles, all JSON, **48 unique Post Office records**, 0 parse failures. The same three Chandler-printed offices already known from the Phoenix Valley sweep were present; no Sun Lakes-printed office appeared. Pass 2: 1, 2, 3, 10, and 20 mile widenings around 85248, 85249, 85286, 85048, 85139, and 85142 (30 queries, **4 added records**: Tolleson, Downtown Glendale, and Cashion from a 1-mile 85048 query that returned a wide default list, plus Coolidge). Total **52 records** (`usps_all.json`). Official pages and both-file geocodes for all 52 were already on file from earlier Valley research (all HTTP 200, `match_api`, coordinates agree) and were copied into `/workspace/step8chn/`.
- **Official pages:** `https://tools.usps.com/locations/details/<id>` for all 52 records. All returned **HTTP 200** and each page's embedded `poDetail` matched the API record (`pages.json`). Retail hours = the BUSINESS block only. Money-order service is taken from the office's own `poDetail` services list.
- **City limits:** all 52 addresses and all 52 official locator map points against Public_AR_Current / Current_Current and Public_AR_Census2020 / Census2020_Census2020, Incorporated Places + CDPs + Counties (`usps_geo_all.jsonl`). OpenStreetMap was not used.

## Candidate includes (3), money orders yes, HTTP 200, verified_official_locator

Retail hours are Arizona Time. "Open evenings" means a weekday BUSINESS close after 17:00 (a 17:00 close does not count). "Open weekends" means Saturday or Sunday retail. Official page for each: `https://tools.usps.com/locations/details/<id>`. All three print Chandler and have Current + 2020 address and both official map points in Chandler city (GEOID 0412000). All three list MONEYORDERSDOM and MONEYORDERSINQ.

| ID | Office | Address | Phone | Retail (BUSINESS) hours | Evenings | Weekends | Geocode |
|---|---|---|---|---|---|---|---|
| 1357617 | ANDERSEN SPRINGS | 1900 W Carla Vista Dr, Chandler, AZ 85224 | 480-899-3760 | Mon-Fri 08:30-16:30; Sat 08:30-14:30; Sun closed | no | yes | Chandler city all four legs; point 33.311437,-111.875535 |
| 1357620 | CHANDLER | 101 N Colorado St, Chandler, AZ 85225 | 480-963-3673 | Mon-Fri 08:30-16:30; Sat 09:00-14:00; Sun closed | no | yes | Chandler city all four legs; point 33.30532,-111.838098 |
| 1357622 | OCOTILLO | 123 W Chandler Heights Rd, Chandler, AZ 85248 | 480-802-4811 | Mon-Fri 08:30-16:30; Sat 08:30-13:30; Sun closed | no | yes | Chandler city all four legs; point 33.232291,-111.843088. ZIP 85248 is also an official Sun Lakes ZIP; the address and official map point are in Chandler city, not the Sun Lakes CDP, so this is an include, not a hold. |

None of the three includes has a weekday close after 17:00. All three have Saturday retail.

## In-city, not listed

None. No Chandler-printed office inside Chandler city lacks money-order tags.

## HOLDS

None. No Chandler-printed office has an address or official map point outside Chandler city, and no other-printed office has an address or official map point inside Chandler city.

## Left off (omissions, not holds)

49 other-printed offices in the 52-record Chandler sweep, all outside Chandler city on both Census files. Printed-city counts: Phoenix 16, Mesa 8, Gilbert 4, Tempe 4, Scottsdale 3, Queen Creek 2, Laveen 2, Maricopa 2, and one each in Higley, Sacaton, Apache Junction, Stanfield, Tolleson, Glendale, Cashion, and Coolidge. No Sun Lakes-printed office was found. No Queen Creek-, Gilbert-, or Mesa-printed office geocodes inside Chandler city. Details are in `usps_geo_all.jsonl`.

## Fetch failures

None of the 46 + 30 locator queries failed to parse. All 52 detail pages returned HTTP 200 and match the API. No address no-matches among the three includes.
