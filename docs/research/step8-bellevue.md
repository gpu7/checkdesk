# Bellevue, Nebraska USPS research (2026-11-17, America/Denver)

Third Nebraska city in the Census ranking (Vintage 2025, SUMLEV 162, POPESTIMATE2025). Census place is Bellevue city, GEOID 3103950, population 64,863, in Sarpy County (GEOID 31153). Official listed pages print Bellevue, NE. This is not Papillion, La Vista, Gretna, Springfield in Sarpy County, or the Offutt AFB census designated place. Hours are Central Time (49 CFR 71.6(a); Bellevue lies east of the 49 CFR 71.7(c) boundary). OpenStreetMap was not used. Raw data: `/workspace/step8ne/`. Classification: `/workspace/checkdesk/research/nebraska-geocode-classify-2026-11-17.md`.

Official Bellevue self ZIPs are the 6 ZIPs listed as Bellevue, NE on the official city page: 68005, 68056, 68123, 68133, 68147, and 68157. Two of those (68147 and 68157) also appear on the Omaha city page. Locator passes and official pages are the shared Nebraska sweep (327 offices, all geocoded on the current and 2020 Census files, 0 errors). The Offutt AFB Post Office was in that sweep; it geocodes in the Offutt AFB census designated place in Sarpy County, not in Bellevue city, and is not listed here.

## Listed (1)

Prints Bellevue, NE, lists money orders, and matches Bellevue city on all four Census legs.

- Bellevue (1354533, 2609 VICTORIA AVE, 68005). Weekdays 08:30-17:00; Saturday 09:00-13:00.

Evenings: 0 (weekday retail closes at 17:00; a 5:00 p.m. close does not count as Open evenings). Weekends: 1, Saturday only, no Sunday.

## Holds (1)

### No money-order tags, inside Bellevue city (1)

- Olde Towne (1530814, 103 E MISSION AVE, BELLEVUE 68005). Prints Bellevue, NE, and matches Bellevue city on all four Census legs. The official page has BUSINESS hours (weekdays 09:00-11:00, closed Saturday and Sunday) but no money-order tags.

## Result

1 listed Post Office, with money orders. 0 Open evenings. 1 Open weekends, Saturday only. Hours labeled Central Time. 1 hold (no money orders). No map-point fallback.

## Site changes in this PR

- New `data/locations/bellevue.csv` and `/bellevue/`, `/bellevue/money-orders/`, and `/bellevue/after-hours/` pages.
- Bellevue is added to the existing Nebraska section after Lincoln on the home page and `/cities/`. No existing city CSV or page changed except those meta and list lines. The unsuffixed `/bellevue/` slug is new and does not collide with an existing page.
