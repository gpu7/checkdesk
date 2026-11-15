# San Diego, CA USPS research — 2026-11-15 (America/Denver)

Post Offices only. Official USPS Location Finder API (`POST https://tools.usps.com/UspsToolsRestServices/rest/POLocator/findLocations`, `requestType` po) and official location pages (`https://tools.usps.com/locations/details/<id>`). Retail hours are the BUSINESS block only. Money-order flags are taken only from that office's own `poDetail.services` tags (`MONEYORDERSDOM`, `MONEYORDERSINQ`). Hours on the city pages are Pacific Time. No businesses were contacted. Walmart was not collected (official walmart.com store locator unavailable).

Census place used for listing: **San Diego city**, GEOID **0666000**, San Diego County GEOID **06073**. Classification matches that exact name and GEOID only.

## ZIP inventory

Official ZIP-Codes.com city page: https://www.zip-codes.com/city/ca-san-diego.asp (USPS data last updated November 1, 2026). 81 codes listed for San Diego, CA (33 Standard, 34 P.O. Box, 14 Unique). That official list includes 92118 (also official for Coronado) and 92173 (also used for San Ysidro). Those were queried but classified by printed city and Census place.

La Jolla has its own official ZIP-Codes.com page (five codes, including 92037), and those ZIPs are **not** on the official San Diego ZIP list. They were added from the La Jolla page. Official pages for nearby incorporated cities (Chula Vista, National City, Coronado, Imperial Beach, La Mesa, El Cajon, Santee, Poway, Del Mar, Encinitas, Escondido, Carlsbad, San Marcos, Vista, Oceanside, and others) and neighborhood search.asp results were added, then filtered to 919xx–921xx to drop homonyms (for example Del Mar's page also listed Aptos-area 95003; Vista listed Los Angeles and Lancaster aliases; Carmel Valley search returned Monterey County 93924; Kensington, San Carlos, Midway, and Del Sur searches returned Bay Area or desert ZIPs). Solana Beach and Lakeside needed `search.asp` because the city-page slug collided or was missing.

Pass 1 used 154 ZIPs.

## Locator sweep

- Pass 1: 154 ZIPs, 308 queries at 5 and 15 miles, 107 unique records, 0 failed queries.
- Pass 2: 300 widening queries (1, 2, 3, 10, and 20 miles) around 60 core and edge ZIPs, including La Jolla, San Ysidro, Otay Mesa, Coronado, Imperial Beach, Del Mar, and northern city ZIPs. 0 failed queries. 0 new records.
- Total unique records: **107**. Raw locator dump: `san-diego-usps-locator-2026-11-15.jsonl`.

All 107 official pages returned HTTP 200 on the first try. Embedded `poDetail` matched the API record on all 107 (`match_api`).

## Geocoding

U.S. Census Bureau Geocoder, address endpoint and coordinates endpoint, Public_AR_Current / Current_Current and Public_AR_Census2020 / Census2020_Census2020, layers Incorporated Places, Census Designated Places, and Counties. All 107 addresses and all 107 official locator map points were geocoded on both files (`san-diego-usps-geocoder-2026-11-15.jsonl`). The geocoder used each office's printed state (CA). OpenStreetMap was not used.

Address retries were run for printed-San-Diego offices with a no-match on either file:

- Andrew Jackson (1353066), 6401 El Cajon Blvd: current file matches in San Diego city; 2020 file still no-match after street-name retries. No money-order tags.
- Carmel Mountain Postal Store (1373421) and San Diego (1440669), both at 11251 Rancho Carmel Dr: current file matches in San Diego city; 2020 file still no-match after retries.
- MCAS Miramar (1371856), 45482 Elrod St Ste 3, and Marine Corp RD (1476496), 4300 Belleau Wood Ave Bldg 148: no address match on either file after retries; official map points in San Diego city on both files.
- NAS North Island (1374416), 124 Murray Ave Bldg 124: no address match after retries; official map point in Coronado city on both files.

Map-point fallback was used only when the official page already prints San Diego and the official map point is in San Diego city on both files. That applies to Carmel Mountain Postal Store and MCAS Miramar (listed) and, for geography only, to Andrew Jackson, San Diego 1440669, and Marine Corp RD (not listed, no money-order tags). It was not used for NAS North Island (point in Coronado), and it is never used when the printed city already disagrees.

## Classification (107 records)

- **27 listed.** Printed city San Diego; money-order tags present. 25 have address and official map point in San Diego city on both Census files. 2 listed under map-point fallback, as documented above (Carmel Mountain Postal Store and MCAS Miramar). All 27 are in San Diego County. 1 Open evenings (Carmel Mountain Postal Store, weekday close 18:00). 24 Open weekends (Saturday retail; no Sunday hours). The three listed offices with no weekend hours are Southeastern, Naval Hospital, and Paradise Hills. Official names kept, including Downtown San Diego, College Grove Center, Carmel Mountain Postal Store, and MCAS Miramar. Ocean Beach and Pacific Beach print SAN DIEGO and are listed.
- **11 in-city, not listed.** Printed San Diego; geography in San Diego city (including three map-point-fallback geographies); no money-order tags. Riverfront Carrier Annex (1379460); Andrew Jackson (1353066, has Saturday BUSINESS hours); Golden Triangle (1365091); La Jolla Annex UC (1474237, prints San Diego); University City Annex (1385474); Serra Mesa Annex (1455132); Rancho Bernardo Annex (1378753); Scripps Ranch Annex (1381051); Marine Corp RD (1476496, has weekday BUSINESS hours); Otay Mesa Annex (1376400); San Diego (1440669) at the same 11251 Rancho Carmel Dr address as the listed Carmel Mountain Postal Store.
- **1 HOLD, printed San Diego, not in San Diego city.** NAS North Island (1374416): address no-match after retries; official point in Coronado city. Has money orders and a weekday midday split (not stored, because the office is not listed).
- **3 HOLD, other printed city, any geocode leg in San Diego city.** All three have all four legs in San Diego city and list money orders: La Jolla (1369384, 1140 Wall St) and La Jolla Village (1484523, 8861 Villa La Jolla Dr Ste 505), both print La Jolla; San Ysidro (1440677, 440 W San Ysidro Blvd) prints San Ysidro.
- **65 left off.** Other printed cities fully outside San Diego city, including Camp Pendleton (10), Chula Vista (4), Oceanside (4), Escondido (4), La Mesa (3), Coronado (1), National City, Imperial Beach, and others.

39 records print San Diego (27 listed + 11 in-city not listed + 1 geographic hold).

No Walmart rows. IDs are `usps-san-diego-<locatorID>`. `last_verified` 2026-11-15. `verification_status` `verified_official_locator`.
