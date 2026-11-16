# Columbus, Georgia USPS research (2026-11-15)

Prepared 2026-11-15 (America/Denver). Second Georgia city in the standing 50-state run. Post Offices only. Hours on the Columbus pages are Eastern Time. Census place: Columbus city, GEOID 1319000, coextensive with Muscogee County (GEOID 13215, FUNCSTAT C). July 1, 2025 population 202,171 (Vintage 2025, SUMLEV 162). This is Columbus, Georgia, not a Columbus in another state. Nearby places such as Fort Benning, Midland, Fortson, and Phenix City, Alabama, are not listed under a Columbus printed city.

## Official ZIPs

The city-page slug ga-columbus.asp collided with Upatoi (title “Upatoi, GA ZIP Code, Map and Demographics,” one ZIP, 31829, updated November 1, 2026). Search title “17 ZIP Codes in Columbus, GA” (Page 1 of 1). Official printed-Columbus ZIPs are the 14 codes search lists as Columbus, all in Muscogee (6 Standard, 4 P.O. Box, 4 Unique; types from the Muscogee County table). Prefix 319. Excluded even though they appear on the Columbus search: 31829 listed Upatoi; 31905 and 31995 listed Fort Benning. Midland 31820 and Fortson 31808 appear on the Muscogee County table but not on the Columbus search.

Pass 1 ZIP list: 48 codes (prefixes 318: 21, 319: 16, 368: 11), including all 14 official printed-Columbus ZIPs and the Phenix City, Alabama edge.

## Locator

Pass 1: 48 ZIPs at 5 and 15 miles, 96 queries, 50 unique, 0 fails, 7 printed Columbus (Georgia). Pass 2: the same 48 official/edge ZIPs at 1, 2, 3, 10, and 20 miles, 240 queries, 0 fails, +15 far records, still 7 printed Columbus, 65 unique. None of the 15 added offices print Columbus.

All 65 official USPS location pages returned HTTP 200 and matched the locator API on name, address, phone, and BUSINESS hours (`match_api` on all). 3 of the 7 printed-Columbus offices have money-order tags (MONEYORDERSDOM and MONEYORDERSINQ). Four do not: Baker Village, Columbus, Columbus GA S&DC, and Wynnton.

## Geocoding

All 65 records were sent to the Census geocoder, current and 2020 address files and current and 2020 coordinate lookups, with layers Incorporated Places, Census Designated Places, and Counties. OpenStreetMap was not used. No geocoder transport errors.

Listed (3), all with money-order tags, printed city Columbus, and inside Columbus city (GEOID 1319000) on both address files and both official map points: Beallwood (4012 Hamilton Rd, 31904), Downtown Columbus (120 12th St Lbby, 31901; Census matched 120 12TH ST, COLUMBUS, GA, 31901), and Lindsey Creek (3465 Macon Rd Ste E, 31907; Census matched 3465 MACON RD, COLUMBUS, GA, 31907). No map-point fallback was used to list a row.

Holds (2), printed-city mismatches with a Columbus city geocode leg:

- Midland (1372987, 9232 County Line Rd, Midland, 31820). The official page prints Midland. The current and 2020 address files both matched 9232 COUNTY LINE RD, MIDLAND, GA, 31820 in Columbus city, and both official map points fall in Columbus city. Held because the printed city is Midland, not Columbus.
- Fortson (1363872, 2511 Double Churches Rd, Fortson, 31808). The official page prints Fortson. 360 street-name, city, and ZIP variants were tried (10 street forms; cities Fortson, Columbus, and Midland; ZIPs 31808, 31909, 31907, 31904, 31820, and blank; current and 2020 files). The official city and ZIP (Fortson, 31808) did not match on any street form (0 of 20). A documented ZIP retry using 31909, including with the printed city Fortson and the official street 2511 DOUBLE CHURCHES RD, matched 2511 DOUBLE CHURCHES RD, COLUMBUS, GA, 31909 in Columbus city on both the current and 2020 files. Queries that used city Columbus also matched that same Columbus city address across the tried ZIPs. Both official map points fall in Columbus city (GEOID 1319000, Muscogee County). Held because the printed city is Fortson, not Columbus. Map-point fallback is only allowed when the printed city matches.

In-city not listed (4), official pages do not list money orders: Baker Village, Columbus and Columbus GA S&DC at 3916 Milgen Rd (the Columbus record has no BUSINESS hours block), and Wynnton. Columbus GA S&DC publishes weekday hours until 6:00 p.m. and Saturday hours, but still has no money-order tags.

No office that prints Columbus geocodes outside Columbus city. No listed office is open after 5:00 p.m. on a weekday or on Saturday or Sunday, so Columbus has no evenings-and-weekends page.

## Result

3 listed Post Offices, all with money orders. 0 Open evenings. 0 Open weekends. Hours labeled Eastern Time.
