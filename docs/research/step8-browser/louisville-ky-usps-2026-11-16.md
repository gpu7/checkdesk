# Step 8: Louisville, KY (2026-11-16, America/Denver)

First Kentucky city in the standing 50-state run (ship order: Louisville, Lexington, Bowling Green, Owensboro, Covington). Census place used for ranking and city-limits checks is Louisville/Jefferson County metro government (balance) (GEOID 2148006), July 1, 2025 population 641,962, in Jefferson County (GEOID 21111). The list uses the SUMLEV 162 balance, not the Jefferson County or SUMLEV 170 consolidated-city total (795,222). Hours labeled Eastern Time (49 CFR 71.4, 71.5; Jefferson County is east of the Eastern–Central boundary). This is Louisville, Kentucky, not Louisville, Colorado (`/louisville/`), and not Jeffersontown, St. Matthews, Shively city, Lyndon, Middletown, Anchorage, or the other remaining Jefferson County municipalities. The slug is `/louisville-ky/` so it does not collide with Louisville, CO (precedent: `/aurora-il/` and `/kansas-city-ks/`). The existing Louisville, CO pages and `data/locations/louisville.csv` were not edited.

The Census geocoder and the 2025/2026 place gazetteers still carry a non-functioning “Louisville city” place (GEOID 2148000, FUNCSTAT N, about 61.465 square miles) for the former city extent. In 2013, Census Geography Division created that record and reduced the TIGER balance (2148006) by excluding it ([2013 Geography Changes](https://www.census.gov/programs-surveys/acs/technical-documentation/table-and-geography-changes/2013/geography-changes.html)). ACS and the Population Estimates Program do not publish a separate estimate for GEOID 2148000 and still define the SUMLEV 162 balance as including that former-city extent. City-limits checks therefore treat a geocode leg as inside Louisville if it returns 2148006 or 2148000. Offices in the 83 other Jefferson County municipalities stay out. See `/workspace/checkdesk/research/louisville-ky-geoid-2148000-note-2026-11-16.md`.

Shared Kentucky sweep raw files: `/workspace/step8ky/`. All 482 official pages returned HTTP 200 and `match_api`, and all 482 records were geocoded on current and 2020 address and coordinate lookups with 0 errors. OpenStreetMap was not used.

Listed (8), with money-order tags and printed city Louisville. Both address files and both official map points are inside the PEP/ACS balance. No map-point fallback:

- Downtown Louisville (1361250, 835 S 7th St, Louisville, 40203; Census current 835 S 7TH ST, LOUISVILLE, KY, 40203; 2020 835 S 7TH ST, LOUISVILLE, KY, 40203; GEOID 2148000 (former Louisville city extent)). Phone 502-587-8546. Weekdays 08:00-17:00, Saturday closed, Sunday closed.
- Dr Martin Luther King Jr (1361277, 2727 W Broadway, Louisville, 40211; Census current 2727 W BROADWAY, LOUISVILLE, KY, 40211; 2020 2727 W BROADWAY, LOUISVILLE, KY, 40211; GEOID 2148000 (former Louisville city extent)). Phone 502-778-7810. Weekdays 09:00-17:00, Saturday 09:00-13:00, Sunday closed.
- Hikes Point (1366965, 3050 Hunsinger Ln, Louisville, 40220; Census current 3050 HUNSINGER LN, LOUISVILLE, KY, 40220; 2020 3050 HUNSINGER LN, LOUISVILLE, KY, 40220; GEOID 2148006 (TIGER balance remainder)). Phone 502-456-4557. Weekdays 09:00-17:00, Saturday 09:00-13:00, Sunday closed.
- Iroquois (1368054, 4772 Allmond Ave, Louisville, 40209; Census current 4772 ALLMOND AVE, LOUISVILLE, KY, 40209; 2020 4772 ALLMOND AVE, LOUISVILLE, KY, 40209; GEOID 2148000 (former Louisville city extent)). Phone 502-368-8911. Weekdays 08:30-16:30, Saturday closed, Sunday closed.
- Okolona (1436317, 7400 Jefferson Blvd, Louisville, 40219; Census current 7400 JEFFERSON BLVD, LOUISVILLE, KY, 40219; 2020 7400 JEFFERSON BLVD, LOUISVILLE, KY, 40219; GEOID 2148006 (TIGER balance remainder)). Phone 502-966-8049. Weekdays 09:00-18:00, Saturday 09:00-14:30, Sunday closed.
- Pleasure Ridge Park (1436323, 6121 Greenwood Rd, Louisville, 40258; Census current 6121 GREENWOOD RD, LOUISVILLE, KY, 40258; 2020 6121 GREENWOOD RD, LOUISVILLE, KY, 40258; GEOID 2148006 (TIGER balance remainder)). Phone 502-933-4841. Weekdays 08:00-17:00, Saturday 09:00-13:00, Sunday closed.
- Shelby (1381423, 2312 S Preston St, Louisville, 40217; Census current 2312 S PRESTON ST, LOUISVILLE, KY, 40217; 2020 2312 S PRESTON ST, LOUISVILLE, KY, 40217; GEOID 2148000 (former Louisville city extent)). Phone 502-636-2524. Weekdays 09:00-16:30, Saturday 09:00-12:00, Sunday closed.
- Shively (1436337, 3131 Crums Ln, Louisville, 40216; Census current 3131 CRUMS LN, LOUISVILLE, KY, 40216; 2020 3131 CRUMS LN, LOUISVILLE, KY, 40216; GEOID 2148006 (TIGER balance remainder)). Phone 502-449-2657. Weekdays 09:00-17:00, Saturday 09:00-13:00, Sunday closed.

The Shively Post Office official page prints Louisville and a Crums Lane address; all four Census legs are in GEOID 2148006, not in Shively city, so it is listed here.

Holds, printed Louisville but in another Jefferson County municipality (6):

- Anchorage (1436248, 11501 Park Rd, Louisville, 40223). All four legs in Anchorage city. Official page does not list money orders.
- Annshire Annex (1436249, 4500 Annshire Ave, Louisville, 40213). All four legs in Watterson Park city. Official page does not list money orders.
- Jeffersontown (1436297, 3801 Billtown Rd, Louisville, 40299). All four legs in Jeffersontown city. Official page lists money orders; held only because it is not in the balance.
- Lyndon (1436306, 8127 La Grange Rd, Louisville, 40222). All four legs in Lyndon city. Official page does not list money orders.
- Middletown (1436312, 119 Evergreen Rd, Louisville, 40243). All four legs in Middletown city. Official page lists money orders; held only because it is not in the balance.
- Saint Matthews (1436331, 4600 Shelbyville Rd Ste 126, Louisville, 40207). All four legs in St. Matthews city. Official page lists money orders; held only because it is not in the balance.

Holds, printed Louisville and inside the PEP/ACS balance, but official page does not list money orders (8):

- Air Mail Facility (1352470, 4440 Crittenden Dr, Louisville, 40221; GEOID 2148000).
- Baxter (1354229, 1527 Highland Ave, Louisville, 40204; GEOID 2148000).
- Cherokee (1357804, 2240 Taylorsville Rd Ste 1, Louisville, 40205; GEOID 2148000).
- 4th Street (1364355, 411 S 4th St Ste 175, Louisville, 40202; GEOID 2148000).
- Louisville (1436304, 1420 Gardiner Ln, Louisville, 40231; GEOID 2148000).
- Fern Creek (1436281, 9100 Fern Creek Rd, Louisville, 40291; GEOID 2148006).
- Fern Creek Carrier Annex New (1565374, 9120 Beulah Church Rd, Louisville, 40291; GEOID 2148006).
- Prospect Carrier Annex (1627613, 3600 Chamberlain Ln Ste 830, Louisville, 40241; GEOID 2148006). The Prospect Carrier Annex geocodes in the balance, not in Prospect city; it is held only because money orders are not listed.

Holds, geocodes inside the PEP/ACS balance but prints another city (5):

- Eastwood (1361967, 16207 Eastwood Cut Off Rd, Eastwood, 40018). Address files did not match; both official map points are in GEOID 2148006.
- Fairdale (1362964, 411 Mount Holly Rd, Fairdale, 40118). All four legs in GEOID 2148006.
- Fisherville (1363434, 15125 Old Taylorsville Rd, Fisherville, 40023). All four legs in GEOID 2148006.
- Harrods Creek (1366345, 6319 Upper River Rd, Harrods Creek, 40027). Address files did not match; both official map points are in GEOID 2148006.
- Masonic Home (1372101, 3761 Johnson Hall Dr, Masonic Home, 40041). Address files did not match; both official map points are in GEOID 2148000.

Evenings: 1 (Okolona until 18:00). Weekends: 6 (Dr Martin Luther King Jr, Hikes Point, Pleasure Ridge Park, and Shively Saturday 09:00-13:00; Shelby Saturday 09:00-12:00; Okolona Saturday 09:00-14:30). Downtown Louisville and Iroquois are weekday-only. None publishes Sunday hours. A 17:00 close does not count as Open evenings.

## Result

8 listed Post Offices, all with money orders. 1 Open evenings. 6 Open weekends. Hours labeled Eastern Time. 19 holds (6 printed-city vs other Jefferson County municipality; 8 no money-order tags; 5 other printed city). No map-point fallback.
