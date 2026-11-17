# Missoula, Montana USPS research (2026-11-17, America/Denver)

Second Montana city in the Census ranking (Vintage 2025, SUMLEV 162, POPESTIMATE2025). Census place is Missoula city, GEOID 3050200, population 78,903, in Missoula County (GEOID 30063). Official pages print Missoula, MT. This is not a CDP or unincorporated place in Missoula County. The Balance of Missoula County stays off this list. Hours are Mountain Time (49 CFR 71.8). OpenStreetMap was not used. Raw data: `/workspace/step8mt/`. Classification: `/workspace/checkdesk/research/montana-geocode-classify-2026-11-17.md`.

Official Missoula self ZIPs are the 8 ZIPs listed as Missoula, MT on the official city page: 59801, 59802, 59803, 59804, 59806, 59807, 59808, and 59812. Locator passes and official pages are the shared Montana sweep (286 offices, all geocoded on the current and 2020 Census files, 0 errors).

## Listed (3)

Prints Missoula, MT, lists money orders, and matches Missoula city on all four Census legs.

- Hellgate (1366675, 200 E BROADWAY ST, 59802). Weekdays 09:00-17:30; Saturday closed.
- Missoula (1373399, 1100 W KENT AVE, 59801). Weekdays 08:30-17:30; Saturday 09:00-13:00.
- Mullan (1374220, 3150 GREAT NORTHERN AVE, 59808). Weekdays 09:00-17:30; Saturday closed.

Evenings: 3, all until 17:30. Weekends: 1, Saturday only, no Sunday (Missoula).

## Holds (0)

No office that prints Missoula geocodes outside Missoula city. No other office in the Montana locator sweep geocodes into Missoula city. No map-point fallback.

## Result

3 listed Post Offices, all with money orders. 3 Open evenings. 1 Open weekends, Saturday only. Hours labeled Mountain Time. 0 holds. No map-point fallback.

## Site changes in this PR

- New `data/locations/missoula.csv` and `/missoula/`, `/missoula/money-orders/`, and `/missoula/after-hours/` pages.
- Missoula is added under the existing Montana section after Billings on the home page and `/cities/`. The Billings `/cities/` paragraph is also corrected so the literal `{hold_sentence}` typo from the Billings PR is replaced with the intended sentence. No existing city CSV or page changed except those meta and list lines. The unsuffixed `/missoula/` slug is new and does not collide with an existing page.
