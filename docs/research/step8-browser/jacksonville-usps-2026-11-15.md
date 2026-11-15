# Jacksonville, FL USPS research (2026-11-15)

America/Denver (MST). Step 8, first Florida city, Post Offices only. Hours are Eastern Time. Census place: Jacksonville city, GEOID 1235000, POPESTIMATE2025 1,017,689 (Vintage 2025, SUMLEV 162). Jacksonville is a consolidated city-county; this vintage has no SUMLEV 170 or 172 rows. Ranking and city-limits classification use the SUMLEV 162 place “Jacksonville city,” the Duval County balance, not the whole county. Duval County (GEOID 12031, FUNCSTAT C) totals 1,062,963, which equals Jacksonville city plus four other independent municipalities: Jacksonville Beach city, Atlantic Beach city, Neptune Beach city, and Baldwin town. Those four places are not listed here. This is Jacksonville, Florida, not a Jacksonville in another state. OpenStreetMap was not used.

## Official ZIPs

ZIP-Codes.com city page `fl-jacksonville.asp` title: “Jacksonville, FL ZIP Codes, Map and Demographics,” Data Last Updated November 1, 2026. search.asp title: “52 ZIP Codes in Jacksonville, FL.” The city page lists 52 unique codes. The search table lists 50 of those 52 (it omits 32266 and 32277).

Official printed-Jacksonville ZIPs are the 46 codes search lists as Jacksonville, plus 32277, which appears only on the city page (type Standard, alias Jax) and is treated as Jacksonville in Duval: **47** codes (31 Standard, 15 P.O. Box, 1 Unique). 45 are listed in Duval, one in Clay (32234), and one in Saint Johns (32260, a P.O. Box).

Excluded from official printed-Jacksonville even though they appear on the Jacksonville city page:

| ZIP | Search listed city | Notes |
|-----|--------------------|-------|
| 32233 | Atlantic Beach | Official Atlantic Beach ZIP (search “1 ZIP Code in Atlantic Beach, FL”). |
| 32240 | Jacksonville Beach | Official Jacksonville Beach P.O. Box ZIP. |
| 32250 | Jacksonville Beach | Official Jacksonville Beach Standard ZIP. |
| 32259 | Saint Johns | Official Saint Johns ZIP. |
| 32266 | (omitted from Jacksonville search) | Official Neptune Beach ZIP (search “1 ZIP Code in Neptune Beach, FL”). |

Slug collisions that used search.asp: Jacksonville Beach and Baldwin both resolved to the Jacksonville city page; Atlantic Beach and Neptune Beach have their own city pages. The St. Augustine slug resolved to Saint Augustine; search.asp “St. Augustine” returned 0 ZIP Codes, and the Saint Augustine search (“6 ZIP Codes in Saint Augustine, FL”) was used instead.

## Locator sweeps

Official USPS locator API, `requestType=po`.

- Pass 1: 90 ZIPs (prefixes 322: 51, 320: 32, 315: 7) at 5 and 15 miles, 180 queries, 77 unique records, 0 fails, 20 printed Jacksonville (Florida).
- Pass 2: the same 90 official and edge ZIPs at 1, 2, 3, 10, and 20 miles, 450 queries, 0 fails, +13 far records, still 20 printed Jacksonville, 90 unique.

Locator dump: `docs/research/step8-browser/jacksonville-usps-locator-2026-11-15.jsonl`.

No printed-Jacksonville office from another state appeared.

## Official pages

All 90 official USPS location pages returned HTTP 200. Embedded `poDetail` matched the locator API on address, phone, and BUSINESS hours for all 90 (`match_api` on all).

## Geocoder

U.S. Census Bureau Geocoder, address and coordinates endpoints, Public_AR_Current / Current_Current and Public_AR_Census2020 / Census2020_Census2020, layers Incorporated Places + CDPs + Counties. Classification uses only the SUMLEV 162 Jacksonville city GEOID 1235000, not Duval County as a whole. Dump: `docs/research/step8-browser/jacksonville-usps-geocoder-2026-11-15.jsonl`. 90 records, 0 errors. OpenStreetMap was not used.

Nineteen records have any leg in Jacksonville city, and all 19 print Jacksonville. The twentieth printed-Jacksonville record is the Baldwin Post Office, whose legs are all in Baldwin town.

### Map-point fallbacks (2)

1. **1438714 Jacksonville NAS, 569 Childs St, printed Jacksonville.** Current and 2020 address files: no match after street-name, city, and ZIP retries (CHILDS ST, CHILDS STREET, CHILD ST, CHILDS RD, CHILDS ROAD, ZIPs 32212/32214/32205 and empty ZIP, and city variants Jacksonville NAS / NAS Jacksonville). No retry snapped to a different street. Official map point (30.221629, -81.692679) is in Jacksonville city on both benchmarks. Listed (money-order tags and BUSINESS hours).

2. **1438744 Mayport Naval Station, 460 Massey Ave, printed Jacksonville.** Current and 2020 address files: no match after street-name, city, and ZIP retries (MASSEY AVE, MASSEY AVENUE, MASSEY RD, MASSEY ROAD, N/S prefixes, ZIPs 32228/32227/32233 and empty ZIP, and city variants Mayport / Mayport Naval Station). No retry snapped to a different street. Official map point (30.388648, -81.401703) is in Jacksonville city on both benchmarks. Listed (money-order tags and BUSINESS hours).

### Other geocode notes

- Springfield (1382584, 1601-1 N Main St): the geocoder dropped the unit and matched `1601 N MAIN ST, JACKSONVILLE, FL, 32206` in Jacksonville city on both address files. Both map points agree.
- Carver (1357170, 4160 N Canal St): the geocoder dropped the leading N and matched `4160 CANAL ST, JACKSONVILLE, FL, 32209` on the same street, still in Jacksonville city, on both address files. Both map points agree.
- Gateway Carrier Annex (1495697, 5258 Norwood Ave Unit 1): current address file no match after the unit was dropped and after street-name retries; no retry snapped to a different street. 2020 address file matched `5258 NORWOOD AVE, JACKSONVILLE, FL, 32208` in Jacksonville city. Both official map points are in Jacksonville city. Not listed (no money-order tags, no BUSINESS block).
- Baymeadows DDC (1354265, 11250 Philips Industrial Blvd E): both address files matched `11250 PHILLIPS INDUSTRIAL BLVD E` (geocoder spelling) in Jacksonville city. Not listed (no money-order tags, no BUSINESS block).

## Classification

- Listed: 15, all with money-order tags (DOM+INQ) and a BUSINESS hours block. Money orders: 15. Open evenings: 5 (Murray Hill and Mandarin until 18:00, Westland until 18:30, Southpoint and Pottsburg until 17:30). Open weekends: 11 (Saturday hours; none publish Sunday hours). Not labeled Open evenings or Open weekends: Springfield, Carver, Jacksonville NAS, and Mayport Naval Station.
- Holds: 1. Baldwin (1438615, 199 Center St S) prints Jacksonville, but all four geocode legs are in Baldwin town GEOID 1203250 / Duval County 12031. The map-point fallback does not apply when the official point is not in the city.
- In-city, not listed: 4, all print Jacksonville and geocode in Jacksonville city, but their official pages do not list money orders: Jacksonville (1438711, 1100 Kings Rd, no BUSINESS); Jacksonville FL SDC (1612768, same address, BUSINESS hours including evenings and Saturday); Gateway Carrier Annex (1495697); Baymeadows DDC (1354265).
- Map-point fallbacks: 2 (Jacksonville NAS and Mayport Naval Station).
- No other printed city has a geocode leg inside Jacksonville city. Offices that print Jacksonville Beach, Atlantic Beach, Orange Park, Saint Johns, and other nearby cities geocode outside Jacksonville city and are not holds.

## Raw files

`/workspace/step8jax/` (official ZIP pages, nearby city/search HTML, locator JSON, official USPS pages, geocoder dump).
