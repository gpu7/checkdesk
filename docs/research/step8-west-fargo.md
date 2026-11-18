# West Fargo, North Dakota USPS research (2026-11-17, America/Denver)

Fifth North Dakota state city in the Census ranking (Vintage 2025, SUMLEV 162, POPESTIMATE2025). Census place is West Fargo city, GEOID 3884780, population 41,175, in Cass County (GEOID 38017). Official listed pages print West Fargo, ND. This is West Fargo, North Dakota, not Fargo, not Horace, and not Moorhead, Minnesota. Hours are Central Time (49 CFR 71.6(a); the Central–Mountain boundary in 49 CFR 71.7(a) does not reach this city). OpenStreetMap was not used. Raw data: `/workspace/step8nd/`. Classification: `/workspace/checkdesk/research/north-dakota-geocode-classify-2026-11-17.md`.

Locator passes and official pages are the shared North Dakota sweep (265 offices, all geocoded on the current and 2020 Census files, 0 errors). Classification still uses printed city and Census geocode, not the ZIP list.

## Listed (1)

- West Fargo (1387021, 415 MAIN AVE E, WEST FARGO 58078). Lists money orders. Official page prints West Fargo, ND. All four Census legs are in West Fargo city. BUSINESS hours: weekdays 8:00 a.m. to 5:30 p.m., Saturday 9:00 a.m. to 12:00 p.m., Sunday closed. Labeled Open evenings and Open weekends.

## Held

None. No other office in the North Dakota locator sweep geocodes into West Fargo city.


Fargo, Bismarck, Grand Forks, and Minot stay on separate lists. Offices in Minnesota, South Dakota, and Montana stay off this list.

## Result

1 listed Post Office, with money orders. It is labeled Open evenings (until 5:30 p.m.). It publishes Saturday hours and is labeled Open weekends (9:00 a.m. to 12:00 p.m.). It does not publish Sunday hours. Hours labeled Central Time. 0 holds.

## Site changes in this PR

- New `data/locations/west-fargo.csv` and `/west-fargo/`, `/west-fargo/money-orders/`, and `/west-fargo/after-hours/` pages.
- West Fargo is inserted under the existing North Dakota section after Minot on the home page and `/cities/`. No other existing city CSV or page changed except the home and `/cities/` meta and list lines. The unsuffixed `/west-fargo/` slug is new and does not collide with an existing page.
