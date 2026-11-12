# Step 8: Windsor (2026-11-12, America/Denver)

**Rows:** 2 (1 Post Office, 1 King Soopers). Town 2 of the batch approved on 2026-11-12 (Brighton, Windsor, Erie, Northglenn, Lafayette, Fountain, Evans, Johnstown, Montrose, Louisville; ranked from Census Vintage 2025, SUB-IP-EST2025-POP-08, where Windsor is rank 22 at 43,840). Windsor is a statutory town; only addresses inside the Town of Windsor ("Windsor town" in the Census geocoder; the town spans Weld and Larimer counties) are listed. No businesses were contacted.

**Counts:** 2 locations; 2 money orders (Windsor Post Office and King Soopers Windsor); 0 check cashing; 0 bill pay; 0 prepaid reload. Labels on the hub: 1 Open evenings (King Soopers), 2 Open weekends. The evenings/weekends page lists both locations (1 Open evenings, 2 Open weekends). No hub-only rows. No check-cashing or bill-pay page (zero listings). No holds.

## Method

- **USPS:** official USPS Location Finder (tools.usps.com, `requestType` po), same method as Brighton, Littleton, and Parker. Searches at 5 and 15 miles around ZIPs 80550 and 80551 (Windsor), 80528, 80524, 80525 (Fort Collins), 80634, 80631 (Greeley), 80516 (Erie), 80534 (Johnstown), 80543 (Milliken), 80615 (Eaton), 80538 (Loveland), 80547 (Timnath), and 80610 (Ault) returned 62 unique Post Office records (`docs/research/step8-browser/windsor-usps-locator-2026-11-12.jsonl`; pass notes in `windsor-usps-2026-11-12.md`). Official location pages loaded on 2026-11-12, each on the first try: 1387952 Windsor (HTTP 200), 1560051 WIN Carrier Annex (HTTP 200), 1381248 Severance (HTTP 200), 1384692 Timnath (HTTP 200). Hours and services come from the same official locator record those pages display; retail hours means the BUSINESS hours block only.
- **Town limits:** every candidate address was checked with the U.S. Census Bureau Geocoder (https://geocoding.geo.census.gov/geocoder/, address endpoint, Public_AR_Current / Current_Current, Incorporated Places, Census Designated Places and Counties layers) on 2026-11-12. Raw results: `windsor-usps-geocoder-2026-11-12.jsonl` (all 62 Post Office records) and `windsor-stores-geocoder-2026-11-12.jsonl` (all 20 store rows in the research CSV).
- **Fallback checks:** Census 2020 benchmark (Public_AR_Census2020) and current one-line lookups for the two Windsor-printed Post Office addresses (215 6th St, 1070 Diamond Valley Dr), King Soopers Windsor (1520 Main St), and King Soopers 00154 Frederick (no current-file match); plus current-benchmark coordinates lookups of every official USPS locator map point. Raw results: `windsor-geocoder-fallback-2026-11-12.jsonl`. No listed row relies on a fallback; both listed rows matched inside Windsor town on the current address file, and the 2020 file and locator point agree.
- Fees reuse existing rows in `data/providers/fees.csv`. No new fee rows or brands.

## USPS

| Office | Address | Geocoder | Services | Retail hours |
|---|---|---|---|---|
| Windsor (1387952) | 215 6th St 80550 | Windsor town (215 6TH ST, WINDSOR, CO, 80550; Weld County). 2020 file agrees; official locator point (40.479372, -104.905553) also Windsor town | Domestic and Inquiry Money Orders | Mon-Fri 08:30-17:00, Sat 09:00-12:00, Sun closed |

- Windsor Post Office: Open weekends (Saturday). **Not** Open evenings: weekday retail closes at 17:00, not after. Phone 970-833-3010. URL https://tools.usps.com/locations/details/1387952. verification_status `verified_official_locator`. The 24-hour lobby / PO box access is not retail and is not used.
- No duplicate or SDC record at 215 6th St.

### Left out (not held)

- **WIN Carrier Annex 1560051** (1070 Diamond Valley Dr Ste 500, Windsor 80550; same phone as the Post Office): carrier/delivery unit only (CALLREFERRAL, CARRIER, DELIVERYUNIT); no retail hours and no money orders, so nothing to list. Current and 2020 files and the locator point all place it in Windsor town. Left out as a no-services unit, not a hold.
- **Severance 1381248** (320 1st St, Severance 80546): current address match returns Eaton town; the locator point returns Severance town. Neither is Windsor.
- Printed another place and the geocoder agrees it is outside Windsor: Timnath (Timnath town), Eaton, Johnstown, Milliken, Ault, La Salle, Pierce, Kersey, Gilcrest, Platteville, Berthoud, Wellington, Nunn, Mead, Frederick, Firestone, Dacono, Erie and Erie Carrier Annex (their own towns); Evans (Evans city); Greeley 1365514 and Downtown Greeley 1365513 (Greeley city); Fort Collins 1363754 / Fort Collins CO SDC 1601572 (same building) and Old Town 1376040 (Fort Collins city); Loveland 1371037 and Valentine 1371038 (Loveland city); Lucerne, Gill, Galeton (unincorporated Weld County); Laporte (Laporte CDP), Bellvue, Masonville, Drake (unincorporated Larimer County); and the far edge of the 80516 sweep (Lafayette, Louisville, Longmont, Niwot, Boulder, Broomfield, Northglenn, Eastlake, Westminster, Brighton, Henderson, Fort Lupton, Indian Tree, North Pecos, Dupont, Hygiene, Eldorado Springs).
- No Post Office printed with another city geocodes inside Windsor town (address geocode or locator map point). USPS contract postal units and Approved Postal Providers were not collected.

## King Soopers and Walmart

Official store pages were opened in a browser on 2026-11-12 (read-only; no sign-in, no store contact). Raw results: `docs/research/step8-browser/windsor-walmart-ks-2026-11-12.csv` and `.md` (20 rows: 13 King Soopers, 7 Walmart Supercenters). Walmart's official store directory for Windsor, CO loaded and listed **0 stores**; directories for Johnstown, Evans, Severance, Eaton, Milliken, Berthoud, Firestone, and Frederick were also empty. Walmart #1008 showed a bot check first; the official page loaded afterward. No Neighborhood Market pages, no standalone fuel listings, and no unexpected grocery or retail brands appeared. Every address was run through the Census geocoder on 2026-11-12.

### Added (1 store row)

| Store | Address | Geocoder | Services listed | Store hours |
|---|---|---|---|---|
| King Soopers 00104 Windsor | 1520 Main St 80550 | Windsor town (1520 MAIN ST, WINDSOR, CO, 80550; Weld County); 2020 file agrees | Money orders (and Money Services) | Sun-Sat 6 AM-11 PM |

- URL https://www.kingsoopers.com/stores/grocery/co/windsor/windsor/620/00104 (HTTP 200). Phone 970-674-2830.
- **Hours:** store hours only. Pharmacy, fuel, sensory-friendly, and holiday hours not used. Open evenings and Open weekends.
- The page tags "Money Orders" and "Money Services" (`money_orders=true`). No check cashing, bill pay, or prepaid reload named; no Western Union mention. "Account Funding" is not a tracked service and is not flagged. King Soopers fees stay "Not published, call ahead."
- The page also shows a **Fuel Center**; that is a feature of the grocery store, not a separate row, and its hours are not used.

### Held for Richard

None. The only store printed Windsor geocodes inside Windsor town, and no store printed with another city geocodes inside Windsor town.

### Left out (not held)

- Printed another city, and the geocoder agrees it is outside Windsor (already-live stores in other cities were not changed):
  - **Timnath** (Timnath town): Walmart Supercenter 4599 (4500 Weitzel St).
  - **Greeley** (Greeley city): King Soopers 00117 North Gate Village, 00032 University Square, 00011 Westlake; Walmart Supercenters 5051 (920 47th Ave) and 980 (3103 S 23rd Ave).
  - **Fort Collins** (Fort Collins city): King Soopers 00009, 00073, 00097, 00099, 00146; Walmart Supercenters 2729 and 3177.
  - **Loveland** (Loveland city): King Soopers 00044, 00074; Walmart Supercenters 953 and 1008.
  - **Firestone** (Firestone town): King Soopers 00105.
  - **No current-file match, printed another city far from Windsor:** King Soopers 00154 (5801 Silverstone Dr, Frederick 80504) had no match on the current or 2020 file, prints Frederick, and lists no money services. Not a reverse-check candidate.
- Walmart Neighborhood Markets: none found. Fuel features (King Soopers Windsor Fuel Center; Walmart Fuel Station tags on 5051 and 953) are not separate rows.

## Not changed

- Thornton holds (Eastlake Post Office, Walmart 4567), `thornton.csv`, `brighton.csv`, and every other city CSV; Grand Junction's Fruitvale hold; the Castle Rock Post Office; City Market; Littleton holds. Erie and later batch cities were not started.

## Not collected

- Payday / title-loan storefronts, including ACE: omitted by policy.
- Stand-alone Western Union / MoneyGram agents and other grocery brands were not collected.
