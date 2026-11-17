# Step 8: Covington, KY (2026-11-16, America/Denver)

Fifth Kentucky city in the standing 50-state run (ship order: Louisville, Lexington, Bowling Green, Owensboro, Covington). Census place is Covington city (GEOID 2117848), July 1, 2025 population 41,847, in Kenton County (GEOID 21117). Hours labeled Eastern Time (49 CFR 71.4, 71.5; Kenton County is east of the Eastern–Central boundary). This is Covington, Kentucky, not a Covington in another state, and not Erlanger, Fort Mitchell, or Florence. The slug is `/covington/`.

Shared Kentucky sweep raw files: `/workspace/step8ky/`. All 482 official pages returned HTTP 200 and `match_api`, and all 482 records were geocoded on current and 2020 address and coordinate lookups with 0 errors. OpenStreetMap was not used.

Listed (2), with money-order tags and printed city Covington. Both address files and both official map points are in Covington city, in Kenton County (GEOID 21117). No map-point fallback:

- Covington (1359465, 700 Scott St, Covington, 41011; Census current 700 SCOTT BLVD, COVINGTON, KY, 41011; 2020 700 SCOTT BLVD, COVINGTON, KY, 41011). Phone 859-261-0809. Weekdays 08:30-17:00, Saturday 09:00-14:00, Sunday closed.
- Latonia (1436300, 111 E Southern Ave, Covington, 41015; Census current 111 E SOUTHERN AVE, COVINGTON, KY, 41015; 2020 111 E SOUTHERN AVE, COVINGTON, KY, 41015). Phone 859-431-4201. Weekdays 09:00-12:00,13:00-17:00, Saturday 09:00-12:00, Sunday closed.

The Latonia Post Office official page prints Covington and 111 E Southern Ave; all four Census legs are in Covington city. Weekdays have a midday closure, 12:00-13:00.

No holds. No other office in the Kentucky locator sweep geocodes into Covington city.

Evenings: 0 (weekday retail closes at 17:00). Weekends: 2 (Covington Saturday 09:00-14:00; Latonia Saturday 09:00-12:00). None publishes Sunday hours. A 17:00 close does not count as Open evenings.

## Result

2 listed Post Offices, both with money orders. 0 Open evenings. 2 Open weekends. Hours labeled Eastern Time. 0 holds. No map-point fallback.

## Site changes in this PR

- New `data/locations/covington.csv` and `/covington/`, `/covington/money-orders/`, and `/covington/after-hours/` pages.
- Covington is inserted under Kentucky after Owensboro on the home page and `/cities/`. Home and `/cities/` meta now say Wichita, Overland Park, Kansas City, Olathe, and Topeka, Kansas, and Louisville, Lexington, Bowling Green, Owensboro, and Covington, Kentucky. No other city CSV or page changed except those meta and list lines.
