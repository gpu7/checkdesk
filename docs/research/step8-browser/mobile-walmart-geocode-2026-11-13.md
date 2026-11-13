# Mobile, AL — Walmart Supercenter Census geocodes (2026-11-13 research)

Research only. Nothing was built, committed, or deployed. No business was contacted. OpenStreetMap was not used. last_verified (Census lookups): 2026-11-13, about 9:55 AM America/Denver.

Official store names, printed cities, and addresses for the four Mobile-printed Supercenters and two nearby Supercenters come from the 2026-11-13 official walmart.com store-page research (`mobile-walmart-2026-11-13.md`). Those pages did not publish official map coordinates (only a Google Maps directions link by address), so **no official map-point lookups were run**. Neighborhood Markets were not geocoded.

## Method

U.S. Census Bureau Geocoder only, geographies address endpoint, two files each time:

- Current: `benchmark=Public_AR_Current`, `vintage=Current_Current`
- 2020 Census: `benchmark=Public_AR_Census2020`, `vintage=Census2020_Census2020`
- Layers: Incorporated Places, Census Designated Places, Counties
- Address: `https://geocoding.geo.census.gov/geocoder/geographies/address`
- Official map point: **not available** (no coordinates on the official store pages)

Place names below are Census NAME values (`Mobile city` GEOID 0150000; `Saraland city` GEOID 0168160; `Semmes city` GEOID 0169240). Every row is in Mobile County (GEOID 01097) in both files when a match exists. No CDP was returned for any lookup.

For store #991, the official street (`101 E I65 Service Rd S`) was tried first, then I-65 / Interstate 65 wording variants, then Svc / Frontage forms and the onelineaddress endpoint. None matched.

Raw lookups: `/workspace/step8mob/wm_geo_raw.json`, `/workspace/step8mob/wm_991_extra.json`. Script: `/workspace/step8mob/wm_geocode.py`.

## Inclusion rule applied

- Include in Mobile only if the printed city is Mobile **and** the address match is in Mobile city. Because no official map point is available, a missing address match cannot be resolved by a point fallback.
- HOLD if the printed city and the geocode disagree, **or** if there is no address match in either Census file.
- Other-city-printed stores that geocode in their printed city (and not in Mobile city) are **left off, other city**.

## Decision table

| Store | Printed city | Official address | Current address (place / county) | 2020 address (place / county) | Official point current | Official point 2020 | Decision |
|---|---|---|---|---|---|---|---|
| 991 | Mobile | 101 E I65 Service Rd S, Mobile, AL 36606 | no match | no match | not available | not available | **HOLD** (no address match; no map-point fallback) |
| 866 | Mobile | 5245 Rangeline Service Rd S, Mobile, AL 36619 | 5245 RANGELINE RD, MOBILE, AL, 36619 — Mobile city, Mobile County | same matched address — Mobile city, Mobile County | not available | not available | **include** |
| 853 | Mobile | 685 Schillinger Rd S, Mobile, AL 36695 | 685 SCHILLINGER RD S, MOBILE, AL, 36695 — Mobile city, Mobile County | same matched address — Mobile city, Mobile County | not available | not available | **include** |
| 4581 | Mobile | 2500 Dawes Rd, Mobile, AL 36695 | 2500 DAWES SVC RD, MOBILE, AL, 36695 — **Mobile city**, Mobile County | same matched address — **no incorporated place or CDP**, Mobile County | not available | not available | **HOLD** (2020 file not in Mobile city) |
| 1212 | Saraland | 1095 Industrial Pkwy, Saraland, AL 36571 | 1095 INDUSTRIAL PKWY, SARALAND, AL, 36571 — Saraland city, Mobile County | same matched address — Saraland city, Mobile County | not available | not available | **left off, other city** |
| 5174 | Semmes | 7855 Moffett Rd, Semmes, AL 36575 | 7855 MOFFETT RD, SEMMES, AL, 36575 — Semmes city, Mobile County | same matched address — **no incorporated place or CDP**, Mobile County | not available | not available | **left off, other city** |

## Notes by store

### Includes (2), both Mobile-printed

- **#866.** Official `5245 Rangeline Service Rd S` matched as `5245 RANGELINE RD` (the words "Service" and directional "S" were dropped) in both files. Address match is Mobile city, Mobile County, in both files. Included on the address match. The street-name shortening is a Census normalization, not a printed-city disagreement.
- **#853.** Official `685 Schillinger Rd S` matched exactly (as `685 SCHILLINGER RD S`) in both files. Address match is Mobile city, Mobile County, in both files.

### HOLD (2)

- **#991**, 101 E I65 Service Rd S, printed **Mobile**, AL 36606. Official form had no match in either Census file. Variants also had no match in either file, including `I-65`, `Interstate 65`, `I 65`, `East …`, `Service Road` / `Service Rd South`, forms without the leading `E`, `Interstate Hwy` / `Interstate Highway`, `Svc Rd`, and `Frontage Rd`, plus the onelineaddress endpoint for the official, I-65, Interstate 65, and "East Interstate 65 Service Road South" strings. No official map point is available, so this cannot be included on a point fallback. HOLD for no address match in either file. Do not list in Mobile unless a later official coordinate or a later address match overrides the hold.
- **#4581**, 2500 Dawes Rd, printed **Mobile**, AL 36695. Census matched the street as `2500 DAWES SVC RD, MOBILE, AL, 36695` in both files. The current file places that match in **Mobile city**, Mobile County. The 2020 file has the same matched address but **no incorporated place or CDP**, Mobile County only. HOLD: the 2020 address geocode is not in Mobile city, and there is no official map point to break the vintage disagreement. Do not list in Mobile unless a later decision overrides the hold. The matched-address city string still says MOBILE (postal city) in both files.

### Left off, other city (2)

- **#1212**, 1095 Industrial Pkwy, printed **Saraland**, AL 36571. Address match is **Saraland city**, Mobile County, in both files. Geocodes in its printed city, not in Mobile city. Left off as another city's store.
- **#5174**, 7855 Moffett Rd, printed **Semmes**, AL 36575. Current file: **Semmes city**, Mobile County. 2020 file: the same matched address has no incorporated place or CDP, Mobile County only. Neither vintage places the store in Mobile city, so it is left off as another city's store. The 2020 no-place result is recorded; it is a Semmes vintage disagreement, not a Mobile inclusion hold.

## Files

- This note: `/workspace/checkdesk/research/mobile-walmart-geocode-2026-11-13.md`
- Spreadsheet of the same rows: `/workspace/checkdesk/research/mobile-walmart-geocode-2026-11-13.csv`
- Official store-page research (names, addresses, hours, URLs): `/workspace/checkdesk/research/mobile-walmart-2026-11-13.md`
