# Step 8: Des Moines, IA (2026-11-16, America/Denver)

Prepared 2026-11-16 (America/Denver). First Iowa city in the standing 50-state run (ship order: Des Moines, Cedar Rapids, Davenport, Sioux City, Ankeny). Post Offices only. Hours on the Des Moines pages are Central Time. Iowa observes Central Time (49 CFR 71.6). Census place: Des Moines city, GEOID 1921000, in Polk County (GEOID 19153) and Warren County (GEOID 19181). July 1, 2025 population 212,086 (Vintage 2025, SUMLEV 162). This is Des Moines, Iowa, not West Des Moines, not Urbandale, not Pleasant Hill, not Ankeny, and not a Des Moines in another state. All six listed offices and the one geographic hold are in Polk County. OpenStreetMap was not used.

Shared Iowa sweep raw files: `/workspace/step8ia/`. All 528 official pages returned HTTP 200 and `match_api`, and all 528 records were geocoded on current and 2020 address and coordinate lookups with 0 errors.

Listed (6), with money-order tags and printed city Des Moines. Both address files and both official map points are in Des Moines city, in Polk County (GEOID 19153). No map-point fallback:

- Beaverdale (1354377, 4023 Urbandale Ave, Des Moines, 50310; Census 4023 URBANDALE AVE, DES MOINES, IA, 50310). Phone 515-255-8593. Weekdays 08:30-17:00, Saturday closed, Sunday closed.
- Capital Square (1356939, 400 Locust St Ste 185, Des Moines, 50309; Census 400 LOCUST ST, DES MOINES, IA, 50309). Phone 515-288-1831. Weekdays 09:00-17:00, Saturday closed, Sunday closed.
- Des Moines (1434736, 1165 2nd Ave, Des Moines, 50318; Census current 1165 2ND AVE, DES MOINES, IA, 50318; 2020 1165 2ND AVE, DES MOINES, IA, 50309). Phone 515-283-7599. Weekdays 08:00-17:30, Saturday closed, Sunday closed.
- East Side (1454543, 1501 E Fleming Ave, Des Moines, 50313; Census 1501 E FLEMING AVE, DES MOINES, IA, 50313). Phone 515-299-2399. Weekdays 09:00-17:00, Saturday closed, Sunday closed.
- South Des Moines (1382146, 430 E Mckinley Ave, Des Moines, 50315; Census 430 E MCKINLEY AVE, DES MOINES, IA, 50315). Phone 515-974-8401. Weekdays 08:30-17:00, Saturday 09:30-13:00, Sunday closed.
- University Station (1385494, 2323 Forest Ave, Des Moines, 50311; Census 2323 FOREST AVE, DES MOINES, IA, 50311). Phone 515-635-6997. Weekdays 08:30-17:00, Saturday closed, Sunday closed.

The Des Moines Post Office current address file matched ZIP 50318 and the 2020 file matched ZIP 50309; both still place it in Des Moines city. Capital Square's official suite (Ste 185) is not in the Census matched street, which is 400 LOCUST ST, DES MOINES, IA, 50309; both files still place it in Des Moines city.

Holds, printed Des Moines but outside the city (1):

- Pleasant Hill (1434763, 1300 NE 56th St, printed Des Moines, 50317). Prints Des Moines and lists money orders, but the current and 2020 address files both matched 1300 NE 56TH ST, DES MOINES, IA, 50327, and both official map points, in Pleasant Hill city (Polk County, GEOID 19153), not in Des Moines city. Held because the printed city and the geocode disagree.

Evenings: 1 (the Des Moines Post Office until 17:30). Weekends: 1 (South Des Moines, Saturday 09:30-13:00). No Sunday hours. A 17:00 close does not count as Open evenings. No other office in the Iowa locator sweep geocodes into Des Moines city.

## Result

6 listed Post Offices, all with money orders. 1 Open evenings. 1 Open weekends. Hours labeled Central Time. 1 hold (printed Des Moines, geocodes in Pleasant Hill city).

## Site changes in this PR

- New `data/locations/des-moines.csv` and `/des-moines/`, `/des-moines/money-orders/`, and `/des-moines/after-hours/` pages.
- Des Moines is added as the first Iowa city, after Indiana, on the home page and `/cities/`. Home and `/cities/` meta now say Indianapolis, Fort Wayne, Evansville, Carmel, and Fishers, Indiana, and Des Moines, Iowa. The Iowa Census Vintage 2025 ranking memo is added under `docs/research/`. No other city CSV or page changed except those meta and list lines.
