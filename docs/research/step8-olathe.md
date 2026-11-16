# Step 8: Olathe, KS (2026-11-16, America/Denver)

Fourth Kansas city in the standing 50-state run (ship order: Wichita, Overland Park, Kansas City, Olathe, Topeka). Census place is Olathe city (GEOID 2052575), July 1, 2025 population 150,025, in Johnson County (GEOID 20091). Hours labeled Central Time (49 CFR 71.6; Johnson County is east of the 49 CFR 71.7(d) Kansas-Colorado boundary). This is Olathe, Kansas, not Overland Park, not Lenexa, not Gardner, not Spring Hill, and not an Olathe in another state.

Shared Kansas sweep raw files: `/workspace/step8ks/`. All 339 official pages returned HTTP 200 and `match_api`, and all 339 records were geocoded on current and 2020 address and coordinate lookups with 0 errors. OpenStreetMap was not used.

Listed (2), with money-order tags and printed city Olathe. Both address files and both official map points are in Olathe city, in Johnson County (GEOID 20091). No map-point fallback:

- Olathe (1375996, 110 N Chestnut St, Olathe, 66061; Census current 110 N CHESTNUT ST, OLATHE, KS, 66061; 2020 110 N CHESTNUT ST, OLATHE, KS, 66061). Phone 913-782-3765. Weekdays 08:30-17:00, Saturday 10:00-13:00, Sunday closed.
- Olathe East (1375995, 15050 W 138th St, Olathe, 66062; Census current 15050 W 138TH ST, OLATHE, KS, 66062; 2020 15050 W 138TH ST, OLATHE, KS, 66062). Phone 913-782-3423. Weekdays 08:00-16:30, Saturday 09:00-14:00, Sunday closed.

Holds: none. No office that prints another city has a geocode leg inside Olathe city.

Evenings: 0 (weekday retail closes at 17:00 or earlier). Weekends: 2 (the Olathe Post Office, Saturday 10:00-13:00, and Olathe East, Saturday 09:00-14:00). No Sunday hours. A 17:00 close does not count as Open evenings. No other office in the Kansas locator sweep geocodes into Olathe city.

## Result

2 listed Post Offices, both with money orders. 0 Open evenings. 2 Open weekends. Hours labeled Central Time. No holds.

## Site changes in this PR

- New `data/locations/olathe.csv` and `/olathe/`, `/olathe/money-orders/`, and `/olathe/after-hours/` pages.
- Olathe is inserted under Kansas after Kansas City on the home page and `/cities/`. Home and `/cities/` meta now say Des Moines, Cedar Rapids, Davenport, Sioux City, and Ankeny, Iowa, and Wichita, Overland Park, Kansas City, and Olathe, Kansas. No other city CSV or page changed except those meta and list lines.
