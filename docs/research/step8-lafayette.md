# Step 8: Lafayette (2026-11-12, America/Denver)

**Rows:** 2 (1 Post Office, 1 Walmart Supercenter). City 5 of the batch approved on 2026-11-12 (Brighton, Windsor, Erie, Northglenn, Lafayette, Fountain, Evans, Johnstown, Montrose, Louisville; ranked from Census Vintage 2025, SUB-IP-EST2025-POP-08, where Lafayette is rank 27 at 30,116). Lafayette is a statutory city; only addresses inside Lafayette city limits ("Lafayette city" in the Census geocoder; Boulder County) are listed. No businesses were contacted.

**Counts:** 2 locations; 1 money orders (Lafayette Post Office); 0 check cashing; 0 bill pay; 0 prepaid reload. Labels on the hub: 1 Open evenings, 2 Open weekends. Hub-only rows: 1 (Walmart Supercenter 1045, "Money Services, call ahead"). The money-orders page lists 1 location. The evenings/weekends page lists the 1 money-order location (0 Open evenings, 1 Open weekends); the Walmart Supercenter is hub-only and does not appear there. No check-cashing or bill-pay page (zero listings). No holds.

## Method

- **USPS:** official USPS Location Finder (tools.usps.com, `requestType` po), same method as Northglenn, Erie, Windsor, and Brighton. Searches at 5 and 15 miles around 80026 (Lafayette), 80027 (Louisville/Superior), 80023, 80020, 80021 (Broomfield), 80516 (Erie), 80301, 80303 (Boulder), 80031 (Westminster), 80025 (Eldorado Springs), 80544 (Niwot), and 80514 (Dacono) returned 71 unique Post Office records (`docs/research/step8-browser/lafayette-usps-locator-2026-11-12.jsonl`; pass notes in `lafayette-usps-2026-11-12.md`). Official location pages were fetched on 2026-11-12, each on the first try: 1369494 Lafayette (HTTP 200) and 1369484 Lafayette Carrier Annex (HTTP 200). Hours and services come from the same official locator record those pages display; retail hours means the BUSINESS hours block only.
- **City limits:** every candidate address was checked with the U.S. Census Bureau Geocoder (https://geocoding.geo.census.gov/geocoder/, address endpoint, Public_AR_Current / Current_Current, Incorporated Places, Census Designated Places and Counties layers) on 2026-11-12. Raw results: `lafayette-usps-geocoder-2026-11-12.jsonl` (all 71 Post Office records) and `lafayette-stores-geocoder-2026-11-12.jsonl` (all 10 in-scope King Soopers and Walmart Supercenter rows in the research CSV; the three Neighborhood Markets were not geocoded because they are excluded by policy).
- **Fallback checks:** Census 2020 benchmark (Public_AR_Census2020) and current one-line lookups for the two Lafayette-printed Post Office addresses (603 S Public Rd, 109 Kimbark St); for King Soopers 00138 (2900 Arapahoe Rd); and for Walmart 1045 address variants (`745 US Highway 287`, `745 Us Highway 287`, `745 US Hwy 287`, `745 Highway 287`, `745 N US Highway 287`, `745 S US Highway 287`, `745 U.S. Highway 287`, and `745 US-287`, Lafayette CO 80026). Current-benchmark coordinates lookups of the official USPS locator map points for 1369494 and 1369484, and of the official store-page map points for Walmart 1045 (recorded from its official Walmart store page in `step8-longmont.md` and reused in the Erie fallback file; not collected from OpenStreetMap) and King Soopers 00138 (JSON-LD `geo` on its official King Soopers page, recorded in `step8-erie.md`). Raw results: `lafayette-geocoder-fallback-2026-11-12.jsonl`. One listed row relies on the fallback: Walmart Supercenter 1045 (below). OpenStreetMap points were not used for any decision. The listed Post Office matches the current file, the 2020 file, and its official locator map point, all in Lafayette city.
- Fees reuse existing rows in `data/providers/fees.csv`. No new fee rows or brands.

## USPS

| Office | Address | Geocoder | Services | Retail hours |
|---|---|---|---|---|
| Lafayette (1369494) | 603 S Public Rd 80026 | Lafayette city (603 S PUBLIC RD, LAFAYETTE, CO, 80026; Boulder County). 2020 file agrees; official locator point (39.993195, -105.090898) also Lafayette city | Domestic and Inquiry Money Orders | Mon-Fri 09:00-17:00, Sat 10:00-13:00, Sun closed |

- Lafayette Post Office: Open weekends (Saturday). Weekday retail closes at 17:00, so no Open evenings label. Phone 303-926-1044. URL https://tools.usps.com/locations/details/1369494. verification_status `verified_official_locator`. Window service hours match retail hours. Lobby and PO box access (Mon-Sat 07:00-18:00) and the self-service kiosk are not retail and are not used. Last collection 17:30 Mon-Sat is not retail. Passports are listed (appointment required) but are not a Check Desk tracked service. No duplicate or SDC record at 603 S Public Rd. The Carrier Annex (below) is a separate building at 109 Kimbark St, about 70 m away by locator points; its record says "MAIN OFFICE AT 603 SOUTH PUBLIC ROAD."

### Left out (not held)

- **Lafayette Carrier Annex 1369484** (109 Kimbark St, Lafayette 80026, 303-664-1241): carrier/delivery unit only (CARRIER, DELIVERYUNIT, CONNECTLOCAL, CALLREFERRAL, and pickup codes); no retail hours and no money orders, so nothing to list. Its hours blocks cover only call referral and pickup. Current and 2020 files and the locator point (39.992675, -105.091398) all place it in Lafayette city. Left out as a no-services unit, not a hold. Page HTTP 200.
- Printed another place and the geocoder agrees it is outside Lafayette: Louisville 1371024, printed Superior 80027 (Louisville city; this is an existing Louisville hold and is not listed here); Erie 1362695 (Erie town) and Erie Carrier Annex 1546616 (Erie town; no retail, no money orders); Broomfield 1356062 (Broomfield city) and Broomfield Eagle View 1361605 (no current-file address match; locator point in Broomfield city); Boulder 1355494, High Mar 1366905, Valmont 1385692 (Boulder city); Valmont and Boulder CO SDC 1612987 share 2995 55th St; the SDC lists no money orders; Niwot 1375136 (Niwot CDP); Dacono 1360137 (Dacono city); Westminster 1439640 (no current-file address match; locator point in Westminster city); and the farther offices in the 15-mile sweeps (Northglenn, Northview, Eastlake, Frederick, Firestone, Longmont, Mead, Lyons, Hygiene, Berthoud, Platteville, Fort Lupton, Henderson, Brighton, Brighton Carrier Annex, Commerce City, Adams City, Dupont, Arvada, Indian Tree, Harris Park, North Pecos, Wheat Ridge, Edgewater, Golden, Lakewood, Eldorado Springs, Jamestown, Ward, Nederland, Rollinsville, Pinecliffe, Black Hawk, and Denver, Aurora, Glendale, and Englewood offices). No office in the sweep is printed Lafayette besides the two Lafayette records above. USPS contract postal units and Approved Postal Providers were not collected.
- No Post Office printed with another city geocodes inside Lafayette city (address geocode or locator map point).

## King Soopers and Walmart

Official store pages were opened in a browser on 2026-11-12 (read-only; no sign-in, no store contact). Raw results: `docs/research/step8-browser/lafayette-walmart-ks-2026-11-12.csv` and `.md` (13 rows: 5 King Soopers, 5 Walmart Supercenters, 3 Walmart Neighborhood Markets excluded by policy). The official King Soopers city directory `/stores/grocery/co/lafayette` does not exist, and no King Soopers store prints Lafayette. Walmart's official store finder for 80026 lists one Supercenter that prints Lafayette (1045). No unexpected grocery or retail brands appeared (no City Market). All 10 in-scope Supercenter and King Soopers addresses were run through the Census geocoder on 2026-11-12; 8 matched the current file. Walmart 1045 and King Soopers 00129 had no current-file address match (00129 is already listed on the Erie page from its official map-point fallback and was not a Lafayette candidate).

### Added

| Store | Address | Geocoder | Services on the official page | Store hours |
|---|---|---|---|---|
| Walmart Supercenter 1045 (Lafayette Supercenter) | 745 US Highway 287 80026 (official page also prints 745 Us Highway 287) | No address match on the current or 2020 file (variants listed under Method). Official store-page map point (40.005992, -105.105136) returns **Lafayette city** (Boulder County, no CDP) in a Census coordinates lookup (current benchmark) | Generic "Money Services" only (hub-only) | Mon-Sun 6am-11pm |

- **Walmart 1045 fallback:** the official page prints Lafayette, CO 80026, and its official map point falls inside Lafayette city, so the row is included under the same documented fallback used for Walmart 5370 in Longmont, King Soopers 00129 in Erie, the Westminster Post Office, and Pueblo Midtown/Belmont; the row's notes say so. An earlier Erie-area pass had already found no current-file address match and the same official map point in Lafayette city; this Lafayette build re-ran the current file, the 2020 file, and the official map-point coordinates lookup and got the same result.
- **Services:** the page shows "Money Services" only. Money orders, check cashing, bill pay, and prepaid reload (load/unload) are not named, so all four flags are false; nothing is inferred from chain policy. No Western Union mention. Hub listing only, labeled "Money Services, call ahead"; not on the money-order or evenings/weekends pages. Unpublished fees stay "Not published, call ahead." Hours are store hours only (daily 6 a.m. to 11 p.m.), so the hub labels it Open evenings and Open weekends; money desk hours are not published.

### Held for Richard

None. No Lafayette-printed store geocodes outside Lafayette city, and no store printed with another city geocodes inside Lafayette city.

### Left out (not held)

- **King Soopers 00138** Highway 287 and Arapahoe Road, 2900 Arapahoe Rd, prints **Erie**, CO 80026 (official store page, locator, and Erie city directory). Current file: 2900 ARAPAHOE RD, ERIE, CO, 80026, **Erie town** (Boulder County). 2020 file: no match. Official store-page map point (40.012189, -105.100416) also returns Erie town (Boulder County). The ZIP 80026 is shared with Lafayette, but official printed city and geocoder agree it is in Erie, and the store is already live on the Erie page. It is not added to Lafayette and is not a new hold on this page. `erie.csv` was not edited.
- Printed another city, and the geocoder agrees it is outside Lafayette (already-live or later-city stores were not changed):
  - **Louisville** (Louisville city): King Soopers 00013 and 00142.
  - **Broomfield** (Broomfield city): King Soopers 00089; Walmart Supercenters 5341 and 4288.
  - **Westminster** (Westminster city): Walmart Supercenters 3867 and 2223.
  - **Erie** (Erie town): King Soopers 00138 (above) and 00129 Vista Ridge (no current-file address match; already listed on the Erie page from its official map point, which returns Erie town).
  - **Louisville hold, not a Lafayette listing:** Louisville Post Office USPS 1371024 prints Superior and geocodes in Louisville city.
- Walmart Neighborhood Markets 4747 (Northglenn), 3019 (Thornton), and 3127 (Denver): excluded by policy; pages not opened for this run.

## Not changed

- Thornton holds (Eastlake Post Office, Walmart 4567), Walmart 4567, Fruitvale, the Castle Rock Post Office, City Market, Littleton holds, Erie 00129/00138, `erie.csv`, `thornton.csv`, and every other city CSV; the Louisville Post Office Superior hold. Later batch cities (Fountain, Evans, Johnstown, Montrose, Louisville) were not started.

## Not collected

- Payday / title-loan storefronts, including ACE: omitted by policy.
- Stand-alone Western Union / MoneyGram agents and other grocery brands, including City Market, were not collected.
