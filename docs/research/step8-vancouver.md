# Vancouver, Washington USPS research (2026-11-18, America/Denver)

Fourth Washington state city in the Census ranking (Vintage 2025, SUMLEV 162, POPESTIMATE2025). Census place is Vancouver city, GEOID 5374060, population 199,698. Official listed pages print Vancouver, WA. This is Vancouver, Washington, at /vancouver/. This is not Vancouver, British Columbia, and not Portland, Oregon (already live at /portland-or/). Offices in Orchards CDP and offices in Oregon stay off this list. Hours are Pacific Time (Washington is in the Pacific zone under 49 CFR 71.10. The mountain–Pacific boundary described in 49 CFR 71.9 does not enter Washington. None of the five cities sits on a zone boundary.). OpenStreetMap was not used. Raw data: `/workspace/step8wa/`. Classification: `/workspace/checkdesk/research/washington-geocode-classify-2026-11-18.md`.

Locator passes and official pages are the shared Washington sweep (529 offices, all geocoded on the current and 2020 Census files, 0 errors). Classification still uses printed city and Census geocode, not the ZIP list. The five cities are ordinary incorporated places in their home counties, not independent cities; classification uses place GEOIDs only. OpenStreetMap was not used.

## Listed (3)

- Cascade Park (1357196, 304 SE HEARTHWOOD BLVD, VANCOUVER 98684). Lists money orders. Official page prints Vancouver, WA. All four Census legs are in Vancouver city. BUSINESS hours: weekdays 9:00 a.m. to 5:00 p.m., Saturday 11:00 a.m. to 3:00 p.m., Sunday closed. Labeled Open weekends.
- Downtown Vancouver (1385740, 1211 DANIELS ST, VANCOUVER 98666). Lists money orders. Official page prints Vancouver, WA. All four Census legs are in Vancouver city. BUSINESS hours: weekdays 9:00 a.m. to 5:15 p.m., Saturday closed, Sunday closed. Labeled Open evenings.
- Vancouver (1385741, 2700 CAPLES AVE, VANCOUVER 98661). Lists money orders. Official page prints Vancouver, WA. All four Census legs are in Vancouver city. BUSINESS hours: weekdays 9:00 a.m. to 5:30 p.m., Saturday 9:00 a.m. to 2:00 p.m., Sunday closed. Labeled Open evenings and Open weekends.

## Held (4)

- Orchards (1376244, 11909 NE 65TH ST, VANCOUVER 98682). Official page prints Vancouver, WA, and lists money orders. The current address file and both official map-point legs are in Orchards CDP (GEOID 5351795), Clark County, not Vancouver city; the 2020 address file did not match. Held because the printed city and the geocode disagree. Map-point fallback is not used, because the official map point is not inside Vancouver city.
- East Vancouver DCU (1361879, 401 NE 136TH AVE, VANCOUVER 98684). Official page prints Vancouver, WA. All four Census legs are in Vancouver city. Held because the official page does not list money orders. This is the same address as Vancouver WA East SDC.
- Vancouver WA SDC (1601568, 2700 CAPLES AVE, VANCOUVER 98661). Official page prints Vancouver, WA. All four Census legs are in Vancouver city. Held because the official page does not list money orders. This is the same address as the listed Vancouver office.
- Vancouver WA East SDC (1612985, 401 NE 136TH AVE, VANCOUVER 98684). Official page prints Vancouver, WA. All four Census legs are in Vancouver city. Held because the official page does not list money orders. This is the same address as East Vancouver DCU.

Offices in Oregon stay off this list.

## Result

3 listed Post Offices, all with money orders, all in Vancouver city, with no map-point fallbacks. Two are labeled Open evenings: Downtown Vancouver, until 5:15 p.m., and Vancouver, until 5:30 p.m. Two publish Saturday hours and are labeled Open weekends: Cascade Park, 11:00 a.m. to 3:00 p.m.; Vancouver, 9:00 a.m. to 2:00 p.m. None publishes Sunday hours. Hours labeled Pacific Time. 4 holds.

## Site changes in this PR

- New `data/locations/vancouver.csv` and `/vancouver/`, `/vancouver/money-orders/`, and `/vancouver/after-hours/` pages.
- Vancouver is inserted under the existing Washington section after Tacoma on the home page and `/cities/`. No other existing city CSV or page changed except the home and `/cities/` meta and list lines. The unsuffixed `/vancouver/` slug is new and does not collide with an existing page.
