# Atlanta, Georgia USPS research (2026-11-15)

Prepared 2026-11-15 (America/Denver). First Georgia city in the standing 50-state run. Post Offices only. Hours on the Atlanta pages are Eastern Time. Census place: Atlanta city, GEOID 1304000, in Fulton County (GEOID 13121, FUNCSTAT A, part 485,770) and DeKalb County (GEOID 13089, FUNCSTAT A, part 43,340). July 1, 2025 population 529,110 (Vintage 2025, SUMLEV 162). This is Atlanta, Georgia, not an Atlanta in another state. Nearby municipalities are separate Census places and are not listed here.

## Official ZIPs

zip-codes.com city page title “Atlanta, GA ZIP Codes, Map and Demographics,” updated November 1, 2026; search title “91 ZIP Codes in Atlanta, GA” (Page 1 of 2 at 50 rows; NR=100 is Page 1 of 1 with all 91). The city page lists 90 unique codes, all of which appear in the search. Official printed-Atlanta ZIPs are the 90 codes search lists as Atlanta (41 Standard, 35 P.O. Box, 14 Unique): 68 in Fulton, 21 in DeKalb, and 1 in Cobb (30339). Prefixes: 303 (75), 311 (14), 399 (1, 39901). Excluded even though it appears on the Atlanta search: 30060, listed Marietta in Cobb. City-page slugs for East Point, College Park, Hapeville, South Fulton, Sandy Springs, Brookhaven, Dunwoody, Chamblee, Doraville, and Vinings collided with the Atlanta city page; their search.asp titles were used instead.

Pass 1 ZIP list: 261 codes (prefixes 300: 83, 303: 75, 301: 42, 302: 38, 311: 15, 305: 7, 399: 1), including all 90 official printed-Atlanta ZIPs plus 30517 (Braselton). The extra 311 code, 31169, is a Peachtree City unique, not official Atlanta.

## Locator

Pass 1: 261 ZIPs at 5 and 15 miles, 522 queries, 232 unique, 0 fails, 42 printed Atlanta (Georgia). Pass 2: the same 261 official/edge ZIPs at 1, 2, 3, 10, and 20 miles, 1,305 queries, 0 fails, +22 far records, still 42 printed Atlanta, 254 unique. None of the 22 added offices print Atlanta.

All 254 official USPS location pages returned HTTP 200 and matched the locator API on name, address, phone, and BUSINESS hours (`match_api` on all). 32 of the 42 printed-Atlanta offices have money-order tags (MONEYORDERSDOM and MONEYORDERSINQ). Ten do not.

## Geocoding

All 254 records were sent to the Census geocoder, current and 2020 address files and current and 2020 coordinate lookups, with layers Incorporated Places, Census Designated Places, and Counties. OpenStreetMap was not used. No geocoder transport errors.

Listed (18), all with money-order tags, printed city Atlanta, and inside Atlanta city (GEOID 1304000) on both address files, except Civic Center as noted: Ben Hill, Broadview, Buckhead Loop, Cascade Heights, Central City, Civic Center, East Atlanta, Eastwood, Greenbriar Mall, Howell Mill, Lakewood, Little Five Points, Martech, Morris Brown, North Highland, Peachtree Center, Pharr Road, West End.

Civic Center (1358112, 570 PIEDMONT AVE NE, 30308) is a documented map-point fallback. The current address file did not match after 110 retries across street-name, directional, suite, and ZIP variants (30308, 30309, 30306, 30303, and blank). The 2020 address file consistently matched 570 PIEDMONT AVE NE, ATLANTA, GA, 30303 in Atlanta city. Both official map points fall in Atlanta city. The printed city is Atlanta.

Holds (16), print Atlanta, geocode outside Atlanta city on both files (or, for Cumberland Carrier Facility, after a documented address retry): Akers Mill (unincorporated Cobb County); Briarcliff (unincorporated DeKalb County); Chamblee (Chamblee city); College Park (College Park city); Cumberland Carrier Facility (Marietta city); Cumberland Mall (unincorporated Cobb County); Doraville (Doraville city); Druid Hills (North Druid Hills CDP); Dunwoody (Dunwoody city); East Point (East Point city); Embry Hills (unincorporated DeKalb County); Hapeville (Hapeville city); Industrial (South Fulton city); Northlake (unincorporated DeKalb County); Old National (College Park city); Perimeter Center (Dunwoody city). Cumberland Carrier Facility (1360017, 1901 TERRELL MILL RD SE STE 500, 30339) did not match the current or 2020 address file when queried as Atlanta, 30339. Retries that used Marietta or ZIP 30067 matched 1901 TERRELL MILL RD SE, MARIETTA, GA, 30067 in Marietta city, and both official map points also fall in Marietta city, so it is held.

In-city not listed (8), inside Atlanta city but no money-order tags: Atlanta Ga Sdc, Atlanta, Martech Annex, Mega Passport Ctr, Midtown Carrier Annex, Midtown, Ralph Mcgill Carrier, South Atlanta Ga Sanddc. Atlanta (1436067) and Atlanta GA SDC (1585797), both at 3900 Crown Rd SW, 30304, did not match either address file after street-name, city, and ZIP retries (384 and 288 queries respectively, zero hits). Both official map points fall in Atlanta city, so they are treated as in-city on a documented map-point fallback, but they are still not listed because the official pages have no money-order tags (Atlanta has no BUSINESS block; Atlanta GA SDC publishes hours through 10:00 p.m. and on Sunday, but no money-order tags).

No other printed city has a geocode leg (address or map point, either file) inside Atlanta city.

## Pages

Hub, money-orders, and after-hours pages use the city slug `/atlanta/`. Hours are labeled Eastern Time. Open evenings means a weekday retail close after 17:00; a 17:00 close does not count. Open weekends means Saturday or Sunday availability. Two are labeled Open evenings: the Greenbriar Mall Post Office and the Pharr Road Post Office, both until 6:00 p.m. Nine publish Saturday hours and are labeled Open weekends: Ben Hill, Broadview, Cascade Heights, Central City, Civic Center, East Atlanta, Greenbriar Mall, Howell Mill, and Pharr Road. None of the listed offices publishes Sunday hours.

Raw locator: `docs/research/step8-browser/atlanta-usps-locator-2026-11-15.jsonl`. Geocoder: `docs/research/step8-browser/atlanta-usps-geocoder-2026-11-15.jsonl`. Address retries: `docs/research/step8-browser/atlanta-usps-geocoder-retries-2026-11-15.jsonl`.
