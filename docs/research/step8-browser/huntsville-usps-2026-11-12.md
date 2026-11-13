# Huntsville, AL: USPS locator research (2026-11-12, America/Denver)

Research only. Nothing was built, committed, or deployed. No business was contacted. No browser was used. No other Alabama city was started. last_verified: 2026-11-12. Official detail pages that were fetched are marked verification_status `verified_official_locator`. City-limits wording: Huntsville is a **city** (Census "Huntsville city", Madison County for every row below).

## Method

- **Locator:** official USPS Location Finder API (`https://tools.usps.com/UspsToolsRestServices/rest/POLocator/findLocations`, `requestType` po), queried with curl the same way as the Colorado cities. Pass 1 (`sweep.py`): 5 and 15 miles around every Huntsville ZIP (35801-35808, 35810-35816, 35824, 35893, 35896-35899) and nearby official ZIPs 35756/35757/35758 (Madison), 35749 (Harvest), 35759 (Meridianville), 35763 (Owens Cross Roads), 35760 (New Hope), 35741 (Brownsboro), 35748 (Gurley), 35761 (New Market), 35773 (Toney), 35750 (Hazel Green), 35611/35613 (Athens), 35670 (Somerville). 72 queries, all JSON, **51 unique Post Office records**. Pass 2 (`sweep2.py`): 1, 2, 3, 10, and 20 miles around 12 Huntsville/edge ZIPs; added only 1 farther record (Arab 1353217). Total **52 records** (`usps_all.json`, `usps_summ.txt`). Note: when nothing lies inside a very small radius the API returns a default ~26-30 nearest list, so some 1-2 mile queries show large counts; that only widens coverage.
- **Official pages:** `https://tools.usps.com/locations/details/<id>` fetched with curl about 8:41-8:42 PM MT for all 9 Huntsville-printed records, Normal, and the 11 nearest other-city offices (21 pages). All returned **HTTP 200 on the first try** (`http.txt`, `d<id>.html`). Each page embeds the official `poDetail` record; `pages.py` parsed it and confirmed name, address, phone, and BUSINESS hours match the API record for all 21 (`pages.json`). "Retail hours" = the `BUSINESS` block only (not lobby, PO Box, pickup, or holiday).
- **City limits:** all 52 addresses through the Census Geocoder address endpoint, Public_AR_Current / Current_Current, Incorporated Places + CDPs + Counties (`usps_geo.jsonl`). Every official locator map point checked against the current benchmark (`coord.jsonl`). One-line lookups against both the Census 2020 file and the current file for every Huntsville-printed address plus Normal and Redstone Arsenal (`fbr.jsonl`). 2020-benchmark point checks for Redstone Arsenal, Normal, Haysland, and Wall Triana (`coord2020.jsonl`). Joined view: `joined.txt`. Structured output: `/workspace/step8hsv/huntsville_usps_records.csv` / `.json` (52 rows, `build.py`).

## Candidate includes (6), all money orders yes (MONEYORDERSDOM, MONEYORDERSINQ), all HTTP 200, verified_official_locator

| ID | Office | Address | Phone | Retail (BUSINESS) hours | Evenings | Weekends | Geocode |
|---|---|---|---|---|---|---|---|
| 1361171 | DOWNTOWN HUNTSVILLE | 615 Clinton Ave W, Huntsville, AL 35801 | 256-532-0391 | Mon-Fri 08:30-17:00; Sat/Sun closed | no | no | Current + 2020 address: Huntsville city; point 34.726786,-86.593801 Huntsville city |
| 1387203 | WEST | 3605 Governors Dr SW, Huntsville, AL 35805 | 256-534-6459 | Mon-Fri 08:30-17:00; Sat 09:00-12:00; Sun closed | no | yes | Current + 2020 address: Huntsville city; point 34.719744,-86.616236 Huntsville city |
| 1372120 | MASTIN LAKE | 2501 Mastin Lake Rd NW, Huntsville, AL 35810 | 256-852-7094 | Mon-Fri 09:00-17:00; Sat 10:00-12:00; Sun closed | no | yes | Current + 2020 address: Huntsville city; point 34.771558,-86.59622 Huntsville city |
| 1388386 | WYNN DRIVE | 645 Wynn Dr NW, Huntsville, AL 35816 | 256-722-4749 | Mon-Fri 08:30-**18:00**; Sat 10:00-14:00; Sun closed | **yes** (closes 18:00) | yes | Current + 2020 address: Huntsville city; point 34.74001,-86.65364 Huntsville city |
| 1366562 | HAYSLAND | 8401 Whitesburg Dr SE, Huntsville, AL 35802 | 256-882-7413 | Mon-Fri 08:30-17:00; Sat 09:00-12:00; Sun closed | no | yes | See note: address matched as "8401 WHITESBURG WAY" (Huntsville city) in both files; point 34.655045,-86.565484 Huntsville city (current and 2020) |
| 1367688 | HUNTSVILLE | 3408 Wall Triana Hwy, Huntsville, AL 35813 | 256-461-6630 | Mon-Fri 08:30-17:00; Sat/Sun closed | no | no | Current address: Huntsville city (2020 file matched same street with ZIP 35824, Huntsville city); point 34.667511,-86.7535159 Huntsville city (current and 2020) |

URLs: https://tools.usps.com/locations/details/1361171, /1387203, /1372120, /1388386, /1366562, /1367688.

Notes:
- **Haysland:** the Census address match normalized the street to "Whitesburg Way" rather than the official "Whitesburg Dr SE" (0.38 km from the USPS point). Because the street name differs, treat the inclusion basis as the official USPS map point (Huntsville city on both the current and 2020 benchmarks) with the address match as supporting evidence. No disagreement with the printed city, so it's not a hold. Pax may choose to hold it if a strict street-exact match is required.
- **Wall Triana (1367688)** shares 3408 Wall Triana Hwy with two non-retail records (1449999, 1472078; see omissions). Use 1367688 only.
- Only Wynn Drive is open evenings (weekday close 18:00). All others close 17:00 or earlier = not evenings. Weekends = Saturday only, at West, Mastin Lake, Wynn Drive, Haysland. No Sunday retail.
- Wynn Drive's official record also lists passport services; not in Check Desk scope, so not used.

## HOLDS (2)

1. **REDSTONE ARSENAL (1437778)**, 3710 Aerobee Rd, printed **Huntsville**, AL 35808, 256-650-1153. https://tools.usps.com/locations/details/1437778 (HTTP 200). Money orders yes; BUSINESS Mon-Fri 09:30-13:30 and 14:30-16:30, Sat/Sun closed. **Disagreement:** official printed city is Huntsville, but the address has **no match** in the current or 2020 Census address file (also no match with "Redstone Arsenal" as the city), and the official USPS map point (34.67864,-86.625659) falls in **Redstone Arsenal CDP** (no incorporated place) on both the current and 2020 benchmarks. Held, not listed in Huntsville. (It's also on a military installation, which may restrict public access. The record's site comment says only "VOICE AND DATA SUBORDINATE TO WEST STATION(35805).")
2. **NORMAL (1375204)**, 100 Drake Dr, printed **Normal**, AL 35762, 256-852-4000. https://tools.usps.com/locations/details/1375204 (HTTP 200). Money orders yes; BUSINESS Mon-Fri 08:00-11:30 and 12:30-16:30, Sat/Sun closed. **Disagreement:** official printed city is Normal (not Huntsville), but the official USPS map point (34.783609,-86.571544) falls in **Huntsville city** on both the current and 2020 benchmarks. The address has no match in either Census address file. Held: not listed in Huntsville, and Normal is not a Check Desk city.

## Left off (omissions, not holds)

- **HUNTSVILLE 1449999**, 3408 Wall Triana Hwy, Huntsville 35813, 256-772-4691 (HTTP 200): no BUSINESS (retail) hours, no money orders. Only lobby, PO Box access, last collection, and pickup/hold-mail/call-referral blocks. Same address as retail office 1367688; Huntsville city by address and point.
- **HUNTSVILLE 1472078**, 3408 Wall Triana Hwy, Huntsville 35813, 256-772-4691 (HTTP 200): no service-hours blocks at all and no services listed; no retail hours, no money orders. Same address as 1367688.
- No carrier annex or plant records with a Huntsville print appeared under `requestType` po other than these two.

### Nearby other-city offices (left off; printed city ≠ Huntsville and the geocoder agrees outside Huntsville city)

All have money orders and retail hours. All pages were HTTP 200 unless marked "API only".
- **MADISON 1371387**, 56 Hughes Rd, Madison 35758, 256-772-7413: address + point **Madison city**. Mon-Fri 08:30-18:00, Sat 09:30-16:00.
- **HARVEST 1366415**, 9157 Wall Triana Hwy, Harvest 35749: address + point **Harvest CDP**. Mon-Fri 08:00-11:30/12:30-16:00, Sat 08:30-10:30.
- **MERIDIANVILLE 1372765**, 11639 Highway 231 431 N, Meridianville 35759: address + point **Meridianville CDP**.
- **OWENS CROSS ROADS 1376485**, 8396 Highway 431 S, Owens Cross Roads 35763: address no match; point **Owens Cross Roads city**.
- **NEW HOPE 1374753**, 5464 Main Dr, New Hope 35760: address + point **New Hope city**.
- **BROWNSBORO 1356084**, 121 Brownsboro Rd, Brownsboro 35741: address matched, no place or CDP; point also none (unincorporated Madison County).
- **GURLEY 1365869**, 6051 Highway 72 E, Gurley 35748: **Gurley town** (address + point).
- **RYLAND 1380190**, 370 Ryland Pike, Ryland 35767: address no match; point in no place or CDP (unincorporated).
- **CAPSHAW 1356969**, 1108 Old Railroad Bed Rd, Capshaw 35742: address no match; point in no place or CDP.
- **HAZEL GREEN 1366577**: Hazel Green CDP. **TONEY 1384808**: no place or CDP. **NEW MARKET 1374795** (API only): New Market CDP.
- Farther (API only, outside Huntsville city by address and/or point; see CSV): Laceys Spring, Valhermoso Springs, Belle Mina, Mooresville, Tanner, Decatur, Somerville, Athens, Ardmore TN, Elkmont, Taft TN, Woodville, Grant, Union Grove, Guntersville, Princeton, Paint Rock, Elora TN, Flintville TN, Huntland TN, Elkton TN, Kelso TN, Fayetteville TN, Hillsboro, Trinity, Prospect TN, Eva, Hartselle, Falkville, Arab.
- No other-city-printed office besides Normal has an address match or map point inside Huntsville city.

## Fetch failures

None. All 72 + 60 locator queries returned JSON. All 21 detail pages returned HTTP 200 on the first try. Census address no-matches (current file): Normal, Redstone Arsenal, Ryland, Owens Cross Roads, Capshaw, Valhermoso Springs, Decatur, and Eva. Each was resolved by the official map point.
