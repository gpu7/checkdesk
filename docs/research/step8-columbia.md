# Columbia, Missouri USPS research (2026-11-17, America/Denver)

Fourth Missouri city in the Census ranking (Vintage 2025, SUMLEV 162, POPESTIMATE2025). Census place is Columbia city, GEOID 2915670, population 130,851, in Boone County (GEOID 29019). Official pages print Columbia, MO. Ashland, Centralia, and Hallsville stay off this list. Hours are Central Time (49 CFR 71.6(a)). OpenStreetMap was not used. Raw data: `/workspace/step8mo/`. Classification: `/workspace/checkdesk/research/missouri-geocode-classify-2026-11-17.md`. Address retries: `/workspace/step8mo/retry_nomatch.jsonl`.

## Listed (2)

1 listed_clean, plus Commerce STA under the documented map-point fallback. Both have money-order tags (Domestic Money Orders and Inquiry Money Orders). Official pages print Columbia, MO.

- Columbia (1358762, 511 E WALNUT ST, 65201). MO:08:30-18:00 TU:08:30-18:00 WE:08:30-18:00 TH:08:30-18:00 FR:08:30-18:00 SA:09:30-14:00 SU:closed.
- Commerce STA (1358851, 3709 SANDMAN LN, 65201). MO:09:00-13:00/13:30-17:00 TU:09:00-13:00/13:30-17:00 WE:09:00-13:00/13:30-17:00 TH:09:00-13:00/13:30-17:00 FR:09:00-13:00/13:30-17:00 SA:09:00-12:00 SU:closed.

## Map-point fallbacks (1)

### Commerce STA (1358851)

The official page already prints Columbia, MO. The address 3709 Sandman Ln, Columbia, MO 65201 did not match on the current Census file. 40 street-name, city, and ZIP variants were tried (official street forms such as 3709 Sandman Ln, 3709 Sandman Lane, and 3709 Sandman; cities Columbia; ZIPs 65201 and blank; current and 2020 vintages). All 20 current-file attempts, including the official street and ZIP, did not match. All 20 2020-file attempts, including the official street and ZIP, matched 3709 SANDMAN LN, COLUMBIA, MO, 65201 in Columbia city (GEOID 2915670), Boone County. The official USPS locator map point (38.909604, -92.334046) places it in Columbia city, Boone County, on both the current and 2020 benchmarks. Map-point fallback is allowed because the printed city already matches and the official point is inside the city. Raw: `/workspace/step8mo/retry_nomatch.jsonl`.

## Holds (2)

### Prints Columbia, MO and geocodes in Columbia city, but official page does not list money orders (2)

- Columbia Mall STA (1358788, 2300 BERNADETTE DR STE 200, 65203). BUSINESS: MO:09:00-17:00 TU:09:00-17:00 WE:09:00-17:00 TH:09:00-17:00 FR:09:00-17:00 SA:09:00-13:00/13:30-14:00 SU:closed.
- Tiger (1384653, 3212B LEMONE INDUSTRIAL BLVD, 65201). No BUSINESS hours.

No hold_geocode_mismatch. No other office in the Missouri locator sweep geocodes into Columbia city.

## Result

2 listed Post Offices, both with money orders. 1 Open evenings. 2 Open weekends, Saturday only. Hours labeled Central Time. 2 holds. One documented map-point fallback.

## Site changes in this PR

- New `data/locations/columbia.csv` and `/columbia/`, `/columbia/money-orders/`, and `/columbia/after-hours/` pages.
- Columbia is inserted under the existing Missouri section, after Springfield, on the home page and `/cities/`. No existing city CSV or page changed except those meta and list lines. The `/kansas-city-ks/` pages (Kansas City, Kansas) and `/springfield/` pages (Springfield, Massachusetts) were not edited.
