# Billings, Montana USPS research (2026-11-17, America/Denver)

First Montana city in the Census ranking (Vintage 2025, SUMLEV 162, POPESTIMATE2025). Census place is Billings city, GEOID 3006550, population 121,239, in Yellowstone County (GEOID 30111). Official pages print Billings, MT. This is not Laurel or Broadview. Hours are Mountain Time (49 CFR 71.8). OpenStreetMap was not used. Raw data: `/workspace/step8mt/`. Classification: `/workspace/checkdesk/research/montana-geocode-classify-2026-11-17.md`.

Official Billings self ZIPs are the 14 ZIPs listed as Billings, MT on the official city page: 59101, 59102, 59103, 59104, 59105, 59106, 59107, 59108, 59111, 59112, 59114, 59115, 59116, and 59117. Locator passes and official pages are the shared Montana sweep (286 offices, all geocoded on the current and 2020 Census files, 0 errors).

## Listed (5)

Prints Billings, MT, lists money orders, and matches Billings city on all four Census legs.

- Billings (1354967, 841 S 26TH ST, 59101). Weekdays 08:30-17:30; Saturday closed.
- Centennial (1357428, 2250 GRANT RD, 59102). Weekdays 08:30-17:30; Saturday closed.
- Downtown Billings (1361247, 2602 1ST AVE N FL 1, 59101). Weekdays 08:00-17:30; Saturday closed.
- Pioneer (1377625, 724 15TH ST W, 59102). Weekdays 08:30-17:30; Saturday 10:00-14:00.
- Ronald Reagan (1366653, 710 WICKS LN, 59105). Weekdays 09:00-17:30; Saturday 10:30-14:00.

Evenings: 5, all until 17:30. Weekends: 2, Saturday only, no Sunday (Pioneer and Ronald Reagan).

## Holds (0)

No office that prints Billings geocodes outside Billings city. No other office in the Montana locator sweep geocodes into Billings city. No map-point fallback.

## Result

5 listed Post Offices, all with money orders. 5 Open evenings. 2 Open weekends, Saturday only. Hours labeled Mountain Time. 0 holds. No map-point fallback.

## Site changes in this PR

- New `data/locations/billings.csv` and `/billings/`, `/billings/money-orders/`, and `/billings/after-hours/` pages.
- Billings is inserted under a new Montana section after Missouri on the home page and `/cities/`. No existing city CSV or page changed except those meta and list lines. The unsuffixed `/billings/` slug is new and does not collide with an existing page.
