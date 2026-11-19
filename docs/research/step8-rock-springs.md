# Rock Springs, Wyoming USPS research (2026-11-19, America/Denver)

Fifth Wyoming city in the Census ranking (Vintage 2025, SUMLEV 162, POPESTIMATE2025). Census place is Rock Springs city, GEOID 5667235, population 22,936. Official listed pages print Rock Springs, WY. This is Rock Springs, Wyoming, at /rock-springs/. This is not Green River city, not Wamsutter, not Superior, not Granger, not Bairoil, and not Rock Hill, Rockford, or Rockville (already live at /rock-hill/, /rockford/, and /rockville/). A Sweetwater County geocode is not enough to list an office here. Hours are Mountain Time (The mountain zone under 49 CFR 71.8 is west of the boundary line described in 49 CFR 71.7 and east of the boundary line described in 49 CFR 71.9. The Central-Mountain boundary in 49 CFR 71.7 is described through Montana-North Dakota, South Dakota, Nebraska, Kansas-Colorado, and Oklahoma-Texas-New Mexico, and does not enter Wyoming. The Mountain-Pacific boundary in 49 CFR 71.9 is described through Montana-Idaho-Oregon and Utah-Nevada-Arizona-California, and does not enter Wyoming. The entire State of Wyoming is in the mountain zone. None of the five cities sits on a zone boundary.). OpenStreetMap was not used. Raw data: `/workspace/step8wy/`. Classification: `/workspace/checkdesk/research/wyoming-geocode-classify-2026-11-19.md`.

Locator passes and official pages are the shared Wyoming sweep (244 offices, all geocoded on the current and 2020 Census files, 0 errors). Classification still uses printed city and Census geocode, not the ZIP list. The five cities are ordinary incorporated places in their home counties, not independent cities. Cheyenne city is in Laramie County; Laramie city is in Albany County; those are two different places, and the two counties are Census-adjacent. Casper, Gillette, and Rock Springs each sit in one home county. Classification uses place GEOIDs only, because a Laramie County match would mix Cheyenne with other places in that county, and an Albany County match would mix Laramie city with other places in that county. Out-of-state offices in Colorado, Montana, Nebraska, and Utah stay off these lists. OpenStreetMap was not used.

## Listed (1)

- Rock Springs (1379630, 2829 COMMERCIAL WAY, ROCK SPRINGS 82901). Lists money orders. Official page prints Rock Springs, WY. All four Census legs are in Rock Springs city. BUSINESS hours: weekdays 9:00 a.m. to 5:00 p.m., Saturday 9:00 a.m. to 12:00 p.m., Sunday closed. Labeled Open weekends.

## Held (1)

- Rock Springs (1473339, 2829 COMMERCIAL WAY, ROCK SPRINGS 82901). Official page prints Rock Springs, WY, and does not list money orders. All four Census legs are in Rock Springs city. Held because the official page does not list money orders. This is a second locator record at the same address as the listed Rock Springs office (1379630).

Green River city, Wamsutter, Superior, Granger, Bairoil, and other Sweetwater County places stay off this list.

## Result

1 listed Post Office, with money orders, in Rock Springs city, with no map-point fallbacks. None is labeled Open evenings. One publishes Saturday hours and is labeled Open weekends: Rock Springs, 9:00 a.m. to 12:00 p.m. None publishes Sunday hours. Hours labeled Mountain Time. 1 hold (no money-order tags, same address as the listed office).

## Site changes in this PR

- New `data/locations/rock-springs.csv` and `/rock-springs/`, `/rock-springs/money-orders/`, and `/rock-springs/after-hours/` pages.
- Rock Springs is inserted under the existing Wyoming section after Laramie on the home page and `/cities/`. No other existing city CSV or page changed except the home and `/cities/` meta and list lines. The unsuffixed `/rock-springs/` slug is new and does not collide with an existing page.
