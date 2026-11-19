# Wheeling, West Virginia USPS research (2026-11-18, America/Denver)

Fifth West Virginia state city in the Census ranking (Vintage 2025, SUMLEV 162, POPESTIMATE2025). Census place is Wheeling city, GEOID 5486452, population 25,680. Official listed pages print Wheeling, WV. This is Wheeling, West Virginia, at /wheeling/. This is not Wheeling, Illinois. An Ohio or Marshall County geocode is not enough to list an office here. Hours are Eastern Time (The eastern zone under 49 CFR 71.4 is west of 67°30′ W. longitude and east of the boundary line described in 49 CFR 71.5, and includes all of the State of Maine, but does not include any part of the Commonwealth of Puerto Rico. Section 71.5 describes the Eastern-Central boundary through Michigan, Indiana, Kentucky, and Tennessee, and then along the Tennessee-Georgia, Alabama-Georgia, and Florida-Georgia lines; it does not mention West Virginia and does not enter the state. None of the five cities sits on a zone boundary.). OpenStreetMap was not used. Raw data: `/workspace/step8wv/`. Classification: `/workspace/checkdesk/research/west-virginia-geocode-classify-2026-11-18.md`.

Locator passes and official pages are the shared West Virginia sweep (1,033 offices, all geocoded on the current and 2020 Census files, 0 errors). Classification still uses printed city and Census geocode, not the ZIP list. The five cities are ordinary incorporated places in their home counties, not independent cities; Huntington and Wheeling each span two counties. Classification uses place GEOIDs only. OpenStreetMap was not used.

## Listed (3)

- Elm Grove (1362428, 2209 NATIONAL RD, WHEELING 26003). Lists money orders. Official page prints Wheeling, WV. All four Census legs are in Wheeling city. BUSINESS hours: weekdays 8:30 a.m. to 5:00 p.m., Saturday 9:00 a.m. to 1:00 p.m., Sunday closed. Labeled Open weekends.
- Warwood (1386477, 605 WARWOOD AVE, WHEELING 26003). Lists money orders. Official page prints Wheeling, WV. All four Census legs are in Wheeling city. BUSINESS hours: weekdays 9:00 a.m. to 11:00 a.m. and 12:00 p.m. to 3:00 p.m., Saturday closed, Sunday closed. Not labeled Open evenings or Open weekends.
- Wheeling (1387463, 2501 CHAPLINE ST, WHEELING 26003). Lists money orders. Official page prints Wheeling, WV. All four Census legs are in Wheeling city. BUSINESS hours: weekdays 9:00 a.m. to 6:00 p.m., Saturday 9:00 a.m. to 1:00 p.m., Sunday closed. Labeled Open evenings and Open weekends.

## Held (2)

- Downtown Wheeling (1361253, 1125 CHAPLINE ST STE 1, WHEELING 26003). Official page prints Wheeling, WV. All four Census legs are in Wheeling city. Held because the official page does not list money orders.
- Wheeling (1473632, 2501 CHAPLINE ST, WHEELING 26003). Official page prints Wheeling, WV. All four Census legs are in Wheeling city. Held because the official page does not list money orders. This is the same address as the listed Wheeling office.

## Result

3 listed Post Offices, all with money orders, all in Wheeling city, with no map-point fallbacks. One is labeled Open evenings: Wheeling, until 6:00 p.m. Two publish Saturday hours and are labeled Open weekends: Elm Grove, 9:00 a.m. to 1:00 p.m.; Wheeling, 9:00 a.m. to 1:00 p.m. None publishes Sunday hours. Hours labeled Eastern Time. 2 holds.

## Site changes in this PR

- New `data/locations/wheeling.csv` and `/wheeling/`, `/wheeling/money-orders/`, and `/wheeling/after-hours/` pages.
- Wheeling is inserted under the existing West Virginia section after Huntington on the home page and `/cities/`. No other existing city CSV or page changed except the home and `/cities/` meta and list lines. The unsuffixed `/wheeling/` slug is new and does not collide with an existing page. Morgantown and Parkersburg, the third and fourth West Virginia Census cities, were researched in the same sweep and are not shipped, because they have no listable offices.
