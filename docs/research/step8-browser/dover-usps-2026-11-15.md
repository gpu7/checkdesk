# Dover, DE USPS research (2026-11-15)

America/Denver (MST). Step 8, second Delaware city, Post Offices only. Hours are Eastern Time. Census place: Dover city, GEOID 1021200, Kent County (10001), POPESTIMATE2025 40,592 (Vintage 2025, SUMLEV 162). OpenStreetMap was not used.

## Official ZIPs

ZIP-Codes.com city page `de-dover.asp` title: “Dover, DE ZIP Codes, Map and Demographics,” Data Last Updated November 1, 2026. search.asp title: “6 ZIP Codes in Dover, DE.” City page and search have the same six unique codes.

| ZIP | Type | Listed city (search.asp) | County | City-page aliases |
|-----|------|--------------------------|--------|-------------------|
| 19901 | Standard | Dover | Kent | Leipsic |
| 19902 | Standard | Dover AFB | Kent | Dover, Dover Air Force Base |
| 19903 | P.O. Box | Dover | Kent | |
| 19904 | Standard | Dover | Kent | |
| 19905 | P.O. Box | Dover | Kent | |
| 19906 | Standard | Dover | Kent | |

Official printed-Dover ZIPs: 19901, 19903, 19904, 19905, 19906 (3 Standard + 2 P.O. Box). 19902 is listed as Dover AFB, not Dover; it was included in pass 1 as a nearby ZIP and was not treated as an official printed-Dover ZIP.

## Nearby collection and slug collisions

Pass 1 used prefixes 199 (Kent/Sussex DE), 197 (southern New Castle), and 216 (Maryland Eastern Shore). Nearby city pages were fetched from ZIP-Codes.com, with search.asp used on slug collisions.

Collisions (search.asp fallback used):

- Camden, DE and Wyoming, DE slugs both resolved to the Camden Wyoming city page; search.asp titles “1 ZIP Code in Camden, DE” and “1 ZIP Code in Wyoming, DE.”
- Leipsic, DE slug collided with the Dover city page; search.asp title “1 ZIP Code in Leipsic, DE.”
- Farmington, DE slug collided with Greenwood; search.asp used.
- Bowers, DE slug collided with Frederica; search.asp used.
- Dover Air Force Base slug collided with the Dover AFB city page; search.asp used.

Kent Acres, Highland Acres, Rodney Village, Rising Sun-Lebanon, and Woodside East have no ZIP-Codes.com city pages (404 / “0 ZIP Codes”).

Pass 1 ZIP inventory: 47 unique codes (199: 25, 216: 19, 197: 3).

## Locator sweeps

Official USPS locator API, `requestType=po`.

- Pass 1: 47 ZIPs at 5 and 15 miles, 94 queries, 83 unique records, 0 fails, 1 printed Dover.
- Pass 2: the same 47 official and edge ZIPs at 1, 2, 3, 10, and 20 miles, 235 queries, 0 fails, +43 far records, still 1 printed Dover, 126 unique.

Locator dump: `docs/research/step8-browser/dover-usps-locator-2026-11-15.jsonl`.

The only record whose official printed city is Dover is Dover Post Office (1361099), 445 Bank Ln, 19904, 302-734-7188. Dover AFB Post Office (1434206), 442 13th St, 19902, 302-677-6196, prints Dover AFB, not Dover.

## Official pages

All 126 official USPS location pages returned HTTP 200. Embedded `poDetail` matched the locator API on address, phone, and BUSINESS hours for all 126 (`match_api` on all).

Dover (1361099) BUSINESS hours, Eastern Time: Mon 07:30–18:00; Tue–Fri 08:00–18:00; Sat 09:00–13:00; Sun closed. Tags: MONEYORDERSDOM and MONEYORDERSINQ.

Dover AFB (1434206) BUSINESS hours: Mon–Fri 09:00–16:30; Sat–Sun closed. Tags: MONEYORDERSDOM and MONEYORDERSINQ. No Open evenings (16:30 close). No weekend hours.

## Geocoder

U.S. Census Bureau Geocoder, address and coordinates endpoints, Public_AR_Current / Current_Current and Public_AR_Census2020 / Census2020_Census2020, layers Incorporated Places + CDPs + Counties. Classification uses only Dover city GEOID 1021200. Dump: `docs/research/step8-browser/dover-usps-geocoder-2026-11-15.jsonl`. 126 records, 0 errors. OpenStreetMap was not used.

Only two records have any leg in Dover city:

1. **1361099 Dover, 445 Bank Ln, printed Dover.** Current address file: no match. 2020 address file: matched `445 BANK LN, DOVER, DE, 19904`, Dover city GEOID 1021200 / Kent County 10001 (same street). Official map point (39.155432, -75.5300209) is in Dover city on both the current and 2020 benchmarks.

   Current-file street-name retries (all n=0, no errors): 445 BANK LN, 445 BANK LANE, 445 BANK LN., 445 BANK ROAD, 445 BANK RD, and N/S/E/W BANK LN, each with ZIPs 19904, 19901, 19903, 19905, 19906, and an empty ZIP, city Dover. No retry snapped to a different street. Because the printed city is Dover and both official map points fall inside Dover city, the office is listed under the documented map-point fallback. The 2020 address match is the same street and also in the city.

2. **1434206 Dover AFB, 442 13th St, printed Dover AFB.** Address file: no match on current or 2020. Official map point (39.123086, -75.480458) is in Dover city on both benchmarks.

   Address retries on both files (all n=0, no errors): 442 13TH ST, 442 13TH STREET, 442 13TH ST., 442 THIRTEENTH ST, 442 THIRTEENTH STREET, directional 13TH ST, and 442 13 ST; cities Dover AFB, Dover, and Dover Air Force Base; ZIPs 19902, 19901, 19904, 19903, 19906, and an empty ZIP. HOLD: another printed city has a geocode leg inside Dover city.

No other printed city has a geocode leg inside Dover city. No other printed-Dover record exists.

## Classification

- Listed: 1 (Dover Post Office 1361099). Money orders: 1. Open evenings: 1 (weekday close 18:00; Monday opens 07:30, Tuesday–Friday 08:00). Open weekends: 1 (Saturday 09:00–13:00; Sunday closed).
- Holds: 1 (Dover AFB 1434206 — prints Dover AFB; both map points inside Dover city; address files unmatched after retries).
- In-city, not listed: none.
- Map-point fallbacks: 1 (Dover Post Office), documented above.
- Nearby Post Offices that print Camden Wyoming, Cheswold, Little Creek, Magnolia, Woodside, Viola, Felton, Hartly, Kenton, Smyrna, Clayton, Harrington, Frederica, Houston, Marydel, and others geocode outside Dover city and are not holds.

## Raw files

`/workspace/step8dov/` (official ZIP pages, nearby city/search HTML, locator JSON, official USPS pages, street-retry log).
