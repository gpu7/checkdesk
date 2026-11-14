# Juneau, AK: USPS locator research (2026-11-14, America/Denver)

Research only until the city pages are shipped. No business was contacted. No browser was used. last_verified: 2026-11-14. Official detail pages that were fetched are marked verification_status `verified_official_locator`. Hours below are **Alaska Time**. City-limits wording: Juneau is a **consolidated city-borough** (Census "Juneau city and borough" GEOID 0236400). The county-equivalent on every in-municipality row below is Juneau City and Borough (GEOID 02110). A USPS printed city of Juneau is treated as agreeing with that Census place name.

## Method

- **Locator:** official USPS Location Finder API (`https://tools.usps.com/UspsToolsRestServices/rest/POLocator/findLocations`, `requestType` po), queried with curl the same way as Anchorage and the Alabama cities. Pass 1 (`sweep.py`): 5 and 15 miles around every Juneau ZIP (the 8 USPS-city Juneau codes listed for Juneau, AK by ZIP-Codes.com from USPS data last updated 2026-11-01: 99801, 99802, 99803, 99811, 99812, 99821, 99824, and 99850). 99821 is also listed for Auke Bay (alias Juneau). 99824 is also listed for Douglas (alias Juneau). 99812 is the unique State Of Alaska Brm ZIP. Nearby official ZIPs: 99826 (Gustavus), 99827 (Haines), 99829 (Hoonah), 99820 (Angoon), 99840 (Skagway), 99832 (Pelican), 99841 (Tenakee Springs), 99825 (Elfin Cove), 99830 (Kake), 99833 (Petersburg), 99835/99836 (Sitka), 99689 (Yakutat). 42 queries, all JSON, **16 unique Post Office records**. No ZIP returned 0 locations. Pass 2 (`sweep2.py`): 1, 2, 3, 10, and 20 miles around 14 Juneau/edge and nearby official ZIPs (the eight Juneau codes plus Gustavus, Haines, Hoonah, Angoon, Skagway, and Pelican); added 1 record, Pelican 1377100, from the 20-mile query around 99832 (5- and 15-mile queries around that ZIP had not returned the Pelican office). Total **17 records** (`usps_all.json`, `usps_summ.txt`). Note: when nothing lies inside a very small radius the API returns a default nearest list, so some 1-2 mile queries show large counts; that only widens coverage.
- **Official pages:** `https://tools.usps.com/locations/details/<id>` fetched with curl about 8:40 AM MT for all 17 records. All returned **HTTP 200 on the first try** (`http.txt`, `d<id>.html`). Each page embeds the official `poDetail` record; `pages.py` parsed it and confirmed name, address, phone, and BUSINESS hours match the API record for all 17 (`pages.json`). "Retail hours" = the `BUSINESS` block only (not lobby, PO Box, pickup, holiday, bulk-mail, or APC).
- **City limits:** all 17 addresses through the Census Geocoder address endpoint and all 17 official locator map points, each against both Public_AR_Current / Current_Current and Public_AR_Census2020 / Census2020_Census2020, Incorporated Places + CDPs + Counties (`usps_geo_all.jsonl`). Joined view: `joined.txt`. Structured output: `/workspace/step8jnu/juneau_usps_records.csv` / `.json` (17 rows, `build.py`). OpenStreetMap was not used.

## Candidate includes (3), all money orders yes (MONEYORDERSDOM, MONEYORDERSINQ), all HTTP 200, verified_official_locator

Retail hours are Alaska Time. "Open evenings" means a weekday BUSINESS close after 17:00 (a 17:00 close does not count). "Open weekends" means Saturday or Sunday retail.

| ID | Office | Address | Phone | Retail (BUSINESS) hours | Evenings | Weekends | Geocode |
|---|---|---|---|---|---|---|---|
| 1363268 | FEDERAL STATION | 709 W 9th St, Juneau, AK 99801 | 907-586-7987 | Mon-Fri 09:00-17:00; Sat/Sun closed | no | no | Current + 2020 address: Juneau city and borough; point 58.301561,-134.420355 Juneau city and borough |
| 1372690 | MENDENHALL | 9491 Vintage Blvd, Juneau, AK 99801 | 907-789-0934 | Mon-Fri 09:00-18:00; Sat 11:00-16:00; Sun closed | yes | yes | Current address: Juneau city and borough; 2020 address file: no match (retries as "Vintage Boulevard," "Vintage Blvd.," and "Vintage Rd" also had no match); official map point 58.372977,-134.593189 Juneau city and borough on both the current and 2020 benchmarks |
| 1439374 | AUKE BAY | 11899 Glacier Hwy, Juneau, AK 99801 | 907-789-0680 | Mon-Fri 11:00-13:00/14:00-17:30; Sat 12:00-15:00; Sun closed | yes | yes | Current + 2020 address: Juneau city and borough; point 58.387245,-134.649189 Juneau city and borough |

URLs: https://tools.usps.com/locations/details/1363268, /1372690, /1439374.

Notes:
- The official locator name for 1439374 is **AUKE BAY**, but the official printed city is **Juneau**, not Auke Bay. The address and map point are in Juneau city and borough on both files, so this is an include, not a hold.
- **Mendenhall (1372690)** is included on the current Census address match and the official map point in both files. The 2020 address file had no match after street-name retries; that is documented and is not a hold, because the printed city is Juneau and the official map point is in Juneau city and borough.
- Two of the three includes are open evenings (weekday close after 17:00). Weekend retail is Saturday only, at Mendenhall and Auke Bay. Federal Station closes at 17:00 on weekdays and is closed on weekends, so it gets neither label. No Sunday retail at any include.
- No separate downtown "Juneau" or "Juneau Main Office" record appeared under `requestType` po. Federal Station is the downtown retail office.

## HOLDS (1)

1. **DOUGLAS (1439392)**, 804 3rd St, printed **Douglas**, AK 99824, 907-364-2445. https://tools.usps.com/locations/details/1439392 (HTTP 200). Money orders yes; BUSINESS Mon-Fri 13:00-17:30, Sat 13:00-15:00, Sun closed (evenings yes; weekends yes). Current + 2020 address and both map points: Juneau city and borough (GEOID 0236400). Official map point 58.276233,-134.393534. Douglas is a community inside Juneau city and borough, not a separate incorporated place. Held because the official printed city is Douglas, not Juneau. The map-point fallback is only for when the printed city already matches; it does not apply here.

## Left off (omissions, not holds)

- No Juneau-printed carrier annex or no-retail record appeared under `requestType` po.
- No other-city-printed office besides Douglas has an address match or map point inside Juneau city and borough.

### Nearby other-city offices (left off; printed city ≠ Juneau and the geocoder agrees outside Juneau city and borough)

All have money orders and retail hours. All pages were HTTP 200.

- **GUSTAVUS 1365874**, 123 Postmark Dr, Gustavus 99826, 907-600-3198: address no match in either file (retry as "Postmark Drive" also had no match); official map point in **Gustavus city**, Hoonah-Angoon Census Area, on both benchmarks. Mon-Fri 09:00-16:00, Sat 12:00-14:00.
- **HAINES 1365954**, 55 Haines Hwy, Haines 99827, 907-766-2930: address + point **Haines CDP**. Mon-Fri 09:00-17:00, Sat 13:00-15:00.
- **HOONAH 1367350**, 420 Airport Dr, Hoonah 99829, 907-600-3216: address + point **Hoonah city**, Hoonah-Angoon Census Area. Mon-Fri 10:00-13:00/14:00-17:00, Sat 10:00-13:00.
- **ANGOON 1353090**, 705 Aandeinatt St, Angoon 99820, 907-788-3442: address no match in either file (retry as "Aandeinatt Street" also had no match); official map point in **Angoon city**, Hoonah-Angoon Census Area, on both benchmarks. Mon-Fri 10:00-13:00/14:00-17:00, Sat 09:00-13:00.
- **SKAGWAY 1381770**, 641 Broadway St, Skagway 99840, 907-983-2330: address + point **Skagway CDP**. Mon-Fri 08:30-11:30/12:30-17:00, Sat/Sun closed.
- **ELFIN COVE 1362254**, 1 Main St, Elfin Cove 99825, 915-400-5313 (the official page and the API agree on this phone number): the Census address file does not match this Alaska address; both the current and 2020 files instead first-match "1 N MAIN ST, COVE, TX, 77520" (Baytown city, Harris County), with further matches in Cove, Texas and Cove, Utah — a city-name collision on "Cove," not an Alaska place. Official map point 58.193388,-136.345512 is in **Elfin Cove CDP**, Hoonah-Angoon Census Area, on both benchmarks, outside Juneau city and borough. Left off, not a Juneau hold. Street and ZIP retries still produced the Texas/Utah matches.
- **TENAKEE SPRINGS 1384422**, 108 E Tenakee Ave, Tenakee Springs 99841, 907-736-2236: address + point **Tenakee Springs city**, Hoonah-Angoon Census Area. Mon-Fri 08:30-12:00/13:00-15:30, Sat 09:00-12:30.
- **KAKE 1368640**, 272 Keku Rd, Kake 99830, 907-785-3123: address + point **Kake city**. Mon-Fri 09:00-13:00/14:00-16:00, Sat 10:00-13:00.
- **PETERSBURG 1377316**, 1201 Haugen Dr, Petersburg 99833, 325-261-4617 (official page and API agree): address + point **Petersburg CDP**. Mon-Fri 09:00-17:30, Sat 14:00-16:00.
- **SITKA 1381757**, 1207 Sawmill Creek Rd, Sitka 99835, 907-747-3381: address + point **Sitka city and borough**. Mon-Fri 09:30-17:00, Sat/Sun closed.
- **PORT ALEXANDER 1439436**, 206 Main St, Port Alexander 99836, 907-568-2311: address + point **Port Alexander city**. MONEYORDERSDOM only. Unusual retail hours: Mon 15:30-16:45, Tue closed, Wed 15:30-16:30, Thu closed, Fri 15:30-17:00, Sat 08:00-16:00, Sun closed.
- **YAKUTAT 1388417**, 477 Mallotts Ave, Yakutat 99689, 907-784-3201: address + point **Yakutat CDP**. Mon-Fri 09:00-13:00/14:00-17:00, Sat 09:30-12:30.
- **PELICAN 1377100**, 171 A Salmon Way, Pelican 99832, 907-735-2248: address + point **Pelican city**. Mon-Fri 10:00-13:00/14:00-17:00, Sat 09:00-13:00. Found in pass 2 at 20 miles around ZIP 99832; not returned at 5 or 15 miles.

## Fetch failures

None. All 42 + 70 locator queries returned JSON. All 17 detail pages returned HTTP 200 on the first try. Census address no-matches: Mendenhall (2020 file only), Gustavus, and Angoon (current and 2020). Each no-match was retried with expanded street wording (`geo_retries.txt`) and still had no address match. Mendenhall is included on the current address match and the official map point (printed city Juneau). Gustavus and Angoon were resolved by official map points outside Juneau city and borough. Elfin Cove's address file produced out-of-state "Cove" matches; the official map point places it in Elfin Cove CDP, outside Juneau, so it is left off.
