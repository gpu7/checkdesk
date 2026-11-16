# Step 8: Topeka, KS (2026-11-16, America/Denver)

Fifth Kansas city in the standing 50-state run (ship order: Wichita, Overland Park, Kansas City, Olathe, Topeka). Census place is Topeka city (GEOID 2071000), July 1, 2025 population 125,795, in Shawnee County (GEOID 20177). Hours labeled Central Time (49 CFR 71.6; Shawnee County is east of the 49 CFR 71.7(d) Kansas-Colorado boundary). This is Topeka, Kansas, not Lawrence, not Silver Lake, and not a Topeka in another state.

Shared Kansas sweep raw files: `/workspace/step8ks/`. All 339 official pages returned HTTP 200 and `match_api`, and all 339 records were geocoded on current and 2020 address and coordinate lookups with 0 errors. OpenStreetMap was not used.

Listed (4), with money-order tags and printed city Topeka. Both address files and both official map points are in Topeka city, in Shawnee County (GEOID 20177). No map-point fallback:

- Gage Center (1364301, 1430 SW Woodhull St, Topeka, 66604; Census current 1430 SW WOODHULL ST, TOPEKA, KS, 66604; 2020 1430 SW WOODHULL ST, TOPEKA, KS, 66604). Phone 785-272-0002. Weekdays 08:00-17:00, Saturday 09:00-12:00, Sunday closed.
- Hicrest (1366885, 2921 SE Adams St, Topeka, 66605; Census current 2921 SE ADAMS ST, TOPEKA, KS, 66605; 2020 2921 SE ADAMS ST, TOPEKA, KS, 66605). Phone 785-266-0347. Weekdays 08:00-17:00, Saturday 09:00-12:00, Sunday closed.
- North Topeka (1375460, 220 NW Lyman Rd, Topeka, 66608; Census current 220 NW LYMAN RD, TOPEKA, KS, 66608; 2020 220 NW LYMAN RD, TOPEKA, KS, 66608). Phone 785-295-9188. Weekdays 08:00-17:00, Saturday 09:00-12:00, Sunday closed.
- Topeka (1435650, 424 S Kansas Ave Ste 1, Topeka, 66603; Census current 424 S KANSAS AVE, TOPEKA, KS, 66603; 2020 424 S KANSAS AVE, TOPEKA, KS, 66603). Phone 785-295-9160. Weekdays 08:00-17:00, Saturday 09:00-12:00, Sunday closed.

The Topeka Post Office official page prints 424 S Kansas Ave Ste 1; both Census address files matched 424 S Kansas Ave, Topeka, KS, 66603, still in Topeka city.

Holds, printed Topeka but not inside the city (1):

- Pauline (1376978, 5826 SW Topeka Blvd, Topeka, 66619). Both Census address files matched 5826 SW TOPEKA BLVD, TOPEKA, KS, 66619, and both official map points, but none of the four legs is in an incorporated place or CDP (all four are in Shawnee County, GEOID 20177). The official page also does not list money orders. Weekdays 09:00-12:00, Saturday closed, Sunday closed.

Holds, printed Topeka and inside the city, but official page does not list money orders (2):

- Topeka (1472085, 1410 NW Gage Blvd Rm 111, Topeka, 66618; no BUSINESS hours).
- Topeka KS S&DC (1578793, same printed street address). It publishes weekday hours until 19:00 and Saturday 09:00-17:00, but it is held because the official page does not list money orders.

No office that prints another city has a geocode leg inside Topeka city.

Evenings: 0 (weekday retail closes at 17:00). Weekends: 4 (all listed offices publish Saturday hours 09:00-12:00; none publishes Sunday hours). A 17:00 close does not count as Open evenings. No other office in the Kansas locator sweep geocodes into Topeka city.

## Result

4 listed Post Offices, all with money orders. 0 Open evenings. 4 Open weekends. Hours labeled Central Time. 3 holds (Pauline, printed-city vs geocode mismatch; Topeka 1472085 and Topeka KS S&DC, no money-order tags).

## Site changes in this PR

- New `data/locations/topeka.csv` and `/topeka/`, `/topeka/money-orders/`, and `/topeka/after-hours/` pages.
- Topeka is inserted under Kansas after Olathe on the home page and `/cities/`. Home and `/cities/` meta now say Des Moines, Cedar Rapids, Davenport, Sioux City, and Ankeny, Iowa, and Wichita, Overland Park, Kansas City, Olathe, and Topeka, Kansas. No other city CSV or page changed except those meta and list lines.
