# Gilbert, AZ: USPS locator research (2026-11-14, America/Denver)

Research only until the city pages are shipped. No business was contacted. No browser was used. last_verified: 2026-11-14. Official detail pages that were fetched are marked verification_status `verified_official_locator`. Hours below are **Arizona Time** (Mountain Standard Time). Arizona does not observe daylight saving. City-limits wording: Gilbert is legally a **town** and an incorporated place in Maricopa County (Census "Gilbert town" GEOID 0427400; SUMLEV 162). The county is Maricopa County (GEOID 04013). Gilbert is not a consolidated city-county. A USPS printed city of Gilbert is treated as agreeing with that Census place name only when the address and official map point also fall inside Gilbert town. Offices printed Gilbert whose address or map point falls outside the town are holds. Offices printed with other place names are left off, or held if they geocode inside Gilbert town. Map-point fallback applies only when the printed city already agrees and the official map point is in Gilbert town.

## Method

- **Locator:** official USPS Location Finder API (`https://tools.usps.com/UspsToolsRestServices/rest/POLocator/findLocations`, `requestType` po), queried with curl the same way as Phoenix, Tucson, and Mesa. Official Gilbert, AZ ZIP list: https://www.zip-codes.com/city/az-gilbert.asp (USPS data last updated November 1, 2026). Seven official codes: 85233, 85234, 85295, 85296, 85297, and 85298 (Standard) and 85299 (P.O. Box). Nearby official ZIPs queried in pass 1: Mesa 85201, 85202, 85204, 85210, 85212, and 85209; Chandler 85224, 85225, 85226, 85248, 85249, and 85286; Higley 85236; and Queen Creek 85142. Pass 1 (`sweep.py`): 21 ZIPs, 42 queries at 5 and 15 miles, all JSON, **40 unique Post Office records**, 0 parse failures. The four Gilbert-printed offices and the Higley office already known from the Phoenix Valley sweep were all present; 85297 and 85298 (official Gilbert ZIPs not used as Gilbert-primary in the Mesa pass) did not add a new Gilbert-printed office. Pass 2: 1, 2, 3, 10, and 20 mile widenings around 85297, 85298, 85236, 85142, 85233, and 85212 (30 queries, **2 added records**: Coolidge, printed Coolidge; and Capitol, printed Phoenix, from a 1-mile 85233 query that returned a wide default list). Total **42 records** (`usps_all.json`). Official pages and both-file geocodes for all 42 were already on file from the Phoenix, Tucson, and Mesa research (all HTTP 200, `match_api`, coordinates agree) and were copied into `/workspace/step8gil/`.
- **Official pages:** `https://tools.usps.com/locations/details/<id>` for all 42 records. All returned **HTTP 200** and each page's embedded `poDetail` matched the API record (`pages.json`). Retail hours = the BUSINESS block only. Money-order service is taken from the office's own `poDetail` services list.
- **City limits:** all 42 addresses and all 42 official locator map points against Public_AR_Current / Current_Current and Public_AR_Census2020 / Census2020_Census2020, Incorporated Places + CDPs + Counties (`usps_geo_all.jsonl`). OpenStreetMap was not used. Address no-matches for Higley and the Gilbert Roadrunner Annex were retried with expanded street names and (for Higley) city Gilbert as well as Higley; all retries still returned no match.

## Candidate includes (2), money orders yes, HTTP 200, verified_official_locator

Retail hours are Arizona Time. "Open evenings" means a weekday BUSINESS close after 17:00 (a 17:00 close does not count). "Open weekends" means Saturday or Sunday retail. Official page for each: `https://tools.usps.com/locations/details/<id>`. Both print Gilbert and have Current + 2020 address and both official map points in Gilbert town (GEOID 0427400). Both list MONEYORDERSDOM and MONEYORDERSINQ.

| ID | Office | Address | Phone | Retail (BUSINESS) hours | Evenings | Weekends | Geocode |
|---|---|---|---|---|---|---|---|
| 1364754 | GILBERT | 137 E Elliot Rd, Gilbert, AZ 85234 | 480-539-6815 | Mon-Fri 08:30-16:30; Sat 09:00-12:00; Sun closed | no | yes | Gilbert town all four legs; point 33.34954,-111.786448 |
| 1450991 | VAL VISTA | 225 S Val Vista Dr, Gilbert, AZ 85296 | 480-926-7595 | Mon-Fri 09:00-17:00; Sat 09:00-12:00; Sun closed | no | yes | Gilbert town all four legs; point 33.345929,-111.754764 |

Neither include has a weekday close after 17:00. Both have Saturday retail.

## In-town, not listed (2)

These print Gilbert and have official map points (and, for Fiesta Annex, addresses) inside Gilbert town, but they are not candidate money-order includes.

1. **FIESTA ANNEX (1451047)**, 2191 W Obispo Ave, Gilbert, AZ 85233, 480-545-1058. No money-order tags and no BUSINESS hours. Current + 2020 address and both map points: Gilbert town (GEOID 0427400). Point 33.362215,-111.8366.
2. **GILBERT ROADRUNNER ANNEX (1602698)**, 2359 E Ocotillo Rd, Gilbert, AZ 85298, 480-926-7595. No money-order tags and no BUSINESS hours. Address no-match after street-name retries on both files. Official map point 33.24816,-111.739069 is Gilbert town on both files. Printed city is already Gilbert, so the map-point fallback would apply if the office listed money orders; it does not, so it is in-town, not listed.

## HOLDS (1)

1. **HIGLEY (1366964)**, 3324 E Ray Rd, printed **Higley**, AZ 85236, 480-988-9796. Money orders yes; BUSINESS Mon-Fri 09:00-17:00, Sat 09:00-11:00. Address no-match after street-name retries and after retrying the city as both Higley and Gilbert, on both Census files. Official map point 33.321885,-111.718534: **Gilbert town** (GEOID 0427400) on both files. Held because the official printed city is Higley, not Gilbert, and the official map point falls inside Gilbert town. The map-point fallback does not apply when the printed city already disagrees.

## Left off (omissions, not holds)

37 other-printed offices in the 42-record Gilbert sweep, all outside Gilbert town on both Census files. Printed-city counts: Phoenix 10, Mesa 8, Tempe 4, Chandler 3, Scottsdale 3, Queen Creek 2, Laveen 2, and one each in Apache Junction, Sacaton, Fountain Hills, Maricopa, and Coolidge. No Queen Creek-, Apache Junction-, or Chandler-printed office geocodes inside Gilbert town. Details are in `usps_geo_all.jsonl`.

## Fetch failures

None of the 42 + 30 locator queries failed to parse. All 42 detail pages returned HTTP 200 and match the API. Address no-matches remain after retries for Higley (a hold) and the Gilbert Roadrunner Annex (in-town, not listed).
