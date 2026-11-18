# Salt Lake City, Utah USPS research (2026-11-18, America/Denver)

First Utah state city in the Census ranking (Vintage 2025, SUMLEV 162, POPESTIMATE2025). Census place is Salt Lake City city, GEOID 4967000, population 218,428. Official listed pages print Salt Lake City, UT. This is Salt Lake City, Utah, in Salt Lake County, at /salt-lake-city/. This is not Salt Lake County, not South Salt Lake, not North Salt Lake, not West Valley City, and not West Jordan. Offices that print Salt Lake City but geocode in Cottonwood Heights, Holladay, Millcreek, or Murray stay off this list. Offices in Arizona, Nevada, and California stay off this list. Hours are Mountain Time (The mountain zone under 49 CFR 71.8 is west of the boundary in 49 CFR 71.7 and east of the boundary in 49 CFR 71.9. The Central-Mountain boundary in 49 CFR 71.7 does not enter Utah. The Mountain-Pacific boundary in 49 CFR 71.9(b), in the stretch headed Utah-Nevada-Arizona-California, follows the Utah-Nevada boundary and carves only the City of West Wendover, Nevada, into the mountain zone. The entire State of Utah lies east of that line and is in the mountain zone. None of the five is a municipality on the 49 CFR 71.9(d) boundary line. Utah has not exempted itself from the Uniform Time Act DST rule in 49 CFR 71.2.). OpenStreetMap was not used. Raw data: `/workspace/step8ut/`. Classification: `/workspace/checkdesk/research/utah-geocode-classify-2026-11-18.md`.

Locator passes and official pages are the shared Utah sweep (164 offices, all geocoded on the current and 2020 Census files, 0 errors). Classification still uses printed city and Census geocode, not the ZIP list.

## Listed (5)

- Downtown SLC Retail EAQ (1588456, 386 W 500 S STE 20, SALT LAKE CITY 84101). Lists money orders. Official page prints Salt Lake City, UT. All four Census legs are in Salt Lake City city. BUSINESS hours: weekdays 8:00 a.m. to 5:30 p.m., Saturday closed, Sunday closed. Labeled Open evenings.
- Foothill (1363635, 2255 E SUNNYSIDE AVE, SALT LAKE CITY 84108). Lists money orders. Official page prints Salt Lake City, UT. All four Census legs are in Salt Lake City city. BUSINESS hours: weekdays 8:30 a.m. to 5:30 p.m., Saturday 10:00 a.m. to 3:30 p.m., Sunday closed. Labeled Open evenings and Open weekends.
- Northwest (1375584, 801 N REDWOOD RD, SALT LAKE CITY 84116). Lists money orders. Official page prints Salt Lake City, UT. All four Census legs are in Salt Lake City city. BUSINESS hours: weekdays 8:30 a.m. to 5:30 p.m., Saturday 10:00 a.m. to 2:00 p.m., Sunday closed. Labeled Open evenings and Open weekends.
- Salt Lake City (1440060, 1760 W 2100 S, SALT LAKE CITY 84199). Lists money orders. Official page prints Salt Lake City, UT. All four Census legs are in Salt Lake City city. BUSINESS hours: weekdays 7:30 a.m. to 6:00 p.m., Saturday 10:00 a.m. to 2:00 p.m., Sunday closed. Labeled Open evenings and Open weekends.
- Sugarhouse (1383850, 1953 S 1100 E, SALT LAKE CITY 84106). Lists money orders. Official page prints Salt Lake City, UT. All four Census legs are in Salt Lake City city. BUSINESS hours: weekdays 8:00 a.m. to 6:00 p.m., Saturday 10:00 a.m. to 2:00 p.m., Sunday closed. Labeled Open evenings and Open weekends.

## Held (6)

- Cottonwood (1440018, 6890 S 2300 E, SALT LAKE CITY 84121). Official page prints Salt Lake City, UT, and lists money orders. All four Census legs are in Cottonwood Heights city, a separate incorporated place. Held because the Census geocoder does not place both the address and the official map point fully inside Salt Lake City city.
- Holladay (1440036, 2350 E ARBOR LN, SALT LAKE CITY 84117). Official page prints Salt Lake City, UT, and lists money orders. All four Census legs are in Holladay city, a separate incorporated place. Held because the Census geocoder does not place both the address and the official map point fully inside Salt Lake City city.
- Millcreek (1440048, 3350 S 2940 E, SALT LAKE CITY 84109). Official page prints Salt Lake City, UT, and lists money orders. All four Census legs are in Millcreek city, a separate incorporated place. Held because the Census geocoder does not place both the address and the official map point fully inside Salt Lake City city.
- Murray (1440053, 4989 S STATE ST, SALT LAKE CITY 84107). Official page prints Salt Lake City, UT, and lists money orders. All four Census legs are in Murray city, a separate incorporated place. Held because the Census geocoder does not place both the address and the official map point fully inside Salt Lake City city.
- North Salt Lake (1440054, 345 N HIGHWAY 89, NORTH SALT LAKE 84054). Official page prints North Salt Lake, UT, not Salt Lake City. The current and 2020 address files place it in Salt Lake City city; both official map-point legs are in North Salt Lake city. Held because the printed city is North Salt Lake.
- Salt Lake City UT West SDC (1614796, 1095 S 4800 W, SALT LAKE CITY 84104). Official page prints Salt Lake City, UT. All four Census legs are in Salt Lake City city. Held because the official page does not list money orders.

Offices in Arizona, Nevada, and California stay off this list.

## Result

5 listed Post Offices, all with money orders, all in Salt Lake County. Five are labeled Open evenings: Downtown SLC Retail EAQ, until 5:30 p.m., Foothill, until 5:30 p.m., Northwest, until 5:30 p.m., Salt Lake City, until 6:00 p.m., and Sugarhouse, until 6:00 p.m. Four publish Saturday hours and are labeled Open weekends: Foothill, 10:00 a.m. to 3:30 p.m.; Northwest, Salt Lake City, and Sugarhouse, 10:00 a.m. to 2:00 p.m. None publishes Sunday hours. Hours labeled Mountain Time. 6 holds.

## Site changes in this PR

- New `data/locations/salt-lake-city.csv` and `/salt-lake-city/`, `/salt-lake-city/money-orders/`, and `/salt-lake-city/after-hours/` pages.
- Salt Lake City is added as the first city in a new Utah section on the home page and `/cities/`, after the Texas section. No other existing city CSV or page changed except the home and `/cities/` meta and list lines. The unsuffixed `/salt-lake-city/` slug is new and does not collide with an existing page.
