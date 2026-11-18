# Salem, Oregon USPS research (2026-11-18, America/Denver)

Second Oregon state city in the Census ranking (Vintage 2025, SUMLEV 162, POPESTIMATE2025). Census place is Salem city, GEOID 4164900, population 181,779. Official listed pages print Salem, OR. This is Salem, Oregon, mostly in Marion County plus a Polk County part, at /salem/. This is not Salem, Massachusetts, and is not Winston-Salem, North Carolina (already live at /winston-salem/). This is not Keizer, not Woodburn, not Dallas, not Independence, not Monmouth, and not Brooks. Portland, Eugene, Gresham, and Hillsboro stay on separate lists. Offices in Washington, Idaho, California, and Nevada stay off this list. Hours are Pacific Time (Oregon is in the Pacific zone under 49 CFR 71.10, west of the mountain–Pacific boundary in § 71.9(a). That boundary follows the north and west lines of Malheur County; none of this five is in Malheur County.). OpenStreetMap was not used. Raw data: `/workspace/step8or/`. Classification: `/workspace/checkdesk/research/oregon-geocode-classify-2026-11-18.md`.

Locator passes and official pages are the shared Oregon sweep (338 offices, all geocoded on the current and 2020 Census files, 0 errors). Classification still uses printed city and Census geocode, not the ZIP list.

## Listed (4)

- Hollywood (1367243, 1050 SUNNYVIEW RD NE, SALEM 97301). Lists money orders. Official page prints Salem, OR. All four Census legs are in Salem city. BUSINESS hours: weekdays 8:30 a.m. to 5:00 p.m., Saturday closed, Sunday closed. Not labeled Open evenings or Open weekends.
- Pringle Park (1378445, 410 MILL ST SE, SALEM 97301). Lists money orders. Official page prints Salem, OR. All four Census legs are in Salem city. BUSINESS hours: weekdays 8:30 a.m. to 5:00 p.m., Saturday closed, Sunday closed. Not labeled Open evenings or Open weekends.
- Vista (1386063, 3624 COMMERCIAL ST SE, SALEM 97302). Lists money orders. Official page prints Salem, OR. All four Census legs are in Salem city. BUSINESS hours: weekdays 8:30 a.m. to 5:00 p.m., Saturday closed, Sunday closed. Not labeled Open evenings or Open weekends.
- West Salem (1387178, 400 GLEN CREEK RD NW, SALEM 97304). Lists money orders. Official page prints Salem, OR. All four Census legs are in Salem city. BUSINESS hours: weekdays 8:30 a.m. to 5:00 p.m., Saturday closed, Sunday closed. Not labeled Open evenings or Open weekends.

## Held (5)

- Hollywood DCU-area and plant offices without money-order tags, all printing Salem, OR, with all four Census legs in Salem city: Salem (1439955, 1050 25th St SE), Salem (1472106, 1050 25th St SE), Salem Hollywood DCU (1367235, 2222 Claxter Rd NE), and Salem OR S&DC (1582133, 1050 25th St SE).
- Brooks (1439905, 5000 Brooklake Rd NE, SALEM 97305). Official page prints Salem, OR, and lists money orders, but all four Census legs are in no incorporated place or CDP (unincorporated Marion County), so it is held.

Portland stays on a separate list at /portland-or/. Eugene, Gresham, and Hillsboro stay on separate lists. Offices in Washington, Idaho, California, and Nevada stay off this list.

## Result

4 listed Post Offices, all with money orders (Hollywood, Pringle Park, and Vista in Marion County; West Salem in the Polk County part). None is labeled Open evenings. None publishes Saturday or Sunday hours. Hours labeled Pacific Time. 5 holds.

## Site changes in this PR

- New `data/locations/salem.csv` and `/salem/` and `/salem/money-orders/` pages. There is no `/salem/after-hours/` page, because none of the listed offices is labeled Open evenings or Open weekends, and the site does not publish an empty evenings-and-weekends list.
- Salem is inserted under the existing Oregon section after Portland on the home page and `/cities/`. No other existing city CSV or page changed except the home and `/cities/` meta and list lines. The unsuffixed `/salem/` slug is new and does not collide with an existing page.
