# South Burlington, Vermont USPS research (2026-11-18, America/Denver)

Second Vermont state city in the Census ranking (Vintage 2025, SUMLEV 162, POPESTIMATE2025). Census place is South Burlington city, GEOID 5066175, population 21,394. Official listed pages print South Burlington, UT. This is South Burlington, Vermont, in Chittenden County, at /south-burlington/. South Burlington is not Burlington. This is not Essex Junction, not Winooski, not Colchester, and not Essex town. Offices in New York, New Hampshire, and Massachusetts stay off this list. Hours are Eastern Time (The eastern zone under 49 CFR 71.4 is west of 67°30′ W. longitude and east of the boundary line described in 49 CFR 71.5, and includes all of the State of Maine, but does not include any part of the Commonwealth of Puerto Rico. Section 71.5 describes the Eastern-Central boundary through Michigan, Indiana, Kentucky, and Tennessee, and then along the Tennessee-Georgia, Alabama-Georgia, and Florida-Georgia lines; it does not mention Vermont and does not enter the state. None of the five cities sits on a zone boundary.). OpenStreetMap was not used. Raw data: `/workspace/step8vt/`. Classification: `/workspace/checkdesk/research/vermont-geocode-classify-2026-11-18.md`.

Locator passes and official pages are the shared Vermont sweep (446 offices, all geocoded on the current and 2020 Census files, 0 errors). Classification still uses printed city and Census geocode, not the ZIP list.

## Listed (1)

- South Burlington (1434619, 60 WHITE ST, SOUTH BURLINGTON 05403). Lists money orders. Official page prints South Burlington, VT. All four Census legs are in South Burlington city. BUSINESS hours: weekdays 9:00 a.m. to 5:00 p.m., Saturday 9:00 a.m. to 1:00 p.m., Sunday closed. Labeled Open weekends.

## Held (1)

- Burlington Champlain (1357611, 370 SHELBURNE RD STE 4, BURLINGTON 05401). Official page prints Burlington, VT, not South Burlington, and lists money orders. The current address file and both official map-point legs are in South Burlington city (GEOID 5066175); the 2020 address file places it in Burlington city (GEOID 5010675). Held because the printed city is Burlington, not South Burlington. This office is also held off the Burlington list because the Census geocoder does not place both the address and the official map point fully inside Burlington city.

Burlington, Essex Junction, Winooski, Colchester, and Essex town stay off this list. Offices in New York, New Hampshire, and Massachusetts stay off this list.

## Result

1 listed Post Office, with money orders, in Chittenden County. None is labeled Open evenings. One publishes Saturday hours and is labeled Open weekends: South Burlington, 9:00 a.m. to 1:00 p.m. None publishes Sunday hours. Hours labeled Eastern Time. 1 hold.

## Site changes in this PR

- New `data/locations/south-burlington.csv` and `/south-burlington/`, `/south-burlington/money-orders/`, and `/south-burlington/after-hours/` pages.
- South Burlington is inserted under the existing Vermont section after Burlington on the home page and `/cities/`. No other existing city CSV or page changed except the home and `/cities/` meta and list lines. The unsuffixed `/south-burlington/` slug is new and does not collide with an existing page.
