# Toledo, Ohio USPS research (2026-11-18, America/Denver)

Fourth Ohio state city in the Census ranking (Vintage 2025, SUMLEV 162, POPESTIMATE2025). Census place is Toledo city, GEOID 3977000, population 263,423, in Lucas County (GEOID 39095). Official listed pages print Toledo, OH. This is Toledo, Ohio, in Lucas County, not Oregon, not Sylvania, not Maumee, and not Monroe, Michigan. Columbus, Cleveland, Cincinnati, and Akron stay on separate lists. Offices in Michigan, Indiana, Kentucky, West Virginia, and Pennsylvania stay off this list. Hours are Eastern Time (49 CFR 71.4 and 71.5; the Eastern–Central boundary runs through Michigan, Indiana, Kentucky, and Tennessee and does not mention Ohio or enter the state). OpenStreetMap was not used. Raw data: `/workspace/step8oh/`. Classification: `/workspace/checkdesk/research/ohio-geocode-classify-2026-11-17.md`.

Locator passes and official pages are the shared Ohio sweep (1,036 offices, all geocoded on the current and 2020 Census files, 0 errors). Classification still uses printed city and Census geocode, not the ZIP list.

## Listed (10)

- Central (1432933, 235 N ERIE ST, TOLEDO 43604). Lists money orders. Official page prints Toledo, OH. All four Census legs are in Toledo city. BUSINESS hours: weekdays 8:30 a.m. to 1:00 p.m. and 2:00 p.m. to 4:30 p.m., Saturday closed, Sunday closed. Not labeled Open evenings or Open weekends.
- Kenwood (1368916, 2941 HAUGHTON DR, TOLEDO 43606). Lists money orders. Official page prints Toledo, OH. All four Census legs are in Toledo city. BUSINESS hours: weekdays 8:00 a.m. to 5:00 p.m., Saturday 8:30 a.m. to 12:30 p.m., Sunday closed. Labeled Open weekends.
- Old West End (1376045, 2280 ASHLAND AVE, TOLEDO 43620). Lists money orders. Official page prints Toledo, OH. All four Census legs are in Toledo city. BUSINESS hours: weekdays 9:00 a.m. to 1:00 p.m. and 2:00 p.m. to 5:00 p.m., Saturday closed, Sunday closed. Not labeled Open evenings or Open weekends.
- Point Place Station (1377929, 4445 N SUMMIT ST, TOLEDO 43611). Lists money orders. Official page prints Toledo, OH. All four Census legs are in Toledo city. BUSINESS hours: weekdays 9:00 a.m. to 5:00 p.m., Saturday 9:00 a.m. to 12:00 p.m., Sunday closed. Labeled Open weekends.
- Reynolds Corners (1379153, 6020 W BANCROFT ST, TOLEDO 43615). Lists money orders. Official page prints Toledo, OH. All four Census legs are in Toledo city. BUSINESS hours: weekdays 8:00 a.m. to 6:00 p.m., Saturday 8:30 a.m. to 1:30 p.m., Sunday closed. Labeled Open evenings and Open weekends.
- South Toledo (1382299, 1144 S DETROIT AVE, TOLEDO 43614). Lists money orders. Official page prints Toledo, OH. All four Census legs are in Toledo city. BUSINESS hours: weekdays 8:00 a.m. to 5:00 p.m., Saturday 8:00 a.m. to 12:00 p.m., Sunday closed. Labeled Open weekends.
- Station A (1517336, 225 MAIN ST, TOLEDO 43605). Lists money orders. Official page prints Toledo, OH. All four Census legs are in Toledo city. BUSINESS hours: weekdays 8:30 a.m. to 12:45 p.m. and 1:45 p.m. to 4:30 p.m., Saturday closed, Sunday closed. Not labeled Open evenings or Open weekends.
- Toledo (1437088, 435 S SAINT CLAIR ST, TOLEDO 43601). Lists money orders. Official page prints Toledo, OH. All four Census legs are in Toledo city. BUSINESS hours: weekdays 9:00 a.m. to 5:30 p.m., Saturday closed, Sunday closed. Labeled Open evenings.
- Wernert (1386922, 2618 TREMAINSVILLE RD, TOLEDO 43613). Lists money orders. Official page prints Toledo, OH. All four Census legs are in Toledo city. BUSINESS hours: weekdays 8:00 a.m. to 5:00 p.m., Saturday 8:00 a.m. to 12:00 p.m., Sunday closed. Labeled Open weekends.
- West Toledo (1387216, 1568 W SYLVANIA AVE, TOLEDO 43612). Lists money orders. Official page prints Toledo, OH. All four Census legs are in Toledo city. BUSINESS hours: weekdays 8:30 a.m. to 5:00 p.m., Saturday 8:30 a.m. to 12:00 p.m., Sunday closed. Labeled Open weekends.

## Held

### Geocode mismatch (1)

- Franklin Park (1364023, 5151 MONROE ST, TOLEDO 43623). Prints Toledo, OH, and lists money orders, but the current address file and the official map point on both Census files are not in an incorporated place or CDP (still in Lucas County). The 2020 address file placed it in Toledo city. Held for a geocode mismatch.

### No money-order tags (4)

- Midtown (1373006, 1609 DORR ST, TOLEDO 43607). Prints Toledo, OH, and all four Census legs are in Toledo city, but the official page does not list money orders. Held for no money-order tags.
- Central (1454774, 430 BROADWAY ST, TOLEDO 43604). Prints Toledo, OH, and all four Census legs are in Toledo city, but the official page does not list money orders. This is a different office from the listed Central office at 235 N Erie St. Held for no money-order tags.
- Toledo (1472104, 435 S SAINT CLAIR ST, TOLEDO 43601). Prints Toledo, OH, and all four Census legs are in Toledo city, but the official page does not list money orders. This is a different office from the listed Toledo office at the same street address. Held for no money-order tags.
- Manhattan (1510699, 549 E MANHATTAN BLVD, TOLEDO 43608). Prints Toledo, OH, and all four Census legs are in Toledo city, but the official page does not list money orders. Held for no money-order tags.

Columbus, Cleveland, Cincinnati, and Akron stay on separate lists. Offices in Michigan, Indiana, Kentucky, West Virginia, and Pennsylvania stay off this list.

## Result

10 listed Post Offices, all with money orders. Two are labeled Open evenings (Reynolds Corners, until 6:00 p.m.; Toledo, until 5:30 p.m.). Six publish Saturday hours and are labeled Open weekends. None publishes Sunday hours. Hours labeled Eastern Time. 5 holds.

## Site changes in this PR

- New `data/locations/toledo.csv` and `/toledo/`, `/toledo/money-orders/`, and `/toledo/after-hours/` pages.
- Toledo is inserted under the existing Ohio section after Cincinnati on the home page and `/cities/`. No other existing city CSV or page changed except the home and `/cities/` meta and list lines. The unsuffixed `/toledo/` slug is new and does not collide with an existing page.
