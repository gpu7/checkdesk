# Gaithersburg, Maryland USPS research (2026-11-16, America/Denver)

Third Maryland city (ship order: Baltimore, Frederick, Gaithersburg, Rockville, Bowie). Post Offices only. Hours labeled Eastern Time (49 CFR 71.4). Census place is Gaithersburg city, GEOID 2431175, Vintage 2025 population 71,113, in Montgomery County (GEOID 24031). This is Gaithersburg, Maryland, not Rockville, and not Montgomery Village, Germantown, or Redland. OpenStreetMap was not used.

Official Gaithersburg self ZIPs are 20877, 20878, 20879, 20882, 20883, 20884, 20885, 20898, and 20899. The Gaithersburg search also lists Montgomery Village 20886, which is not a Gaithersburg self ZIP. Locator passes and official pages are the shared Maryland sweep (661 offices, all geocoded, 0 errors).

## Listed (3)

All three print Gaithersburg, MD, list money orders, and match Gaithersburg city on all four Census legs.

- Diamond Farms (1360813, 23 Firstfield Rd, 20878). Weekdays 09:00-17:00; Saturday 09:00-13:00.
- Gaithersburg (1364318, 21 S Summit Ave, 20877). Weekdays 09:00-17:00; Saturday 09:00-13:00.
- Kentlands (1368903, 618 Center Point Way, 20878). Weekdays 09:00-17:00; Saturday 09:00-13:00.

Evenings: 0 (a 17:00 close does not count). Weekends: 3 (all Saturday 09:00-13:00, none Sunday).

## Holds (2)

- Suburban Window SCV (1449464, 16501 Shady Grove Rd, 20898). Prints Gaithersburg and lists money orders, but the current and 2020 address files and both official map points fall in Redland CDP, not Gaithersburg city. Map-point fallback is not allowed.
- Diamond Farms Rural (1584557, 7 Metropolitan Ct, 20878). Prints Gaithersburg and geocodes in Gaithersburg city on all four legs, but the official page does not list money orders and has no published retail hours.

## Result

3 listed Post Offices, all with money orders. 0 Open evenings. 3 Open weekends. Hours labeled Eastern Time. 2 holds. No map-point fallback.

## Site changes in this PR

- New `data/locations/gaithersburg.csv` and `/gaithersburg/`, `/gaithersburg/money-orders/`, and `/gaithersburg/after-hours/` pages.
- Gaithersburg is inserted under Maryland after Frederick on the home page and `/cities/`. Baltimore remains 21 and Frederick remains 2. `/westminster/` remains Westminster, Colorado. No other city CSV or page changed except those meta and list lines.
