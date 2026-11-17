# Reno, Nevada USPS research (2026-11-17, America/Denver)

Fourth Nevada city in the Census ranking (Vintage 2025, SUMLEV 162, POPESTIMATE2025). Census place is Reno city, GEOID 3260600, population 283,621, in Washoe County (GEOID 32031). Official listed pages print Reno, NV. This is not Sparks, Carson City, or an unincorporated place in the Balance of Washoe County. Hours are Pacific Time (49 CFR 71.10; Reno lies west of the 49 CFR 71.9 boundary; West Wendover, the mountain-zone exception, is outside this city). OpenStreetMap was not used. Raw data: `/workspace/step8nv/`. Classification: `/workspace/checkdesk/research/nevada-geocode-classify-2026-11-17.md`.

Official Reno self ZIPs are the 23 ZIPs listed as Reno, NV on the official city page: 89501, 89502, 89503, 89504, 89505, 89506, 89507, 89508, 89509, 89510, 89511, 89512, 89513, 89515, 89519, 89520, 89521, 89523, 89533, 89557, 89570, 89595, and 89599. Locator passes and official pages are the shared Nevada sweep (414 offices, all geocoded on the current and 2020 Census files, 0 errors).

## Listed (6)

- Downtown Reno (1457367, 135 N SIERRA ST STE A1, RENO 89501). Lists money orders. All four Census legs are in Reno city. BUSINESS hours: weekdays 8:30 a.m. to 12:00 p.m. and 1:00 p.m. to 5:00 p.m., Saturday closed, Sunday closed. Not labeled Open evenings or Open weekends.
- Peavine (1377060, 1580 GRAND POINT WAY, RENO 89523). Lists money orders. All four Census legs are in Reno city. BUSINESS hours: weekdays 8:30 a.m. to 5:00 p.m., Saturday 9:00 a.m. to 3:00 p.m., Sunday closed. Labeled Open weekends. A 5:00 p.m. weekday close does not count as Open evenings.
- Reno (1439877, 2000 VASSAR ST, RENO 89510). Lists money orders. All four Census legs are in Reno city. BUSINESS hours: weekdays 9:00 a.m. to 5:30 p.m., Saturday 9:00 a.m. to 3:00 p.m., Sunday closed. Labeled Open evenings and Open weekends.
- Sierra (1381637, 1050 N HILLS BLVD, RENO 89506). Lists money orders. All four Census legs are in Reno city. BUSINESS hours: weekdays 9:00 a.m. to 5:00 p.m., Saturday 10:00 a.m. to 2:00 p.m., Sunday closed. Labeled Open weekends. A 5:00 p.m. weekday close does not count as Open evenings.
- University Reno (1439890, 1674 N VIRGINIA ST, RENO 89503). Lists money orders. All four Census legs are in Reno city. BUSINESS hours: weekdays 9:00 a.m. to 5:00 p.m., Saturday closed, Sunday closed. Not labeled Open evenings or Open weekends.
- Washington (1439891, 1490 STARDUST ST, RENO 89503). Lists money orders. All four Census legs are in Reno city. BUSINESS hours: weekdays 8:30 a.m. to 5:00 p.m., Saturday closed, Sunday closed. Not labeled Open evenings or Open weekends.

No map-point fallback.

## Held

### Geocode mismatch (1)

- Steamboat (1383475, 75 MCCABE DR, RENO 89511). Lists money orders. The official page prints Reno, NV, but the current and 2020 address and official map-point lookups find no incorporated place or census designated place. Held because the printed city and the geocode disagree. No map-point fallback (the official point is not inside Reno city).

### No money-order tags, inside Reno city (1)

- Galena (1364325, 299 E PLUMB LN STE 110, RENO 89502). Prints Reno, NV, and matches Reno city on all four Census legs. The official page has BUSINESS hours but no money-order tags.

## Result

6 listed Post Offices, all with money orders. 1 Open evenings (Reno, until 5:30 p.m.). 3 Open weekends, Saturday only (Peavine, Reno, and Sierra). Hours labeled Pacific Time. 2 holds (1 geocode mismatch, 1 no money orders).

## Site changes in this PR

- New `data/locations/reno.csv` and `/reno/`, `/reno/money-orders/`, and `/reno/after-hours/` pages.
- Reno is added under the existing Nevada section after North Las Vegas on the home page and `/cities/`. No existing city CSV or page changed except those meta and list lines. The unsuffixed `/reno/` slug is new and does not collide with an existing page.
