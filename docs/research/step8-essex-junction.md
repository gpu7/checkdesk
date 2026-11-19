# Essex Junction, Vermont USPS research (2026-11-18, America/Denver)

Fourth Vermont state city in the Census ranking (Vintage 2025, SUMLEV 162, POPESTIMATE2025). Census place is Essex Junction city, GEOID 5024400, population 10,921. Official listed pages print Essex Junction, UT. This is Essex Junction, Vermont, in Chittenden County, at /essex-junction/. Essex town is not Essex Junction. This is not Burlington, not South Burlington, not Winooski, not Colchester, not Essex County, Vermont, and not Essex County, New York. Offices in New York, New Hampshire, and Massachusetts stay off this list. Hours are Eastern Time (The eastern zone under 49 CFR 71.4 is west of 67°30′ W. longitude and east of the boundary line described in 49 CFR 71.5, and includes all of the State of Maine, but does not include any part of the Commonwealth of Puerto Rico. Section 71.5 describes the Eastern-Central boundary through Michigan, Indiana, Kentucky, and Tennessee, and then along the Tennessee-Georgia, Alabama-Georgia, and Florida-Georgia lines; it does not mention Vermont and does not enter the state. None of the five cities sits on a zone boundary.). OpenStreetMap was not used. Raw data: `/workspace/step8vt/`. Classification: `/workspace/checkdesk/research/vermont-geocode-classify-2026-11-18.md`.

Locator passes and official pages are the shared Vermont sweep (446 offices, all geocoded on the current and 2020 Census files, 0 errors). Classification still uses printed city and Census geocode, not the ZIP list.

## Listed (1)

- Pearl Street (1377051, 78 PEARL ST, ESSEX JUNCTION 05453). Lists money orders. Official page prints Essex Junction, VT. All four Census legs are in Essex Junction city. BUSINESS hours: weekdays 8:30 a.m. to 5:00 p.m., Saturday 10:00 a.m. to 1:00 p.m., Sunday closed. Labeled Open weekends.

## Held (1)

- Essex Junction (1362737, 22 ESSEX WAY, ESSEX JUNCTION 05452). Official page prints Essex Junction, VT, and lists money orders. All four Census legs return Chittenden County (GEOID 50007) with no incorporated place or CDP. That is Essex town, a SUMLEV 061 county subdivision, not Essex Junction city (GEOID 5024400). The official map point is not inside Essex Junction city, so map-point fallback is not used. Held because the Census geocoder does not place both the address and the official map point fully inside Essex Junction city.

Burlington, South Burlington, Winooski, and Colchester stay off this list. Essex town is not Essex Junction. Offices in New York, New Hampshire, and Massachusetts stay off this list.

## Result

1 listed Post Office, with money orders, in Chittenden County. None is labeled Open evenings. One publishes Saturday hours and is labeled Open weekends: Pearl Street, 10:00 a.m. to 1:00 p.m. None publishes Sunday hours. Hours labeled Eastern Time. 1 hold.

## Site changes in this PR

- New `data/locations/essex-junction.csv` and `/essex-junction/`, `/essex-junction/money-orders/`, and `/essex-junction/after-hours/` pages.
- Essex Junction is inserted under the existing Vermont section after Rutland on the home page and `/cities/`. No other existing city CSV or page changed except the home and `/cities/` meta and list lines. The unsuffixed `/essex-junction/` slug is new and does not collide with an existing page.
