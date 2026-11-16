# Miami, FL USPS research (2026-11-15)

America/Denver (MST). Step 8, second Florida city, Post Offices only. Hours are Eastern Time. Census place: Miami city, GEOID 1245000, POPESTIMATE2025 489,812 (Vintage 2025, SUMLEV 162), inside Miami-Dade County (GEOID 12086, FUNCSTAT A, 2,802,029). This is Miami, Florida, not a Miami in another state, and not Miami Beach, Miami Springs, Miami Shores, Miami Gardens, or another nearby municipality. OpenStreetMap was not used.

## Official ZIPs

ZIP-Codes.com city page `fl-miami.asp` title: “Miami, FL ZIP Codes, Map and Demographics,” Data Last Updated November 1, 2026. The page says Miami has 102 ZIP Codes and lists 102 unique codes. search.asp title: “111 ZIP Codes in Miami, FL,” paginated (Page 1 of 3, 50 rows per page; pages 1–3 fetched, 111 unique codes). All 102 city-page codes appear in the search. Nine search codes do not appear on the city page (33014–33018 listed Hialeah; 33054 and 33055 listed Opa Locka; 33056 listed Miami Gardens; 33139 listed Miami Beach).

Official printed-Miami ZIPs are the **93** codes search lists as Miami, all in Miami-Dade (58 Standard, 29 P.O. Box, 6 Unique). All 93 also appear on the city page.

Excluded from official printed-Miami even though they appear on the Miami search (and, for nine of them, on the Miami city page):

| ZIP | Search listed city |
|-----|--------------------|
| 33109, 33119, 33139, 33140, 33141, 33154, 33239 | Miami Beach |
| 33014, 33015, 33016, 33017, 33018 | Hialeah |
| 33054, 33055 | Opa Locka |
| 33114 | Coral Gables |
| 33149 | Key Biscayne |
| 33160 | North Miami Beach |
| 33056 | Miami Gardens |

Many nearby city slugs collide with another city’s page (for example `fl-miami-gardens` opens as Hialeah, and `fl-aventura` opens as North Miami Beach). Nearby ZIP lists therefore come from search.asp titles, which name the intended city. A search for “Opa-Locka” returned 0 ZIP Codes; the Miami search lists 33054 and 33055 as Opa Locka, and the Opa Locka city page title is “Opa Locka, FL ZIP Codes, Map and Demographics.”

## Locator sweeps

Official USPS locator API, `requestType=po`.

- Pass 1: 147 ZIPs (prefixes 331: 81, 330: 40, 332: 22, 333: 4), including all 93 official printed-Miami ZIPs and 54 official or edge ZIPs from nearby city searches, at 5 and 15 miles, 294 queries, 107 unique records, 0 fails, 38 printed Miami (Florida).
- Pass 2: the same 147 official and edge ZIPs at 1, 2, 3, 10, and 20 miles, 735 queries, 0 fails, +7 far records (Lighthouse Point, Deerfield Beach, Coconut Creek, and Boca Raton), still 38 printed Miami, 114 unique.

Locator dump: `docs/research/step8-browser/miami-usps-locator-2026-11-15.jsonl`.

No printed-Miami office from another state appeared.

## Official pages

All 114 official USPS location pages returned HTTP 200. Embedded `poDetail` matched the locator API on address, phone, and BUSINESS hours for all 114 (`match_api` on all).

## Geocoder

U.S. Census Bureau Geocoder, address and coordinates endpoints, Public_AR_Current / Current_Current and Public_AR_Census2020 / Census2020_Census2020, layers Incorporated Places + CDPs + Counties. Classification uses only the SUMLEV 162 Miami city GEOID 1245000, not Miami-Dade County as a whole and not a CDP. Dump: `docs/research/step8-browser/miami-usps-geocoder-2026-11-15.jsonl`. 114 records, 0 errors. OpenStreetMap was not used.

Eleven records have any leg in Miami city, and all 11 print Miami. The other 27 printed-Miami records have no leg in Miami city.

### Street-name alias (1 listed)

**1381462 Shenandoah, 1800 Coral Way, printed Miami.** Current and 2020 address files: no match after street-name, city, and ZIP retries (CORAL WAY, CORAL WAY BLVD, CORALWAY, SW CORAL WAY, ZIPs 33145/33135/33125 and empty ZIP). A retry on the local street alias SW 22ND ST (Coral Way is SW 22nd Street) matched `1800 SW 22ND ST, MIAMI, FL, 33145` in Miami city on both address files. No retry snapped to a different street number. Official map point (25.750536, -80.224216) is in Miami city on both benchmarks. Listed (money-order tags and BUSINESS hours).

### Other geocode notes

- Metro (1478274, 150 SE 2ND AVE STE 103): the geocoder dropped the suite and matched `150 SE 2ND AVE, MIAMI, FL, 33131` in Miami city on both address files. Both map points agree.
- Flagler Miami (1363470, 500 NW 2ND AVE): the 2020 address file matched the same street with ZIP 33136 instead of 33101, still in Miami city. Both map points agree.
- Hibiscus Carrier Annex (1438804, 3500 S Dixie Hwy): current and 2020 address files unmatched; both official map points are in Miami city. Not listed (no money-order tags, no BUSINESS block).
- Several held offices also had unmatched address files (Ludlam, Kendall, West Dade, Country Lakes, Quail Heights). In each case the official map points fall outside Miami city, so the map-point fallback does not apply. A West Dade retry on the local alias SW 88TH ST (N Kendall Dr) matched in The Hammocks CDP, still outside Miami city.

## Classification

- Listed: 7, all with money-order tags (DOM+INQ) and a BUSINESS hours block. Money orders: 7. Open evenings: 0 (every listed office’s weekday retail closes at 17:00, which does not count). Open weekends: 6 (Saturday hours; none publish Sunday hours). Metro is not labeled Open evenings or Open weekends.
- Holds: 27, all print Miami, with no geocode leg in Miami city. Seven sit in another incorporated place (Aventura city, North Miami city, Miami Shores village, Miami Springs city, Miami Gardens city, Palmetto Bay village, Pinecrest village). Eleven sit in a census-designated place (Gladeview, Goulds, Kendall, Glenvar Heights, Ojus, Westchester, The Hammocks). Nine sit in unincorporated Miami-Dade County with no place or CDP, including the General Mail Facility cluster around 2200 NW 72nd Ave. CDPs and unincorporated areas stay off the list.
- In-city, not listed: 4, all print Miami and geocode in Miami city, but their official pages do not list money orders: Brickell (1534797, BUSINESS hours); Buena Vista (1533657, BUSINESS hours); Buena Vista Carrier Annex (1532914); Hibiscus Carrier Annex (1438804, in-city by official map points).
- Map-point fallbacks used to list an office: 0. Shenandoah is listed on a documented street-name alias, with official map points in agreement.
- No other printed city has a geocode leg inside Miami city. Offices that print Miami Beach, Coral Gables, Hialeah, Doral, North Miami, South Miami, and other nearby cities geocode outside Miami city and are not holds for Miami.

## Raw files

`/workspace/step8mia/` (official ZIP pages, nearby city/search HTML, locator JSON, official USPS pages, geocoder dump).
