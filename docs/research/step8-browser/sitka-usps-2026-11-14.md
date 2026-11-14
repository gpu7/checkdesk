# Sitka, AK: USPS locator research (2026-11-14, America/Denver)

Research only until the city pages are shipped. No business was contacted. No browser was used. last_verified: 2026-11-14. Official detail pages that were fetched are marked verification_status `verified_official_locator`. Hours below are **Alaska Time**. City-limits wording: Sitka is a **consolidated city-borough** (Census "Sitka city and borough" GEOID 0270540). The county-equivalent on every in-municipality row below is Sitka City and Borough (GEOID 02220). A USPS printed city of Sitka is treated as agreeing with that Census place name.

## Method

- **Locator:** official USPS Location Finder API (`https://tools.usps.com/UspsToolsRestServices/rest/POLocator/findLocations`, `requestType` po), queried with curl the same way as Juneau, Fairbanks, and Wasilla. Pass 1 (`sweep.py`): 5 and 15 miles around every Sitka ZIP (the 2 USPS-city Sitka codes listed for Sitka, AK by ZIP-Codes.com from USPS data last updated 2026-11-01: 99835 and 99836). 99836 is also listed for Port Alexander (aliases Prt Alexander, Sitka). Nearby official ZIPs: 99801 (Juneau), 99830 (Kake), 99833 (Petersburg), 99929 (Wrangell), 99921 (Craig), 99925 (Klawock), 99922 (Hydaburg), 99926 (Metlakatla), 99827 (Haines), 99840 (Skagway), 99829 (Hoonah), 99820 (Angoon), 99689 (Yakutat), 99826 (Gustavus). 32 queries, all JSON, **19 unique Post Office records**. No ZIP returned 0 locations. Pass 2 (`sweep2.py`): 1, 2, 3, 10, and 20 miles around 9 Sitka/edge and nearby official ZIPs (99835, 99836, 99801, 99830, 99833, 99929, 99921, 99925, 99826); added 0 records. Total **19 records** (`usps_all.json`). Note: when nothing lies inside a very small radius the API returns a default nearest list, so some 1-2 mile queries show large counts; that only widens coverage. Queries around 99835 (Sitka) returned only the Sitka office at every radius from 1 to 20 miles.
- **Official pages:** `https://tools.usps.com/locations/details/<id>` fetched with curl about 9:08 AM MT for all 19 records. All returned **HTTP 200 on the first try** (`http.txt`, `d<id>.html`). Each page embeds the official `poDetail` record; `pages.py` parsed it and confirmed name, address, phone, and BUSINESS hours match the API record for all 19 (`pages.json`). "Retail hours" = the `BUSINESS` block only (not lobby, PO Box, pickup, holiday, bulk-mail, or APC).
- **City limits:** all 19 addresses through the Census Geocoder address endpoint and all 19 official locator map points, each against both Public_AR_Current / Current_Current and Public_AR_Census2020 / Census2020_Census2020, Incorporated Places + CDPs + Counties (`usps_geo_all.jsonl`). OpenStreetMap was not used.

## Candidate includes (1), money orders yes (MONEYORDERSDOM, MONEYORDERSINQ), HTTP 200, verified_official_locator

Retail hours are Alaska Time. "Open evenings" means a weekday BUSINESS close after 17:00 (a 17:00 close does not count). "Open weekends" means Saturday or Sunday retail.

| ID | Office | Address | Phone | Retail (BUSINESS) hours | Evenings | Weekends | Geocode |
|---|---|---|---|---|---|---|---|
| 1381757 | SITKA | 1207 Sawmill Creek Rd, Sitka, AK 99835 | 907-747-3381 | Mon-Fri 09:30-17:00; Sat/Sun closed | no | no | Current + 2020 address: Sitka city and borough (GEOID 0270540); point 57.049543,-135.311298 Sitka city and borough |

URL: https://tools.usps.com/locations/details/1381757.

Notes:
- This is the only office whose official printed city is Sitka and whose address and official map point both fall inside Sitka city and borough on both Census files. No second Sitka-printed retail office appeared.
- Weekday retail closes at 17:00, so it is not labeled Open evenings. Saturday and Sunday are closed, so it is not labeled Open weekends. The evenings-and-weekends page for Sitka therefore lists zero locations. That is a correct application of the standing hours rule, not a missing office.

## HOLDS (0)

No Sitka-printed office has an address or official map point outside Sitka city and borough. No other-city-printed office has an address or official map point inside Sitka city and borough.

## Left off (omissions, not holds)

- No Sitka-printed carrier annex or no-retail record appeared under `requestType` po.

### Nearby other-city offices (left off; printed city ≠ Sitka and the geocoder agrees outside Sitka city and borough)

All pages were HTTP 200. Juneau-area offices in this sweep (Federal Station, Mendenhall, Auke Bay, Douglas) were already classified in the Juneau research and remain outside Sitka city and borough.

- **PORT ALEXANDER 1439436**, 206 Main St, Port Alexander 99836, 907-568-2311: MONEYORDERSDOM only. Address + official map point 56.247918,-134.647125 in **Port Alexander city** (GEOID 0262510), Prince of Wales-Hyder Census Area. Port Alexander is a separate incorporated city, not inside Sitka city and borough. Unusual retail hours: Mon 15:30-16:45, Tue closed, Wed 15:30-16:30, Thu closed, Fri 15:30-17:00, Sat 08:00-16:00, Sun closed.
- **KAKE 1368640**, 272 Keku Rd, Kake 99830, 907-785-3123: address + point **Kake city**. Mon-Fri 09:00-13:00/14:00-16:00, Sat 10:00-13:00.
- **PETERSBURG 1377316**, 1201 Haugen Dr, Petersburg 99833, 325-261-4617 (official page and API agree): address + point **Petersburg CDP**. Mon-Fri 09:00-17:30, Sat 14:00-16:00.
- **WRANGELL 1388328**, 112 Federal Way, Wrangell 99929: official page and API agree on an empty phone field and on **no money-order tags**. Address + official map point 56.472488,-132.387184 in **Wrangell city and borough** (GEOID 0286380). Mon-Fri 09:00-17:00, Sat 10:00-12:00. Left off (other city, and no money orders).
- **CRAIG 1359718**, 303 Thompson Rd, Craig 99921, 907-600-3157: address no match; official map point **Craig city**. Mon-Fri 08:30-17:00, Sat 12:00-14:00.
- **KLAWOCK 1369203**, 6488 Klawock Hollis Hwy, Klawock 99925, 907-755-2977: address no match; official map point **Klawock city**. Mon-Fri 09:00-12:30/13:00-17:00, Sat 12:00-14:00.
- **HYDABURG 1367770**, 1 Postal Way, Hydaburg 99922, 907-285-3514: address no match; official map point **Hydaburg city**. Mon-Fri 10:00-12:00/13:00-17:00, Sat 08:00-12:00.
- **METLAKATLA 1372851**, 352 8th Ave, Metlakatla 99926, 907-886-6712: address no match; official map point **Metlakatla CDP**. Mon-Fri 11:30-13:00/14:00-17:00, Sat 11:00-13:00.
- **HAINES 1365954**, 55 Haines Hwy, Haines 99827, 907-766-2930: address + point **Haines CDP**. Mon-Fri 09:00-17:00, Sat 13:00-15:00.
- **SKAGWAY 1381770**, 641 Broadway St, Skagway 99840, 907-983-2330: address + point **Skagway CDP**. Mon-Fri 08:30-11:30/12:30-17:00, Sat/Sun closed.
- **HOONAH 1367350**, 420 Airport Dr, Hoonah 99829, 907-600-3216: address + point **Hoonah city**. Mon-Fri 10:00-13:00/14:00-17:00, Sat 10:00-13:00.
- **ANGOON 1353090**, 705 Aandeinatt St, Angoon 99820, 907-788-3442: address no match; official map point **Angoon city**. Mon-Fri 10:00-13:00/14:00-17:00, Sat 09:00-13:00.
- **YAKUTAT 1388417**, 477 Mallotts Ave, Yakutat 99689, 907-784-3201: address + point **Yakutat CDP**. Mon-Fri 09:00-13:00/14:00-17:00, Sat 09:30-12:30.
- **GUSTAVUS 1365874**, 123 Postmark Dr, Gustavus 99826, 907-600-3198: address no match; official map point **Gustavus city**. Mon-Fri 09:00-16:00, Sat 12:00-14:00.
- **JUNEAU offices** already listed or held on the Juneau pages (Federal Station, Mendenhall, Auke Bay, and Douglas): all geocode in Juneau city and borough, outside Sitka.

## Fetch failures

None of the 32 + 45 locator queries failed to parse. All 19 detail pages returned HTTP 200 on the first try. Census address no-matches remain for Craig, Klawock, Hydaburg, Metlakatla, Angoon, and Gustavus (same pattern as the Juneau research for Angoon and Gustavus); each was resolved by an official map point outside Sitka city and borough. Mendenhall's 2020 address no-match is unchanged from the Juneau research.
