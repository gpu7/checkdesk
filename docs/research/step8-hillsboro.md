# Hillsboro, Oregon USPS research (2026-11-18, America/Denver)

Fifth Oregon state city in the Census ranking (Vintage 2025, SUMLEV 162, POPESTIMATE2025). Census place is Hillsboro city, GEOID 4134100, population 111,126. Official listed pages print Hillsboro, OR. This is Hillsboro, Oregon, in Washington County, at /hillsboro/. This is not Beaverton, not Tigard, not Forest Grove, not Cornelius, and not Portland. Portland, Salem, Eugene, and Gresham stay on separate lists. Offices in Washington, Idaho, California, and Nevada stay off this list, including Vancouver, WA. Hours are Pacific Time (Oregon is in the Pacific zone under 49 CFR 71.10, west of the mountain–Pacific boundary in § 71.9(a). That boundary follows the north and west lines of Malheur County; none of this five is in Malheur County.). OpenStreetMap was not used. Raw data: `/workspace/step8or/`. Classification: `/workspace/checkdesk/research/oregon-geocode-classify-2026-11-18.md`.

Locator passes and official pages are the shared Oregon sweep (338 offices, all geocoded on the current and 2020 Census files, 0 errors). Classification still uses printed city and Census geocode, not the ZIP list.

## Listed (1)

- Hillsboro (1367024, 125 S 1ST AVE, HILLSBORO 97123). Lists money orders. Official page prints Hillsboro, OR. All four Census legs are in Hillsboro city. BUSINESS hours: weekdays 8:00 a.m. to 5:00 p.m., Saturday 9:30 a.m. to 1:30 p.m., Sunday closed. Labeled Open weekends.

## Held (2)

- Hillsboro DCU (1367007, 1330 SW Walnut St, HILLSBORO 97123). Official page prints Hillsboro, OR, and all four Census legs are in Hillsboro city, but the official page does not list money orders.
- Beaverton OR S&DC (1582546, 3685 NE Aloclek Dr, PORTLAND 97291). Official page prints Portland, OR; both address files did not match and the official map point is in Hillsboro city on both files. Also held on the Portland list as a geocode mismatch. The official page does not list money orders.

Portland stays on a separate list at /portland-or/. Salem, Eugene, and Gresham stay on separate lists. Offices in Washington, Idaho, California, and Nevada stay off this list.

## Result

1 listed Post Office with money orders, in Washington County. It is not labeled Open evenings (weekday retail closes at 5:00 p.m.). It publishes Saturday hours and is labeled Open weekends. It does not publish Sunday hours. Hours labeled Pacific Time. 2 holds.

## Site changes in this PR

- New `data/locations/hillsboro.csv` and `/hillsboro/`, `/hillsboro/money-orders/`, and `/hillsboro/after-hours/` pages.
- Hillsboro is inserted under the existing Oregon section after Gresham on the home page and `/cities/`. No other existing city CSV or page changed except the home and `/cities/` meta and list lines. The unsuffixed `/hillsboro/` slug is new and does not collide with an existing page.
