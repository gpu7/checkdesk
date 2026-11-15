# Milford, DE USPS research (2026-11-15)

America/Denver (MST). Step 8, fifth Delaware city, Post Offices only. Hours are Eastern Time. Census place: Milford city, GEOID 1047420, POPESTIMATE2025 14,723 (Vintage 2025, SUMLEV 162). Milford is one incorporated place split across Sussex County (part 8,216) and Kent County (part 6,507). Ranking and city-limits classification use the whole-place total and GEOID 1047420. This is Milford, Delaware, not a Milford in another state. OpenStreetMap was not used.

## Official ZIPs

ZIP-Codes.com city page `de-milford.asp` title: “Milford, DE ZIP Code, Map and Demographics,” Data Last Updated November 1, 2026. search.asp title: “1 ZIP Code in Milford, DE.” City page and search have the same one unique code.

| ZIP | Type | Listed city (search.asp) | County (search.asp) | City-page aliases |
|-----|------|--------------------------|---------------------|-------------------|
| 19963 | Standard | Milford | Sussex | Slaughter Beach |

Official printed-Milford ZIP: 19963 (Standard). Search lists the ZIP’s city as Milford and its county as Sussex. That is the ZIP-Codes.com county for the code, not a claim that the whole Census place is in one county. The city-page alias is Slaughter Beach, a separate incorporated town.

The Slaughter Beach slug collided with the Milford city page; search.asp title “1 ZIP Code in Slaughter Beach, DE” still lists 19963 as Milford in Sussex.

## Nearby collection and slug collisions

Pass 1 used prefixes 199 (Kent and Sussex, DE) and 216 (Maryland Eastern Shore). Nearby city pages were fetched from ZIP-Codes.com, with search.asp used on slug collisions.

Collisions (search.asp fallback used):

- Slaughter Beach, DE slug collided with the Milford city page, as above.
- Farmington, DE slug collided with Greenwood; search.asp title “1 ZIP Code in Farmington, DE.”
- Camden, DE and Wyoming, DE slugs both resolved to the Camden Wyoming city page; search.asp titles “1 ZIP Code in Camden, DE” and “1 ZIP Code in Wyoming, DE.”
- Bowers, DE slug collided with Frederica; search.asp used.
- Leipsic, DE slug collided with the Dover city page; search.asp used.

Pass 1 ZIP inventory: 36 unique codes (199: 28, 216: 8).

## Locator sweeps

Official USPS locator API, `requestType=po`.

- Pass 1: 36 ZIPs at 5 and 15 miles, 72 queries, 86 unique records, 0 fails, 1 printed Milford (Delaware).
- Pass 2: the same 36 official and edge ZIPs at 1, 2, 3, 10, and 20 miles, 180 queries, 0 fails, +28 far records, still 1 printed Milford, 114 unique.

Locator dump: `docs/research/step8-browser/milford-usps-locator-2026-11-15.jsonl`.

The only record whose official printed city is Milford is Milford Post Office (1373085), 110 Causey Ave, 19963, 302-422-5618. No printed-Slaughter Beach office appeared. No printed-Milford office from another state appeared.

## Official pages

All 114 official USPS location pages returned HTTP 200. Embedded `poDetail` matched the locator API on address, phone, and BUSINESS hours for all 114 (`match_api` on all).

Milford (1373085) BUSINESS hours, Eastern Time: Mon–Fri 08:30–17:00; Sat 09:00–13:00; Sun closed. Tags: MONEYORDERSDOM and MONEYORDERSINQ. No Open evenings (weekday close 17:00; a 5:00 p.m. close does not count). Open weekends (Saturday).

## Geocoder

U.S. Census Bureau Geocoder, address and coordinates endpoints, Public_AR_Current / Current_Current and Public_AR_Census2020 / Census2020_Census2020, layers Incorporated Places + CDPs + Counties. Classification uses only the whole-place Milford city GEOID 1047420, which covers both the Sussex and Kent county parts. Dump: `docs/research/step8-browser/milford-usps-geocoder-2026-11-15.jsonl`. 114 records, 0 errors. OpenStreetMap was not used.

Only one record has any leg in Milford city, and it prints Milford:

1. **1373085 Milford, 110 Causey Ave, printed Milford.** Current address file: matched `110 CAUSEY AVE, MILFORD, DE, 19963`, Milford city GEOID 1047420 / Sussex County 10005 (the Sussex part of the place). 2020 address file: same match, still in Milford city. Official map point (38.911139, -75.431772) is in Milford city on both the current and 2020 benchmarks.

No other printed city has a geocode leg inside Milford city. No printed-Milford office sits outside the city. No map-point fallbacks were used.

## Classification

- Listed: 1 (Milford Post Office 1373085). Money orders: 1. Open evenings: 0 (weekday close 17:00). Open weekends: 1 (Saturday 09:00–13:00; Sunday closed).
- Holds: none.
- In-city, not listed: none.
- Map-point fallbacks: none.
- Nearby Post Offices that print Houston, Harrington, Frederica, Lincoln, Greenwood, Ellendale, Milton, Seaford, and others geocode outside Milford city and are not holds.

## Raw files

`/workspace/step8mlf/` (official ZIP pages, nearby city/search HTML, locator JSON, official USPS pages, geocoder dump).
