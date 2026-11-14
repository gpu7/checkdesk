# Wasilla, AK: USPS locator research (2026-11-14, America/Denver)

Research only until the city pages are shipped. No business was contacted. No browser was used. last_verified: 2026-11-14. Official detail pages that were fetched are marked verification_status `verified_official_locator`. Hours below are **Alaska Time**. City-limits wording: Wasilla is an **incorporated city** inside Matanuska-Susitna Borough (Census "Wasilla city" GEOID 0283080). The county-equivalent is Matanuska-Susitna Borough (GEOID 02170). A USPS printed city of Wasilla is treated as agreeing with that Census place name only when the address and official map point also fall inside Wasilla city. Offices printed Wasilla whose address or map point falls outside the city (in a CDP, another city, or unincorporated borough land) are holds. Offices printed with other place names (Palmer, Houston, and others) are left off, or held if they geocode inside Wasilla city.

## Method

- **Locator:** official USPS Location Finder API (`https://tools.usps.com/UspsToolsRestServices/rest/POLocator/findLocations`, `requestType` po), queried with curl the same way as Fairbanks, Juneau, and Anchorage. Pass 1 (`sweep.py`): 5 and 15 miles around every Wasilla ZIP (the 5 USPS-city Wasilla codes listed for Wasilla, AK by ZIP-Codes.com from USPS data last updated 2026-11-01: 99623, 99629, 99652, 99654, and 99687). 99623 is also listed for Big Lake, Houston, and Meadow Lake (aliases). 99629 is also listed for Meadow Lake. 99652 is also listed for Big Lake (Wasilla is an alias on that code). Nearby official ZIPs: 99645 (Palmer), 99674 (Sutton / Chickaloon), 99676 (Talkeetna), 99683 (Trapper Creek; Willow is an alias), 99688 (Willow), 99694 (Houston). 22 queries, all JSON, **11 unique Post Office records**. No ZIP returned 0 locations. Pass 2 (`sweep2.py`): 1, 2, 3, 10, and 20 miles around all 11 of those ZIPs; added 0 records. Total **11 records** (`usps_all.json`). Note: when nothing lies inside a very small radius the API returns a default nearest list, so some 1-2 mile queries show large counts; that only widens coverage. Some 15-mile queries returned fewer records than the 5-mile queries around the same ZIP; the 20-mile pass-2 queries did not add anything new.
- **Official pages:** `https://tools.usps.com/locations/details/<id>` fetched with curl about 9:04 AM MT for all 11 records. All returned **HTTP 200 on the first try** (`http.txt`, `d<id>.html`). Each page embeds the official `poDetail` record; `pages.py` parsed it and confirmed name, address, phone, and BUSINESS hours match the API record for all 11 (`pages.json`). "Retail hours" = the `BUSINESS` block only (not lobby, PO Box, pickup, holiday, bulk-mail, or APC).
- **City limits:** all 11 addresses through the Census Geocoder address endpoint and all 11 official locator map points, each against both Public_AR_Current / Current_Current and Public_AR_Census2020 / Census2020_Census2020, Incorporated Places + CDPs + Counties (`usps_geo_all.jsonl`). OpenStreetMap was not used.

## Candidate includes (1), money orders yes (MONEYORDERSDOM, MONEYORDERSINQ), HTTP 200, verified_official_locator

Retail hours are Alaska Time. "Open evenings" means a weekday BUSINESS close after 17:00 (a 17:00 close does not count). "Open weekends" means Saturday or Sunday retail.

| ID | Office | Address | Phone | Retail (BUSINESS) hours | Evenings | Weekends | Geocode |
|---|---|---|---|---|---|---|---|
| 1386558 | WASILLA | 401 N Main St, Wasilla, AK 99654 | 907-376-5327 | Mon-Fri 09:00-17:30; Sat/Sun closed | yes | no | Current + 2020 address: Wasilla city (GEOID 0283080); point 61.583617,-149.440788 Wasilla city |

URL: https://tools.usps.com/locations/details/1386558.

Notes:
- This is the only office whose official printed city is Wasilla, that lists money orders and retail hours, and whose address and official map point both fall inside Wasilla city on both Census files.
- Weekday retail closes at 17:30, so it is labeled Open evenings. Saturday and Sunday are closed, so it is not labeled Open weekends.

## HOLDS (1)

1. **WASILLA ANNEX (1386557)**, 626 N Bobby Day Cir, printed **Wasilla**, AK 99654, 907-376-4206. https://tools.usps.com/locations/details/1386557 (HTTP 200). **No money-order tags and no BUSINESS hours block** on the official page or in the API (match_api). Current + 2020 address: no match after street-name retries ("Bobby Day Circle," "North Bobby Day Cir," "Bobby Day Cir"). Official map point 61.586544,-149.372444 is in **South Lakes CDP** (GEOID 0272135), Matanuska-Susitna Borough, on both benchmarks, not Wasilla city. Held because the official printed city is Wasilla but the official map point falls outside the city, in a CDP. It would not be listable in any case, because it has no retail hours and no money orders.

## Left off (omissions, not holds)

- No Big Lake-printed or Meadow Lake-printed office appeared under `requestType` po. Queries around 99623, 99629, and 99652 returned only the records listed here.
- No Wasilla-printed carrier-annex-style record besides 1386557 appeared.

### Nearby other-city offices (left off; printed city ≠ Wasilla and the geocoder agrees outside Wasilla city)

All pages were HTTP 200.

- **HOUSTON 1439406**, 17152 W Parks Hwy, Houston 99694, 907-892-6129: MONEYORDERSDOM only. Address no match in either file (retries as "W Parks Highway," "West Parks Hwy," and with city Wasilla also had no match); official map point 61.629726,-149.811307 in **Houston city** (GEOID 0233800), Matanuska-Susitna Borough, on both benchmarks. Houston is a separate incorporated city. Mon-Fri 09:00-17:00, Sat 09:00-13:00.
- **PALMER 1376656**, 500 S Cobb St, Palmer 99645, 907-745-5051: address + point **Palmer city** (GEOID 0258660). Mon-Fri 10:00-17:30, Sat 09:00-12:00.
- **WILLOW 1387815**, 13232 N McKinley Way, Willow 99688, 907-495-6266: address + point **Willow CDP** (GEOID 0285280). Mon-Fri 08:00-11:00/12:00-17:00, Sat 09:00-12:00.
- **SUTTON 1384070**, 11266 N Chickaloon Way, Sutton 99674, 907-745-3433: address + point **Sutton-Alpine CDP** (GEOID 0274525). Mon-Fri 09:30-12:30/13:30-16:30, Sat 09:00-12:00.
- **CHICKALOON 1439381**, 33968 N Glenn Hwy, printed **Sutton**, AK 99674, 907-746-0280: MONEYORDERSDOM only. Address (matched as 33968 GLENN HWY, SUTTON, AK, 99674) + official map point 61.776438,-148.493154 in **Chickaloon CDP** (GEOID 0213340). Printed city is Sutton, not Wasilla, and the geocode is outside Wasilla city, so this is left off, not a Wasilla hold. Mon-Sat 13:00-18:00, Sun closed.
- **TALKEETNA 1384230**, 13707 E First St, Talkeetna 99676, 907-733-2275: address + point **Talkeetna CDP** (GEOID 0274830). Mon-Fri 09:00-13:00/14:00-17:00, Sat/Sun closed.
- **TRAPPER CREEK 1439454**, 23161 S Watson Cir, Trapper Creek 99683, 907-733-4440: MONEYORDERSDOM only. Address + point **Trapper Creek CDP** (GEOID 0278680). Mon-Fri 09:30-16:30, Sat/Sun closed.
- **EAGLE RIVER 1361596**, 11471 Business Blvd, Eagle River 99577, 907-694-2732: address + point **Anchorage municipality**. Already held on the Anchorage pages (prints Eagle River). Left off under Wasilla. Mon-Fri 09:30-17:30, Sat 10:00-14:00.
- **CHUGIAK 1358023**, 22255 Dogsled Ct, Chugiak 99567, 907-688-2747: current address and both map points **Anchorage municipality**. 2020 address file: no match (same no-match already documented in the Anchorage research). Already held on the Anchorage pages (prints Chugiak). Left off under Wasilla. Mon-Fri 09:00-17:30, Sat 09:00-13:00.

## Fetch failures

None of the 22 + 55 locator queries failed to parse. All 11 detail pages returned HTTP 200 on the first try. Census address no-matches after street-name retries remain for Wasilla Annex and Houston; each was resolved by an official map point outside Wasilla city (South Lakes CDP and Houston city). Chugiak's 2020 address no-match is unchanged from the Anchorage research; the official map point is in Anchorage municipality.
