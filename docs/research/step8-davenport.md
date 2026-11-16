# Step 8: Davenport, IA (2026-11-16, America/Denver)

Prepared 2026-11-16 (America/Denver). Third Iowa city in the standing 50-state run (ship order: Des Moines, Cedar Rapids, Davenport, Sioux City, Ankeny). Post Offices only. Hours on the Davenport pages are Central Time. Iowa observes Central Time (49 CFR 71.6). Census place: Davenport city, GEOID 1919000, in Scott County (GEOID 19163). July 1, 2025 population 100,358 (Vintage 2025, SUMLEV 162). This is Davenport, Iowa, not Bettendorf, not the Illinois Quad Cities (Moline, Rock Island, or East Moline), not Eldridge, and not a Davenport in another state. OpenStreetMap was not used.

Shared Iowa sweep raw files: `/workspace/step8ia/`. All 528 official pages returned HTTP 200 and `match_api`, and all 528 records were geocoded on current and 2020 address and coordinate lookups with 0 errors.

Listed (2), with money-order tags and printed city Davenport. Both address files and both official map points are in Davenport city, in Scott County (GEOID 19163). No map-point fallback:

- Davenport (1360330, 933 W 2nd St, Davenport, 52802; Census 933 W 2ND ST, DAVENPORT, IA, 52802). Phone 563-323-0306. Weekdays 08:30-17:00, Saturday 10:00-13:00, Sunday closed.
- Northwest (1375567, 4018 Marquette St, Davenport, 52806; Census 4018 N MARQUETTE ST, DAVENPORT, IA, 52806). Phone 563-445-0457. Weekdays 08:30-17:00, Saturday 09:30-13:00, Sunday closed. Official page prints 4018 MARQUETTE ST; both Census files matched 4018 N MARQUETTE ST, still in Davenport city.

Holds: none. No office that prints another city has a geocode leg inside Davenport city.

Evenings: 0 (weekday retail closes at 17:00). Weekends: 2 (Davenport Saturday 10:00-13:00; Northwest Saturday 09:30-13:00). No Sunday hours. A 17:00 close does not count as Open evenings. No other office in the Iowa locator sweep geocodes into Davenport city.

## Result

2 listed Post Offices, all with money orders. 0 Open evenings. 2 Open weekends. Hours labeled Central Time. No holds.

## Site changes in this PR

- New `data/locations/davenport.csv` and `/davenport/`, `/davenport/money-orders/`, and `/davenport/after-hours/` pages.
- Davenport is inserted under Iowa after Cedar Rapids on the home page and `/cities/`. Home and `/cities/` meta now say Des Moines, Cedar Rapids, and Davenport, Iowa. No other city CSV or page changed except those meta and list lines.
