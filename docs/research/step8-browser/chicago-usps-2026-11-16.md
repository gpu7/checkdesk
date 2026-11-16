# Chicago, Illinois USPS research (2026-11-16)

Prepared 2026-11-16 (America/Denver). First Illinois city in the standing 50-state run (ship order: Chicago, Aurora, Illinois, Naperville, Joliet, Rockford). Post Offices only. Hours on the Chicago pages are Central Time. Census place: Chicago city, GEOID 1714000, in Cook County (GEOID 17031; Vintage 2025 place-county population 2,731,585) with a DuPage County remainder of 0. July 1, 2025 population 2,731,585 (Vintage 2025, SUMLEV 162). This is Chicago, Illinois, in Cook County, not a Chicago in another state, and not Cicero, Evanston, Oak Park, Norridge, Harwood Heights, Chicago Heights, West Chicago, or North Chicago. Nearby municipalities stay off this list. OpenStreetMap was not used.

## Official ZIPs and locator

Shared Illinois sweep raw files: `/workspace/step8il/`. ZIP-Codes.com data last updated November 1, 2026. Official printed-Chicago ZIPs from search.asp (listed as Chicago in Illinois): 84. The city page listed 91, including 7 neighboring-city aliases; the search title was “98 ZIP Codes in Chicago, IL”, of which 14 are North Chicago, West Chicago, Chicago Heights, Chicago Ridge, Harwood Heights, Elmwood Park, Alsip, Cicero, Evergreen Park, Riverdale, or Great Lakes and are not official Chicago ZIPs.

Pass 1: 574 ZIPs from home counties (Cook, DuPage, Kane, Kendall, Will, Winnebago, Ogle) plus adjacent Illinois counties (Lake, McHenry, DeKalb, Grundy, Kankakee, La Salle — the `il-lasalle` slug 404s, so the sweep used `il-la-salle`), Boone, Stephenson, and Lee, plus Lake County, IN and Rock County, WI, queried at 5 and 15 miles (1,148 queries, 591 unique records, 0 failed queries). Printed-Chicago count: 60. Pass 2: 158 official and edge ZIPs at 1, 2, 3, 10, and 20 miles (790 queries, 0 added records, 0 failed queries, still 591 unique). Printed-Chicago count stayed at 60.

All 591 official USPS location pages returned HTTP 200 and matched the locator API on name, address, phone, and BUSINESS hours (`match_api` on all). 49 of the 60 printed-Chicago offices have money-order tags (MONEYORDERSDOM and MONEYORDERSINQ). Eleven do not.

## Geocoding

All 591 records were sent to the Census geocoder, current and 2020 address files and current and 2020 coordinate lookups, with layers Incorporated Places, Census Designated Places, and Counties. Finished 10:52:45 AM MST on 2026-11-16. 0 geocoder transport errors. In-city means the Census place Chicago city, GEOID 1714000. Independent check: no office that prints a city other than Chicago has a geocode leg inside Chicago city.

Listed (49), all with money-order tags and printed city Chicago.

Clean (46). Both address files and both official map points are in Chicago city. No ambiguity.

Mixed-vintage / map-point fallback (3). Printed city already Chicago; official map point in Chicago city on both files; one address vintage already in Chicago city; the other vintage did not match after retries and did not snap to a different place:

- AMC Ohare (1352964, 11600 W Irving Park Rd, Chicago, 60666). The 2020 address file matched 11600 IRVING PARK RD, CHICAGO, IL, 60666 in Chicago city. The current address file did not match 11600 W IRVING PARK RD, or 40 retries (11600 W/WEST IRVING PARK RD/ROAD, 11600 IRVING PARK RD/ROAD, 11600 W IRVING PARK, and STE 1; ZIPs 60666, 60656, 60631, 60634, and blank; 0 matches, 0 geocoder errors). Both official map points fall in Chicago city.
- Jefferson Park (1441668, 5401 W Lawrence Ave, Chicago, 60630). The current address file matched 5401 W LAWRENCE AVE, CHICAGO, IL, 60630 in Chicago city. The 2020 address file did not match 5401 W LAWRENCE AVE, or 28 retries (5401 W/WEST LAWRENCE AVE/AVENUE, 5401 LAWRENCE AVE/AVENUE, and 5401 W LAWRENCE; ZIPs 60630, 60641, 60646, and blank; 0 matches, 0 geocoder errors). Both official map points fall in Chicago city.
- Northtown (1375559, 3401 W Devon Ave, Chicago, 60659). The 2020 address file matched 3401 W DEVON AVE, CHICAGO, IL, 60659 in Chicago city. The current address file did not match 3401 W DEVON AVE, or 28 retries (3401 W/WEST DEVON AVE/AVENUE, 3401 DEVON AVE/AVENUE, and 3401 W DEVON; ZIPs 60659, 60645, 60625, and blank; 0 matches, 0 geocoder errors). Both official map points fall in Chicago city.

Holds (11), printed Chicago and in-city on both address files and both official map points, but no money-order tags:

- Chicago Cent Carrier Annex Post Office (1357902, 433 W HARRISON ST FL 3W, Chicago, 60699). No BUSINESS hours. Official page does not list money orders. Both address files and both official map points are in Chicago city.
- Fort Dearborn Post Office (1363759, 540 N DEARBORN ST, Chicago, 60610). Official page does not list money orders. Both address files and both official map points are in Chicago city.
- Graceland Carrier Annex Post Office (1365237, 3635 N LINCOLN AVE, Chicago, 60657). No BUSINESS hours. Official page does not list money orders. Both address files and both official map points are in Chicago city.
- Grand Crossing C Annex Post Office (1365301, 7748 S COTTAGE GROVE AVE, Chicago, 60619). No BUSINESS hours. Official page does not list money orders. Both address files and both official map points are in Chicago city.
- Grand Crossing Post Office (1441672, 7715 S COTTAGE GROVE AVE STE 1, Chicago, 60619). Official page does not list money orders. Both address files and both official map points are in Chicago city.
- Jefferson Park Carrier Annex Post Office (1368354, 4810 N MILWAUKEE AVE, Chicago, 60630). No BUSINESS hours. Official page does not list money orders. Both address files and both official map points are in Chicago city.
- Lincoln Park Carrier Annex Post Office (1370486, 2643 N CLARK ST, Chicago, 60614). No BUSINESS hours. Official page does not list money orders. Both address files and both official map points are in Chicago city.
- Loop Carrier Annex Post Office (1457302, 433 W HARRISON ST FL 3E, Chicago, 60699). No BUSINESS hours. Official page does not list money orders. Both address files and both official map points are in Chicago city.
- Rev Milton R Brunson Post Office (1373244, 324 S LARAMIE AVE, Chicago, 60644). Official page does not list money orders. Both address files and both official map points are in Chicago city.
- Southwest Carrier Annex Post Office (1441504, 4301 W 69TH ST, Chicago, 60629). No BUSINESS hours. Official page does not list money orders. Both address files and both official map points are in Chicago city.
- Wicker Park Carrier Annex Post Office (1450950, 1419 W CARROLL AVE STE 1, Chicago, 60607). No BUSINESS hours. Official page does not list money orders. Both address files and both official map points are in Chicago city.

No printed-Chicago office is held for a geographic mismatch. No office that prints another city has a geocode leg inside Chicago city.

Evenings: 22. Weekends: 40 (all 40 have Saturday hours). Sunday hours: 2 (Cardiss Collins 10:00–21:00 and Graceland 11:00–14:00). A 17:00 close does not count as Open evenings. No midday splits among the 49 listed offices.

## Listed offices

- AMC Ohare Post Office (1352964, 11600 W IRVING PARK RD, Chicago, 60666; 773-894-1350). Weekdays 16:00-19:00, Saturday closed, Sunday closed. Mixed-vintage / map-point fallback.
- Ashburn Post Office (1353453, 3639 W 79TH ST, Chicago, 60652; 773-767-1590). Weekdays 09:00-17:00, Saturday 09:00-13:30, Sunday closed.
- Auburn Park Post Office (1434827, 8345 S ASHLAND AVE, Chicago, 60620; 773-239-5088). Weekdays 09:00-19:00, Saturday 08:30-14:30, Sunday closed.
- Cardiss Collins Post Office (1434877, 433 W HARRISON ST FL LBBY, Chicago, 60699; 312-983-8130). Weekdays 08:30-23:59, Saturday 09:00-23:00, Sunday 10:00-21:00.
- Charles A Hayes Post Office (1357664, 7436 S EXCHANGE AVE, Chicago, 60649; 773-375-2180). Weekdays 09:00-17:30, Saturday 09:00-14:00, Sunday closed.
- Chicago Lawn Post Office (1357904, 6037 S KEDZIE AVE, Chicago, 60629; 773-925-1210). Weekdays 09:00-16:30, Saturday 09:00-13:00, Sunday closed.
- Chinatown Post Office (1357957, 2345 S WENTWORTH AVE STE A, Chicago, 60616; 312-326-6440). Weekdays 09:00-17:00, Saturday 09:00-14:30, Sunday closed.
- Clearing Post Office (1358287, 5645 S ARCHER AVE, Chicago, 60638; 773-767-1917). Weekdays 08:00-17:00, Saturday 08:30-14:00, Sunday closed.
- Cragin Post Office (1359714, 5100 W GRAND AVE, Chicago, 60639; 773-237-0710). Weekdays 09:00-17:00, Saturday 09:00-13:00, Sunday closed.
- Daniel J Doffyn Post Office (1360261, 3750 N KEDZIE AVE, Chicago, 60618; 773-539-6210). Weekdays 08:30-17:00, Saturday 09:00-14:30, Sunday closed.
- Edgebrook Post Office (1441670, 5424 W DEVON AVE, Chicago, 60646; 773-763-5370). Weekdays 09:00-17:00, Saturday 09:00-13:00, Sunday closed.
- Elsdon Post Office (1362491, 4922 S KEDZIE AVE, Chicago, 60632; 773-863-1402). Weekdays 09:00-17:00, Saturday 09:00-13:00, Sunday closed.
- Englewood Post Office (1362618, 611 W 63RD ST, Chicago, 60621; 773-873-0790). Weekdays 08:00-17:00, Saturday 08:00-13:00, Sunday closed.
- Finance Station H Post Office (1435475, 10238 S VINCENNES AVE, Chicago, 60643; 773-779-0306). Weekdays 09:00-17:00, Saturday 09:00-12:00, Sunday closed.
- Finance Station K Post Office (1435476, 3933 W NORTH AVE STE 1, Chicago, 60647; 312-486-7218). Weekdays 09:30-16:30, Saturday closed, Sunday closed.
- Finance Station L Post Office (1383460, 4642 S BISHOP ST, Chicago, 60609; 773-257-9438). Weekdays 10:00-15:00, Saturday closed, Sunday closed.
- Finance Station M Post Office (1383461, 7617 N PAULINA ST, Chicago, 60626; 773-943-6105). Weekdays 11:00-17:00, Saturday closed, Sunday closed.
- Finance Station Q Post Office (1378581, 4749 N BERNARD ST, Chicago, 60625; 773-539-9524). Weekdays 11:00-16:00, Saturday closed, Sunday closed.
- Finance Station T Post Office (1383464, 2011 W MONTROSE AVE, Chicago, 60618; 773-472-1314). Weekdays 09:00-18:30, Saturday closed, Sunday closed.
- Finance Station W Post Office (1383467, 10422 S EWING AVE, Chicago, 60617; 773-221-9405). Weekdays 10:00-16:30, Saturday 10:00-13:30, Sunday closed.
- Graceland Post Office (1365238, 3024 N ASHLAND AVE, Chicago, 60657; 773-248-0201). Weekdays 08:30-19:00, Saturday 09:00-15:00, Sunday 11:00-14:00.
- Hegewisch Post Office (1366646, 13234 S BALTIMORE AVE, Chicago, 60633; 773-646-6721). Weekdays 10:00-16:00, Saturday 10:00-12:00, Sunday closed.
- Henry W McGee Post Office (1366755, 4601 S COTTAGE GROVE AVE, Chicago, 60653; 773-924-6658). Weekdays 09:00-18:00, Saturday 09:00-15:00, Sunday closed.
- Irving Park Post Office (1368065, 3319 N CICERO AVE, Chicago, 60641; 773-725-3701). Weekdays 08:00-18:30, Saturday 09:00-15:00, Sunday closed.
- Jackson Park Post Office (1368194, 700 E 61ST ST, Chicago, 60637; 773-493-3125). Weekdays 09:00-17:00, Saturday 09:00-12:30, Sunday closed.
- Jefferson Park Post Office (1441668, 5401 W LAWRENCE AVE, Chicago, 60630; 773-736-1672). Weekdays 08:30-17:00, Saturday 08:30-15:00, Sunday closed. Mixed-vintage / map-point fallback.
- John Buchanan Post Office (1368461, 9308 S SOUTH CHICAGO AVE, Chicago, 60617; 773-221-9578). Weekdays 08:30-17:00, Saturday 08:30-15:00, Sunday closed.
- John Hancock Post Office (1441669, 875 N MICHIGAN AVE STE GP-07, Chicago, 60611; 312-644-0485). Weekdays 10:00-17:30, Saturday closed, Sunday closed.
- Lakeview Post Office (1369693, 1343 W IRVING PARK RD, Chicago, 60613; 773-327-0345). Weekdays 08:30-18:30, Saturday 08:30-15:00, Sunday closed.
- Lincoln Park Postal Store Post Office (1370489, 2405 N SHEFFIELD AVE, Chicago, 60614; 773-929-2680). Weekdays 09:00-18:30, Saturday 09:00-15:00, Sunday closed.
- Loop Clark Street Post Office (1370924, 211 S CLARK ST, Chicago, 60604; 312-385-3530). Weekdays 07:00-18:00, Saturday closed, Sunday closed.
- Mary Alice Henry Post Office (1372047, 4222 W MADISON ST, Chicago, 60624; 773-722-3740). Weekdays 08:30-17:00, Saturday 08:00-13:00, Sunday closed.
- Morgan Park Post Office (1373780, 1805 W MONTEREY AVE, Chicago, 60643; 773-238-2791). Weekdays 09:00-18:00, Saturday 09:00-14:00, Sunday closed.
- Mount Greenwood Post Office (1373993, 3349 W 111TH ST, Chicago, 60655; 773-238-2849). Weekdays 09:30-17:00, Saturday 09:00-13:00, Sunday closed.
- Nancy B Jefferson Post Office (1374364, 116 S WESTERN AVE, Chicago, 60612; 312-243-2560). Weekdays 09:00-17:00, Saturday 09:00-12:30, Sunday closed.
- Northtown Post Office (1375559, 3401 W DEVON AVE, Chicago, 60659; 773-583-8640). Weekdays 08:30-18:00, Saturday 09:00-16:00, Sunday closed. Mixed-vintage / map-point fallback.
- Norwood Park Post Office (1375630, 6300 N NORTHWEST HWY, Chicago, 60631; 773-631-2204). Weekdays 09:00-17:30, Saturday 09:00-14:30, Sunday closed.
- Ogden Park Post Office (1375924, 6559 S ASHLAND AVE, Chicago, 60636; 773-776-4458). Weekdays 09:00-17:00, Saturday 09:00-13:00, Sunday closed.
- Otis Grant Collins Post Office (1434860, 2302 S PULASKI RD, Chicago, 60623; 773-277-3070). Weekdays 08:30-17:00, Saturday 08:00-13:00, Sunday closed.
- Pilsen Post Office (1377506, 1859 S ASHLAND AVE, Chicago, 60608; 312-733-4750). Weekdays 09:00-17:30, Saturday 09:30-14:30, Sunday closed.
- Ravenswood Post Office (1378851, 2522 W LAWRENCE AVE, Chicago, 60625; 773-561-8633). Weekdays 08:00-19:00, Saturday 09:00-15:00, Sunday closed.
- Robert Leflore Jr Post Office (1379541, 5001 W DIVISION ST, Chicago, 60651; 773-378-5850). Weekdays 09:00-17:00, Saturday 09:00-12:30, Sunday closed.
- Roberto Clemente Post Office (1379544, 2339 N CALIFORNIA AVE, Chicago, 60647; 773-489-2855). Weekdays 08:30-19:00, Saturday 09:00-15:00, Sunday closed.
- Roger P Mc Auliffe Post Office (1379748, 6441 W IRVING PARK RD, Chicago, 60634; 773-736-0714). Weekdays 08:30-17:00, Saturday 09:00-15:00, Sunday closed.
- Rogers Park Post Office (1379762, 1723 W DEVON AVE, Chicago, 60660; 773-743-2650). Weekdays 08:00-18:00, Saturday 08:30-15:00, Sunday closed.
- Roseland Post Office (1379896, 11033 S STATE ST, Chicago, 60628; 773-928-6280). Weekdays 09:30-17:00, Saturday 09:30-13:00, Sunday closed.
- Streeterville Post Office (1376171, 355 E OHIO ST STE 200, Chicago, 60611; 312-212-4678). Weekdays 09:00-18:00, Saturday closed, Sunday closed.
- Twenty Second Street Post Office (1385239, 2035 S STATE ST, Chicago, 60616; 312-225-0218). Weekdays 09:00-18:00, Saturday 09:00-15:00, Sunday closed.
- Uptown Post Office (1385553, 4850 N BROADWAY ST, Chicago, 60640; 773-561-4846). Weekdays 09:00-19:00, Saturday 08:30-15:00, Sunday closed.

## Result

49 listed Post Offices, all with money orders. 22 Open evenings. 40 Open weekends. 2 publish Sunday hours. Hours labeled Central Time.
