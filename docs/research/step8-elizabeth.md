# Elizabeth, New Jersey USPS research (2026-11-17, America/Denver)

Fourth New Jersey city in the Census ranking (Vintage 2025, SUMLEV 162, POPESTIMATE2025). Census place is Elizabeth city, GEOID 3421000, population 141,675, in Union County (GEOID 34039). Official listed pages print Elizabeth, NJ. This is not Linden, not Plainfield, and not a township in the Balance of Union County. Hours are Eastern Time (49 CFR 71.4; the Eastern–Central boundary in 49 CFR 71.5 does not enter New Jersey). OpenStreetMap was not used. Raw data: `/workspace/step8nj/`. Classification: `/workspace/checkdesk/research/new-jersey-geocode-classify-2026-11-17.md`.

Official Elizabeth self ZIPs are the 6 ZIPs listed as Elizabeth, NJ on the official city page: 07201, 07202, 07206, 07207, 07208, and 08348. Some of those ZIPs sit outside the Census place (including 08348); classification still uses printed city and Census geocode, not the ZIP list. Locator passes and official pages are the shared New Jersey sweep (1418 offices, all geocoded on the current and 2020 Census files, 0 errors).

## Listed (5)

- Bayway (1354286, 544 BAYWAY AVE, ELIZABETH 07202). Lists money orders. All four Census legs are in Elizabeth city. BUSINESS hours: weekdays 10:00 a.m. to 5:00 p.m., Saturday 10:00 a.m. to 2:00 p.m., Sunday closed. A 5:00 p.m. close does not count as Open evenings. Labeled Open weekends.
- Elizabeth (1362281, 310 N BROAD ST, ELIZABETH 07208). Lists money orders. All four Census legs are in Elizabeth city. BUSINESS hours: weekdays 7:30 a.m. to 5:30 p.m., Saturday 7:30 a.m. to 2:00 p.m., Sunday closed. Labeled Open evenings and Open weekends.
- Elmora (1362463, 175 ELMORA AVE STE 1, ELIZABETH 07202). Lists money orders. All four Census legs are in Elizabeth city. BUSINESS hours: weekdays 10:00 a.m. to 5:00 p.m., Saturday 10:00 a.m. to 2:00 p.m., Sunday closed. A 5:00 p.m. close does not count as Open evenings. Labeled Open weekends.
- North Elizabeth (1375305, 772 NEWARK AVE, ELIZABETH 07208). Lists money orders. All four Census legs are in Elizabeth city. BUSINESS hours: weekdays 10:00 a.m. to 5:00 p.m., Saturday closed, Sunday closed. A 5:00 p.m. close does not count as Open evenings. Not labeled Open evenings or Open weekends.
- Union Square (1385406, 946 ELIZABETH AVE, ELIZABETH 07201). Lists money orders. All four Census legs are in Elizabeth city. BUSINESS hours: weekdays 10:00 a.m. to 5:00 p.m., Saturday closed, Sunday closed. A 5:00 p.m. close does not count as Open evenings. Not labeled Open evenings or Open weekends.

No map-point fallback.

## Held

No office that prints Elizabeth is held, and no other office in the New Jersey locator sweep geocodes into Elizabeth city.

## Result

5 listed Post Offices, all with money orders. 1 Open evenings (Elizabeth, until 5:30 p.m.). 3 Open weekends, Saturday only. Hours labeled Eastern Time. 0 holds.

## Site changes in this PR

- New `data/locations/elizabeth.csv` and `/elizabeth/`, `/elizabeth/money-orders/`, and `/elizabeth/after-hours/` pages.
- Elizabeth is added under the existing New Jersey section after Paterson on the home page and `/cities/`. The existing Newark, Delaware, pages and `data/locations/newark.csv` were not changed. No other existing city CSV or page changed except the home and `/cities/` meta and list lines. The unsuffixed `/elizabeth/` slug is new and does not collide with an existing page.
