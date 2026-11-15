# Little Rock, AR: USPS locator research (2026-11-15, America/Denver)

Research only. No pages, PRs, or deploys until Richard approves the Arkansas five-city list. No business was contacted. No browser was used. last_verified: 2026-11-15. Official detail pages that were fetched are marked verification_status `verified_official_locator`. Hours below are **Central Time**. Arkansas observes daylight saving (this date is Central Standard Time). City-limits wording: Little Rock is an **incorporated city** in Pulaski County (Census "Little Rock city" GEOID 0541000). The county is Pulaski County (GEOID 05119). Little Rock is not a consolidated city-county. North Little Rock is a separate incorporated city (GEOID 0550450) in the same county. A USPS printed city of Little Rock is treated as agreeing with that Census place name only when the address and official map point also fall inside Little Rock city. Offices printed Little Rock whose address or map point falls outside the city are holds. Offices printed with other place names are left off, or held if they geocode inside Little Rock city. Map-point fallback applies only when the printed city already agrees and the official map point is in Little Rock city.

Raw records are under `/workspace/step8lrk/`.

## Method

- **Locator:** official USPS Location Finder API (`https://tools.usps.com/UspsToolsRestServices/rest/POLocator/findLocations`, `requestType` po), queried with curl the same way as Phoenix. Official Little Rock, AR ZIP list: https://www.zip-codes.com/city/ar-little-rock.asp (USPS data last updated November 1, 2026). The official table lists **36** codes: 72201, 72202, 72204–72207, 72209–72212, 72223, and 72227 (Standard); 72203, 72214–72217, 72219, 72221, 72222, 72225, 72231, 72260, and 72295 (P.O. Box); 72255 (Unique); plus 11 North Little Rock / Sherwood codes that also appear on this Little Rock page (72113, 72114, 72116–72118, 72120 Standard; 72115, 72119, 72124, 72190 P.O. Box; 72199 Unique). Those 11 are also the official North Little Rock set returned by ZIP-Codes.com search.asp for “North Little Rock, AR” (11 results). Nearby official ZIPs not already on that list, queried in pass 1: Alexander 72002; Benton 72015, 72018, 72019, 72022, and 72158; Bryant 72089 (plus 72015, 72019, and 72022, already on the Benton list; Bryant’s city page slug redirects to Benton); Cabot 72023; Conway 72032, 72033, 72034, and 72035; England 72046; Jacksonville 72076, 72078, and 72099; Lonoke 72086; Mabelvale / Shannon Hills 72103; Wrightsville 72183; and Pine Bluff 71601, 71602, and 71603. Shannon Hills’ official ZIP is 72103 (Mabelvale page; search.asp for Shannon Hills returns that one code). Pass 1 (`sweep.py`): **58 ZIPs, 116 queries** at 5 and 15 miles, all JSON, **69 unique Post Office records**, 0 parse failures. Pass 2: 1, 2, 3, 10, and 20 mile widenings around edge Little Rock and fringe ZIPs 72223, 72210, 72212, 72183, 72002, 72023, 72032, 71601, 71603, 72046, 72086, 72015, 72076, and 72206 (70 queries, **20 added records**, all far from Little Rock city: Paron, McRae, Morrilton, Malvern, Sheridan, and similar). Some 1-mile queries returned a wide default list, the same locator quirk seen in Arizona; the union of all radii is the source of truth. Total **89 records** (`usps_all.json`).
- **Official pages:** `https://tools.usps.com/locations/details/<id>` fetched with curl for all 89 records. All returned **HTTP 200 on the first try**. Each page’s embedded `poDetail` matched the API record on name, address, phone, BUSINESS hours, and map coordinates (`pages.json`, `match_api` on all 89). Retail hours = the BUSINESS block only. Money-order service is taken from the office’s own `poDetail` services list.
- **City limits:** all 89 addresses and all 89 official locator map points against Public_AR_Current / Current_Current and Public_AR_Census2020 / Census2020_Census2020, Incorporated Places + CDPs + Counties (`usps_geo_all.jsonl`). OpenStreetMap was not used.

## Candidate includes (10), money orders yes, HTTP 200, verified_official_locator

Retail hours are Central Time. “Open evenings” means a weekday BUSINESS close after 17:00 (a 17:00 close does not count). “Open weekends” means Saturday or Sunday retail. Official page for each: `https://tools.usps.com/locations/details/<id>`. All ten print Little Rock and have Current + 2020 address and both official map points in Little Rock city (GEOID 0541000) / Pulaski County (GEOID 05119). All ten list MONEYORDERSDOM and MONEYORDERSINQ.

| ID | Office | Address | Phone | Retail (BUSINESS) hours | Evenings | Weekends | Geocode |
|---|---|---|---|---|---|---|---|
| 1383332 | STATE CAPITOL | 500 Woodlane St Ste 136, Little Rock, AR 72201 | 501-372-8998 | Mon-Fri 10:00-13:00; Sat/Sun closed | no | no | Little Rock city all four legs; point 34.746645,-92.2890829 |
| 1353468 | ASHER | 7401 Colonel Glenn Rd, Little Rock, AR 72204 | 501-562-5250 | Mon-Fri 08:30-17:00; Sat 09:30-12:00; Sun closed | no | yes | Little Rock city all four legs; point 34.715389,-92.3573689 |
| 1355646 | BRADY | 8509 W Markham St, Little Rock, AR 72205 | 501-219-2933 | Mon-Fri 08:00-17:00; Sat 10:00-13:00; Sun closed | no | yes | Little Rock city all four legs; point 34.752483,-92.3692179 |
| 1366987 | HILLCREST | 2803 Kavanaugh Blvd, Little Rock, AR 72205 | 501-663-2265 | Mon-Fri 08:30-17:00; Sat/Sun closed | no | no | Little Rock city all four legs; point 34.757596,-92.3244819 |
| 1382280 | SOUTHSIDE | 1700 Main St, Little Rock, AR 72206 | 501-374-5382 | Mon-Fri 08:30-17:00; Sat 10:00-13:00; Sun closed | no | yes | Little Rock city all four legs; point 34.731539,-92.27402 |
| 1363693 | FOREST PARK | 5420 Kavanaugh Blvd, Little Rock, AR 72207 | 501-666-5126 | Mon-Fri 08:30-17:00; Sat 10:00-13:00; Sun closed | no | yes | Little Rock city all four legs; point 34.770385,-92.334474 |
| 1367929 | INDUSTRIAL | 6909 Baseline Rd, Little Rock, AR 72209 | 501-565-1253 | Mon-Fri 08:30-17:00; Sat 09:30-12:00; Sun closed | no | yes | Little Rock city all four legs; point 34.668797,-92.354562 |
| 1432896 | OTTER CREEK | 13501 Otter Creek Pkwy, Little Rock, AR 72210 | 501-407-9443 | Mon-Fri 10:00-13:00, 14:00-16:00; Sat/Sun closed | no | no | Little Rock city all four legs; point 34.657801,-92.428539. Midday closure; a future CSV row must use a comma between windows, not a slash. |
| 1387380 | WESTSIDE | 11415 Huron Ln, Little Rock, AR 72211 | 501-225-2307 | Mon-Fri 09:00-18:00; Sat 10:00-14:00; Sun closed | yes | yes | Little Rock city all four legs; point 34.765713,-92.4009409 |
| 1357782 | CHENAL | 815 Technology Dr, Little Rock, AR 72223 | 501-821-6299 | Mon-Fri 09:15-17:30; Sat 09:00-13:00; Sun closed | yes | yes | Little Rock city all four legs; point 34.761942,-92.452148 |

Two of the ten includes have a weekday close after 17:00 (Westside 18:00, Chenal 17:30). Seven have Saturday retail. None publishes Sunday retail.

## In-city, not listed (2)

These print Little Rock and geocode inside Little Rock city on both files, but they are not candidate money-order includes.

1. **BRADY ANNEX (1355651)**, 8313 W Markham St, Little Rock, AR 72205, 501-223-9934. No money-order tags and no BUSINESS hours. Point 34.752798,-92.365997, Little Rock city on all four legs.
2. **LITTLE ROCK (1370647)**, 600 E Capitol Ave, Little Rock, AR 72202, 501-375-2644. No money-order tags. BUSINESS Mon-Fri 07:00-17:30, Sat/Sun closed (evenings, but not listable without money-order tags). Point 34.743902,-92.264905, Little Rock city on all four legs. This is the city’s main Post Office name; it is not listed as a money-order location.

## HOLDS (3)

1. **GMF BOX SECTION (1439300)**, 4700 E McCain Blvd, printed **Little Rock**, AR 72231, 501-355-6335. No money-order tags. BUSINESS Mon-Fri 09:00-18:30, Sat/Sun closed. Current + 2020 address and both official map points: **North Little Rock city** (GEOID 0550450), Pulaski County, not Little Rock city. Point 34.787521,-92.209436. Held because the printed city is Little Rock but the address and official map point fall in a separate incorporated city. ZIP 72231 appears as a Little Rock P.O. Box code (with a North Little Rock alias) on the Little Rock ZIP-Codes.com page.
2. **MABELVALE (1371292)**, 10715 Mabelvale West Rd, printed **Mabelvale**, AR 72103, 501-455-2318. Money orders yes; BUSINESS Mon-Fri 08:30-16:30, Sat 09:00-12:00. Current + 2020 address and both official map points: **Little Rock city** (GEOID 0541000). Point 34.655197,-92.3971349. Held because the official printed city is Mabelvale, not Little Rock, and the address and official map point fall inside Little Rock city. The map-point fallback does not apply when the printed city already disagrees. 72103 is the official Mabelvale / Shannon Hills ZIP.
3. **ALEXANDER (1352652)**, 15604 Alexander Rd, printed **Alexander**, AR 72002, 501-455-1637. Money orders yes; BUSINESS Mon-Fri 08:30-10:30, 11:30-16:30, Sat 09:00-11:00. Current + 2020 **address**: Little Rock city (GEOID 0541000). Official map point 34.631975,-92.4430419: **Alexander city** (GEOID 0500580) on both files. Held because the official printed city is Alexander, not Little Rock, and the address falls inside Little Rock city (the official map point is in Alexander city). The map-point fallback does not apply when the printed city already disagrees.

## Left off (omissions, not holds)

74 other-printed offices in the 89-record sweep, all outside Little Rock city on both Census files (or otherwise printed with another place name and geocoding outside Little Rock city). Nearby other-city offices include, among others: NORTH LITTLE ROCK 1375370, PARKHILL 1376803, and ROSE CITY 1379862 (all North Little Rock city; the North Little Rock office itself lists Saturday hours but no money-order tags); SHERWOOD 1438600 (Sherwood city; current-file address no-match, 2020 address and both points in Sherwood city); GRAVEL RIDGE 1438584 (prints Jacksonville; address no-match both files; official map point in Sherwood city); LITTLE ROCK AIR FORCE BASE 1439342 and JACKSONVILLE 1368214 (Jacksonville city); MAUMELLE 1438595 (Maumelle city); BRYANT 1356173 (Bryant city); BENTON 1354695 (Benton city); CABOT 1356560 (Cabot city); WRIGHTSVILLE 1388349 (address no-match both files; official map point in Wrightsville city); COLLEGE STATION 1358673 (College Station CDP); SWEET HOME 1384117 (Sweet Home CDP); plus Conway, Pine Bluff, and farther pass-2 offices. No Cammack Village-printed office was found, and no office geocoded in Cammack Village city. Details and remaining address no-matches among far offices are in `usps_geo_all.jsonl`.

## Fetch failures

None of the 116 + 70 locator queries failed to parse. All 89 detail pages returned HTTP 200 on the first try and match the API. No address no-matches among the ten includes. The three holds all had complete address and map-point results (no retries required).

## Summary counts (if this city is later approved and shipped, USPS-only)

- **10** listable offices, all money orders
- **2** Open evenings (Westside, Chenal)
- **7** Open weekends (Asher, Brady, Southside, Forest Park, Industrial, Westside, Chenal)
- **3** holds (GMF Box Section, Mabelvale, Alexander)
- **2** in-city, not listed (Brady Annex; Little Rock / 600 E Capitol Ave)
- **74** other-printed offices left off
- No Walmart rows were collected. A curl-only check of `https://www.walmart.com/store/directory/al/birmingham` on 2026-11-15 still redirected (HTTP 307) to `/blocked` and returned the “Robot or human?” page with “activate and hold the button to confirm that you’re human” (PerimeterX `px-captcha`). The block was not bypassed.
