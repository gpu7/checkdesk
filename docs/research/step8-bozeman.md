# Bozeman, Montana USPS research (2026-11-17, America/Denver)

Fourth Montana city in the Census ranking (Vintage 2025, SUMLEV 162, POPESTIMATE2025). Census place is Bozeman city, GEOID 3008950, population 58,814, in Gallatin County (GEOID 30031). Official pages print Bozeman, MT. This is not Belgrade, Manhattan, Three Forks, or West Yellowstone. The Balance of Gallatin County stays off this list. Hours are Mountain Time (49 CFR 71.8). OpenStreetMap was not used. Raw data: `/workspace/step8mt/`. Classification: `/workspace/checkdesk/research/montana-geocode-classify-2026-11-17.md`.

Official Bozeman self ZIPs are the 6 ZIPs listed as Bozeman, MT on the official city page: 59715, 59717, 59718, 59719, 59771, and 59772. Locator passes and official pages are the shared Montana sweep (286 offices, all geocoded on the current and 2020 Census files, 0 errors).

## Listed (1)

Prints Bozeman, MT, lists money orders, and matches Bozeman city on all four Census legs.

- Babcock (1353834, 32 E BABCOCK ST, 59715). Weekdays 09:00-17:00; Saturday closed.

Evenings: 0. Weekends: 0. The listed office weekday retail closes at 17:00, which does not count as Open evenings, and it does not publish Saturday or Sunday hours, so Bozeman has no evenings-and-weekends page.

## Holds (1)

### Geocode mismatch (1)

- Bozeman (1355595, 2201 BAXTER LN, BOZEMAN 59718). Prints Bozeman, MT, and lists money orders. The current address file did not match (including street-name retries: 2201 BAXTER LN, 2201 Baxter Lane, 2201 BAXTER LANE, 2201 W Baxter Lane, 2201 E Baxter Lane, 2201 Baxter Road, and 2201 Baxter Rd). The 2020 address file matched 2201 BAXTER LN, BOZEMAN, MT, 59718 in Gallatin County (GEOID 30031) with no incorporated place and no CDP. The official USPS locator map point (45.700987, -111.068378) and the 2020 address point are also in Gallatin County with no incorporated place and no CDP on both files. Map-point fallback is not used, because the official point is not inside Bozeman city. OpenStreetMap was not used.

## Result

1 listed Post Office, with money orders. 0 Open evenings. 0 Open weekends. Hours labeled Mountain Time. 1 hold (geocode mismatch). No map-point fallback. No `/bozeman/after-hours/` page.

## Site changes in this PR

- New `data/locations/bozeman.csv` and `/bozeman/` and `/bozeman/money-orders/` pages. No evenings-and-weekends page, because the listed office is not open after 5:00 p.m. on a weekday and does not publish Saturday or Sunday hours.
- Bozeman is added under the existing Montana section after Great Falls on the home page and `/cities/`. No existing city CSV or page changed except those meta and list lines. The unsuffixed `/bozeman/` slug is new and does not collide with an existing page.
