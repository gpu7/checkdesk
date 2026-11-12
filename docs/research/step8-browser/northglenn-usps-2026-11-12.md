# Northglenn, CO: USPS locator research (2026-11-12, America/Denver)

Research only. Nothing was built, committed, or deployed. No business was contacted. No browser was used. last_verified: 2026-11-12.

## Method

- **Locator:** official USPS Location Finder API (`https://tools.usps.com/UspsToolsRestServices/rest/POLocator/findLocations`, `requestType` po), queried with curl, the same way as Erie, Windsor, and Brighton. Searches ran at 5 and 15 miles around 80233 and 80234 (Northglenn), 80241, 80229, 80602 (Thornton), 80260 (Federal Heights), 80221 (Denver/Sherrelwood), 80031 and 80030 (Westminster), 80035 (Westminster), 80022 (Commerce City), 80023 and 80020 (Broomfield), and 80216 (Denver). Together they returned **71 unique Post Office records**. All 28 queries returned JSON (`sweep.out`). Raw data: `/workspace/step8ng/usps_all.json`. One-line summary: `usps_summ.txt`. Script: `sweep.py`.
- **Official pages:** `https://tools.usps.com/locations/details/<id>` was fetched with curl at about 3:31 PM MT. 1439617 Northglenn returned HTTP 200, and so did 1375562 Northview. Both loaded on the first try (`http.txt`, `d1439617.html`, `d1375562.html`). Hours and services come from the official locator record that these pages display. "Retail hours" means the `BUSINESS` hours block only.
- **City limits:** I checked all 71 records with the U.S. Census Geocoder address endpoint, Public_AR_Current / Current_Current, using the Incorporated Places, CDPs, and Counties layers (`usps_geo.jsonl`). I also checked every official USPS locator map point against the current benchmark (`coord.jsonl`). For both Northglenn-printed addresses, I ran one-line lookups against the Census 2020 file and the current file (`fbr.jsonl`). Joined view: `joined.txt`.
- **Structured output:** `/workspace/step8ng/northglenn_usps_records.csv` / `.json` cover all 71 records. Fields: ID, name, address, phone, URL, retail hours, money orders, HTTP status, geocode, map-point place, classification, and shared-building IDs. Built by `build.py`.

## Candidate include (1)

| Office | Address | Phone | Services | Retail hours | Geocoder |
|---|---|---|---|---|---|
| Northglenn (1439617) | 11887 Washington St, Northglenn 80233 | 303-452-2316 | Money orders, Domestic and Inquiry (MONEYORDERSDOM, MONEYORDERSINQ) | Mon-Fri 08:30-18:00, Sat 09:30-12:30, Sun closed | Current file: 11887 WASHINGTON ST, NORTHGLENN, CO, 80233, **Northglenn city**, Adams County. The 2020 file agrees (Northglenn city), and so does the official locator point (39.91231, -104.978533 → Northglenn city, Adams County). |

- URL: https://tools.usps.com/locations/details/1439617 (HTTP 200). verification_status: verified_official_locator.
- It is open Saturdays. Weekday retail closes at **18:00**, so `open_after_1700_weekday` = true, unlike Erie, Windsor, and Brighton. Whether it also counts as "Open evenings" / `after_hours` should follow the same rule the site uses for other 18:00 closers. Window service hours match retail hours. The lobby, PO box access, and the self-service kiosk (APC) are listed 00:01-23:59 daily. None of those is retail.
- The record also lists a self-service kiosk, PO boxes, gift cards, duck stamps, and bulk mail. None of those is a Check Desk tracked service. No passport service is listed.
- The locator record has fax 303-254-8013 (not used).
- No duplicate or SDC record at 11887 Washington St.

## Holds

- **None.** No Northglenn-printed record geocodes outside Northglenn city. No record printed with another city falls inside Northglenn city, either by address geocode or by locator map point.

## Left out (not holds)

- **Northview (1375562)**, 850 W 112th Ave, Northglenn 80234, 303-457-6991. This is a carrier/delivery unit: its services are CARRIER, DELIVERYUNIT, CALLREFERRAL, and the PICKUP* (hold mail / notice left / accountable) codes. It has **no BUSINESS (retail) hours block and no money orders**. Its hours blocks (Mon-Fri 07:00-17:00, Sat 07:00-16:15) cover only lobby, PO box access, pickup, and call referral, and last collection is 17:30. The current and 2020 files both match 850 W 112TH AVE, NORTHGLENN, in Northglenn city (Adams County), and so does the locator point (39.899381, -104.99803). It is inside the city but left out because it has no retail and no tracked service, the same as the Erie Carrier Annex. Page HTTP 200. It does not share a building with the Northglenn Post Office.
- Nearby offices printed with other cities, where the geocoder agrees they are outside Northglenn. All list money orders unless noted:
  - Eastlake 1361915, 12470 York St, printed "Eastlake" 80614. No current-file match; the locator point is in Thornton city. No office is printed Thornton or Federal Heights.
  - Westminster 1439640, 3051 W 105th Ave. No current-file match; the locator point is in Westminster city. Harris Park 1366303 (Westminster city).
  - North Pecos 1375398, 1411 Cortez St, printed Denver 80221 (Sherrelwood CDP, unincorporated Adams County).
  - Broomfield 1356062 (Broomfield city). Broomfield Eagle View 1361605: no address match; the locator point is in Broomfield city.
  - Commerce City 1358845 and Adams City 1439552 (Commerce City city). Dupont 1361498, printed Commerce City (Derby CDP). Henderson 1366713 (unincorporated Adams County).
  - Brighton 1355853 (Brighton city). Brighton Carrier Annex 1555032 has no retail and no money orders; no address match, locator point in Brighton city.
  - Arvada and Indian Tree (Arvada city). Erie 1362695 (Erie town); Erie Carrier Annex 1546616 has no retail and no money orders. Lafayette 1369494 (Lafayette city); Lafayette Carrier Annex 1369484 has no retail and no money orders. Louisville 1371024, printed Superior (Louisville city). Dacono, Frederick, Firestone, Fort Lupton (each its own municipality).
  - Far edge of the 15-mile sweeps: many Denver offices (Stockyards, GMF Finance, Sunnyside, Park Hill, Montbello, Alcott, Denver main, Capitol Hill, Mile High, Montclair, Cherry Creek, South Denver, Westwood, University Park, Wellshire, Bear Valley, Sullivan, Glendale). Capitol Hill Annex 1356950 has no retail and no money orders. Also Aurora offices; Aurora 1353711 and Aurora CO SDC 1613885 share 16890 E Alameda Pkwy, and the SDC lists no money orders. Also Wheat Ridge, Edgewater, Golden, and Downtown Golden; Golden 1365086 and Golden CO S&DC 1578795 share 1100 Johnson Rd, and neither lists money orders. Also Lakewood 1439615 and Lakewood CO SDC 1612989, which share 10799 W Alameda Ave; no address match, locator point in Lakewood city, and the SDC lists no money orders. Also Englewood, Downtown Englewood, Littleton, Centennial, Greenwood Village, Morrison, Eldorado Springs, Niwot, Longmont, and the Boulder offices. Valmont 1385692 and Boulder CO SDC 1612987 share 2995 55th St; the SDC lists no money orders.
- USPS contract postal units and Approved Postal Providers were not collected, the same as for earlier cities.

## Fetch failures

- None. All 28 locator API queries returned JSON, and both detail pages returned HTTP 200 on the first try. Seven records had no current-file address match: Eastlake, Westminster, Broomfield Eagle View, Brighton Carrier Annex, Eldorado Springs, Lakewood, and Lakewood CO SDC. I used their official locator points instead, and all of them fall outside Northglenn.
