# Johnstown, CO: USPS locator research (2026-11-12, America/Denver)

Research only. Nothing was built, committed, or deployed. No business was contacted. No browser was used. last_verified: 2026-11-12.

## Method

- **Locator:** official USPS Location Finder API (`https://tools.usps.com/UspsToolsRestServices/rest/POLocator/findLocations`, `requestType` po), queried with curl, the same way as Evans, Lafayette, Erie, and Fountain. First-pass searches ran at 5 and 15 miles around 80534 (Johnstown), 80543 (Milliken), 80623 (Gilcrest), 80542 (Mead), 80513 (Berthoud), 80550 and 80551 (Windsor), 80537 and 80538 (Loveland), 80631, 80632, 80634, 80633, and 80639 (Greeley), 80620 (Evans), 80520 (Firestone), 80651 (Platteville), plus confirmed nearby official ZIPs 80645 (La Salle), 80530 (Frederick), 80514 (Dacono), 80546 (Severance), 80547 (Timnath), 80621 (Fort Lupton), 80528 (Fort Collins SE), and 80501 (Longmont). That first pass returned **60 unique Post Office records**. Because 80534 at 5 miles returned only 2 offices, a spot-check of 80534 at 10 miles (9 offices) and 20 miles (31 offices) was run; neither added a new office. A second pass at 5 and 15 miles around additional official nearby ZIPs 80615 (Eaton), 80644 (Kersey), 80525 and 80521 (Fort Collins), 80516 (Erie), 80610 (Ault), 80533 (Hygiene), 80642 (Hudson), 80646 (Lucerne), 80540 (Lyons), 80624 (Gill), 80622 (Galeton), and 80544 (Niwot) added 9 farther offices. All **78** locator queries returned JSON (`sweep.out`); together they returned **69 unique Post Office records**. Raw data: `/workspace/step8jt/usps_all.json` (first pass also saved as `usps_all_pass1.json`). One-line summary: `usps_summ.txt`. Scripts: `sweep.py`, `sweep_pass2.py`.
- **Official pages:** `https://tools.usps.com/locations/details/<id>` was fetched with curl at about 3:45 PM MT for 1368496 Johnstown, 1373182 Milliken, 1364775 Gilcrest, 1372465 Mead, and 1354778 Berthoud. All five returned HTTP 200 on the first try (`http.txt`, `d<id>.html`). Hours and services come from the official locator record that these pages display. "Retail hours" means the `BUSINESS` hours block only.
- **Town limits:** all 69 records checked with the U.S. Census Geocoder address endpoint, Public_AR_Current / Current_Current, Incorporated Places, CDPs, and Counties layers (`usps_geo.jsonl`). Every official USPS locator map point was also checked against the current benchmark (`coord.jsonl`). For the one Johnstown-printed address and every current-file no-match, one-line lookups were run against the Census 2020 file and the current file (`fbr.jsonl`). Joined view: `joined.txt`.
- **Structured output:** `/workspace/step8jt/johnstown_usps_records.csv` / `.json` cover all 69 records (same fields as Evans and Lafayette). Built by `build.py`.

## Candidate include (1)

| Office | Address | Phone | Services | Retail hours | Geocoder |
|---|---|---|---|---|---|
| Johnstown (1368496) | 121 Castle Pines Ave, Johnstown 80534 | 970-587-4246 | Money orders, Domestic and Inquiry (MONEYORDERSDOM, MONEYORDERSINQ) | Mon-Fri 08:30-13:00 and 14:00-16:30, Sat 09:30-12:00, Sun closed | Current file: 121 CASTLE PINES AVE, JOHNSTOWN, CO, 80534, **Johnstown town**, Weld County. The 2020 file agrees (Johnstown town), and so does the official locator point (40.3327, -104.906784 → Johnstown town, Weld County). |

- URL: https://tools.usps.com/locations/details/1368496 (HTTP 200). verification_status: verified_official_locator.
- Open Saturdays. Weekday retail closes at **16:30**, so `open_after_1700_weekday` = false: **not** open evenings (a close at 17:00 is also not evenings; evenings require a close after 17:00). The weekday retail block has a lunch break (closed 13:00-14:00). Window service hours match retail hours. Lobby and PO box access are listed 00:01-23:59 daily (not retail). Last collection Mon-Fri 16:30, Sat 12:00.
- The record also lists passport services (appointment required; appointments/photos Mon-Fri 09:00-12:00 and 14:00-16:00; walk-in Tue, Wed, and Thu 12:00-13:00), PO boxes, general delivery, burial flags, duck stamps, greeting cards, hold-mail/notice-left pickup, and bulk mail (Mon-Fri 09:00-11:30 and 14:15-16:00). None of those is a Check Desk tracked service unless the site tracks passports.
- Fax 970-587-0140 (not used). Parking: lot. No site comment in the record.
- No duplicate, SDC, or carrier-annex record at or near 121 Castle Pines Ave in the locator results. This is the only Johnstown-printed retail office in the sweep.

## Holds

- **None.** The only Johnstown-printed record geocodes inside Johnstown town. No record printed with another city falls inside Johnstown town, either by address geocode or by locator map point. No Milliken, Mead, Gilcrest, Berthoud, Windsor, Loveland, Greeley, Evans, Firestone, Platteville, or unincorporated-Weld/Larimer record lands in Johnstown.

## Left out (not holds)

Printed with another city, and both the address geocode (where matched) and the locator point agree it is outside Johnstown. Nearest/most relevant:

- **Milliken (1373182)**, 1009 Broad St, Milliken 80543, 970-587-3332: Milliken town (address + point). The only other office in the 80534 5-mile search; a close miss, not a hold. Money orders; Mon-Fri 07:30-12:00 and 13:00-16:30, Sat 09:00-11:00. HTTP 200.
- **Gilcrest (1364775)**, 301 Main St, Gilcrest 80623, 970-737-2934: Gilcrest town (address + point). Money orders; Mon-Fri 09:30-12:30 and 13:30-16:30, Sat 09:00-11:00. HTTP 200.
- **Mead (1372465)**, 350 Welker Ave, Mead 80542, 970-535-4612: Mead town (address + point). Money orders; Mon-Fri 08:00-12:00 and 13:00-16:30, Sat 08:00-10:00. HTTP 200.
- **Berthoud (1354778)**, 425 3rd St, Berthoud 80513, 970-532-5379: Berthoud town (address + point). Money orders; Mon-Fri 08:00-16:30, Sat 09:30-12:30. HTTP 200.
- **Windsor (1387952)**, 215 6th St, Windsor 80550, 970-833-3010: Windsor town (address + point). Money orders; Mon-Fri 08:30-17:00, Sat 09:00-12:00.
- **WIN Carrier Annex (1560051)**, 1070 Diamond Valley Dr Ste 500, Windsor 80550: Windsor town. No retail hours and no money orders (carrier/delivery unit). Left out, not a hold.
- **Evans (1362838)**, 3344 11th Ave, Evans 80620, 970-339-8293: Evans city (address + point). Money orders; Mon-Fri 08:00-17:00, Sat 09:00-12:00.
- **Downtown Greeley (1365513)**, 925 11th Ave, Greeley 80631, 970-392-2782: Greeley city (address + point). Money orders; Mon-Fri 07:30-17:30, Sat 09:00-13:00.
- **Greeley (1365514)**, 930 39th Ave, Greeley 80634, 970-392-0298: Greeley city (address + point). Money orders; Mon-Fri 07:30-17:30, Sat 09:00-13:00.
- **Loveland (1371037)**, 446 E 29th St, Loveland 80538, 970-663-3010: Loveland city (address + point). Money orders; Mon-Fri 08:30-17:30, Sat 09:00-13:00.
- **Valentine (1371038)**, 601 Cleveland Ave, Loveland 80537, 970-667-5303: Loveland city (address + point). Money orders; Mon-Fri 09:00-16:30, Sat 09:00-12:00.
- **Platteville (1377758)**, 400 Marion St, Platteville 80651, 970-785-2295: Platteville town (address + point). Money orders; Mon-Fri 07:30-16:30, Sat 08:00-11:00.
- **Firestone (1363406)**, 478 1st St, Firestone 80520: Firestone town (address + point). Money orders; outside Johnstown.
- La Salle (1369426, La Salle town), Timnath (1384692, Timnath town), Frederick (1364064, Frederick town), Dacono (1360137, Dacono city), Fort Lupton (1363805), Longmont (1370889), Eaton (1361975), Kersey (1368942): all outside Johnstown.
- Lucerne (1371125; address no match on current or 2020, point in no place = unincorporated Weld), Gill (1364780, unincorporated Weld), Galeton (1439603, unincorporated Weld): all outside Johnstown.
- Farther records (Severance, Ault, Pierce, Nunn, Wellington, Fort Collins + Fort Collins CO SDC duplicate at 301 Boardwalk Dr, Old Town, Erie, Erie Carrier Annex, Lyons, Hygiene, Niwot, Masonville, Drake, Laporte, Bellvue, Brighton, Brighton Carrier Annex, Lafayette, Lafayette Carrier Annex, Eastlake, Henderson, Hudson, Keenesburg, Northglenn, Northview, Broomfield, Broomfield Eagle View, Westminster, Harris Park, Louisville printed Superior, Boulder, Valmont, Boulder CO SDC, High Mar, Indian Tree, Eldorado Springs, Dupont, North Pecos, Jamestown, Allenspark, Estes Park, Briggsdale): outside Johnstown; see CSV.
- Carrier annexes in the sweep (WIN 1560051, Erie 1546616, Brighton 1555032, Lafayette 1369484) have no retail hours and no money orders, and none is in Johnstown. Northview (1375562, Northglenn city) also has no retail hours and no money orders.
- Shared-building pairs in the sweep, neither in Johnstown: Fort Collins 1363754 / Fort Collins CO SDC 1601572 (301 Boardwalk Dr, Fort Collins); Valmont 1385692 / Boulder CO SDC 1612987 (2995 55th St, Boulder; the SDC record has no money orders).
- Minor geocoder notes (not Johnstown-relevant): Severance 320 1st St address geocodes to Eaton town while its locator point is in Severance town. Louisville 1371024 is printed Superior and geocodes to Louisville city. Current-file address no-matches (10 of 69: Lucerne, Hygiene, Masonville, Drake, Brighton Carrier Annex, Eastlake, Westminster, Broomfield Eagle View, Eldorado Springs, Briggsdale) were resolved by locator map point, all far from Johnstown; the 2020 file additionally matched Drake in unincorporated Larimer County and Westminster in Westminster city.

## Fetch failures

- None. All 78 locator queries returned JSON; all 5 detail pages returned HTTP 200 on the first try. Census geocoder: 59/69 current-file address matches; the 10 no-matches were resolved by locator map point (and, where the 2020 file matched, by that file), all far from Johnstown.
