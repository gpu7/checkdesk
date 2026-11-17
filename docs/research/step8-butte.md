# Butte, Montana USPS research (2026-11-17, America/Denver)

Fifth Montana city in the Census ranking (Vintage 2025, SUMLEV 162, POPESTIMATE2025). Check Desk pages use the name Butte for the Census place Butte-Silver Bow (balance), GEOID 3011397, population 35,469, FUNCSTAT F, the consolidated-government remainder in Silver Bow County (GEOID 30093). Ranking and city-limits checks use that SUMLEV 162 balance, not the SUMLEV 170 row "Butte-Silver Bow" (CONCIT 11390; 36,118) and not Walkerville town (649; GEOID 3077650). 35,469 + 649 = 36,118. Anaconda-Deer Lodge is outside this five. Official listed pages print Butte, MT. Hours are Mountain Time (49 CFR 71.8). OpenStreetMap was not used. Raw data: `/workspace/step8mt/`. Classification: `/workspace/checkdesk/research/montana-geocode-classify-2026-11-17.md`.

Official Butte self ZIPs are the 5 ZIPs listed as Butte, MT on the official city page after dropping 59446 (that ZIP appears on the Butte city page only as the alias Square Butte; the Chouteau County page places it in Geraldine / Square Butte): 59701, 59702, 59703, 59707, and 59750. Locator passes and official pages are the shared Montana sweep (286 offices, all geocoded on the current and 2020 Census files, 0 errors). No office prints Walkerville.

## Listed (2)

Prints Butte, MT, lists money orders, and matches Butte-Silver Bow (balance) on all four Census legs.

- Butte (1356496, 701 DEWEY BLVD, 59701). Weekdays 08:30-17:30; Saturday 09:00-13:00.
- Copper Hill (1359211, 60 W GALENA ST, 59701). Weekdays 09:30-13:00 and 14:00-16:30; Saturday closed.

Evenings: 1 (Butte until 17:30). Weekends: 1, Saturday only, no Sunday (Butte). Copper Hill weekday retail closes at 16:30, with a midday closure 13:00-14:00, which does not count as Open evenings.

## Holds (4)

### No money-order tags, inside the balance (1)

- Butte (1472093, 701 DEWEY BLVD, BUTTE 59701). Prints Butte, MT, and matches the balance on all four Census legs, but the official page has no money-order tags and no BUSINESS hours (services and hours are null). Same printed street address as the listed Butte office (1356496).

### Other printed city, at least one leg in the balance (3)

- Divide (1360940, 43 N RIVER RD, DIVIDE 59727). Prints Divide, MT, and lists money orders. Address legs match Dewey CDP in Beaverhead County (the geocoder matched 43 DEWEY RIVER RD). Official map-point legs are in Butte-Silver Bow (balance). Held because it prints a different city.
- Melrose (1372647, 228 MAIN ST, MELROSE 59743). Prints Melrose, MT, and lists money orders. All four Census legs are in Butte-Silver Bow (balance). Held because it prints a different city.
- Ramsay (1378743, 1 BEULAH ST, RAMSAY 59748). Prints Ramsay, MT, and lists money orders. The current address file and both official map-point legs are in Butte-Silver Bow (balance); the 2020 address file did not match. Held because it prints a different city.

## Result

2 listed Post Offices, all with money orders. 1 Open evenings. 1 Open weekends, Saturday only. Hours labeled Mountain Time. 4 holds (1 no money orders, 3 other printed city). No map-point fallback.

## Site changes in this PR

- New `data/locations/butte.csv` and `/butte/`, `/butte/money-orders/`, and `/butte/after-hours/` pages.
- Butte is added under the existing Montana section after Bozeman on the home page and `/cities/`. No existing city CSV or page changed except those meta and list lines. The unsuffixed `/butte/` slug is new and does not collide with an existing page.
