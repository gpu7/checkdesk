# Stamford, CT USPS research — 2026-11-15 (America/Denver)

Post Offices only. Official USPS Location Finder API (`POST https://tools.usps.com/UspsToolsRestServices/rest/POLocator/findLocations`, `requestType` po) and official location pages (`https://tools.usps.com/locations/details/<id>`). Retail hours are the BUSINESS block only. Money-order flags are taken only from that office's own `poDetail.services` tags (`MONEYORDERSDOM`, `MONEYORDERSINQ`). Hours on the city pages are Eastern Time. No businesses were contacted. Walmart was not collected (official walmart.com store locator unavailable).

Census place used for listing: **Stamford city**, GEOID **0973000**, Western Connecticut Planning Region GEOID **09190**. Classification matches that exact name and GEOID only. Stamford is coextensive with Stamford town. Greenwich, Darien, New Canaan, and Norwalk are not folded in.

## ZIP inventory

ZIP-Codes.com slug `https://www.zip-codes.com/city/ct-stamford.asp` is not a collision: the page title is Stamford, CT, last updated November 1, 2026. Official Stamford ZIPs were taken from `search.asp?fld-city=Stamford&fld-state=CT`. The search title says "14 ZIP Codes in Stamford, CT". The city page and the search results table have the same 14 unique codes, all listed as Stamford in Western CT: 06901, 06902, 06903, 06904, 06905, 06906, 06907, 06910, 06911, 06912, 06913, 06914, 06926, 06927 (7 Standard, 3 P.O. Box, 4 Unique). Official unique total: 14. Nearby city and town ZIPs were added and filtered to prefixes 069 and 068 (37 ZIPs in pass 1). Neighborhood slugs `ct-glenbrook`, `ct-springdale`, and `ct-ridgeway` collided with the Stamford city page (search.asp fallback, 1 ZIP each; those are official Stamford ZIPs). Rowayton's slug collided with Norwalk. South Norwalk and East Norwalk city pages are the Norwalk page.

## Locator sweep

- Pass 1: 37 ZIPs, 74 queries at 5 and 15 miles, 131 unique records, 0 failed queries, 7 printed Stamford.
- Pass 2: 135 widening queries (1, 2, 3, 10, and 20 miles) around 27 official and edge ZIPs, 0 fails, 118 added records far from the city (Bronx, Long Island, Westchester, and New Jersey), no new printed-Stamford offices.
- Total unique records: **249**. Raw locator dump: `stamford-usps-locator-2026-11-15.jsonl`.

## Official pages

All 249 official location pages returned HTTP 200 on the first try. Each page's embedded `poDetail` matched the API record on address, phone, and BUSINESS hours (`match_api` on all 249).

Seven records print Stamford:

| locatorID | Official name | Address | ZIP | MONEYORDERS tags | BUSINESS hours |
|---|---|---|---|---|---|
| 1481674 | SUMMER ATLANTIC | 550 SUMMER ST | 06901 | DOM only | Weekdays 09:00-17:00; Saturday 09:00-12:00; Sunday closed |
| 1433268 | WEST AVE | 317 WEST AVE | 06902 | DOM + INQ | Weekdays 09:00-17:00; Saturday 09:00-14:00; Sunday closed |
| 1457819 | BULLS HEAD | 19 HIGH RIDGE RD | 06905 | DOM + INQ | Weekdays 08:30-17:00; Saturday 09:00-14:00; Sunday closed |
| 1364924 | GLENBROOK | 370 HOPE ST | 06906 | DOM + INQ | Weekdays 09:00-17:00; Saturday and Sunday closed |
| 1473583 | STAMFORD | 427 WEST AVE RM 334 | 06910 | none | No BUSINESS block |
| 1488835 | WEST AVE CARRIER UNIT | 427 WEST AVE | 06910 | none | No BUSINESS block |
| 1601560 | STAMFORD CT SDC | 24 CAMP AVE | 06907 | none | Weekdays 08:30-17:30; Saturday 08:30-14:30; Sunday closed |

## Geocoder

U.S. Census Bureau Geocoder, address and coordinates, Public_AR_Current / Current_Current and Public_AR_Census2020 / Census2020_Census2020, layers Incorporated Places + Census Designated Places + Counties. OpenStreetMap was not used. All 249 records were geocoded with no request errors. Raw: `stamford-usps-geocoder-2026-11-15.jsonl`.

Six of the seven printed-Stamford records have an address match and an official map point in Stamford city (GEOID 0973000) on both files. The two 427 West Ave records print ZIP 06910; the geocoder matched 427 WEST AVE, STAMFORD, CT, 06902, still in Stamford city (the unit on the Stamford Post Office record was dropped by the geocoder). Stamford CT SDC (24 CAMP AVE, 06907) is an address no-match on both files. Street-name retries (CAMP AVENUE, CAMP AV, E/W/N/S CAMP AVE, CAMP RD/ROAD, CAMP ST/STREET, and official and nearby ZIPs including an empty ZIP) also did not match. The official map point (41.096455, -73.518092) is in Stamford city on both benchmarks. No record that prints another city has any geocode leg in Stamford city. No printed-Stamford record's official point falls outside the city.

## Classification

- **Listed (4):** Summer Atlantic, West Ave, Bulls Head, and Glenbrook. All print Stamford, have money-order tags, and have address and official map point in Stamford city on both files. None is labeled Open evenings (a 17:00 weekday close does not count). Summer Atlantic, West Ave, and Bulls Head are labeled Open weekends. Summer Atlantic lists Domestic Money Orders only (Inquiry Money Orders are not listed).
- **HOLD, printed Stamford, not in the city:** none.
- **HOLD, other printed city, any geocode leg in Stamford city:** none.
- **In-city, not listed (3):** Stamford (1473583) and West Ave Carrier Unit (1488835) at 427 West Ave, and Stamford CT SDC (1601560) at 24 Camp Ave. All print Stamford and have official points in the city; none of the official pages lists money orders. The SDC record publishes BUSINESS hours past 17:00 on weekdays and on Saturday. The map-point fallback is not used for listing because there are no money-order tags.

7 records print Stamford (4 listed + 3 not listed + 0 holds).
