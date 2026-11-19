# Charleston, West Virginia USPS research (2026-11-18, America/Denver)

First West Virginia state city in the Census ranking (Vintage 2025, SUMLEV 162, POPESTIMATE2025). Census place is Charleston city, GEOID 5414600, population 46,117. Official listed pages print Charleston, WV. This is Charleston, West Virginia, at /charleston-wv/. This is not Charleston, South Carolina, which is already live at /charleston/, and not North Charleston, South Carolina, at /north-charleston/. A Kanawha County geocode is not enough to list an office here. Hours are Eastern Time (The eastern zone under 49 CFR 71.4 is west of 67°30′ W. longitude and east of the boundary line described in 49 CFR 71.5, and includes all of the State of Maine, but does not include any part of the Commonwealth of Puerto Rico. Section 71.5 describes the Eastern-Central boundary through Michigan, Indiana, Kentucky, and Tennessee, and then along the Tennessee-Georgia, Alabama-Georgia, and Florida-Georgia lines; it does not mention West Virginia and does not enter the state. None of the five cities sits on a zone boundary.). OpenStreetMap was not used. Raw data: `/workspace/step8wv/`. Classification: `/workspace/checkdesk/research/west-virginia-geocode-classify-2026-11-18.md`.

Locator passes and official pages are the shared West Virginia sweep (1,033 offices, all geocoded on the current and 2020 Census files, 0 errors). Classification still uses printed city and Census geocode, not the ZIP list. The five cities are ordinary incorporated places in their home counties, not independent cities; Huntington and Wheeling each span two counties. Classification uses place GEOIDs only. OpenStreetMap was not used.

## Listed (1)

- Charleston (1357676, 1002 LEE ST E, CHARLESTON 25301). Lists money orders. Official page prints Charleston, WV. All four Census legs are in Charleston city. BUSINESS hours: weekdays 8:00 a.m. to 6:00 p.m., Saturday 9:00 a.m. to 1:00 p.m., Sunday closed. Labeled Open evenings and Open weekends.

## Held (9)

- Cross Lanes (1437444, 5306 BIG TYLER RD, CHARLESTON 25313). Official page prints Charleston, WV, and lists money orders. All four Census legs are in Cross Lanes CDP, not Charleston city. Held because the printed city and the geocode disagree, including a CDP. Map-point fallback is not used, because the official map point is not inside Charleston city.
- Kanawha City (1368665, 4600 MACCORKLE AVE SE, CHARLESTON 25304). Official page prints Charleston, WV, and does not list money orders. The current address and both official map-point legs are in Charleston city; the 2020 address file did not match. Held because the Census geocoder does not place both the address and the official map point fully inside the city, and because the official page does not list money orders. Map-point fallback is not used, because the office has no money-order tags.
- Marmet (1437484, 9303 MACCORKLE AVE, CHARLESTON 25315). Official page prints Charleston, WV, and does not list money orders. All four Census legs are in Marmet city, not Charleston city. Held because the printed city and the geocode disagree, and because the official page does not list money orders. Map-point fallback is not used, because the official map point is not inside Charleston city.
- Sissonville (1437512, 6088 SISSONVILLE DR, CHARLESTON 25312). Official page prints Charleston, WV, and lists money orders. Both address legs are in Sissonville CDP; both official map-point legs are in no incorporated place or CDP. Held because the printed city and the geocode disagree, including a CDP. Map-point fallback is not used, because the official map point is not inside Charleston city.
- Town Center (1437527, 1057 CHARLESTON TOWN CTR, CHARLESTON 25389). Official page prints Charleston, WV, and does not list money orders. The current and 2020 address files did not match; both official map-point legs are in Charleston city. Held because the Census geocoder does not place both the address and the official map point fully inside the city, and because the official page does not list money orders. Map-point fallback is not used, because the office has no money-order tags.
- Southridge Centre (1382376, 2470 MOUNTAINEER BLVD, SOUTH CHARLESTON 25309). Official page prints South Charleston, WV, not Charleston, and does not list money orders. The current address and both official map-point legs are in Charleston city; the 2020 address file did not match. Held because the printed city is South Charleston, not Charleston.
- Charleston WV E Lee SDC (1599150, 1002 LEE ST E, CHARLESTON 25301). Official page prints Charleston, WV. All four Census legs are in Charleston city. Held because the official page does not list money orders. This is the same address as the listed Charleston office.
- Station C (1383448, 2328 7TH AVE, CHARLESTON 25387). Official page prints Charleston, WV. All four Census legs are in Charleston city. Held because the official page does not list money orders.
- Stonewall (1521495, 401 VIRGINIA ST W, CHARLESTON 25302). Official page prints Charleston, WV. All four Census legs are in Charleston city. Held because the official page does not list money orders.

South Charleston, Marmet, Cross Lanes CDP, Sissonville CDP, and other Kanawha County places stay off this list.

## Result

1 listed Post Office, with money orders, in Charleston city, with no map-point fallbacks. One is labeled Open evenings: Charleston, until 6:00 p.m. One publishes Saturday hours and is labeled Open weekends: Charleston, 9:00 a.m. to 1:00 p.m. None publishes Sunday hours. Hours labeled Eastern Time. 9 holds.

## Site changes in this PR

- New `data/locations/charleston-wv.csv` and `/charleston-wv/`, `/charleston-wv/money-orders/`, and `/charleston-wv/after-hours/` pages.
- Charleston is added as the first city in a new West Virginia section on the home page and `/cities/`, after the Washington section. No other existing city CSV or page changed except the home and `/cities/` meta and list lines. The `/charleston-wv/` slug is used because `/charleston/` is Charleston, South Carolina.
