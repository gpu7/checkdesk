# Paterson, New Jersey USPS research (2026-11-17, America/Denver)

Third New Jersey city in the Census ranking (Vintage 2025, SUMLEV 162, POPESTIMATE2025). Census place is Paterson city, GEOID 3457000, population 161,793, in Passaic County (GEOID 34031). Official listed pages print Paterson, NJ. This is not Clifton, not Passaic, and not a township in the Balance of Passaic County. Hours are Eastern Time (49 CFR 71.4; the Eastern–Central boundary in 49 CFR 71.5 does not enter New Jersey). OpenStreetMap was not used. Raw data: `/workspace/step8nj/`. Classification: `/workspace/checkdesk/research/new-jersey-geocode-classify-2026-11-17.md`.

Official Paterson self ZIPs are the 19 ZIPs listed as Paterson, NJ on the official city page: 07424, 07501, 07502, 07503, 07504, 07505, 07508, 07509, 07510, 07511, 07512, 07513, 07514, 07522, 07524, 07533, 07538, 07543, and 07544. Locator passes and official pages are the shared New Jersey sweep (1418 offices, all geocoded on the current and 2020 Census files, 0 errors).

## Listed (3)

- Park (1376823, 497 21ST AVE, PATERSON 07513). Lists money orders. All four Census legs are in Paterson city. BUSINESS hours: weekdays 9:30 a.m. to 4:30 p.m., Saturday closed, Sunday closed. Not labeled Open evenings or Open weekends.
- Paterson (1433632, 194 WARD ST, PATERSON 07510). Lists money orders. All four Census legs are in Paterson city. BUSINESS hours: weekdays 8:30 a.m. to 5:00 p.m., Saturday 8:30 a.m. to 1:30 p.m., Sunday closed. A 5:00 p.m. close does not count as Open evenings. Labeled Open weekends.
- South Paterson (1382236, 958 MAIN ST STE 1, PATERSON 07503). Lists money orders. All four Census legs are in Paterson city. BUSINESS hours: weekdays 9:00 a.m. to 5:00 p.m., Saturday closed, Sunday closed. A 5:00 p.m. close does not count as Open evenings. Not labeled Open evenings or Open weekends.

No map-point fallback.

## Held

- Paterson NJ SDC (1594598, 194 WARD ST, PATERSON 07510). Prints Paterson, NJ, and all four Census legs are in Paterson city, but the official page does not list money orders. It is at the same address as the listed Paterson office.

No other office in the New Jersey locator sweep geocodes into Paterson city.

## Result

3 listed Post Offices, all with money orders. 0 Open evenings. 1 Open weekends, Saturday only (Paterson at 194 Ward St). Hours labeled Eastern Time. 1 hold (no money-order tags).

## Site changes in this PR

- New `data/locations/paterson.csv` and `/paterson/`, `/paterson/money-orders/`, and `/paterson/after-hours/` pages.
- Paterson is added under the existing New Jersey section after Jersey City on the home page and `/cities/`. The existing Newark, Delaware, pages and `data/locations/newark.csv` were not changed. No other existing city CSV or page changed except the home and `/cities/` meta and list lines. The unsuffixed `/paterson/` slug is new and does not collide with an existing page.
