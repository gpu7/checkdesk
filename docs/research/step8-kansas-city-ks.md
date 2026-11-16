# Step 8: Kansas City, KS (2026-11-16, America/Denver)

Third Kansas city in the standing 50-state run (ship order: Wichita, Overland Park, Kansas City, Olathe, Topeka). Census place is Kansas City city (GEOID 2036000), July 1, 2025 population 157,805, in Wyandotte County (GEOID 20209). The list uses the SUMLEV 162 place, not the Wyandotte County total. Hours labeled Central Time (49 CFR 71.6; Wyandotte County is east of the 49 CFR 71.7(d) Kansas-Colorado boundary). This is Kansas City, Kansas, not Kansas City, Missouri, and not Bonner Springs, Edwardsville, or Lake Quivira. The slug is `/kansas-city-ks/` so it will not collide with Kansas City, MO later (precedent: `/aurora-il/`).

Shared Kansas sweep raw files: `/workspace/step8ks/`. All 339 official pages returned HTTP 200 and `match_api`, and all 339 records were geocoded on current and 2020 address and coordinate lookups with 0 errors. OpenStreetMap was not used.

Listed (5), with money-order tags and printed city Kansas City, KS. Both address files and both official map points are in Kansas City city, Kansas, in Wyandotte County (GEOID 20209). No map-point fallback:

- Argentine (1435551, 3400 Strong Ave, Kansas City, KS, 66106; Census current 3400 STRONG AVE, KANSAS CITY, KS, 66106; 2020 3400 STRONG AVE, KANSAS CITY, KS, 66106). Phone 913-789-8153. Weekdays 09:00-12:00, Saturday closed, Sunday closed.
- Civic Center (1358113, 550 Nebraska Ave, Kansas City, KS, 66101; Census current 550 NEBRASKA AVE, KANSAS CITY, KS, 66101; 2020 550 NEBRASKA AVE, KANSAS CITY, KS, 66101). Phone 913-621-0013. Weekdays 08:30-17:00, Saturday 09:00-12:00, Sunday closed.
- Robert L Roberts (1379539, 3115 N 51st St, Kansas City, KS, 66104; Census current 3115 N 51ST ST, KANSAS CITY, KS, 66104; 2020 3115 N 51ST ST, KANSAS CITY, KS, 66104). Phone 913-287-7165. Weekdays 08:30-17:00, Saturday 09:00-12:00, Sunday closed.
- Rosedale (1379893, 2200 W 36th Ave, Kansas City, KS, 66103; Census current 2200 W 36TH AVE, KANSAS CITY, KS, 66103; 2020 2200 W 36TH AVE, KANSAS CITY, KS, 66103). Phone 913-262-6463. Weekdays 08:30-17:00, Saturday 09:00-12:00, Sunday closed.
- Wyandotte West (1435654, 1310 N 78th Ter, Kansas City, KS, 66112; Census current 1310 N 78TH TER, KANSAS CITY, KS, 66112; 2020 1310 N 78TH TER, KANSAS CITY, KS, 66112). Phone 913-334-4182. Weekdays 08:30-17:00, Saturday 09:00-12:00, Sunday closed.

Holds, printed Kansas City, KS and inside the city, but official page does not list money orders (2):

- Kansas City (1435568, 550 Nebraska Ave, Kansas City, KS, 66101; no money-order tags; same printed street address as listed Civic Center 1358113; official page has no BUSINESS hours).
- Muncie (1374236, 6540 Kaw Dr, Kansas City, KS, 66111; no money-order tags).

23 offices that print Kansas City, MO were excluded from this page. None of them has a geocode leg inside Kansas City, KS (GEOID 2036000). No hold for a printed-city vs geocode mismatch.

Evenings: 0 (weekday retail closes at 17:00 or earlier). Weekends: 4 (Civic Center, Robert L Roberts, Rosedale, and Wyandotte West, all Saturday 09:00-12:00). Argentine is closed Saturday and Sunday. No Sunday hours. A 17:00 close does not count as Open evenings. No other office in the Kansas locator sweep geocodes into Kansas City, Kansas.

## Result

5 listed Post Offices, all with money orders. 0 Open evenings. 4 Open weekends. Hours labeled Central Time. 2 holds (Kansas City 1435568 and Muncie, no money-order tags). 23 Kansas City, MO offices excluded.

## Site changes in this PR

- New `data/locations/kansas-city-ks.csv` and `/kansas-city-ks/`, `/kansas-city-ks/money-orders/`, and `/kansas-city-ks/after-hours/` pages.
- Kansas City is inserted under Kansas after Overland Park on the home page and `/cities/`. Home and `/cities/` meta now say Des Moines, Cedar Rapids, Davenport, Sioux City, and Ankeny, Iowa, and Wichita, Overland Park, and Kansas City, Kansas. No other city CSV or page changed except those meta and list lines.
