# Step 8: Northglenn (2026-11-12, America/Denver)

**Rows:** 1 (1 Post Office). City 4 of the batch approved on 2026-11-12 (Brighton, Windsor, Erie, Northglenn, Lafayette, Fountain, Evans, Johnstown, Montrose, Louisville; ranked from Census Vintage 2025, SUB-IP-EST2025-POP-08, where Northglenn is rank 24 at 38,893). Northglenn is a statutory city; only addresses inside Northglenn city limits ("Northglenn city" in the Census geocoder; Adams County) are listed. No businesses were contacted.

**Counts:** 1 location; 1 money orders (Northglenn Post Office); 0 check cashing; 0 bill pay; 0 prepaid reload. Labels on the hub: 1 Open evenings, 1 Open weekends (the Post Office; weekday retail closes at 18:00). Hub-only rows: none. The money-orders page lists 1 location. The evenings/weekends page lists 1 location (1 Open evenings, 1 Open weekends). No check-cashing or bill-pay page (zero listings). No holds.

## Method

- **USPS:** official USPS Location Finder (tools.usps.com, `requestType` po), same method as Erie, Windsor, and Brighton. Searches at 5 and 15 miles around 80233 and 80234 (Northglenn), 80241, 80229, 80602 (Thornton), 80260 (Federal Heights), 80221 (Denver/Sherrelwood), 80031 and 80030 (Westminster), 80035 (Westminster), 80022 (Commerce City), 80023 and 80020 (Broomfield), and 80216 (Denver) returned 71 unique Post Office records (`docs/research/step8-browser/northglenn-usps-locator-2026-11-12.jsonl`; pass notes in `northglenn-usps-2026-11-12.md`). Official location pages were fetched on 2026-11-12, each on the first try: 1439617 Northglenn (HTTP 200) and 1375562 Northview (HTTP 200). Hours and services come from the same official locator record those pages display; retail hours means the BUSINESS hours block only.
- **City limits:** every candidate address was checked with the U.S. Census Bureau Geocoder (https://geocoding.geo.census.gov/geocoder/, address endpoint, Public_AR_Current / Current_Current, Incorporated Places, Census Designated Places and Counties layers) on 2026-11-12. Raw results: `northglenn-usps-geocoder-2026-11-12.jsonl` (all 71 Post Office records) and `northglenn-stores-geocoder-2026-11-12.jsonl` (all 21 King Soopers and Walmart Supercenter rows in the research CSV; the two Neighborhood Markets were not geocoded because they are excluded by policy).
- **Fallback checks:** Census 2020 benchmark (Public_AR_Census2020) and current one-line lookups for the two Northglenn-printed Post Office addresses (11887 Washington St, 850 W 112th Ave). Current-benchmark coordinates lookups of every official USPS locator map point. Raw results: `northglenn-geocoder-fallback-2026-11-12.jsonl`. Every in-scope King Soopers and Walmart Supercenter address matched the current file, so no store-page map-point fallback was used. OpenStreetMap points were not used for any decision. The listed Post Office matches the current file, the 2020 file, and its official locator map point, all in Northglenn city.
- Fees reuse existing rows in `data/providers/fees.csv`. No new fee rows or brands.

## USPS

| Office | Address | Geocoder | Services | Retail hours |
|---|---|---|---|---|
| Northglenn (1439617) | 11887 Washington St 80233 | Northglenn city (11887 WASHINGTON ST, NORTHGLENN, CO, 80233; Adams County). 2020 file agrees; official locator point (39.91231, -104.978533) also Northglenn city | Domestic and Inquiry Money Orders | Mon-Fri 08:30-18:00, Sat 09:30-12:30, Sun closed |

- Northglenn Post Office: Open weekends (Saturday) and Open evenings (weekday retail closes at 18:00, which is after 17:00). Phone 303-452-2316. URL https://tools.usps.com/locations/details/1439617. verification_status `verified_official_locator`. The 24-hour lobby, PO box access, and self-service kiosk are not retail and are not used. Passports are not listed. No duplicate or SDC record at 11887 Washington St.

### Left out (not held)

- **Northview 1375562** (850 W 112th Ave, Northglenn 80234, 303-457-6991): carrier/delivery unit only (CARRIER, DELIVERYUNIT, CALLREFERRAL, and pickup codes); no retail hours and no money orders, so nothing to list. Current and 2020 files and the locator point (39.899381, -104.99803) all place it in Northglenn city. Left out as a no-services unit, not a hold.
- Printed another place and the geocoder agrees it is outside Northglenn: Eastlake 1361915, printed Eastlake 80614 (no current-file address match; official locator point in Thornton city; this is an existing Thornton hold and is not listed here); Westminster 1439640 and Harris Park 1366303 (Westminster city); North Pecos 1375398, printed Denver 80221 (Sherrelwood CDP, unincorporated Adams County); Broomfield 1356062 (Broomfield city) and Broomfield Eagle View 1361605 (no address match; locator point in Broomfield city); Commerce City 1358845 and Adams City 1439552 (Commerce City city); Dupont 1361498, printed Commerce City (Derby CDP); Henderson 1366713 (unincorporated Adams County); Brighton 1355853 (Brighton city) and Brighton Carrier Annex 1555032 (no retail and no money orders; locator point in Brighton city); Arvada and Indian Tree (Arvada city); Erie 1362695 (Erie town) and Erie Carrier Annex; Lafayette 1369494 (Lafayette city) and Lafayette Carrier Annex; Louisville 1371024, printed Superior (Louisville city); and the farther offices in the 15-mile sweeps (Dacono, Frederick, Firestone, Fort Lupton, Denver, Aurora, Wheat Ridge, Edgewater, Golden, Lakewood, Englewood, Littleton, Centennial, Greenwood Village, Boulder, and others). No office in the sweep is printed Thornton or Federal Heights.
- No Post Office printed with another city geocodes inside Northglenn city (address geocode or locator map point). USPS contract postal units and Approved Postal Providers were not collected.

## King Soopers and Walmart

Official store pages were opened in a browser on 2026-11-12 (read-only; no sign-in, no store contact). Raw results: `docs/research/step8-browser/northglenn-walmart-ks-2026-11-12.csv` and `.md` (23 rows: 14 King Soopers, 7 Walmart Supercenters, 2 Walmart Neighborhood Markets excluded by policy). The official King Soopers locator for “Northglenn, CO” returned no grocery store that prints Northglenn. Walmart's official Northglenn directory lists only Neighborhood Market 4747. No Walmart Supercenter prints Northglenn. No unexpected grocery or retail brands appeared. Every in-scope Supercenter and King Soopers address was run through the Census geocoder on 2026-11-12; all 21 matched the current file.

### Added

None. No King Soopers and no Walmart Supercenter prints Northglenn, so there is no store row to add.

### Held for Richard

None. No store printed with another city geocodes inside Northglenn city.

Priority nearby stores that were checked because they might sit inside Northglenn, but the current-file geocoder places each outside the city, in agreement with the printed city except as noted:

- **King Soopers 00024** 104th and Washington, 750 E 104Th Ave Unit A, prints Thornton 80233. Current file: 750 E 104TH AVE, THORNTON, CO, 80233, **Thornton city**. Left out, not a hold.
- **King Soopers 00068** Mission Trace, 3801 E 120Th Ave, prints Thornton 80233. Current file: 3801 E 120TH AVE, THORNTON, CO, 80233, **Thornton city**. Left out, not a hold.
- **Walmart Supercenter 1231**, 9901 Grant St, prints Thornton 80229. Current file: 9901 GRANT ST, THORNTON, CO, 80229, **Thornton city**. Left out, not a hold.
- **King Soopers 00034** Federal Heights, 1575 W 84Th Ave, prints Denver 80260. Current file: 1575 W 84TH AVE, DENVER, CO, 80260, **Federal Heights city**. Outside Northglenn; already in scope for Federal Heights, not a Northglenn hold.
- **Walmart Supercenter 4567**, 7101 E 128th Ave, prints Brighton 80602. Current file: 7101 E 128TH AVE, BRIGHTON, CO, 80602, **Thornton city**. Already held off both Brighton and Thornton; not added here, and `thornton.csv` was not edited.

### Left out (not held)

- Printed another city, and the geocoder agrees it is outside Northglenn (already-live stores in other cities were not changed):
  - **Thornton** (Thornton city): King Soopers 00024, 00068, 00101, 00116; Walmart Supercenter 1231.
  - **Westminster** (Westminster city): King Soopers 00062, 00055; Walmart Supercenters 3867, 3824, 2223.
  - **Broomfield** (Broomfield city): King Soopers 00118, 00086, 00089; Walmart Supercenter 4288.
  - **Commerce City** (Commerce City city): King Soopers 00092, 00114; Walmart Supercenter 2752.
  - **Arvada** (Arvada city): King Soopers 00121, 00036.
  - **Federal Heights** (Federal Heights city): King Soopers 00034 (prints Denver; named Federal Heights).
  - **Thornton, already held:** Walmart Supercenter 4567 (prints Brighton; see above).
- Walmart Neighborhood Markets 4747 (Northglenn, 10755 Washington St; official page shows no Money Services label) and 3019 (Thornton): excluded by policy. 4747 is not a hold.

## Not changed

- Thornton holds (Eastlake Post Office, Walmart 4567), `thornton.csv`, `brighton.csv`, `windsor.csv`, `erie.csv`, and every other city CSV; Grand Junction's Fruitvale hold; the Castle Rock Post Office; City Market; Littleton holds; Erie 00129/00138. No Lafayette files. Later batch cities were not started.

## Not collected

- Payday / title-loan storefronts, including ACE: omitted by policy.
- Stand-alone Western Union / MoneyGram agents and other grocery brands were not collected.
