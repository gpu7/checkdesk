# Jonesboro, AR: USPS locator research (2026-11-15, America/Denver)

Research only until the city pages are shipped. No business was contacted. No browser was used. last_verified: 2026-11-15. Official detail pages that were fetched are marked verification_status `verified_official_locator`. Hours below are **Central Time**. Arkansas observes daylight saving. City-limits wording: Jonesboro is an **incorporated city** in Craighead County (Census "Jonesboro city" GEOID 0535710). The county is Craighead County (GEOID 05031). Jonesboro is not a consolidated city-county. A USPS printed city of Jonesboro is treated as agreeing with that Census place name only when the address and official map point also fall inside Jonesboro city. Offices printed Jonesboro whose address or map point falls outside the city are holds. Offices printed with other place names are left off, or held if they geocode inside Jonesboro city. Map-point fallback applies only when the printed city already agrees and the official map point is in Jonesboro city.

Raw records are under `/workspace/step8jbr/`.

## Method

- **Locator:** official USPS Location Finder API (`https://tools.usps.com/UspsToolsRestServices/rest/POLocator/findLocations`, `requestType` po), queried with curl the same way as the earlier Arkansas cities. Official Jonesboro, AR ZIP list: https://www.zip-codes.com/city/ar-jonesboro.asp (USPS data last updated November 1, 2026). The official table lists **5** codes: 72401, 72404, and 72405 (Standard); 72402 and 72403 (P.O. Box). Nearby official ZIPs not already on that list, queried in pass 1: Bono 72416; Brookland 72417; Bay 72411; Cash 72421; Monette 72447; Lake City 72437; Trumann 72472; Marked Tree 72365; Paragould 72450 and 72451; Walnut Ridge 72476; Hoxie 72433; Pocahontas 72455; Harrisburg 72432; Weiner 72479; Egypt 72427; Caraway 72419; Black Oak 72414; Leachville 72438; Manila 72442; Blytheville 72315, 72316, and 72319; Osceola 72370; Newport 72112; Alicia 72410; Minturn 72445; Sedgwick 72465; Swifton 72471; and State University 72467. The official Bay, AR page also lists 71651 alongside 72411, and the official State University, AR page also lists Unique 71999 alongside 72467; those two codes were added in pass 2. The `ar-college-city` slug was not found. Pass 1 (`sweep.py`): **35 ZIPs, 70 queries** at 5 and 15 miles, all JSON, **86 unique Post Office records**, 0 parse failures. Pass 2: 5 and 15 miles around 71651 and 71999, plus 1, 2, 3, 10, and 20 mile widenings around 72401, 72404, 72405, 72467, 72416, 72417, 72450, 72112, 71651, and 71999 (54 queries, **25 added records**, all far from Jonesboro city; 71651 and 71999 returned south-Arkansas offices such as Jersey and Arkadelphia). Total **111 records** (`usps_all.json`). Only six offices print Jonesboro; no additional Jonesboro-printed office appeared in pass 2.
- **Official pages:** `https://tools.usps.com/locations/details/<id>` fetched with curl for all 111 records. All returned **HTTP 200 on the first try**. Each page’s embedded `poDetail` matched the API record (`pages.json`, `match_api` on all 111). Retail hours = the BUSINESS block only. Money-order service is taken from the office’s own `poDetail` services list.
- **City limits:** all 111 addresses and all 111 official locator map points against Public_AR_Current / Current_Current and Public_AR_Census2020 / Census2020_Census2020, Incorporated Places + CDPs + Counties (`usps_geo_all.jsonl`). OpenStreetMap was not used.

## Candidate includes (3), money orders yes, HTTP 200, verified_official_locator

Retail hours are Central Time. “Open evenings” means a weekday BUSINESS close after 17:00 (a 17:00 close does not count). “Open weekends” means Saturday or Sunday retail. Official page for each: `https://tools.usps.com/locations/details/<id>`. All three print Jonesboro and have Current + 2020 address and both official map points in Jonesboro city (GEOID 0535710) / Craighead County (GEOID 05031). All three list MONEYORDERSDOM and MONEYORDERSINQ.

| ID | Office | Address | Phone | Retail (BUSINESS) hours | Evenings | Weekends | Geocode |
|---|---|---|---|---|---|---|---|
| 1368521 | CARAWAY JONESBORO | 2404 Race St, Jonesboro, AR 72401 | 870-932-1261 | Mon-Fri 08:30-17:00; Sat 09:00-12:00; Sun closed | no | yes | Jonesboro city all four legs; point 35.814876,-90.6753349 |
| 1442231 | DOWNTOWN JONESBORO | 310 East St Ste C, Jonesboro, AR 72401 | 870-933-6857 | Mon-Fri 08:30-15:00; Sat closed; Sun closed | no | no | Jonesboro city all four legs; point 35.839905,-90.702322 |
| 1374605 | NETTLETON | 4808 E Nettleton Ave, Jonesboro, AR 72401 | 870-932-4374 | Mon-Fri 09:00-13:00, 14:00-16:00; Sat closed; Sun closed | no | no | Jonesboro city all four legs; point 35.818951,-90.65092 |

None of the three includes has a weekday close after 17:00. One has Saturday retail (Caraway Jonesboro, 09:00-12:00). None publishes Sunday retail. The CSV stores Nettleton’s midday split with commas (`09:00-13:00,14:00-16:00`), not slashes.

## In-city, not listed (3)

All three print Jonesboro and have all four geocode legs in Jonesboro city (GEOID 0535710). None lists money-order tags. None publishes a BUSINESS hours block.

1. **JONESBORO (1368525)**, 2404 Race St, Jonesboro, AR 72401, 870-932-4057. Same address and official map point as the listed Caraway Jonesboro office. Official page services are pickup- and referral-related only.
2. **NORTHEAST ARKANSAS (1473451)**, 3405 Moore Rd, Jonesboro, AR 72401, 870-931-5763. Official page has no BUSINESS block.
3. **JONESBORO AR SDC (1599137)**, 3405 Moore Rd, Jonesboro, AR 72401, 870-932-4057. Same address as Northeast Arkansas (map points differ by a few feet). Official page has no BUSINESS block.

## HOLDS (1)

1. **STATE UNIVERSITY (1454626)**, 105 N Caraway, printed **State University**, AR 72467, 870-932-7192. Money orders yes; BUSINESS Mon-Fri 08:00-16:00, Sat closed. Address matches 105 N CARAWAY RD, STATE UNIVERSITY, AR, 72467 on both Census files, and both the address and the official map point 35.841637,-90.6772429 are in **Jonesboro city** (GEOID 0535710) / Craighead County on both files. Held because the official printed city is State University, not Jonesboro. The map-point fallback does not apply when the printed city already disagrees.

## Left off (omissions, not holds)

104 other-printed offices in the 111-record Jonesboro sweep, all outside Jonesboro city on both Census files (111 minus 6 Jonesboro-printed minus 1 State University hold). Nearby other-city offices include Brookland, Bono, Bay, Paragould, Trumann, Lake City, Walnut Ridge, Hoxie, Harrisburg, Caraway (the Caraway city office, not Caraway Jonesboro), and farther offices, including the south-Arkansas records returned from official Bay ZIP 71651 and official State University Unique ZIP 71999. Details and remaining address no-matches among far offices are in `usps_geo_all.jsonl`.

## Fetch failures

None of the 70 + 54 locator queries failed to parse. All 111 detail pages returned HTTP 200 on the first try and match the API. No address no-matches among the six Jonesboro-printed records or the State University hold.

## Summary counts (USPS-only)

- **3** listable offices, all money orders
- **0** Open evenings
- **1** Open weekends (Caraway Jonesboro)
- **1** hold (State University)
- **3** in-city, not listed (Jonesboro at 2404 Race St; Northeast Arkansas and Jonesboro AR SDC at 3405 Moore Rd)
- **104** other-printed offices left off
