# Evans, CO: USPS locator research (2026-11-12, America/Denver)

Research only. Nothing was built, committed, or deployed. No business was contacted. No browser was used. last_verified: 2026-11-12.

## Method

- **Locator:** official USPS Location Finder API (`https://tools.usps.com/UspsToolsRestServices/rest/POLocator/findLocations`, `requestType` po), queried with curl, the same way as Lafayette, Erie, and Fountain. Searches ran at 5 and 15 miles around 80620 (Evans), 80631, 80632, 80634, 80639 (Greeley/UNC), 80645 (La Salle), 80643 (Keenesburg), 80534 (Johnstown), 80621 (Fort Lupton), 80615 (Eaton), 80633 (Greeley PO boxes), 80610 (Ault), 80650 (Pierce), 80644 (Kersey), and 80651 (Platteville). All 30 queries returned JSON (`sweep.out`); together they returned **40 unique Post Office records**. Raw data: `/workspace/step8ev/usps_all.json`. One-line summary: `usps_summ.txt`. Script: `sweep.py`.
- **Official pages:** `https://tools.usps.com/locations/details/<id>` was fetched with curl at about 3:40 PM MT for 1362838 Evans, 1369426 La Salle, 1365513 Downtown Greeley, and 1365514 Greeley. All four returned HTTP 200 on the first try (`http.txt`, `d<id>.html`). Hours and services come from the official locator record that these pages display. "Retail hours" means the `BUSINESS` hours block only.
- **City limits:** all 40 records checked with the U.S. Census Geocoder address endpoint, Public_AR_Current / Current_Current, Incorporated Places, CDPs, and Counties layers (`usps_geo.jsonl`). Every official USPS locator map point was also checked against the current benchmark (`coord.jsonl`). For the one Evans-printed address, one-line lookups were run against the Census 2020 file and the current file (`fbr.jsonl`). Joined view: `joined.txt`.
- **Structured output:** `/workspace/step8ev/evans_usps_records.csv` / `.json` cover all 40 records (same fields as Lafayette). Built by `build.py`.

## Candidate include (1)

| Office | Address | Phone | Services | Retail hours | Geocoder |
|---|---|---|---|---|---|
| Evans (1362838) | 3344 11th Ave, Evans 80620 | 970-339-8293 | Money orders, Domestic and Inquiry (MONEYORDERSDOM, MONEYORDERSINQ) | Mon-Fri 08:00-17:00, Sat 09:00-12:00, Sun closed | Current file: 3344 11TH AVE, EVANS, CO, 80620, **Evans city**, Weld County. The 2020 file agrees (Evans city), and so does the official locator point (40.381418, -104.69635 → Evans city, Weld County). |

- URL: https://tools.usps.com/locations/details/1362838 (HTTP 200). verification_status: verified_official_locator.
- Open Saturdays. Weekday retail closes at **17:00**, so `open_after_1700_weekday` = false: **not** open evenings (same as Erie, Windsor, Lafayette). Window service hours match retail hours. Lobby and PO box access are listed 00:01-23:59 daily (not retail). Last collection Mon-Fri 17:00, Sat 15:30.
- The record also lists passport services (appointment required; appointments/photos Mon-Fri 10:00-15:00; walk-in Tue and Thu 13:30-15:00), PO boxes, general delivery, burial flags, duck stamps, greeting cards, hold-mail/notice-left pickup, and bulk mail (Mon-Fri 09:00-15:00). None of those is a Check Desk tracked service unless the site tracks passports.
- Fax 970-330-8190 (not used). Parking: lot. No site comment in the record.
- No duplicate, SDC, or carrier-annex record at or near 3344 11th Ave in the locator results.

## Holds

- **None.** The only Evans-printed record geocodes inside Evans city. No record printed with another city falls inside Evans city, either by address geocode or by locator map point. No Greeley, La Salle, Garden City, or unincorporated-Weld record lands in Evans.

## Left out (not holds)

Printed with another city, and both the address geocode (where matched) and the locator point agree it is outside Evans. Nearest/most relevant:

- **Downtown Greeley (1365513)**, 925 11th Ave, Greeley 80631, 970-392-2782: Greeley city (address + point). Money orders; Mon-Fri 07:30-17:30, Sat 09:00-13:00. HTTP 200.
- **Greeley (1365514)**, 930 39th Ave, Greeley 80634, 970-392-0298: Greeley city (address + point). Money orders; Mon-Fri 07:30-17:30, Sat 09:00-13:00. HTTP 200.
- **La Salle (1369426)**, 524 N 2nd St, La Salle 80645, 970-284-6569: La Salle town (address + point). Money orders; Mon-Fri 08:00-16:30, Sat 09:00-12:00. HTTP 200.
- Kersey (1368942, Kersey town), Gilcrest (1364775, Gilcrest town), Milliken (1373182, Milliken town), Johnstown (1368496, Johnstown town), Platteville (1377758), Eaton (1361975), Lucerne (1371125; address no match, point in no place = unincorporated Weld), Gill (1364780, unincorporated), Galeton (1439603, unincorporated): all outside Evans.
- Farther records (Windsor, Win Carrier Annex, Severance, Ault, Pierce, Nunn, Wellington, Timnath, Loveland, Valentine, Berthoud, Mead, Fort Collins + Fort Collins CO SDC duplicate at 301 Boardwalk Dr, Fort Lupton, Dacono, Frederick, Firestone, Erie, Erie Carrier Annex, Brighton, Brighton Carrier Annex, Henderson, Eastlake, Hudson, Keenesburg, Roggen): outside Evans; see CSV.
- Carrier annexes in the sweep (Win 1560051, Brighton 1555032, Erie 1546616) have no retail hours and no money orders, and none is in Evans.
- Only shared-building pair in the sweep: Fort Collins 1363754 / Fort Collins CO SDC 1601572 (301 Boardwalk Dr, Fort Collins). Not relevant to Evans.
- Minor geocoder note (not Evans-relevant): Severance 320 1st St address geocodes to Eaton town while its locator point is in Severance town.

## Fetch failures

- None. All 30 locator queries returned JSON; all 4 detail pages returned HTTP 200 on the first try. Census geocoder: 37/40 current-file address matches; 3 no-match (Lucerne, Brighton Carrier Annex, Eastlake) were resolved by locator map point, all far from Evans.
