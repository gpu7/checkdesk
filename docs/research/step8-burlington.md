# Burlington, Vermont USPS research (2026-11-18, America/Denver)

First Vermont state city in the Census ranking (Vintage 2025, SUMLEV 162, POPESTIMATE2025). Census place is Burlington city, GEOID 5010675, population 44,019. Official listed pages print Burlington, UT. This is Burlington, Vermont, in Chittenden County, at /burlington/. This is not a Burlington in another state, not South Burlington, not Essex Junction, not Winooski, not Colchester, and not Essex town. Offices in New York, New Hampshire, and Massachusetts stay off this list. Hours are Eastern Time (The eastern zone under 49 CFR 71.4 is west of 67°30′ W. longitude and east of the boundary line described in 49 CFR 71.5, and includes all of the State of Maine, but does not include any part of the Commonwealth of Puerto Rico. Section 71.5 describes the Eastern-Central boundary through Michigan, Indiana, Kentucky, and Tennessee, and then along the Tennessee-Georgia, Alabama-Georgia, and Florida-Georgia lines; it does not mention Vermont and does not enter the state. None of the five cities sits on a zone boundary.). OpenStreetMap was not used. Raw data: `/workspace/step8vt/`. Classification: `/workspace/checkdesk/research/vermont-geocode-classify-2026-11-18.md`.

Locator passes and official pages are the shared Vermont sweep (446 offices, all geocoded on the current and 2020 Census files, 0 errors). Classification still uses printed city and Census geocode, not the ZIP list.

## Listed (2)

- Burlington (1356391, 11 ELMWOOD AVE LBBY, BURLINGTON 05401). Lists money orders. Official page prints Burlington, VT. All four Census legs are in Burlington city. BUSINESS hours: weekdays 8:00 a.m. to 5:00 p.m., Saturday 9:00 a.m. to 1:00 p.m., Sunday closed. Labeled Open weekends.
- North Burlington (1444610, 1127 NORTH AVE STE 40, BURLINGTON 05408). Lists money orders. Official page prints Burlington, VT. All four Census legs are in Burlington city. BUSINESS hours: weekdays 9:00 a.m. to 5:00 p.m., Saturday 9:00 a.m. to 12:00 p.m., Sunday closed. Labeled Open weekends.

## Held (2)

- Burlington Champlain (1357611, 370 SHELBURNE RD STE 4, BURLINGTON 05401). Official page prints Burlington, VT, and lists money orders. The current address file and both official map-point legs are in South Burlington city (GEOID 5066175); the 2020 address file places it in Burlington city (GEOID 5010675). Held because the Census geocoder does not place both the address and the official map point fully inside Burlington city. The official map point is in South Burlington city, so map-point fallback is not used. This office is also held off the South Burlington list because it prints Burlington, not South Burlington.
- Burlington Annex (1441654, 320 PINE ST, BURLINGTON 05401). Official page prints Burlington, VT. All four Census legs are in Burlington city. Held because the official page does not list money orders.

South Burlington, Essex Junction, Winooski, Colchester, and Essex town stay off this list. Offices in New York, New Hampshire, and Massachusetts stay off this list.

## Result

2 listed Post Offices, both with money orders, both in Chittenden County. None is labeled Open evenings. Two publish Saturday hours and are labeled Open weekends: Burlington, 9:00 a.m. to 1:00 p.m.; North Burlington, 9:00 a.m. to 12:00 p.m. None publishes Sunday hours. Hours labeled Eastern Time. 2 holds.

## Site changes in this PR

- New `data/locations/burlington.csv` and `/burlington/`, `/burlington/money-orders/`, and `/burlington/after-hours/` pages.
- Burlington is added as the first city in a new Vermont section on the home page and `/cities/`, after the Utah section. No other existing city CSV or page changed except the home and `/cities/` meta and list lines. The unsuffixed `/burlington/` slug is new and does not collide with an existing page.
