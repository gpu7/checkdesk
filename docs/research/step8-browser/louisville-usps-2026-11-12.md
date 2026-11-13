# Louisville, CO: USPS locator research (2026-11-12, America/Denver)

Research only. Nothing was built, committed, or deployed. No business was contacted. No browser was used. last_verified: 2026-11-12.

## Method

- **Locator:** official USPS Location Finder API (`https://tools.usps.com/UspsToolsRestServices/rest/POLocator/findLocations`, `requestType` po), queried with curl, the same way as Lafayette, Erie, Northglenn, and Johnstown. First pass: 5 and 15 miles around 80027 (Louisville/Superior; they share this official ZIP, and Superior has no unique ZIP), 80026 (Lafayette), 80023, 80020, 80021 (Broomfield), 80516 (Erie), 80301, 80303 (Boulder), 80031 (Westminster), 80025 (Eldorado Springs), 80544 (Niwot), and 80514 (Dacono). That pass returned **71 unique Post Office records**. Second pass: 80027 was spot-checked at 10 and 20 miles (0 new relative to the combined first pass), plus 5 and 15 miles around additional official nearby ZIPs not in the first pass — 80030 (Westminster), 80302, 80304, 80305 (Boulder), 80503 (Longmont; Gunbarrel has no unique official ZIP and is served by Boulder 80301 and Longmont 80503 per Boulder County), 80234, 80233 (Northglenn), 80501 (Longmont), and 80005 (Arvada/Westminster edge). The second pass added **7** farther offices. Together: **78 unique Post Office records**. All **44** queries returned JSON (`sweep.out`, `sweep_pass1.out`, `sweep_pass2.out`). Raw data: `/workspace/step8lv/usps_all.json` (pass 1 snapshot: `usps_all_pass1.json`). One-line summary: `usps_summ.txt`. Scripts: `sweep.py`, `sweep_pass2.py`.
- **Official pages:** `https://tools.usps.com/locations/details/<id>` was fetched with curl at about 3:53–3:54 PM MT. 1371024 (named Louisville, printed Superior) returned HTTP 200 on the first try, and so did the nearby close-miss / possible-hold pages: 1369494 Lafayette, 1369484 Lafayette Carrier Annex, 1366905 High Mar, 1356062 Broomfield, 1361605 Broomfield Eagle View, 1362695 Erie, 1546616 Erie Carrier Annex, 1355494 Boulder, 1385692 Valmont, 1612987 Boulder CO SDC, and 1362237 Eldorado Springs (`http.txt` and `d<id>.html`). Hours and services come from the official locator record that these pages display. "Retail hours" means the `BUSINESS` hours block only. The 1371024 detail page `poDetail` object prints city **SUPERIOR**, name **LOUISVILLE**, and the same retail hours and money-order services as the locator API record.
- **City limits:** I checked all 78 records with the U.S. Census Geocoder address endpoint, Public_AR_Current / Current_Current, using the Incorporated Places, CDPs, and Counties layers (`usps_geo.jsonl`). I also checked every official USPS locator map point against the current benchmark (`coord.jsonl`). For 1371024 and for every record with no current-file address match, I ran one-line lookups against the Census 2020 file and the current file (`fbr.jsonl`). Joined view: `joined.txt` (`joined.py`).
- **Structured output:** `/workspace/step8lv/louisville_usps_records.csv` / `.json` cover all 78 records (same fields as Lafayette and Johnstown). Built by `build.py`. Working summary: `/workspace/step8lv/summary.txt`.

## Candidate includes

- **None.** No official USPS locator record in this sweep has printed city Louisville. The only office whose name is Louisville (1371024) prints Superior and is a hold, below.

## Holds

- **Louisville (1371024) — HOLD, do not auto-include.** Official name Louisville; official printed city **Superior**, CO 80027. Address 566 S McCaslin Blvd. Phone 303-665-0030. Money orders yes (MONEYORDERSDOM, MONEYORDERSINQ). Retail hours Mon-Fri 09:00-17:30, Sat 09:00-12:00, Sun closed. Weekday retail closes after 17:00, so it would be marked open evenings if it were an include; it is open Saturdays. URL: https://tools.usps.com/locations/details/1371024 (HTTP 200, first try). verification_status: verified_official_locator.
  - Current address file: 566 S MCCASLIN BLVD, SUPERIOR, CO, 80027, **Louisville city**, Boulder County.
  - 2020 address file: the same matched address, **Louisville city**.
  - Official locator map point 39.96163, -105.159983 → **Louisville city**, Boulder County.
  - Official printed city (Superior) and the geocoder / map point (Louisville city) disagree, so this is a hold, not a candidate include. Window service hours match retail hours. Lobby, PO box access, and the self-service kiosk (APC) are listed 00:01-23:59 daily (not retail). Last collection 17:15 Mon-Fri, 14:45 Sat. The locator record also lists passport services (appointment required; appointments and photos Mon-Fri 10:00-16:00; walk-in Saturday 09:00-12:00), parcel lockers, gift cards, duck stamps, burial flags, general delivery, and bulk mail (Mon-Fri 09:00-16:00). Fax 303-665-3068 (not used). Parking: lot. No site comment. No duplicate or SDC record at 566 S McCaslin Blvd. This is the only Superior-printed office in the sweep; there is no separate Superior Post Office record.

## Left out (not holds)

- There is **no Louisville Carrier Annex** (or other Louisville-printed carrier/SDC record) in the sweep.
- Nearby offices printed with other cities, where the geocoder or official map point agrees they are outside Louisville city. All list money orders unless noted:
  - Lafayette 1369494, 603 S Public Rd, Lafayette 80026 (Lafayette city; retail Mon-Fri 09:00-17:00, Sat 10:00-13:00). Page HTTP 200.
  - Lafayette Carrier Annex 1369484, 109 Kimbark St, Lafayette 80026: **no BUSINESS (retail) hours and no money orders**. Current file: Lafayette city. Page HTTP 200. Left out as an annex with no retail and no tracked service, not a hold.
  - High Mar 1366905, 4985 Moorhead Ave, Boulder 80305 (Boulder city; retail Mon-Fri to 17:30). Page HTTP 200.
  - Broomfield 1356062, 280 E 1st Ave, Broomfield 80020 (Broomfield city; retail Mon-Fri 08:00-18:00, Sat 09:00-13:00). Page HTTP 200.
  - Broomfield Eagle View 1361605, 8800 W 116th Cir, Broomfield 80021: no current-file or 2020 address match; official locator point is in Broomfield city, Broomfield County. Page HTTP 200.
  - Erie 1362695, 150 Wells St, Erie 80516 (Erie town, Weld County). Page HTTP 200.
  - Erie Carrier Annex 1546616, 621 Mitchell Way, Erie 80516: no retail, no money orders (Erie town). Page HTTP 200.
  - Boulder 1355494, 1905 15th St, Boulder 80302 (Boulder city). Page HTTP 200.
  - Valmont 1385692 and Boulder CO SDC 1612987 share 2995 55th St, Boulder 80301 (Boulder city). Valmont lists money orders; the SDC does not. Pages HTTP 200.
  - Eldorado Springs 1362237, 3330 Eldorado Springs Dr, Eldorado Springs 80025: no current-file or 2020 address match; official locator point is in Eldorado Springs CDP, Boulder County (unincorporated). Retail Mon-Fri 13:00-17:00, Saturday closed. Left out as an unincorporated CDP outside Louisville city, not a hold. Page HTTP 200.
  - Niwot 1375136 (Niwot CDP, unincorporated Boulder County). Westminster 1439640: no current-file match; 2020 file matches Westminster city, and the locator point is in Westminster city, Adams County. Longmont 1370889 (Longmont city).
  - Farther out in the 15- and 20-mile sweeps: Northglenn, Northview (no retail/no money orders), Eastlake (no current-file or 2020 match; locator point in Thornton city), Harris Park, Arvada, Indian Tree, North Pecos, Wheat Ridge, Dacono, Frederick, Firestone, Mead, Lyons, Hygiene (no current-file or 2020 match; locator point unincorporated Boulder County), Berthoud, Platteville, Fort Lupton, Henderson, Brighton, Brighton Carrier Annex (no retail/no money orders; locator point in Brighton city), Commerce City, Adams City, Dupont, Edgewater, Golden and Golden CO S&DC (share 1100 Johnson Rd; neither lists money orders), Downtown Golden, Lakewood and Lakewood CO SDC (share 10799 W Alameda Ave; no current-file match; 2020 file and locator points are in Lakewood city; SDC has no money orders), Jamestown, Ward, Nederland (no current-file or 2020 match; locator point in Nederland town), Rollinsville, Pinecliffe, Black Hawk (no current-file or 2020 match; locator point in Black Hawk city), many Denver offices (Capitol Hill Annex has no retail/no money orders), Aurora offices (Fletcher, Hoffman Heights, plus second-pass Altura and Buckingham), Glendale, Downtown Englewood, and second-pass Englewood, Littleton, Morrison, Sullivan, and Idledale.
- USPS contract postal units and Approved Postal Providers were not collected, the same as for earlier cities.

## Fetch failures

- None. All 44 locator API queries returned JSON, and all 12 detail pages returned HTTP 200 on the first try. Ten records had no current-file address match: Broomfield Eagle View, Eldorado Springs, Westminster, Eastlake, Hygiene, Brighton Carrier Annex, Lakewood, Lakewood CO SDC, Nederland, and Black Hawk. Their official locator points all fall outside Louisville city. Where the 2020 file did match (Westminster, Lakewood), those matches are also outside Louisville city.

## Scope notes

- Existing Louisville Walmart/King Soopers research under `/workspace/checkdesk/research/louisville-walmart-ks-2026-11-12.md` and `.csv` was not modified, and store working files already in `/workspace/step8lv/` (`stores_in.txt`, `store_geo.jsonl`, `mk_lv.py`, `pages_lv.py`) were left untouched. This work did not start another city and did not touch other `step8*` worktrees, `site-src`, or `data/locations`.
