# Norman, Oklahoma USPS research (2026-11-18, America/Denver)

Third Oklahoma state city in the Census ranking (Vintage 2025, SUMLEV 162, POPESTIMATE2025). Census place is Norman city, GEOID 4052500, population 130,943, in Cleveland County (GEOID 40027). Official listed pages print Norman, OK. This is Norman, Oklahoma, in Cleveland County, not Moore, not Noble, not Slaughterville, and not Lexington. Oklahoma City, Tulsa, Broken Arrow, and Edmond stay on separate lists. Offices in Kansas, Texas, Arkansas, Missouri, Colorado, and New Mexico stay off this list. Hours are Central Time (Oklahoma is in the Central zone under 49 CFR 71.6 and 71.7(e). The central–mountain boundary runs along the Colorado-Oklahoma boundary to the northwest corner of Oklahoma, then south along the west boundary of Oklahoma; all of Oklahoma, including the panhandle, is east of that line.). OpenStreetMap was not used. Raw data: `/workspace/step8ok/`. Classification: `/workspace/checkdesk/research/oklahoma-geocode-classify-2026-11-18.md`.

Locator passes and official pages are the shared Oklahoma sweep (353 offices, all geocoded on the current and 2020 Census files, 0 errors). Classification still uses printed city and Census geocode, not the ZIP list.

## Listed (2)

- Norman (1375206, 129 W GRAY ST, NORMAN 73069). Lists money orders. Official page prints Norman, OK. All four Census legs are in Norman city. BUSINESS hours: weekdays 8:30 a.m. to 5:30 p.m., Saturday 9:30 a.m. to 1:00 p.m., Sunday closed. Labeled Open evenings and Open weekends.
- Sooner (1382059, 200 36TH AVE NW, NORMAN 73072). Lists money orders. Official page prints Norman, OK. All four Census legs are in Norman city. BUSINESS hours: weekdays 8:30 a.m. to 5:00 p.m., Saturday 9:30 a.m. to 1:00 p.m., Sunday closed. Labeled Open weekends.

## Held

None. No other office in the Oklahoma locator sweep geocodes into Norman city.

Oklahoma City, Tulsa, Broken Arrow, and Edmond stay on separate lists. Offices in Kansas, Texas, Arkansas, Missouri, Colorado, and New Mexico stay off this list.

## Result

2 listed Post Offices, both with money orders. One is labeled Open evenings: Norman, until 5:30 p.m. Both publish Saturday hours and are labeled Open weekends. None publishes Sunday hours. Hours labeled Central Time. 0 holds.

## Site changes in this PR

- New `data/locations/norman.csv` and `/norman/`, `/norman/money-orders/`, and `/norman/after-hours/` pages.
- Norman is inserted under the existing Oklahoma section after Tulsa on the home page and `/cities/`. No other existing city CSV or page changed except the home and `/cities/` meta and list lines. The unsuffixed `/norman/` slug is new and does not collide with an existing page.
