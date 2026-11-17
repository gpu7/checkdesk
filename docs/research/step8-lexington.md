# Step 8: Lexington, KY (2026-11-16, America/Denver)

Second Kentucky city in the standing 50-state run (ship order: Louisville, Lexington, Bowling Green, Owensboro, Covington). Census place is Lexington-Fayette urban county (GEOID 2146027), July 1, 2025 population 329,751, which equals Fayette County (GEOID 21067). Census publishes no balance label and no SUMLEV 170 row for this government. Hours labeled Eastern Time (49 CFR 71.4, 71.5; Fayette County is east of the Eastern–Central boundary). This is Lexington, Kentucky, not Lexington, Indiana, and not Georgetown, Nicholasville, Versailles, Paris, Winchester, or Richmond. The slug is `/lexington/`.

Shared Kentucky sweep raw files: `/workspace/step8ky/`. All 482 official pages returned HTTP 200 and `match_api`, and all 482 records were geocoded on current and 2020 address and coordinate lookups with 0 errors. OpenStreetMap was not used.

Listed (4), with money-order tags and printed city Lexington, KY. Both address files and both official map points are in Lexington-Fayette urban county, in Fayette County (GEOID 21067). No map-point fallback:

- Beaumont (1354348, 1025 Majestic Dr, Lexington, 40513; Census current 1025 MAJESTIC DR, LEXINGTON, KY, 40513; 2020 1025 MAJESTIC DR, LEXINGTON, KY, 40513). Phone 859-219-2266. Weekdays 08:30-17:00, Saturday 09:00-13:00, Sunday closed.
- Bluegrass (1436258, 3525 Lansdowne Dr, Lexington, 40517; Census current 3525 LANSDOWNE DR, LEXINGTON, KY, 40517; 2020 3525 LANSDOWNE DR, LEXINGTON, KY, 40517). Phone 859-271-3281. Weekdays 08:00-18:00, Saturday 09:00-13:00, Sunday closed.
- Gardenside (1364436, 1729 Alexandria Dr, Lexington, 40504; Census current 1729 ALEXANDRIA DR, LEXINGTON, KY, 40504; 2020 1729 ALEXANDRIA DR, LEXINGTON, KY, 40504). Phone 859-278-6425. Weekdays 09:00-17:00, Saturday 09:00-12:00, Sunday closed.
- Liberty Road (1370406, 2041 Creative Dr Ste 100, Lexington, 40505; Census current 2041 CREATIVE DR, LEXINGTON, KY, 40505; 2020 2041 CREATIVE DR, LEXINGTON, KY, 40505). Phone 859-255-6995. Weekdays 08:00-17:00, Saturday 09:00-12:00, Sunday closed.

Holds, printed Lexington, KY and inside the city, but official page does not list money orders (4):

- Henry Clay (1366748, 365 Duke Rd Ste A, Lexington, 40502). Weekdays 09:00-12:30,13:30-16:30; Saturday closed.
- Lexington (1370366, 1088 Nandino Blvd, Lexington, 40511). Weekdays 08:00-18:00, Saturday 09:00-13:00; held only because money orders are not listed.
- Post Rider (1378206, 210 E High St, Lexington, 40507). Weekdays 09:00-17:00; Saturday closed.
- Brentwood Carrier Annex (1436741, 1045 Brentwood Ct Ste 110, Lexington, 40511; no BUSINESS hours).

The Lexington, IN Post Office (1370373, 2765 S Cherry St, Lexington, IN 47138) prints Lexington, Indiana, and was excluded.

Evenings: 1 (Bluegrass until 18:00). Weekends: 4 (Beaumont and Bluegrass Saturday 09:00-13:00; Gardenside and Liberty Road Saturday 09:00-12:00). None publishes Sunday hours. A 17:00 close does not count as Open evenings. No other office in the Kentucky locator sweep geocodes into Lexington.

## Result

4 listed Post Offices, all with money orders. 1 Open evenings. 4 Open weekends. Hours labeled Eastern Time. 4 holds (no money-order tags). Lexington, IN excluded. No map-point fallback.

## Site changes in this PR

- New `data/locations/lexington.csv` and `/lexington/`, `/lexington/money-orders/`, and `/lexington/after-hours/` pages.
- Lexington is inserted under Kentucky after Louisville on the home page and `/cities/`. Home and `/cities/` meta now say Wichita, Overland Park, Kansas City, Olathe, and Topeka, Kansas, and Louisville and Lexington, Kentucky. No other city CSV or page changed except those meta and list lines.
