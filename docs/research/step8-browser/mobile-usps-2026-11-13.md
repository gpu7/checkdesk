# Mobile, AL: USPS locator research (2026-11-13, America/Denver)

Research only. Nothing was built, committed, or deployed. No business was contacted. No browser was used. No other Alabama city was started. last_verified: 2026-11-13. Official detail pages that were fetched are marked verification_status `verified_official_locator`. City-limits wording: Mobile is a **city** (Census "Mobile city" GEOID 0150000, Mobile County GEOID 01097 for every Mobile-area row below unless a Baldwin County office is noted).

## Method

- **Locator:** official USPS Location Finder API (`https://tools.usps.com/UspsToolsRestServices/rest/POLocator/findLocations`, `requestType` po), queried with curl the same way as the Huntsville and Colorado cities. Pass 1 (`sweep.py`): 5 and 15 miles around every Mobile ZIP (36601-36613, 36615-36619, 36628, 36633, 36640, 36641, 36644, 36652, 36660, 36663, 36670, 36671, 36675, 36685, 36688, 36689, 36691, 36693, 36695) and nearby official ZIPs 36571 (Saraland), 36526 (Daphne), 36527 (Spanish Fort), 36575 (Semmes), 36582 (Theodore), 36572 (Satsuma), 36505 (Axis), 36541 (Grand Bay), 36544 (Irvington), 36509 (Bayou La Batre), 36522 (Citronelle), 36525 (Creola), 36532 (Fairhope), 36528 (Dauphin Island), 36587 (Wilmer), 36521 (Chunchula), 36560 (Mount Vernon), 36523 (Coden). 106 queries, all JSON, **51 unique Post Office records**. ZIP 36641 returned 0 locations at both radii (likely not a live ZIP) and was not a parse failure. Pass 2 (`sweep2.py`): 1, 2, 3, 10, and 20 miles around 17 Mobile/edge ZIPs (36602-36606, 36608, 36609, 36617-36619, 36693, 36695, 36615, 36571, 36575, 36582, 36526); added 0 records. Total **51 records** (`usps_all.json`, `usps_summ.txt`). Note: when nothing lies inside a very small radius the API returns a default ~26-30 nearest list, so some 1-2 mile queries show large counts; that only widens coverage.
- **Official pages:** `https://tools.usps.com/locations/details/<id>` fetched with curl about 9:58 AM MT for all 13 Mobile-printed records, Theodore, and the 14 nearest other-city offices (28 pages). All returned **HTTP 200 on the first try** (`http.txt`, `d<id>.html`). Each page embeds the official `poDetail` record; `pages.py` parsed it and confirmed name, address, phone, and BUSINESS hours match the API record for all 28 (`pages.json`). "Retail hours" = the `BUSINESS` block only (not lobby, PO Box, pickup, or holiday).
- **City limits:** all 51 addresses through the Census Geocoder address endpoint and all 51 official locator map points, each against both Public_AR_Current / Current_Current and Public_AR_Census2020 / Census2020_Census2020, Incorporated Places + CDPs + Counties (`usps_geo_all.jsonl`). Joined view: `joined.txt`. Structured output: `/workspace/step8mob/mobile_usps_records.csv` / `.json` (51 rows, `build.py`). OpenStreetMap was not used.

## Candidate includes (12), all money orders yes (MONEYORDERSDOM, MONEYORDERSINQ), all HTTP 200, verified_official_locator

| ID | Office | Address | Phone | Retail (BUSINESS) hours | Evenings | Weekends | Geocode |
|---|---|---|---|---|---|---|---|
| 1373428 | MOBILE | 250 Saint Joseph St, Mobile, AL 36601 | 251-694-5969 | Mon-Fri 08:00-17:00; Sat 09:00-12:00; Sun closed | no | yes | Current + 2020 address: Mobile city (matched as 250 ST JOSEPH ST, ZIP 36602); point 30.696852,-88.0435749 Mobile city |
| 1373019 | MIDTOWN | 907 Spring Hill Ave, Mobile, AL 36604 | 251-432-0270 | Mon-Fri 09:00-16:30; Sat/Sun closed | no | no | Current + 2020 address: Mobile city; point 30.689576,-88.0565039 Mobile city |
| 1370927 | LOOP | 415 Dauphin Island Pkwy, Mobile, AL 36606 | 251-479-9571 | Mon-Fri 08:30-16:30; Sat/Sun closed | no | no | Current + 2020 address: Mobile city; point 30.674391,-88.086597 Mobile city |
| 1359833 | CRICHTON | 168 Bay Shore Ave, Mobile, AL 36607 | 251-478-5639 | Mon-Fri 09:00-16:30; Sat/Sun closed | no | no | Current + 2020 address: Mobile city; point 30.696555,-88.105997 Mobile city |
| 1354449 | BEL AIR | 3410 Bel Air Mall, Mobile, AL 36606 | 251-478-8513 | Mon-Fri 11:00-**18:00**; Sat 12:00-17:00; Sun closed | **yes** (closes 18:00) | yes | See note: current address no match; 2020 address Mobile city; point 30.672143,-88.121899 Mobile city (current and 2020) |
| 1354246 | BAYSIDE | 2000 Rosedale Rd, Mobile, AL 36605 | 251-479-9569 | Mon-Fri 08:30-16:30; Sat/Sun closed | no | no | Current address: Mobile city (2020 file no match); point 30.624029,-88.0839759 Mobile city (current and 2020) |
| 1359368 | COTTAGE HILL | 705 Oak Circle Dr W, Mobile, AL 36609 | 251-660-8559 | Mon-Fri 08:30-16:30; Sat 09:00-12:00; Sun closed | no | yes | Current + 2020 address: Mobile city; point 30.652134,-88.155833 Mobile city |
| 1382538 | SPRING HILL | 5551 Old Shell Rd, Mobile, AL 36608 | 251-341-5624 | Mon-Fri 08:30-16:30; Sat 09:30-12:00; Sun closed | no | yes | Current address no match; 2020 address Mobile city; point 30.689104,-88.170429 Mobile city (current and 2020) |
| 1384895 | TOWNE WEST | 5701M Moffett Rd, Mobile, AL 36618 | 251-342-8665 | Mon-Fri 09:00-16:30; Sat 09:00-12:00; Sun closed | no | yes | Current + 2020 address: Mobile city (unit letter kept as 5701M); point 30.727912,-88.1730669 Mobile city |
| 1377773 | PLAZA DE MALAGA | 6157 Airport Blvd Ste 310, Mobile, AL 36608 | 251-341-6186 | Mon-Fri 08:30-16:30; Sat/Sun closed | no | no | Current + 2020 address: Mobile city (matched as 6157 AIRPORT BLVD, suite dropped); point 30.675096,-88.183486 Mobile city |
| 1384671 | TILLMANS CORNER | 5441 Highway 90 W Ste 13, Mobile, AL 36619 | 251-666-6580 | Mon-Fri 09:00-16:30; Sat 09:00-12:00; Sun closed | no | yes | See note: no address match in either file; point 30.5864,-88.1677929 Mobile city (current and 2020) |
| 1352482 | AIRPORT | 8400 Airport Blvd, Mobile, AL 36608 | 251-635-1743 | Mon-Fri 09:00-16:30; Sat 09:00-12:00; Sun closed | no | yes | Current + 2020 address: Mobile city; point 30.681214,-88.2409589 Mobile city |

URLs: https://tools.usps.com/locations/details/1373428, /1373019, /1370927, /1359833, /1354449, /1354246, /1359368, /1382538, /1384895, /1377773, /1384671, /1352482.

Notes:
- **Downtown Mobile (1373428):** Census matched the street as "ST JOSEPH ST" rather than the official "SAINT JOSEPH ST" and assigned ZIP 36602 rather than the printed 36601. Address match and official map point are Mobile city, Mobile County, in both files. No disagreement with the printed city, so it's not a hold.
- **Bel Air, Bayside, Spring Hill:** one of the two Census address files had no match; the other address file (where it matched) and the official map point on both benchmarks are Mobile city. Included on the official map point, with the matching vintage as supporting evidence. No printed-city disagreement.
- **Tillmans Corner:** the official address (including forms without "Ste 13" and "US Hwy 90" variants) has **no match** in the current or 2020 Census address file. The official USPS map point falls in **Mobile city** (not Tillmans Corner CDP) on both the current and 2020 benchmarks. Included on the official map point. No disagreement with the printed city, so it's not a hold. Pax may choose to hold it if a strict address match is required.
- Only Bel Air is open evenings (weekday close 18:00). All others close 17:00 or earlier = not evenings. Weekends = Saturday only, at Mobile, Bel Air, Cottage Hill, Spring Hill, Towne West, Tillmans Corner, and Airport. No Sunday retail.

## HOLDS (2)

1. **PRICHARD (1437776)**, 130 E Prichard Ave, printed **Mobile**, AL 36610, 251-457-4512. https://tools.usps.com/locations/details/1437776 (HTTP 200). Money orders yes; BUSINESS Mon-Fri 08:30-16:30, Sat 09:00-12:00, Sun closed. **Disagreement:** official printed city is Mobile, but the address match (130 E PRICHARD AVE, MOBILE, AL, 36610) and the official USPS map point (30.730075,-88.081575) fall in **Prichard city** (GEOID 0162496), Mobile County, on both the current and 2020 benchmarks. Held, not listed in Mobile.
2. **THEODORE (1384530)**, 5631 Highway 90, printed **Theodore**, AL 36582, 251-653-8718. https://tools.usps.com/locations/details/1384530 (HTTP 200). Money orders yes; BUSINESS Mon-Fri 09:00-16:30, Sat 09:00-11:00, Sun closed. **Disagreement:** official printed city is Theodore (not Mobile), but the address match (normalized to 5631 US HWY 90, THEODORE, AL, 36582) and the official USPS map point (30.569951,-88.1706959) fall in **Mobile city** on both the current and 2020 benchmarks. Held: not listed in Mobile, and Theodore is not a Check Desk city. The matched-address city string still says THEODORE (postal city); the Census incorporated place is Mobile city.

## Left off (omissions, not holds)

- No Mobile-printed carrier annex or plant records without retail hours or money orders appeared under `requestType` po. All 13 Mobile-printed records have BUSINESS hours and money orders; the only Mobile-printed record not included is the Prichard hold above.
- No Spanish Fort office appeared in the locator sweep.

### Nearby other-city offices (left off; printed city ≠ Mobile and the geocoder agrees outside Mobile city)

All have money orders and retail hours. All pages were HTTP 200 unless marked "API only".
- **CHICKASAW 1437733**, 411 Parker Ln, Chickasaw 36611, 251-457-2018: address + point **Chickasaw city**. Mon-Fri 08:30-13:00/14:15-16:30, Sat/Sun closed.
- **SARALAND 1380794**, 104 Norton Ave, Saraland 36571, 251-679-0393: address + point **Saraland city**. Mon-Fri 08:30-16:30, Sat 09:00-12:00.
- **DAPHNE 1360296**, 808 Daphne Ave, Daphne 36526, 251-621-7314: address + point **Daphne city**, Baldwin County. Mon-Fri 09:00-16:30, Sat 09:00-12:00.
- **SATSUMA 1380841**, 50 Orange Ave W, Satsuma 36572, 251-679-9251: address + point **Satsuma city**. Mon-Fri 09:00-16:30 (Wed closes 13:00), Sat 09:00-11:00.
- **SEMMES 1381200**, 9051 Moffett Rd, Semmes 36575, 251-645-2789: address + point **Semmes city**. Mon-Fri 08:30-16:30, Sat 09:00-12:00.
- **CREOLA 1359785**, 9617 Old Highway 43, Creola 36525, 251-675-0672: current address + current point **Creola town**; 2020 address no match; 2020 point **Creola city**. Mon-Fri 07:00-11:00/12:00-14:00, Sat 07:00-10:00.
- **FAIRHOPE 1363003**, 509 Fairhope Ave, Fairhope 36532, 251-990-3623: address + point **Fairhope city**, Baldwin County. Mon-Fri 09:00-16:30, Sat 09:30-12:00.
- **GRAND BAY 1365289**, 12580 US Highway 90, Grand Bay 36541, 251-865-7904: address + point **Grand Bay CDP**. Mon-Fri 09:00-16:30, Sat 09:00-11:00.
- **DAUPHIN ISLAND 1360327**, 423 La Vente St, Dauphin Island 36528, 251-861-2702: address + point **Dauphin Island town**. Mon-Fri 09:30-12:30/13:30-15:45, Sat 10:00-11:00.
- **MONTROSE 1373682**, 7325 Sibley St, Montrose 36559: address matched, no place or CDP (unincorporated Baldwin County); point also none.
- **IRVINGTON 1368071**, 9251 Irvington Blb Hwy, Irvington 36544: address no match; point in no place or CDP (unincorporated Mobile County).
- **SAINT ELMO 1380322**, 8900 Highway 90 W, Saint Elmo 36568: address no match; point in no place or CDP (unincorporated Mobile County).
- **WILMER 1387836**, 13255 Moffett Rd, Wilmer 36587: address matched, no place or CDP; point also none (unincorporated Mobile County).
- **AXIS 1353805**, 11436 Old Highway 43, Axis 36505: address + point **Axis CDP**.
- Farther (API only, outside Mobile city by address and/or point; see CSV): Point Clear, Chunchula, Bayou La Batre, Coden, Hurley MS, Bucks, Loxley, Silverhill, Robertsdale, Stapleton, Summerdale, Bay Minette, Magnolia Springs, Stockton, Mount Vernon, Escatawpa MS, Moss Point MS, Citronelle, Deer Park, Calvert, Foley, Malcolm, Mc Intosh.
- No other-city-printed office besides Theodore has an address match or map point inside Mobile city.

## Fetch failures

None. All 106 + 85 locator queries returned JSON (ZIP 36641 simply had 0 locations). All 28 detail pages returned HTTP 200 on the first try. Census address no-matches (current file): Bel Air, Spring Hill, Tillmans Corner, Irvington, Saint Elmo, Point Clear, Hurley, Summerdale, Magnolia Springs, Escatawpa, Calvert, and Mc Intosh. Each was resolved by the official map point, except Irvington, Saint Elmo, and Hurley, whose points also have no incorporated place or CDP (unincorporated; left off as other-city offices).
