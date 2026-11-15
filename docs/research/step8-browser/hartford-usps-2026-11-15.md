# Hartford, CT USPS research — 2026-11-15 (America/Denver)

Fourth Connecticut city. Classification used only Census "Hartford city", GEOID 0937000, in the Capitol Planning Region (GEOID 09110). West Hartford, East Hartford, Wethersfield, Newington, and other nearby municipalities were not folded in. Hours are Eastern Time. Public sources only; no business was contacted.

## Official ZIPs

ZIP-Codes.com city page slug `ct-hartford` is not a collision (title Hartford, CT, last updated November 1, 2026). search.asp title "52 ZIP Codes in Hartford, CT". The search table has 50 unique codes; the city page has 51 unique; the union is 52.

34 of the search rows are listed Hartford in Capitol (8 Standard, 15 P.O. Box, 11 Unique): 06101, 06102, 06103, 06104, 06105, 06106, 06112, 06114, 06115, 06120, 06123, 06126, 06132, 06134, 06140, 06141, 06142, 06143, 06144, 06145, 06146, 06147, 06150, 06151, 06152, 06153, 06154, 06155, 06156, 06160, 06161, 06167, 06176, 06180.

The other search-listed cities, included in pass 1 but not treated as official Hartford printed-city ZIPs: West Hartford 06107, 06110, 06117, 06119, 06127, 06133, 06137; East Hartford 06108, 06118, 06128, 06138; Wethersfield 06109, 06129; Newington 06111, 06131; New Hartford 06057.

The city page has two codes not in the search table, treated as official Hartford ZIPs: 06183 (Unique, Travelers Ins) and 06199 (P.O. Box). Official printed-Hartford ZIP total: 36.

The West Hartford slug `ct-west-hartford` collided with the Hartford city page. West Hartford ZIPs were taken from search.asp (title "8 ZIP Codes in West Hartford, CT"), which includes 06105 listed as Hartford (already an official Hartford ZIP). Neighborhood slugs that collided with the Hartford city page: Blue Hills, Unity Plaza, Barry Square, and Central. Elmwood, Bishops Corner, and Corbins Corner collided with West Hartford; Forbes Village and Silver Lane with East Hartford.

## Locator sweeps

Pass 1 used prefixes 061/060 (107 ZIPs), 5 and 15 miles (214 queries). 166 unique records, 0 failures, 8 printed Hartford.

Pass 2 used 1, 2, 3, 10, and 20 mile widenings around 75 official and edge ZIPs (West Hartford, East Hartford, Wethersfield, Newington, Bloomfield, Windsor, South Windsor, Rocky Hill, New Britain, Farmington, Glastonbury, Manchester, Windsor Locks, Broad Brook/East Windsor, New Hartford, and Avon, plus official ZIPs). 375 queries, 0 failures, 16 added records, still 8 printed Hartford. Total 182 unique records in `hartford-usps-locator-2026-11-15.jsonl`.

## Official pages

All 182 official pages returned HTTP 200 on the first try. Embedded `poDetail` matched the API record on all 182 (`match_api`).

The 8 records that print Hartford:

| locatorID | Official name | Address | ZIP | Phone | BUSINESS | Money orders |
|-----------|---------------|---------|-----|-------|----------|--------------|
| 1434099 | HARTFORD | 141 WESTON ST | 06101 | 860-524-6050 | 08:00-18:00 weekdays; Saturday 08:00-15:00 | DOM and INQ |
| 1353103 | ANN STREET | 185 ANN UCCELLO ST | 06103 | 860-240-7553 | weekdays 09:00-13:30,15:00-16:00; Sat/Sun closed | DOM and INQ |
| 1376031 | OLD STATE HOUSE | 80 STATE HOUSE SQ | 06103 | 860-240-7553 | 09:00-17:00 weekdays; Sat/Sun closed | DOM and INQ |
| 1434070 | WASHINGTON STREET | 189 WASHINGTON ST | 06106 | 860-240-1740 | 09:00-17:00 weekdays; Saturday 09:00-13:00 | DOM and INQ |
| 1355244 | BLUE HILLS | 433 WOODLAND ST | 06112 | 860-240-1740 | 09:30-17:00 weekdays; Saturday 09:00-13:30 | DOM and INQ |
| 1354105 | BARRY SQUARE | 645 MAPLE AVE | 06114 | 860-493-6325 | 09:00-17:00 weekdays; Saturday 09:00-13:30 | DOM and INQ |
| 1385446 | UNITY PLAZA | 271 BARBOUR ST | 06120 | 860-240-1740 | weekdays 09:30-13:00,14:15-16:00; Saturday 09:00-12:00 | DOM and INQ |
| 1374268 | MURPHY RD CARRIER ANNEX | 70 MURPHY RD STE 1 | 06114 | 860-493-6325 | no BUSINESS block | none |

Sunday is closed at all seven listed offices. Midday splits are stored in the CSV as comma-separated windows. Several offices share a published phone number; the published number is kept.

## Geocoder

U.S. Census Bureau Geocoder, address and coordinates endpoints, Public_AR_Current / Current_Current and Public_AR_Census2020 / Census2020_Census2020, layers Incorporated Places + CDPs + Counties. OpenStreetMap was not used. Full dump: `hartford-usps-geocoder-2026-11-15.jsonl`.

Six listed offices match in Hartford city (GEOID 0937000) on both address files and both official-map-point legs. Hartford Post Office official ZIP 06101 vs 2020 match ZIP 06120 is the same street (141 WESTON ST) and still in Hartford city.

Old State House (80 STATE HOUSE SQ) did not match on either address file. Street-name retries (STATE HOUSE SQUARE, STATEHOUSE SQ, STATE HOUSE ST, directional forms, ZIP variants) also did not match. Shortening to STATE ST / STATE STREET snapped to 80 STATE ST, a different street, and was rejected (one STATE SQUARE + 06106 current match snapped to 80 SQUIRE ST and was also rejected). The official map point (41.76658, -72.672196) is in Hartford city on both files. The office is listed on the documented map-point fallback because the printed city is Hartford and the official page lists money orders.

Murphy Rd Carrier Annex: unit STE 1 dropped; matched 70 MURPHY RD, HARTFORD, CT, 06114, all four legs in Hartford city; not listed because there are no money-order tags.

No printed-Hartford office geocodes outside the city. No other printed city has any geocode leg inside Hartford city.

## Classification

Listed (7), all money orders: Hartford, Ann Street, Old State House (map-point fallback), Washington Street, Blue Hills, Barry Square, and Unity Plaza. Open evenings: 1 (Hartford). Open weekends: 5. Holds: none. In-city, not listed: Murphy Rd Carrier Annex.
