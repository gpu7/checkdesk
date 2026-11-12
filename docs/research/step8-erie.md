# Step 8: Erie (2026-11-12, America/Denver)

**Rows:** 3 (1 Post Office, 2 King Soopers). Town 3 of the batch approved on 2026-11-12 (Brighton, Windsor, Erie, Northglenn, Lafayette, Fountain, Evans, Johnstown, Montrose, Louisville; ranked from Census Vintage 2025, SUB-IP-EST2025-POP-08, where Erie is rank 23 at 40,904). Erie is a statutory town; only addresses inside the Town of Erie ("Erie town" in the Census geocoder; the town spans Boulder and Weld counties) are listed. No businesses were contacted.

**Counts:** 3 locations; 1 money orders (Erie Post Office); 0 check cashing; 0 bill pay; 0 prepaid reload. Labels on the hub: 2 Open evenings (both King Soopers), 3 Open weekends. Hub-only rows: 2 (King Soopers Vista Ridge and King Soopers Highway 287 and Arapahoe Road, generic "Money Services" only). The money-orders page lists 1 location. The evenings/weekends page lists 1 location (the Post Office: 0 Open evenings, 1 Open weekends); hub-only rows are not on service pages. No check-cashing or bill-pay page (zero listings). No holds.

## Method

- **USPS:** official USPS Location Finder (tools.usps.com, `requestType` po), same method as Windsor and Brighton. Searches at 5 and 15 miles around 80516 (Erie), 80504, 80501, 80503 (Longmont), 80026 (Lafayette), 80027 (Louisville/Superior), 80023, 80020, 80021 (Broomfield), 80602 (Brighton/Thornton), 80514 (Dacono), 80530 (Frederick), 80621 (Fort Lupton), 80234 (Northglenn/Westminster), and 80031 (Westminster) returned 73 unique Post Office records (`docs/research/step8-browser/erie-usps-locator-2026-11-12.jsonl`; pass notes in `erie-usps-2026-11-12.md`). Official location pages loaded on 2026-11-12, each on the first try: 1362695 Erie (HTTP 200) and 1546616 Erie Carrier Annex (HTTP 200). Hours and services come from the same official locator record those pages display; retail hours means the BUSINESS hours block only.
- **Town limits:** every candidate address was checked with the U.S. Census Bureau Geocoder (https://geocoding.geo.census.gov/geocoder/, address endpoint, Public_AR_Current / Current_Current, Incorporated Places, Census Designated Places and Counties layers) on 2026-11-12. Raw results: `erie-usps-geocoder-2026-11-12.jsonl` (all 73 Post Office records) and `erie-stores-geocoder-2026-11-12.jsonl` (all 22 King Soopers and Walmart Supercenter rows in the research CSV; the two Neighborhood Markets were not geocoded because they are excluded by policy).
- **Fallback checks:** Census 2020 benchmark (Public_AR_Census2020) and current one-line lookups for the two Erie-printed Post Office addresses (150 Wells St, 621 Mitchell Way); for King Soopers 00129 (three address variants of 1891 State Highway 7) and 00138 (2900 Arapahoe Rd); and for the three nearby stores with no current-file match (King Soopers 00154 Frederick, Walmart 1045 Lafayette, Walmart 5370 Longmont). Current-benchmark coordinates lookups of every official USPS locator map point, and of the official store-page map points for King Soopers 00129, 00138, and 00154 (JSON-LD `geo` on each official King Soopers page, read in a browser on 2026-11-12) and Walmart 1045 and 5370 (official store-page points recorded in `step8-longmont.md`). Raw results: `erie-geocoder-fallback-2026-11-12.jsonl`. One listed row relies on the fallback: King Soopers 00129 Vista Ridge (below). OpenStreetMap points were not used for any decision.
- Fees reuse existing rows in `data/providers/fees.csv`. No new fee rows or brands.

## USPS

| Office | Address | Geocoder | Services | Retail hours |
|---|---|---|---|---|
| Erie (1362695) | 150 Wells St 80516 | Erie town (150 WELLS ST, ERIE, CO, 80516; Weld County). 2020 file agrees; official locator point (40.049879, -105.047065) also Erie town | Domestic and Inquiry Money Orders | Mon-Fri 09:00-17:00, Sat 09:00-12:00, Sun closed |

- Erie Post Office: Open weekends (Saturday). **Not** Open evenings: weekday retail closes at 17:00, not after. Phone 303-828-0781. URL https://tools.usps.com/locations/details/1362695. verification_status `verified_official_locator`. The 24-hour lobby is not retail and is not used. Passports, parcel lockers, and general delivery are not tracked services.
- No duplicate or SDC record at 150 Wells St.

### Left out (not held)

- **Erie Carrier Annex 1546616** (621 Mitchell Way, Erie 80516; same phone as the Post Office): carrier/delivery unit only (CARRIER, DELIVERYUNIT); no retail hours and no money orders, so nothing to list. Current and 2020 files and the locator point all place it in Erie town. Left out as a no-services unit, not a hold.
- Printed another place and the geocoder agrees it is outside Erie: Lafayette 1369494 and Lafayette Carrier Annex (Lafayette city); Louisville 1371024, printed Superior (Louisville city); Dacono (Dacono city); Frederick, Firestone, Mead, Platteville, Johnstown, Milliken, Berthoud, Lyons, Hudson, Gilcrest, Keenesburg (their own towns); Longmont (Longmont city); Niwot (Niwot CDP); Hygiene (unincorporated Boulder County, locator point); Broomfield and Broomfield Eagle View (Broomfield city); Northglenn and Northview (Northglenn city); Eastlake (Thornton city, locator point); Westminster and Harris Park (Westminster city); Brighton and Brighton Carrier Annex (Brighton city); Henderson (unincorporated Adams County); Fort Lupton (Fort Lupton city); Boulder, Valmont, High Mar, Boulder CO SDC (Boulder city); Eldorado Springs (Eldorado Springs CDP); Jamestown (Jamestown town); Pinecliffe (unincorporated Boulder County); and the far edge of the 15-mile sweeps (Arvada, Indian Tree, North Pecos, Dupont, Adams City, Commerce City, Wheat Ridge, Edgewater, Golden, Lakewood, and Denver, Aurora, Glendale, and Englewood offices).
- No Post Office printed with another city geocodes inside Erie town (address geocode or locator map point). USPS contract postal units and Approved Postal Providers were not collected.

## King Soopers and Walmart

Official store pages were opened in a browser on 2026-11-12 (read-only; no sign-in, no store contact). Raw results: `docs/research/step8-browser/erie-walmart-ks-2026-11-12.csv` and `.md` (24 rows: 14 King Soopers, 8 Walmart Supercenters, 2 Walmart Neighborhood Markets excluded by policy). The official King Soopers Erie directory lists 2 grocery stores in Erie. Walmart's official Erie directory URL redirected to the generic directory; the official store finder for 80516 lists no Erie store, and no Walmart Supercenter prints Erie. No unexpected grocery or retail brands appeared. Every in-scope address was run through the Census geocoder on 2026-11-12.

### Added (2 store rows, both hub-only)

| Store | Address | Town-limits evidence | Services listed | Store hours |
|---|---|---|---|---|
| King Soopers 00129 Vista Ridge | 1891 State Highway 7 80516 | No address match on the current or 2020 file (variants `1891 State Highway 7`, `1891 Highway 7`, `1891 E State Highway 7`, Erie CO 80516). Official store-page map point (40.002236, -105.009925) returns **Erie town** (Weld County, no CDP) in a Census coordinates lookup (current benchmark) | Generic "Money Services" only (hub-only) | Sun-Sat 6 AM-11 PM |
| King Soopers 00138 Highway 287 and Arapahoe Road | 2900 Arapahoe Rd 80026 | Current file: 2900 ARAPAHOE RD, ERIE, CO, 80026, **Erie town** (Boulder County). 2020 file: no match. Official store-page map point (40.012189, -105.100416) also returns Erie town | Generic "Money Services" only (hub-only) | Sun-Sat 6 AM-11 PM |

- **00129 fallback:** the official page prints Erie, CO 80516 and its official map point falls inside Erie town, so the row is included under the same documented fallback used for Walmart 5370 in Longmont, the Westminster Post Office, and Pueblo Midtown/Belmont; the row's notes say so. (An earlier pass noted only an OpenStreetMap point for this store; that point was not used here.)
- **00138 and the Lafayette ZIP:** the page, the official Erie city directory, and the locator all print Erie, but the ZIP 80026 is shared with Lafayette. The current Census file places the address in Erie town (Boulder County), and the official map point agrees, so printed city and geocoder agree and it is included. No Lafayette file was changed.
- URLs: https://www.kingsoopers.com/stores/grocery/co/erie/vista-ridge/620/00129 and https://www.kingsoopers.com/stores/grocery/co/erie/highway-287-and-arapahoe-road/620/00138 (both HTTP 200). Phones 303-729-4161 and 303-301-1150.
- **Services:** each page shows "Money Services" only. Money orders, check cashing, bill pay, and prepaid reload are not named, so all four flags are false; nothing is inferred from chain policy. No Western Union mention. "Account Funding" (00129) is not a tracked service. Hub listing only, labeled "Money Services, call ahead"; not on the money-order or evenings/weekends pages. King Soopers fees stay "Not published, call ahead."
- **Hours:** store hours only. Pharmacy, fuel, sensory-friendly, and holiday hours not used. Both get Open evenings and Open weekends labels on the hub.
- Both pages show a **Fuel Center**; that is a feature of the grocery store, not a separate row, and its hours are not used.

### Held for Richard

None. Both Erie-printed King Soopers fall inside Erie town (00138 on the current address file, 00129 on its official map point), and no store printed with another city geocodes inside Erie town.

### Left out (not held)

- Printed another city, and the geocoder agrees it is outside Erie (already-live stores in other cities were not changed):
  - **Lafayette** (Lafayette city): Walmart Supercenter 1045 (745 US Highway 287): no address match on the current or 2020 file; its official store-page map point (40.005992, -105.105136) returns Lafayette city.
  - **Louisville** (Louisville city): King Soopers 00013 LOUISVILLE, 00142 Louisville Marketplace.
  - **Broomfield** (Broomfield city): King Soopers 00118, 00089, 00086; Walmart Supercenters 4288 and 5341.
  - **Thornton** (Thornton city): King Soopers 00101, 00116; Walmart Supercenter 4567 (prints Brighton; already held in the Thornton and Brighton passes and not changed here).
  - **Westminster** (Westminster city): Walmart Supercenter 3867.
  - **Longmont** (Longmont city): King Soopers 00080, 00102; Walmart Supercenter 905 (matched 2285 KEN PRATT BLVD; its Walmart Fuel Station is not a separate row); Walmart Supercenter 5370 (no address match; official map point in Longmont city).
  - **Boulder** (Boulder city): King Soopers 00028 Gun Barrel.
  - **Firestone** (Firestone town): King Soopers 00105.
  - **Brighton** (Brighton city): Walmart Supercenter 1659.
  - **Frederick** (Frederick town): King Soopers 00154 (no address match on either file; official store-page map point 40.089792, -104.94377 returns Frederick town; its page lists no money services).
- Walmart Neighborhood Markets 4747 (Northglenn) and 3019 (Thornton): excluded by policy.

## Not changed

- Thornton holds (Eastlake Post Office, Walmart 4567), `thornton.csv`, `brighton.csv`, `windsor.csv`, and every other city CSV; Grand Junction's Fruitvale hold; the Castle Rock Post Office; City Market; Littleton holds. No Lafayette files. Northglenn and later batch cities were not started.

## Not collected

- Payday / title-loan storefronts, including ACE: omitted by policy.
- Stand-alone Western Union / MoneyGram agents and other grocery brands were not collected.
