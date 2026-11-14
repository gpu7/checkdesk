# Fairbanks, AK: USPS locator research (2026-11-14, America/Denver)

Research only until the city pages are shipped. No business was contacted. No browser was used. last_verified: 2026-11-14. Official detail pages that were fetched are marked verification_status `verified_official_locator`. Hours below are **Alaska Time**. City-limits wording: Fairbanks is an **incorporated city** inside Fairbanks North Star Borough (Census "Fairbanks city" GEOID 0224230). The county-equivalent is Fairbanks North Star Borough (GEOID 02090). A USPS printed city of Fairbanks is treated as agreeing with that Census place name only when the address and official map point also fall inside Fairbanks city. Offices printed Fairbanks whose address or map point falls outside the city (in a CDP, another city, or unincorporated borough land) are holds. Offices printed with other place names are left off, or held if they geocode inside Fairbanks city.

## Method

- **Locator:** official USPS Location Finder API (`https://tools.usps.com/UspsToolsRestServices/rest/POLocator/findLocations`, `requestType` po), queried with curl the same way as Anchorage and Juneau. Pass 1 (`sweep.py`): 5 and 15 miles around every Fairbanks ZIP (the 15 USPS-city Fairbanks codes listed for Fairbanks, AK by ZIP-Codes.com from USPS data last updated 2026-11-01: 99701, 99702, 99705, 99706, 99707, 99708, 99709, 99710, 99711, 99712, 99714, 99716, 99767, 99775, and 99790). 99702 is also listed for Eielson AFB (alias Fairbanks). 99705 is also listed for North Pole (alias Fairbanks). 99714 is also listed for Salcha (alias Fairbanks). 99716 is also listed for Two Rivers (alias Fairbanks). 99767 is also listed for Rampart (alias Fairbanks). 99710 alias Steese; 99711 alias Badger; 99775 is the unique Univ Of Ak ZIP. Nearby official ZIPs: 99703 (Fort Wainwright), 99725 (Ester), 99704 (Clear), 99744 (Anderson), 99760 (Nenana), 99743 (Healy), 99729 (Cantwell), 99737 (Delta Junction), 99731 (Fort Greely), 99780 (Tok), 99756 (Manley Hot Springs), 99758 (Minto), 99730 (Central), 99733 (Circle). 58 queries, all JSON, **20 unique Post Office records**. ZIP 99730 (Central) returned 0 locations at both 5 and 15 miles (not a parse failure). Pass 2 (`sweep2.py`): 1, 2, 3, 10, and 20 miles around 25 Fairbanks/edge and nearby official ZIPs; added 0 records. 99730 was still 0 at 1-20 miles. One-off follow-ups (same as the Anchorage 99693 / Juneau 99832 widenings): a 50-mile query around 99730 returned Central 1357498; queries around 99776 (Tanacross) returned Tanacross 1439449 and Tok 1384764, which 5- to 50-mile queries around Tok's official ZIP 99780 had not returned (those queries returned only the already-known Northway office). Total **23 records** (`usps_all.json`). Note: when nothing lies inside a very small radius the API returns a default nearest list, so some 1-2 mile queries show large counts; that only widens coverage.
- **Official pages:** `https://tools.usps.com/locations/details/<id>` fetched with curl about 8:56 AM MT for all 23 records. All returned **HTTP 200 on the first try** (`http.txt`, `d<id>.html`). Each page embeds the official `poDetail` record; `pages.py` parsed it and confirmed name, address, phone, and BUSINESS hours match the API record for all 23 (`pages.json`). "Retail hours" = the `BUSINESS` block only (not lobby, PO Box, pickup, holiday, bulk-mail, or APC).
- **City limits:** all 23 addresses through the Census Geocoder address endpoint and all 23 official locator map points, each against both Public_AR_Current / Current_Current and Public_AR_Census2020 / Census2020_Census2020, Incorporated Places + CDPs + Counties (`usps_geo_all.jsonl`). OpenStreetMap was not used.

## Candidate includes (1), money orders yes (MONEYORDERSDOM, MONEYORDERSINQ), HTTP 200, verified_official_locator

Retail hours are Alaska Time. "Open evenings" means a weekday BUSINESS close after 17:00 (a 17:00 close does not count). "Open weekends" means Saturday or Sunday retail.

| ID | Office | Address | Phone | Retail (BUSINESS) hours | Evenings | Weekends | Geocode |
|---|---|---|---|---|---|---|---|
| 1361212 | FAIRBANKS DOWNTOWN STA | 315 Barnette St, Fairbanks, AK 99701 | 907-452-3223 | Mon-Fri 09:30-17:30; Sat/Sun closed | yes | no | Current + 2020 address: Fairbanks city (GEOID 0224230); point 64.842568,-147.723458 Fairbanks city |

URL: https://tools.usps.com/locations/details/1361212.

Notes:
- This is the only office whose official printed city is Fairbanks and whose address and official map point both fall inside Fairbanks city on both Census files.
- Weekday retail closes at 17:30, so it is labeled Open evenings. Saturday and Sunday are closed, so it is not labeled Open weekends.

## HOLDS (3)

1. **FAIRBANKS MAIN OFFICE (1439417)**, 5400 Mail Trail Rd, printed **Fairbanks**, AK 99709, 907-455-5444. https://tools.usps.com/locations/details/1439417 (HTTP 200). Money orders yes; BUSINESS Mon-Fri 09:30-18:00, Sat/Sun closed (evenings yes; weekends no). Current + 2020 address and both map points: **College CDP** (GEOID 0216750), Fairbanks North Star Borough, not Fairbanks city. Official map point 64.815682,-147.881225. Held because the printed city is Fairbanks but the address and official map point fall outside the city, in a CDP. The map-point fallback does not apply when the point is outside the city.

2. **COLLEGE (1439388)**, 755 Fairbanks St, printed **Fairbanks**, AK 99709, 907-479-6021. https://tools.usps.com/locations/details/1439388 (HTTP 200). Money orders yes; BUSINESS Mon-Fri 10:00-17:30, Sat 11:00-15:00, Sun closed (evenings yes; weekends yes). Current + 2020 address and both map points: **College CDP** (GEOID 0216750), Fairbanks North Star Borough, not Fairbanks city. Official map point 64.848484,-147.828121. The official locator name is College, but the official printed city is Fairbanks. Held because the address and official map point fall outside Fairbanks city, in a CDP. This is the same printed-Fairbanks / outside-city rule as the Main Office, not the Auke Bay pattern (Auke Bay printed Juneau and geocoded inside Juneau city and borough).

3. **FORT WAINWRIGHT (1439402)**, 3726 Neely Rd, printed **Fort Wainwright**, AK 99703, 907-356-7602. https://tools.usps.com/locations/details/1439402 (HTTP 200). Money orders yes; BUSINESS Mon-Fri 10:30-13:00/14:00-16:30, Sat/Sun closed (evenings no; weekends no). Current + 2020 address and both map points: **Fairbanks city** (GEOID 0224230). Official map point 64.827373,-147.642119. The current address match is 3726 NEELY RD, FORT WAINWRIGHT, AK, 99703 at 64.827879,-147.680019, a short distance from the official map point; both the address match and the official map point are in Fairbanks city on both files. Held because the official printed city is Fort Wainwright, not Fairbanks, even though the geocoder places the office inside Fairbanks city.

## Left off (omissions, not holds)

- No Fairbanks-printed carrier annex or no-retail record appeared under `requestType` po.
- No Two Rivers-printed or Fox-printed office appeared. 99716 queries returned only already-known offices.
- No Fort Greely-printed office appeared. 99731 queries returned only Delta Junction.

### Nearby other-city offices (left off; printed city ≠ Fairbanks and the geocoder agrees outside Fairbanks city)

All pages were HTTP 200. All have money orders unless noted.

- **NORTH POLE 1439429**, 325 S Santa Claus Ln, North Pole 99705, 907-488-7534: address + point **North Pole city** (GEOID 0255910), Fairbanks North Star Borough. Mon-Fri 09:00-17:00, Sat 10:00-14:00.
- **EIELSON AFB 1439397**, 5514 Kodiak St, Eielson AFB 99702, 907-372-6300: address no match in either file (retries as "Kodiak Street" and with city Fairbanks also had no match); official map point 64.677837,-147.094773 in **Eielson AFB CDP** (GEOID 0221370), Fairbanks North Star Borough, on both benchmarks. Mon-Fri 10:00-14:00, Sat/Sun closed.
- **ESTER 1362753**, 501 Village Rd, Ester 99725, 907-479-2050: address no match in either file (retries as "Village Road" and with city Fairbanks also had no match); official map point 64.845236,-148.019716 in **Ester CDP** (GEOID 0223460), Fairbanks North Star Borough, on both benchmarks. Mon-Fri 10:00-13:00/13:30-17:30, Sat 10:00-11:00.
- **SALCHA 1439441**, 9162 Richardson Hwy, Salcha 99714, 907-488-2233: address + point **Salcha CDP** (GEOID 0266550), Fairbanks North Star Borough. Mon-Fri 12:00-18:00, Sat 10:00-14:00.
- **NENANA 1374569**, 803 Market St, Nenana 99760, 907-832-5545: address no match (retry as "Market Street" also had no match); official map point in **Nenana city**. Mon-Fri 08:30-12:00/13:00-16:00, Sat/Sun closed.
- **ANDERSON 1439370**, 260 W 1st St, Anderson 99744, 907-582-2992: address no match (retries as "W 1st Street" and "West 1st St" also had no match); official map point in **Anderson city**, Denali Borough. Mon-Fri 12:00-15:15, Sat/Sun closed.
- **CLEAR 1439385**, 202 A St Stop 1047, printed **Clear**, AK 99704, 907-582-2650: address (matched as 202 A ST, CLEAR, AK, 99704) and official map point 64.347973,-149.186777 are in **Anderson city**, Denali Borough, on both benchmarks. Printed city is Clear, not Fairbanks, and the geocode is outside Fairbanks city, so this is left off, not a Fairbanks hold. Mon-Fri 08:00-10:30, Sat/Sun closed.
- **HEALY 1366610**, 9998 Coal St, Healy 99743, 907-205-4987: address no match; official map point **Healy CDP**, Denali Borough. Mon-Fri 08:30-12:30/13:30-17:00, Sat 10:30-12:00.
- **DENALI NATIONAL PARK 1360657**, 55998 Denali Park Rd, Denali National Park 99755, 907-683-2291: address no match; official map point **Denali Park CDP**, Denali Borough. Mon-Fri 08:30-10:30/11:30-18:00, Sat 10:00-12:30.
- **CANTWELL 1356910**, 210 George Parks Hwy, Cantwell 99729, 907-768-2292: address no match; official map point **Cantwell CDP**, Denali Borough. Mon-Fri 10:30-16:00, Sat 09:30-13:00.
- **DELTA JUNCTION 1360635**, 266 Richardson Hwy, Delta Junction 99737, 907-895-4601: the address file matches 266 RICHARDSON HWY, DELTA JUNCTION, AK, 99737 in Southeast Fairbanks Census Area with no incorporated place or CDP, at 64.283215,-146.266377, well away from the official map point. Official map point 64.043064,-145.734768 is in **Delta Junction city** (GEOID 0218620) on both benchmarks. A retry as "Richardson Highway" produced the same address-file match. Left off on the official map point, which is outside Fairbanks city. Mon-Fri 09:30-17:00, Sat 10:30-12:00.
- **MANLEY HOT SPRINGS 1371664**, 100 Landing Rd, Manley Hot Springs 99756, 907-672-3577: **no money-order tags**. Address no match; official map point **Manley Hot Springs CDP**, Yukon-Koyukuk Census Area. Mon-Fri 09:00-11:30/12:30-16:00, Sat/Sun closed. Left off (other city, and no money orders).
- **MINTO 1373361**, 100 3rd St, Minto 99758, 907-798-7226: address no match; official map point **Minto CDP**. Mon-Fri 09:00-13:00/14:00-16:00, Sat/Sun closed.
- **RAMPART 1439440**, 9767 Front St, Rampart 99767, 907-358-3114: address no match; official map point **Rampart CDP**. Unusual retail hours: Tue/Thu/Sat 10:00-14:00; Mon/Wed/Fri/Sun closed.
- **CIRCLE 1358068**, 161 Steese Hwy, Circle 99733, 907-773-1220: address + point **Circle CDP**. Mon-Fri 10:00-16:00, Sat/Sun closed.
- **CENTRAL 1357498**, 128 Steese Hwy, Central 99730, 907-520-5959: address no match; official map point **Central CDP**. Mon-Fri 09:00-15:00, Sat/Sun closed. Found only at 50 miles around 99730.
- **TOK 1384764**, 1314.3 Alaska Hwy, Tok 99780, 907-883-5880: address no match (retries as "Alaska Highway" and "1314 Alaska Hwy" also had no match); official map point **Tok CDP**. Mon-Fri 08:30-17:00, Sat/Sun closed. Found via 99776 (Tanacross); 5- to 50-mile queries around official ZIP 99780 returned only Northway.
- **TANACROSS 1439449**, 1000 1st Ave, Tanacross 99776, 907-883-4496: MONEYORDERSDOM only. Address no match; official map point **Tanacross CDP**. Daily 10:30-13:30 except Sunday closed. Found with Tok via 99776.
- **NORTHWAY 1375566**, 6650 Northway Rd, Northway 99764, 907-778-2255: address + point **Northway CDP**. Mon-Fri 10:00-13:00/14:00-17:00, Sat/Sun closed.

## Fetch failures

None of the 58 + 125 locator queries failed to parse. All 23 detail pages returned HTTP 200 on the first try. Census address no-matches after street-name retries remain for Eielson AFB, Ester, Anderson, Cantwell, Central, Rampart, Nenana, Healy, Denali National Park, Manley Hot Springs, Minto, Tanacross, and Tok; each was resolved by an official map point outside Fairbanks city. Delta Junction's address file matches a no-place location in Southeast Fairbanks Census Area away from the official map point, which is in Delta Junction city; it is left off.
