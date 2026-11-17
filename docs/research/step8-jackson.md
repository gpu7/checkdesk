# Jackson, Mississippi USPS research (2026-11-17, America/Denver)

First Mississippi city in the Census ranking (ship order: Jackson, Gulfport, Southaven, Hattiesburg, Biloxi). Post Offices only. Hours labeled Central Time (49 CFR 71.6(a); the Eastern–Central boundary in 49 CFR 71.5 and the Central–Mountain boundary in 49 CFR 71.7 both lie outside Mississippi). Census place is Jackson city, GEOID 2836000, Vintage 2025 population 141,196, primarily in Hinds County (GEOID 28049), with SUMLEV 157 parts also in Madison County and Rankin County. All eight listed offices are in Hinds County. This is Jackson, Mississippi, not Jacksonville, Florida (already at `/jacksonville/`), not Jackson County, Mississippi, and not Clinton, Byram, Madison, Ridgeland, Pearl, Brandon, or Flowood. Official pages print Jackson, MS. Gulfport, Southaven, Hattiesburg, and Biloxi stay on separate lists. OpenStreetMap was not used.

Official Jackson self ZIPs are the 30 ZIPs listed as Jackson, MS on the official city page: 39201, 39202, 39203, 39204, 39205, 39206, 39207, 39208, 39209, 39210, 39211, 39212, 39213, 39215, 39216, 39217, 39218, 39225, 39232, 39236, 39269, 39272, 39282, 39283, 39284, 39286, 39288, 39289, 39296, and 39298. Some of those ZIPs also cover nearby municipalities such as Pearl, Flowood, or Byram; listing still requires the office to geocode inside Jackson city. Locator passes and official pages are the shared Mississippi sweep (329 offices, all geocoded on the current and 2020 Census files, 0 errors).

## Listed (8)

Prints Jackson, MS, lists money orders, and matches Jackson city on all four Census legs.

- Candlestick Park (1356851, 820 COOPER RD STE A, 39212). Weekdays 08:00-16:00; Saturday 09:00-12:00.
- Delta Station (1360634, 550 MELVIN BENDER DR, 39213). Weekdays 08:30-16:30; Saturday closed.
- Fondren (1363621, 629 FONDREN PL, 39216). Weekdays 08:00-16:00; Saturday closed.
- Jackson (1438060, 401 E SOUTH ST, 39201). Weekdays 07:30-19:00; Saturday 08:00-12:00.
- Lefleur (1370141, 1501 JACKSONIAN PLZ, 39211). Weekdays 08:00-17:00; Saturday closed.
- North Jackson (1375449, 4040 NORTHVIEW DR, 39206). Weekdays 08:30-16:30; Saturday 10:00-12:00.
- Southwest (1368198, 4542 ROBINSON RD, 39204). Weekdays 09:00-16:30; Saturday closed.
- Westland (1387311, 905 ELLIS AVE, 39209). Weekdays 08:30-16:30; Saturday closed.

Evenings: 1 (Jackson, until 19:00). Weekends: 3 (Candlestick Park, Jackson, and North Jackson, Saturday, no Sunday). Delta Station, Fondren, Lefleur, Southwest, and Westland are closed Saturday and Sunday. Lefleur weekday retail closes at 17:00, which does not count as Open evenings.

## Holds (1)

### Prints a different city, geocode leg in Jackson city (1)

- Tougaloo (1384861, 501 W COUNTY LINE RD, TOUGALOO 39174). The official page prints Tougaloo. The current and 2020 address files did not match. Both official map points fall in Jackson city, Hinds County. Held because the printed city is Tougaloo, not Jackson. Map-point fallback is only allowed when the printed city matches.

No map-point fallback. No other office in the Mississippi locator sweep geocodes into Jackson city.

## Result

8 listed Post Offices, all with money orders. 1 Open evenings. 3 Open weekends, Saturday only. Hours labeled Central Time. 1 hold. No map-point fallback.

## Site changes in this PR

- New `data/locations/jackson.csv` and `/jackson/`, `/jackson/money-orders/`, and `/jackson/after-hours/` pages.
- Jackson is inserted under a new Mississippi section after Minnesota on the home page and `/cities/`. No existing city CSV or page changed except those meta and list lines. The unsuffixed `/jackson/` slug is new and does not collide with `/jacksonville/` (Jacksonville, Florida), which is unchanged.
