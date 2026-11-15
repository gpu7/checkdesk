# Los Angeles, CA USPS research — 2026-11-15 (America/Denver)

Post Offices only. Official USPS Location Finder API (`POST https://tools.usps.com/UspsToolsRestServices/rest/POLocator/findLocations`, `requestType` po) and official location pages (`https://tools.usps.com/locations/details/<id>`). Retail hours are the BUSINESS block only. Money-order flags are taken only from that office's own `poDetail.services` tags (`MONEYORDERSDOM`, `MONEYORDERSINQ`). Hours on the city pages are Pacific Time. No businesses were contacted. Walmart was not collected (official walmart.com store locator unavailable).

Census place used for listing: **Los Angeles city**, GEOID **0644000**, Los Angeles County GEOID **06037**. Classification matches that exact name and GEOID only, so East Los Angeles CDP and Lake Los Angeles CDP cannot count as the city.

## ZIP inventory

Official ZIP-Codes.com city page: https://www.zip-codes.com/city/ca-los-angeles.asp (USPS data last updated November 1, 2026). 102 codes listed for Los Angeles, CA (69 Standard, 24 P.O. Box, 9 Unique). That official list includes 90230 and Antelope Valley 93535 / 93550 / 93591 (Lake Los Angeles CDP area). Those were queried but classified by printed city and Census place, not by the ZIP list.

Many neighborhood postal ZIPs (for example Van Nuys 91401 and San Pedro 90731) are **not** on the official Los Angeles ZIP page. Those were added from neighborhood and adjacent-city ZIP-Codes.com pages and from `search.asp?fld-city=...&fld-state=CA`.

ZIP-Codes.com slug collisions are common and were resolved with that search form, then filtered to Southern California ranges (90000–91899 and 935xx) to drop homonyms (for example Brentwood CA 94513 is the Contra Costa city, not the Los Angeles neighborhood; Palms, Silver Lake, Valley Village, and Westwood search results also included out-of-area ZIPs). Confirmed collisions included `ca-long-beach` → Carson, `ca-pasadena` → La Cañada Flintridge, `ca-brentwood` → Brentwood 94513, and `ca-westwood` → 96137. The `ca-hollywood` slug does land on the official Los Angeles page.

## Locator sweep

- Pass 1: 435 ZIPs, 870 queries at 5 and 15 miles, 336 unique records, 0 failed queries (resumable `sweep.py`).
- Pass 2: 130 widening queries (1, 2, 3, 10, and 20 miles) around core and edge ZIPs, including harbor, valley, 90272, 90291, and 93535 / 93550. Added one record (Piru 93040). No new printed-Los-Angeles offices.
- Total unique records: **337**. Raw locator dump: `los-angeles-usps-locator-2026-11-15.jsonl`.

All 337 official pages returned HTTP 200 on the first try. Embedded `poDetail` matched the API record on all 337 (`match_api`).

## Geocoding

U.S. Census Bureau Geocoder, address endpoint and coordinates endpoint, Public_AR_Current / Current_Current and Public_AR_Census2020 / Census2020_Census2020, layers Incorporated Places, Census Designated Places, and Counties. All 337 addresses and all 337 official locator map points were geocoded on both files (`los-angeles-usps-geocoder-2026-11-15.jsonl`). The geocoder used each office's printed state (CA). OpenStreetMap was not used.

Address retries were run for printed-Los-Angeles offices with a no-match on either file:

- Terminal Annex Finance (1441876), 900 N Alameda St: current file matches in Los Angeles city; 2020 file still no-match after street-name retries. A 2020 hit on "900 Alameda St" resolved to a different address (900 S Alameda St, 90021) and was not used.
- Sunset (1440792), 1425 N Cherokee Ave: no address match on either file after retries.
- West Los Angeles Finance (1387092), 11420 Santa Monica Blvd: current file still no-match; 2020 file matches in Los Angeles city.
- Airport Los Angeles (1557631), 8821 Aviation Blvd: no address match on either file after retries; official map point is in Inglewood city.

Map-point fallback was used only when the official page already prints Los Angeles and the official map point is in Los Angeles city on both files. That applies to Terminal Annex Finance, Sunset, and West Los Angeles Finance. It was not used for Airport Los Angeles (point in Inglewood) or Barrington (point not in any incorporated place), and it is never used when the printed city already disagrees.

## Classification (337 records)

- **43 listed.** Printed city Los Angeles; money-order tags present. 40 have address and official map point in Los Angeles city on both Census files. 3 listed under map-point fallback, as documented above. All 43 are in Los Angeles County. 13 Open evenings (weekday BUSINESS close after 17:00). 31 Open weekends (Saturday retail; no Sunday hours). Midday weekday splits stored with commas, not slashes: Federal Los Angeles `08:00-13:30,14:30-16:30`; Ramirez `09:00-11:30,12:00-16:30`; Westvern `10:00-12:00,13:00-16:00`. Official names kept, including Main Office Los Angeles, Augustus F Hawkins, and Macys Retail Store. The Hollywood Post Office (1367244, 1615 Wilcox Ave) prints LOS ANGELES and is listed.
- **10 in-city, not listed.** Printed Los Angeles; all four geocode legs in Los Angeles city; no money-order tags. Los Angeles (1440580) at 7001 S Central Ave Rm 322 (no BUSINESS); Greenmead Annex (1573734, no BUSINESS); Alameda Carrier Annex (1440516, no BUSINESS); Lincoln Hgts Carrier Annex (1370472, no BUSINESS); Sanford (1573616, has BUSINESS including Saturday); Los Angeles CA Bicentl SDC (1612756, Saturday) and Bicentennial (1354879, no BUSINESS) at 7610 Beverly Blvd; Century City Mall (1513317, midday BUSINESS, no Saturday); West Los Angeles (1440824) at 11270 Exposition Blvd Fl 2 (no BUSINESS; the listed Rancho Park office is Fl 1 of that building); Village (1511655, BUSINESS weekdays).
- **5 HOLD, printed Los Angeles, not fully in Los Angeles city.**
  - Wagner Branch (1386144), 2200 W Century Blvd 90047: address in Westmont CDP; official point in Inglewood city. Has money orders and Saturday hours.
  - Hazard (1440545), 3729 E 1st St 90063: address and official point in East Los Angeles CDP. Has money orders and Saturday hours.
  - East Los Angeles (1440501), 975 S Atlantic Blvd 90022: address and official point in East Los Angeles CDP. Has money orders, evenings (18:00), and Saturday hours.
  - Airport Los Angeles (1557631), 8821 Aviation Blvd 90009: address no-match after retries; official point in Inglewood city. No money-order tags. BUSINESS hours include a 18:00 weekday close and Saturday.
  - Barrington (1354097), 200 S Barrington Ave 90049: address in Los Angeles city on both files; official map point not in any incorporated place (Los Angeles County only). Has money orders and Saturday hours.
- **40 HOLD, other printed city, any geocode leg in Los Angeles city.** All 40 have all four legs in Los Angeles city. Printed cities: North Hollywood (5), Van Nuys (3; none of the three has money-order tags), Canoga Park (2), Encino (2), San Pedro (2), and one each in Arleta, Chatsworth, Granada Hills, Harbor City, Marina del Rey, North Hills, Northridge, Pacific Palisades, Pacoima, Panorama City, Playa del Rey, Porter Ranch, Reseda, Sherman Oaks, Studio City, Sun Valley, Sunland, Sylmar, Tarzana, Tujunga, Valley Village, Venice, West Hills, Wilmington, Winnetka, and Woodland Hills. No office in this collection prints Hollywood as its city.
- **239 left off.** Other printed cities fully outside Los Angeles city, including Long Beach (15), Pasadena (8), Beverly Hills (4), Santa Monica (3), Burbank (3), West Hollywood (2), Culver City (2), and San Pedro Eastview (1361964; official point in Rancho Palos Verdes city).

58 records print Los Angeles (43 listed + 10 in-city not listed + 5 geographic holds).

## Listed offices (ZIP order)

Main Office Los Angeles 1440583 (90001); Augustus F Hawkins 1386656 (90002); Oakwood 1375826 (90004); Dockweiler 1360972 (90007); Crenshaw 1359781 (90008); Washington Los Angeles 1386490 (90011); Federal Los Angeles 1363254 and Terminal Annex Finance 1441876 (90012); Arcade 1353236 (90013); Del Valle 1360568 (90015); West Adams 1386939 (90016); Macys Retail Store 1440900 (90017); Rimpau 1379349 (90018); Market 1371904 (90021); Lugo 1371148 (90023); West Los Angeles Finance 1387092 (90025); Edendale 1362046 (90026); Los Feliz 1370971 (90027); Hollywood 1367244 (90028); Lincoln 1370506 (90031); El Sereno 1362195 (90032); Boyle Heights 1355581 (90033); Palms 1376672 (90034); Preuss 1378390 (90035); Miracle Mile 1373376 (90036); Ramirez 1440652 (90037); Griffith 1365742 (90039); Eagle Rock 1361598 (90041); Highland Park 1366944 and York 1388483 (90042); La Tijera 1369431 (90043); Hancock 1366131 (90044); Westchester 1387256 (90045); Foy 1363953 (90057); Greenmead Finance 1365606 (90061); Westvern 1387391 (90062); Rancho Park 1378759 (90064); Glassell 1364859 (90065); Mar Vista 1371776 (90066); Arco 1353610 and Bunker Hill 1356330 (90071); Pico Heights 1377432 (90075); Sunset 1440792 (90093).

Open evenings (13): Main Office Los Angeles, Oakwood, Dockweiler, Del Valle, Macys Retail Store, West Los Angeles Finance, Edendale, Los Feliz, Hollywood, Palms, Westchester, Foy, Mar Vista.

No Walmart rows. IDs are `usps-los-angeles-<locatorID>`. `last_verified` 2026-11-15. `verification_status` `verified_official_locator`.
