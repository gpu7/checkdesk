# Step 8: Naperville, IL (2026-11-16, America/Denver)

Prepared 2026-11-16 (America/Denver). Third Illinois city in the standing 50-state run (ship order: Chicago, Aurora, Illinois, Naperville, Joliet, Rockford). Post Offices only. Hours on the Naperville pages are Central Time. Census place: Naperville city, GEOID 1751622, in DuPage and Will Counties. July 1, 2025 population 153,114 (Vintage 2025, SUMLEV 162). This is Naperville, Illinois, not a Naperville in another state, and not Aurora, Lisle, or Bolingbrook. OpenStreetMap was not used.

Shared Illinois sweep raw files: `/workspace/step8il/`. Official printed-Naperville ZIPs from search.asp: 6. The shared locator and official-page work is documented in the Illinois progress file and the Chicago memo; all 591 official pages returned HTTP 200 and `match_api`, and all 591 records were geocoded on current and 2020 address and coordinate lookups with 0 errors.

Listed (2), both with money-order tags and printed city Naperville. Both address files and both official map points are in Naperville city, in DuPage County (GEOID 17043). No map-point fallback:

- Naperville (1374385, 1750 W Ogden Ave, Naperville, 60540; Census matched 1750 W OGDEN AVE, NAPERVILLE, IL, 60540). Phone 630-717-2662. Weekdays 07:00–19:00, Saturday 07:00–17:00, Sunday 11:00–16:00.
- Washington Street (1374384, 5 S Washington St Ste 105, Naperville, 60540; Census matched 5 S WASHINGTON ST, NAPERVILLE, IL, 60540). Phone 630-717-2662. Weekdays 08:30–17:00, Saturday 08:30–17:00, Sunday closed.

Holds:

- Naperville IL SDC (1610979, 1750 W Ogden Ave, Naperville, 60540). Prints Naperville and geocodes in Naperville city on both address files and both official map points, but the official page does not list money orders. Held because the official page does not list money orders.
- Naperville Sta (1374387, 3075 Book Rd Ste 103, Naperville, 60564). Prints Naperville and lists money orders. Both official map points fall in Naperville city in Will County (GEOID 17197). Both Census address files, and 54 street/ZIP/vintage retries (3075 BOOK RD/ROAD with STE/SUITE/#/UNIT 103 and without; ZIPs 60564, 60540, and blank; current and 2020 vintages; 0 geocoder errors), snap to 3075 BOOK RD, NAPERVILLE, IL, 60540 in DuPage County with no incorporated place, about 1.7 miles north of the official map point (41.73311, −88.18676 vs official 41.708768, −88.187095). That address match is not in Naperville city, so this is a printed-city vs geocode disagreement. The map-point fallback does not apply when the address successfully matches a location that is not in the city. Held.

Evenings: 1 (Naperville until 19:00). Weekends: 2. Sunday hours: 1 (Naperville 11:00–16:00). A 17:00 close does not count as Open evenings.

## Result

2 listed Post Offices, both with money orders. 1 Open evenings. 2 Open weekends. 1 publishes Sunday hours. Hours labeled Central Time.

## Site changes in this PR

- New `data/locations/naperville.csv` and `/naperville/`, `/naperville/money-orders/`, and `/naperville/after-hours/` pages.
- Naperville is inserted under Illinois after Aurora, Illinois on the home page and `/cities/`. Home and `/cities/` meta now say Chicago, Aurora, and Naperville, Illinois. No other city CSV or page changed except those meta and list lines.
