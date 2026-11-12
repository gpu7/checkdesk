# Lafayette, CO: USPS locator research (2026-11-12, America/Denver)

Research only. Nothing was built, committed, or deployed. No business was contacted. No browser was used. last_verified: 2026-11-12.

## Method

- **Locator:** official USPS Location Finder API (`https://tools.usps.com/UspsToolsRestServices/rest/POLocator/findLocations`, `requestType` po), queried with curl, the same way as Northglenn, Erie, Windsor, and Brighton. Searches ran at 5 and 15 miles around 80026 (Lafayette), 80027 (Louisville/Superior), 80023, 80020, 80021 (Broomfield), 80516 (Erie), 80301, 80303 (Boulder), 80031 (Westminster), 80025 (Eldorado Springs), 80544 (Niwot), and 80514 (Dacono). Together they returned **71 unique Post Office records**. All 24 queries returned JSON (`sweep.out`). Raw data: `/workspace/step8lf/usps_all.json`. One-line summary: `usps_summ.txt`. Script: `sweep.py`.
- **Official pages:** `https://tools.usps.com/locations/details/<id>` was fetched with curl at about 3:37 PM MT. 1369494 Lafayette returned HTTP 200, and so did 1369484 Lafayette Carrier Annex. Both loaded on the first try (`http.txt`, `d1369494.html`, `d1369484.html`). Hours and services come from the official locator record that these pages display. "Retail hours" means the `BUSINESS` hours block only.
- **City limits:** I checked all 71 records with the U.S. Census Geocoder address endpoint, Public_AR_Current / Current_Current, using the Incorporated Places, CDPs, and Counties layers (`usps_geo.jsonl`). I also checked every official USPS locator map point against the current benchmark (`coord.jsonl`). For both Lafayette-printed addresses, I ran one-line lookups against the Census 2020 file and the current file (`fbr.jsonl`). Joined view: `joined.txt` (`joined.py`).
- **Structured output:** `/workspace/step8lf/lafayette_usps_records.csv` / `.json` cover all 71 records (same fields as Northglenn). Built by `build.py`.

## Candidate include (1)

| Office | Address | Phone | Services | Retail hours | Geocoder |
|---|---|---|---|---|---|
| Lafayette (1369494) | 603 S Public Rd, Lafayette 80026 | 303-926-1044 | Money orders, Domestic and Inquiry (MONEYORDERSDOM, MONEYORDERSINQ) | Mon-Fri 09:00-17:00, Sat 10:00-13:00, Sun closed | Current file: 603 S PUBLIC RD, LAFAYETTE, CO, 80026, **Lafayette city**, Boulder County. The 2020 file agrees (Lafayette city), and so does the official locator point (39.993195, -105.090898 → Lafayette city, Boulder County). |

- URL: https://tools.usps.com/locations/details/1369494 (HTTP 200). verification_status: verified_official_locator.
- It is open Saturdays. Weekday retail closes at **17:00**, so `open_after_1700_weekday` = false: **not** open evenings (same as Erie and Windsor). Window service hours match retail hours. Lobby and PO box access are Mon-Sat 07:00-18:00 (not retail). The self-service kiosk (APC) is listed 00:01-23:59 daily (not retail). Last collection 17:30 Mon-Sat.
- The record also lists passport services (appointment required; appointments/photos Mon-Fri 10:00-16:00, Sat 10:30-12:30; walk-in Tue-Thu 10:30-11:30), PO boxes, gift cards, duck stamps, burial flags, general delivery, and bulk mail (Mon-Fri 09:30-13:30). None of those is a Check Desk tracked service unless the site tracks passports.
- The locator record has fax 303-665-1325 (not used). Site comment: "BOULDER TURNPIKE WEST, THEN NORTH ON 287, RIGHT ON S. PUBLIC RD." Parking: lot.
- No duplicate or SDC record at 603 S Public Rd. The Carrier Annex (below) is a separate record at a different street address (109 Kimbark St), about 70 m away by locator points; its record says "MAIN OFFICE AT 603 SOUTH PUBLIC ROAD."

## Holds

- **None.** No Lafayette-printed record geocodes outside Lafayette city. No record printed with another city falls inside Lafayette city, either by address geocode or by locator map point.

## Left out (not holds)

- **Lafayette Carrier Annex (1369484)**, 109 Kimbark St, Lafayette 80026, 303-664-1241. A carrier/delivery unit: services are CARRIER, DELIVERYUNIT, CONNECTLOCAL, CALLREFERRAL, and the PICKUP* (hold mail / notice left / accountable) codes. **No BUSINESS (retail) hours block and no money orders**. Its hours blocks (Mon-Fri 09:00-17:00, Sat 10:00-13:00) cover only call referral and pickup. Site comment: "MAIN OFFICE AT 603 SOUTH PUBLIC ROAD. THIS FACILITY IS A CARRIER ANNEX." The current and 2020 files both match 109 KIMBARK ST, LAFAYETTE in Lafayette city, and so does the locator point (39.992675, -105.091398). Inside the city but left out because it has no retail and no tracked service, like the Erie Carrier Annex and Northview. Page HTTP 200.
- Nearby offices printed with other cities, where the geocoder agrees they are outside Lafayette. All list money orders unless noted:
  - Louisville 1371024, 566 S McCaslin Blvd, printed Superior 80027 (Louisville city; retail Mon-Fri to 17:30).
  - Erie 1362695, 150 Wells St (Erie town). Erie Carrier Annex 1546616, 621 Mitchell Way (Erie town; no retail, no money orders).
  - Broomfield 1356062 (Broomfield city). Broomfield Eagle View 1361605: no current-file match; locator point in Broomfield city.
  - Boulder 1355494, High Mar 1366905, Valmont 1385692 (Boulder city). Valmont and Boulder CO SDC 1612987 share 2995 55th St; the SDC lists no money orders.
  - Niwot 1375136 (Niwot CDP, unincorporated Boulder County). Dacono 1360137 (Dacono city). Westminster 1439640: no current-file match; locator point in Westminster city.
  - Farther out in the 15-mile sweeps: Northglenn, Northview (no retail/no MO), Eastlake, Frederick, Firestone, Longmont, Mead, Lyons, Hygiene, Berthoud, Platteville, Fort Lupton, Henderson, Brighton, Brighton Carrier Annex (no retail/no MO), Commerce City, Adams City, Dupont, Arvada, Indian Tree, Harris Park, North Pecos, Wheat Ridge, Edgewater, Golden and Golden CO S&DC (share 1100 Johnson Rd; neither lists money orders), Downtown Golden, Lakewood and Lakewood CO SDC (share 10799 W Alameda Ave; SDC no money orders; no address match, locator point in Lakewood city), Eldorado Springs, Jamestown, Ward, Nederland, Rollinsville, Pinecliffe, Black Hawk, many Denver offices (Capitol Hill Annex has no retail/no MO), Aurora offices (Fletcher, Hoffman Heights), Glendale, and Downtown Englewood.
- USPS contract postal units and Approved Postal Providers were not collected, the same as for earlier cities.

## Fetch failures

- None. All 24 locator API queries returned JSON, and both detail pages returned HTTP 200 on the first try. Ten records had no current-file address match: Broomfield Eagle View, Westminster, Eastlake, Eldorado Springs, Hygiene, Brighton Carrier Annex, Lakewood, Lakewood CO SDC, Nederland, and Black Hawk. Their official locator points all fall outside Lafayette city. (Process note: a first sweep run had a script bug that iterated ZIP characters; it was fixed and fully rerun; the files reflect the rerun only.)
