# Lincoln, Nebraska USPS research (2026-11-17, America/Denver)

Second Nebraska city in the Census ranking (Vintage 2025, SUMLEV 162, POPESTIMATE2025). Census place is Lincoln city, GEOID 3128000, population 301,522, in Lancaster County (GEOID 31109). Official listed pages print Lincoln, NE. This is not Waverly, Hickman, or a Lincoln township. Hours are Central Time (49 CFR 71.6(a); Lincoln lies east of the 49 CFR 71.7(c) boundary). The Lincoln County named in that boundary is the county around North Platte, not Lincoln city. OpenStreetMap was not used. Raw data: `/workspace/step8ne/`. Classification: `/workspace/checkdesk/research/nebraska-geocode-classify-2026-11-17.md`.

Official Lincoln self ZIPs are the 29 ZIPs listed as Lincoln, NE on the official city page: 68501, 68502, 68503, 68504, 68505, 68506, 68507, 68508, 68509, 68510, 68512, 68514, 68516, 68517, 68520, 68521, 68522, 68523, 68524, 68526, 68527, 68528, 68529, 68531, 68532, 68542, 68544, 68583, and 68588. Locator passes and official pages are the shared Nebraska sweep (327 offices, all geocoded on the current and 2020 Census files, 0 errors).

## Listed (3)

Prints Lincoln, NE, lists money orders, and matches Lincoln city on all four Census legs.

- College View (1358675, 5100 VAN DORN ST, 68506). Weekdays 08:30-17:00; Saturday 09:00-12:00.
- Indian Village (1367911, 1201 CALVERT ST, 68502). Weekdays 08:30-17:00; Saturday 09:00-13:00.
- Lincoln (1370482, 700 R ST, 68501). Weekdays 07:30-18:00; Saturday 09:00-14:00.

Evenings: 1 (Lincoln until 18:00). Weekends: 3, Saturday only, no Sunday.

## Holds (7)

### Geocode mismatch, prints Lincoln (2)

- Cheney Ridge Annex (1357788, 5301 RED ROCK LN, LINCOLN 68516). Prints Lincoln, NE. The current address file and both official map-point legs are in Lincoln city; the 2020 address file did not match. The official page has no money-order tags and no BUSINESS hours. Held because the address is not confirmed in the city on both Census files. No map-point fallback is used to list it, because it also lacks money-order tags.
- State House (1383340, 301 CENTENNIAL MALL S, LINCOLN 68508). Prints Lincoln, NE. The 2020 address file and both official map-point legs are in Lincoln city; the current address file did not match. The official page has BUSINESS hours but no money-order tags. Held because the address is not confirmed in the city on both Census files.

### No money-order tags, inside Lincoln city (5)

- Gateway (1477116, 6401 Q ST STE 100, LINCOLN 68505). Prints Lincoln, NE, and matches Lincoln city on all four Census legs, but the official page does not list money orders.
- Havelock (1366490, 6240 PLATTE AVE, LINCOLN 68507). Prints Lincoln, NE, and matches Lincoln city on all four Census legs, but the official page does not list money orders.
- Lincoln (1472102, 700 R ST, LINCOLN 68501). Same printed street address as the listed Lincoln office (1370482). Official page has no money-order tags and no BUSINESS hours. All four Census legs are in Lincoln city.
- Northview Annex (1375473, 3120 BAIR AVE, LINCOLN 68504). Prints Lincoln, NE, and matches Lincoln city on all four Census legs, but the official page has no money-order tags and no BUSINESS hours.
- University Place (1385495, 2427 N 48TH ST, LINCOLN 68504). Prints Lincoln, NE, and matches Lincoln city on all four Census legs, but the official page does not list money orders.

## Result

3 listed Post Offices, all with money orders. 1 Open evenings. 3 Open weekends, Saturday only. Hours labeled Central Time. 7 holds (2 geocode mismatch, 5 no money orders). No map-point fallback.

## Site changes in this PR

- New `data/locations/lincoln.csv` and `/lincoln/`, `/lincoln/money-orders/`, and `/lincoln/after-hours/` pages.
- Lincoln is added to the existing Nebraska section after Omaha on the home page and `/cities/`. No existing city CSV or page changed except those meta and list lines. The unsuffixed `/lincoln/` slug is new and does not collide with an existing page.
