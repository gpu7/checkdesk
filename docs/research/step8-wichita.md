# Step 8: Wichita, KS (2026-11-16, America/Denver)

First Kansas city in the standing 50-state run (ship order: Wichita, Overland Park, Kansas City, Olathe, Topeka). Census place is Wichita city (GEOID 2079000), July 1, 2025 population 400,987, in Sedgwick County (GEOID 20173). Hours labeled Central Time (49 CFR 71.6; Sedgwick County is east of the 49 CFR 71.7(d) Kansas-Colorado boundary). This is Wichita, Kansas, not Wichita Falls, Texas, and not Derby, Andover, Maize, Park City, or Bel Aire.

Shared Kansas sweep raw files: `/workspace/step8ks/`. All 339 official pages returned HTTP 200 and `match_api`, and all 339 records were geocoded on current and 2020 address and coordinate lookups with 0 errors. OpenStreetMap was not used.

Listed (7), with money-order tags and printed city Wichita. Both address files and both official map points are in Wichita city, in Sedgwick County (GEOID 20173). No map-point fallback:

- Chisholm (1357980, 2510 S Elizabeth Ave, Wichita, 67217; Census current 2510 S ELIZABETH AVE, WICHITA, KS, 67217; 2020 2510 S ELIZABETH AVE, WICHITA, KS, 67217). Phone 316-264-0114. Weekdays 08:30-17:00, Saturday 08:30-12:00, Sunday closed.
- Corporate Hills (1359312, 9350 E Corporate Hills Dr, Wichita, 67207; Census current 9350 E CORPORATE HILLS DR, WICHITA, KS, 67207; 2020 9350 E CORPORATE HILLS DR, WICHITA, KS, 67207). Phone 316-612-8013. Weekdays 08:00-17:30, Saturday 09:00-13:00, Sunday closed.
- Downtown (1361226, 330 W 2nd St N, Wichita, 67202; Census current 330 W 2ND ST N, WICHITA, KS, 67202; 2020 330 W 2ND ST N, WICHITA, KS, 67202). Phone 316-267-7710. Weekdays 08:00-17:00, Saturday 09:00-12:00, Sunday closed.
- GMF Retail Window (1435564, 7117 W Harry St, Wichita, 67276; Census current 7117 W HARRY ST, WICHITA, KS, 67276; 2020 7117 E HARRY ST, WICHITA, KS, 67207). Phone 316-219-4361. Weekdays 08:00-17:30, Saturday 09:00-14:00, Sunday closed.
- Munger (1374247, 1314 N Oliver Ave, Wichita, 67208; Census current 1314 N OLIVER ST, WICHITA, KS, 67208; 2020 1314 N OLIVER ST, WICHITA, KS, 67208). Phone 316-618-0054. Weekdays 08:00-17:00, Saturday 08:30-12:00, Sunday closed.
- North Wichita (1375482, 2325 N Arkansas Ave, Wichita, 67204; Census current 2325 ARKANSAS AVE, WICHITA, KS, 67204; 2020 2325 ARKANSAS AVE, WICHITA, KS, 67204). Phone 316-838-0309. Weekdays 08:30-16:30, Saturday 10:00-12:00, Sunday closed.
- River City (1379435, 3241 S Hydraulic St, Wichita, 67216; Census current 3241 S HYDRAULIC ST, WICHITA, KS, 67216; 2020 3241 S HYDRAULIC ST, WICHITA, KS, 67216). Phone 316-529-1653. Weekdays 08:30-17:00, Saturday 08:30-12:00, Sunday closed.

Address-file notes, still inside Wichita city on both vintages: Munger printed 1314 N Oliver Ave, both files matched 1314 N Oliver St; North Wichita printed 2325 N Arkansas Ave, both files matched 2325 Arkansas Ave; GMF Retail Window printed 7117 W Harry St, 67276, the current file matched that address, and the 2020 file matched 7117 E Harry St, Wichita, KS, 67207.

Holds, printed Wichita and inside the city, but official page does not list money orders (1):

- Delano (1360573, 626 S Tyler Rd, Wichita, 67209; no money-order tags, and the official page has no BUSINESS hours). Both address files and both official map points are in Wichita city.

No hold for a printed-city vs geocode mismatch. No office that prints another city has a geocode leg inside Wichita city.

Evenings: 2 (Corporate Hills and the GMF Retail Window, both until 17:30). Weekends: 7 (all listed offices publish Saturday hours; none publishes Sunday hours). A 17:00 close does not count as Open evenings. No other office in the Kansas locator sweep geocodes into Wichita city.

## Result

7 listed Post Offices, all with money orders. 2 Open evenings. 7 Open weekends. Hours labeled Central Time. 1 hold (Delano, no money-order tags).

## Site changes in this PR

- New `data/locations/wichita.csv` and `/wichita/`, `/wichita/money-orders/`, and `/wichita/after-hours/` pages.
- Wichita is added as the first Kansas city, after Iowa, on the home page and `/cities/`. Home and `/cities/` meta now say Des Moines, Cedar Rapids, Davenport, Sioux City, and Ankeny, Iowa, and Wichita, Kansas. The Kansas Census Vintage 2025 ranking memo is added under `docs/research/`. No other city CSV or page changed except those meta and list lines.
