# Middletown, DE USPS research (2026-11-15)

America/Denver (MST). Step 8, fourth Delaware city, Post Offices only. Hours are Eastern Time. Census place: Middletown town, GEOID 1047030, New Castle County (10003), POPESTIMATE2025 25,798 (Vintage 2025, SUMLEV 162). Middletown is an incorporated town; Check Desk pages use the name Middletown. This is Middletown, Delaware, not a Middletown in another state. OpenStreetMap was not used.

## Official ZIPs

ZIP-Codes.com city page `de-middletown.asp` title: “Middletown, DE ZIP Code, Map and Demographics,” Data Last Updated November 1, 2026. search.asp title: “1 ZIP Code in Middletown, DE.” City page and search have the same one unique code.

| ZIP | Type | Listed city (search.asp) | County | City-page aliases |
|-----|------|--------------------------|--------|-------------------|
| 19709 | Standard | Middletown | New Castle | |

Official printed-Middletown ZIP: 19709 (Standard). It is listed Middletown in New Castle County, with no alias.

## Nearby collection and slug collisions

Pass 1 used prefixes 197 (southern New Castle), 198 (Wilmington), 199 (Kent County, DE), 219 (Cecil County, MD), and 216 (Maryland Eastern Shore). Nearby city pages were fetched from ZIP-Codes.com, with search.asp used on slug collisions.

Collisions (search.asp fallback used):

- Christiana, DE slug collided with the Newark city page; search.asp title “2 ZIP Codes in Christiana, DE.”
- Elsmere and Newport slugs collided with the Wilmington city page; search.asp used.
- Leipsic, DE slug collided with the Dover city page; search.asp title “1 ZIP Code in Leipsic, DE.”
- Golts, MD slug collided with the Galena, MD city page; search.asp used.

St. Georges and Glasgow have no ZIP-Codes.com city pages (404 / “0 ZIP Codes”).

Pass 1 ZIP inventory: 68 unique codes (198: 25, 197: 21, 199: 11, 216: 6, 219: 5).

## Locator sweeps

Official USPS locator API, `requestType=po`.

- Pass 1: 68 ZIPs at 5 and 15 miles, 136 queries, 166 unique records, 0 fails, 1 printed Middletown (Delaware).
- Pass 2: the same 68 official and edge ZIPs at 1, 2, 3, 10, and 20 miles, 340 queries, 0 fails, +86 far records, still 1 printed Middletown, 252 unique.

Locator dump: `docs/research/step8-browser/middletown-usps-locator-2026-11-15.jsonl`.

The only record whose official printed city is Middletown is Middletown Post Office (1372966), 298 E Main St, 19709, 302-378-6241. No printed-Middletown office from another state appeared.

## Official pages

All 252 official USPS location pages returned HTTP 200. Embedded `poDetail` matched the locator API on address, phone, and BUSINESS hours for all 252 (`match_api` on all).

Middletown (1372966) BUSINESS hours, Eastern Time: Mon–Fri 08:00–17:30; Sat 08:30–13:00; Sun closed. Tags: MONEYORDERSDOM and MONEYORDERSINQ. Open evenings (weekday close 17:30). Open weekends (Saturday).

## Geocoder

U.S. Census Bureau Geocoder, address and coordinates endpoints, Public_AR_Current / Current_Current and Public_AR_Census2020 / Census2020_Census2020, layers Incorporated Places + CDPs + Counties. Classification uses only Middletown town GEOID 1047030. Dump: `docs/research/step8-browser/middletown-usps-geocoder-2026-11-15.jsonl`. 252 records, 0 errors. OpenStreetMap was not used.

Only one record has any leg in Middletown town, and it prints Middletown:

1. **1372966 Middletown, 298 E Main St, printed Middletown.** Current address file: matched `298 E MAIN ST, MIDDLETOWN, DE, 19709`, Middletown town GEOID 1047030 / New Castle County 10003. 2020 address file: same match, still in Middletown town. Official map point (39.44956, -75.707863) is in Middletown town on both the current and 2020 benchmarks.

No other printed city has a geocode leg inside Middletown town. No printed-Middletown office sits outside the town. No map-point fallbacks were used.

## Classification

- Listed: 1 (Middletown Post Office 1372966). Money orders: 1. Open evenings: 1 (weekday close 17:30). Open weekends: 1 (Saturday 08:30–13:00; Sunday closed).
- Holds: none.
- In-city, not listed: none.
- Map-point fallbacks: none.
- Nearby Post Offices that print Odessa, Townsend, Smyrna, Clayton, Delaware City, Bear, Newark, and others geocode outside Middletown town and are not holds.

## Raw files

`/workspace/step8mdt/` (official ZIP pages, nearby city/search HTML, locator JSON, official USPS pages, geocoder dump).
