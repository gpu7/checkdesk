# Boise, Idaho USPS research (2026-11-16)

Prepared 2026-11-16 (America/Denver). First Idaho city in the standing 50-state run (ship order: Boise, Meridian, Nampa, Caldwell, Idaho Falls). Post Offices only. Hours on the Boise pages are Mountain Time. Census place: Boise City city, GEOID 1608830, entirely in Ada County (GEOID 16001, FUNCSTAT A). July 1, 2025 population 238,429 (Vintage 2025, SUMLEV 162). The Census NAME is “Boise City city”; Check Desk pages use the name Boise. This is Boise, Idaho, in Ada County, not Boise County (GEOID 16015), and not a Boise in another state. Nearby Ada municipalities (Meridian, Eagle, Kuna, Star, and Garden City) are separate places and are not folded into this list.

## Official ZIPs

zip-codes.com city page title “Boise, ID ZIP Codes, Map and Demographics,” updated November 1, 2026; search title “28 ZIP Codes in Boise, ID” (Page 1 of 1). Official printed-Boise ZIPs are the 27 codes search lists as Boise, all in Ada County (10 Standard, 7 P.O. Box, 10 Unique). Prefix 837. Excluded even though it appears on the Boise search and city page: 83714, listed Garden City. Types come from the Ada County page and the Boise city page (they agree; county rows say “PO Box,” normalized here to “P.O. Box”). A search for “Boise City, ID” returned 0 ZIP Codes, as expected.

Pass 1 ZIP list: 113 codes (prefixes 836: 44, 837: 28, 834: 27, 832: 14), the union of Ada, Canyon, and Bonneville County ZIPs plus the adjacent counties Boise, Elmore, Gem, Owyhee, Payette, Bingham, Jefferson, Madison, Teton, and Caribou. All 27 official printed-Boise ZIPs are in that list.

City-page slug collisions elsewhere in this sweep, documented so those lists use search.asp only: `/city/id-meridian.asp` served the Kuna city page (canonical still pointed at id-meridian.asp); `/city/id-nampa.asp` served the Meridian city page. The Boise city page itself did not collide.

## Locator

Pass 1: 113 ZIPs at 5 and 15 miles, 226 queries, 93 unique, 0 fails, 9 printed Boise. Pass 2: the same 113 official/edge ZIPs at 1, 2, 3, 10, and 20 miles, 565 queries, 0 fails, +8 far records (none printed Boise), 101 unique. Printed-Boise count stayed at 9.

All 101 official USPS location pages returned HTTP 200 and matched the locator API on name, address, phone, and BUSINESS hours (`match_api` on all). Monteview (1373604) timed out on the first fetch and returned HTTP 200 on retry. 7 of the 9 printed-Boise offices have money-order tags (MONEYORDERSDOM and MONEYORDERSINQ). Two do not: Boise (1439679) and Boise ID SDC (1612994), both at 770 S 13th St.

## Geocoding

All 101 records were sent to the Census geocoder, current and 2020 address files and current and 2020 coordinate lookups, with layers Incorporated Places, Census Designated Places, and Counties. OpenStreetMap was not used. No geocoder transport errors. In-city means the Census place Boise City city, GEOID 1608830.

Listed (7), all with money-order tags and printed city Boise. Both address files and both official map points are in Boise City city. No ambiguity and no map-point fallback:

- Boise Airport Station (1439677, 2625 W Apollo St, Boise, 83705; Census matched 2625 APOLLO ST, BOISE, ID, 83705). Phone 208-424-0331. Weekdays 09:00–12:30 and 13:30–17:00, Saturday closed, Sunday closed.
- Borah (1355447, 750 W Bannock St, Boise, 83702; Census matched 750 W BANNOCK ST, BOISE, ID, 83702). Phone 208-331-0037. Weekdays 08:30–17:00, Saturday closed, Sunday closed.
- Cole Village (1358614, 3485 N Cole Rd, Boise, 83704; Census matched 3485 N COLE RD, BOISE, ID, 83704). Phone 208-376-8651. Weekdays 08:30–17:00, Saturday closed, Sunday closed.
- Collister (1358706, 4650 W State St, Boise, 83703; Census matched 4650 W STATE ST, BOISE, ID, 83703). Phone 208-424-0378. Weekdays 09:00–13:00 and 14:00–17:00, Saturday closed, Sunday closed.
- Five Mile (1363454, 1350 S Five Mile Rd, Boise, 83709; Census matched 1350 S FIVE MILE RD, BOISE, ID, 83709). Phone 208-376-7819. Weekdays 08:30–17:30, Saturday 10:00–13:00, Sunday closed.
- Oregon Trail (1376258, 2208 E Summersweet Dr, Boise, 83716; Census matched 2208 E SUMMERSWEET DR, BOISE, ID, 83716). Phone 208-344-9265. Weekdays 08:30–13:30 and 14:30–17:00, Saturday closed, Sunday closed.
- Overland (1376467, 1650 W Targee St, Boise, 83705; Census matched 1650 W TARGEE ST, BOISE, ID, 83705). Phone 208-344-2280. Weekdays 08:30–17:00, Saturday closed, Sunday closed.

Holds (2), printed Boise and in-city, but no money-order tags:

- Boise (1439679, 770 S 13th St, Boise, 83708). The official page prints Boise, has no BUSINESS hours, and does not list money orders. Both address files matched 770 S 13TH ST, BOISE, ID, 83702 in Boise City city, and both official map points fall there. Held because the official page does not list money orders.
- Boise ID SDC (1612994, 770 S 13th St, Boise, 83708). The official page prints Boise and publishes BUSINESS hours (weekdays 07:30–17:30, Saturday 10:00–14:00) but does not list money orders. Both address files matched 770 S 13TH ST, BOISE, ID, 83702 in Boise City city, and both official map points fall there. Held because the official page does not list money orders.

In-city not listed: those two, already held. No office that prints another city has a geocode leg inside Boise city. Garden City (1364422, 8100 W Marigold St, Garden City, 83714) prints Garden City, not Boise, and does not geocode into Boise city. Meridian, Eagle, Kuna, and Star likewise print their own cities and geocode there.

Evenings: 1 (Five Mile until 17:30). Weekends: 1 (Five Mile Saturday 10:00–13:00). No listed Sunday hours. A 17:00 close does not count as Open evenings. The other six listed offices close at 17:00 weekdays and are closed weekends.

## Result

7 listed Post Offices, all with money orders. 1 Open evenings. 1 Open weekends. Hours labeled Mountain Time.
