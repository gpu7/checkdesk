# Step 8: Brighton (2026-11-12, America/Denver)

**Rows:** 4 (1 Post Office, 2 King Soopers, 1 Walmart Supercenter). City 1 of the batch approved on 2026-11-12 (Brighton, Windsor, Erie, Northglenn, Lafayette, Fountain, Evans, Johnstown, Montrose, Louisville; ranked from Census Vintage 2025, SUB-IP-EST2025-POP-08, where Brighton is rank 21 at 45,395). Only addresses inside Brighton city (incorporated place, "Brighton city" in the Census geocoder; the city spans Adams and Weld counties) are listed. No businesses were contacted.

**Counts:** 4 locations; 3 money orders (Brighton Post Office and 2 King Soopers); 0 check cashing; 0 bill pay; 0 prepaid reload. Labels on the hub: 4 Open evenings, 4 Open weekends. The evenings/weekends page lists the 3 money-order locations (3 Open evenings, 3 Open weekends). The Walmart Supercenter at 60 W Bromley Ln is hub-only ("Money Services, call ahead"). No check-cashing or bill-pay page (zero listings). One hold: Walmart Supercenter 4567 (see below).

## Method

- **USPS:** official USPS Location Finder (tools.usps.com, `requestType` po), same method as Littleton and Parker. Searches at 5 and 15 miles around ZIPs 80601, 80602, 80603 (Brighton), 80640 (Henderson), 80022 (Commerce City), 80621 (Fort Lupton), and 80642 (Hudson) returned 58 unique Post Office records (`docs/research/step8-browser/brighton-usps-locator-2026-11-12.jsonl`). Official location pages loaded on 2026-11-12: 1355853 Brighton (HTTP 200; the first request timed out with no response and the retry returned 200), 1555032 Brighton Carrier Annex (HTTP 200), 1366713 Henderson (HTTP 200). Hours and services come from the same official locator record those pages display; retail hours means the BUSINESS hours block only.
- **City limits:** every candidate address was checked with the U.S. Census Bureau Geocoder (https://geocoding.geo.census.gov/geocoder/, address endpoint, Public_AR_Current / Current_Current, Incorporated Places, Census Designated Places and Counties layers) on 2026-11-12. Raw results: `brighton-usps-geocoder-2026-11-12.jsonl` (all 58 Post Office records) and `brighton-stores-geocoder-2026-11-12.jsonl` (all 54 store rows in the research CSV).
- **Fallback checks:** Census 2020 benchmark (Public_AR_Census2020) and current one-line lookups for the Brighton, Brighton Carrier Annex, Henderson, and Eastlake (as 12470 York St, Thornton) Post Office addresses, for Walmart 4567 and Walmart 1659, and for the two store addresses with no current-file match (King Soopers 00154 Frederick and 00129 Erie); plus current-benchmark coordinates lookups of every official USPS locator map point. Raw results: `brighton-geocoder-fallback-2026-11-12.jsonl`. No listed row relies on a fallback; every listed row matched inside Brighton city on the current address file, and the fallbacks agree.
- Fees reuse existing rows in `data/providers/fees.csv`. No new fee rows or brands.

## USPS

| Office | Address | Geocoder | Services | Retail hours |
|---|---|---|---|---|
| Brighton (1355853) | 90 N 4th Ave 80601 | Brighton city (90 N 4TH AVE, BRIGHTON, CO, 80601; Adams County). 2020 file agrees; official locator point (39.9883, -104.817812) also Brighton city | Domestic and Inquiry Money Orders | Mon-Fri 07:30-17:30, Sat 09:00-13:00, Sun closed |

- Brighton Post Office: Open evenings (open past 17:00 on weekdays; closes 17:30) and Open weekends (Saturday). Phone 303-637-0826. verification_status `verified_official_locator`.
- No duplicate or SDC record at 90 N 4th Ave.

### Out of city (left off, not held)

- **Brighton Carrier Annex 1555032** (729 Baseline Pl, Brighton 80603): carrier/delivery unit only (CALLREFERRAL, CARRIER, DELIVERYUNIT); no retail hours and no money orders, so nothing to list. No address match on the current or 2020 file; the official locator point returns Brighton city (Weld County). Left out as a no-services unit, not a hold.
- **Henderson 1366713** (12210 Brighton Rd, Henderson 80640): prints Henderson; current and 2020 files match it in no incorporated place and no CDP (unincorporated Adams County), and the locator point agrees.
- **Eastlake 1361915** (12470 York St, prints Eastlake 80614): no current match as printed; as 12470 York St, Thornton 80241 both files return Thornton city, as does the locator point. It is not a Brighton candidate. The existing Thornton hold for this office is unchanged.
- Printed another place and the geocoder agrees it is outside Brighton: Fort Lupton 1363805 (Fort Lupton city); Dupont 1361498 (Derby CDP); Commerce City 1358845 and Adams City 1439552 (Commerce City city); Northglenn 1439617 and Northview 1375562 (Northglenn city; Northview has no retail and no money orders); Hudson, Dacono, Frederick, Firestone, Keenesburg, Platteville, Gilcrest, and Mead (their own towns or cities); Erie 1362695 and Erie Carrier Annex 1546616 (Erie town); Westminster 1439640 and Broomfield Eagle View 1361605 (no current address match; locator points return Westminster city and Broomfield city); the Denver, Aurora, Arvada, Lafayette, Louisville, Broomfield, Wheat Ridge, Glendale, Edgewater, and Englewood offices; North Pecos (Sherrelwood CDP); the Aurora 1353711 / Aurora CO SDC 1613885 duplicate (Aurora city); Capitol Hill Annex 1356950 (no retail).
- No Post Office printed with another city geocodes inside Brighton (address geocode or locator map point). USPS contract postal units and Approved Postal Providers were not collected.

## King Soopers and Walmart

Official store pages were opened in a browser on 2026-11-12 (read-only; no sign-in, no store contact). Raw results: `docs/research/step8-browser/brighton-walmart-ks-2026-11-12.csv` and `.md` (54 rows: 31 King Soopers, 23 Walmart, of which six are Neighborhood Markets excluded by policy). The King Soopers locator returned 31 grocery results for "Brighton, CO"; all were opened. Walmart's store finder showed no result cards for 80601, so local Walmart pages were found through official store-page Nearby stores sections; facts come from official store pages. Walmart #3824 showed a bot check first; the official page loaded afterward. No unexpected grocery or retail brands appeared (the fuel filter surfaced only Shell / Loaf 'N Jug fuel listings, excluded). Every address was run through the Census geocoder on 2026-11-12.

### Added (3 store rows)

| Store | Address | Geocoder | Services listed | Store hours |
|---|---|---|---|---|
| King Soopers 00081 4th and Bromley Lane | 500 E Bromley Ln 80601 | Brighton city (500 E BROMLEY LN, BRIGHTON, CO, 80601) | Money orders (and Money Services) | Sun-Sat 6 AM-11 PM |
| King Soopers 00136 50th and Bridge Street | 100 N 50th Ave 80601 | Brighton city (100 N 50TH AVE, BRIGHTON, CO, 80601) | Money orders (and Money Services) | Sun-Sat 6 AM-11 PM |
| Walmart Supercenter 1659 (Brighton W Bromley Lane Supercenter) | 60 W Bromley Ln 80601 | Brighton city (60 W BROMLEY LN, BRIGHTON, CO, 80601); 2020 file agrees | Generic "Money Services" only (hub-only) | Mon-Sun 6am-11pm |

- Phones from the official pages: 00081 303-655-7555; 00136 303-637-0342; Walmart 1659 303-659-1560. All pages HTTP 200.
- **Hours:** store hours only. Pharmacy, fuel, sensory-friendly, and holiday hours not used. All three are Open evenings and Open weekends.
- **King Soopers:** both listed pages tag "Money Orders" and "Money Services" (`money_orders=true`). No check cashing, bill pay, or prepaid reload named; no Western Union mention. "Account Funding" is not a tracked service and is not flagged. King Soopers fees stay "Not published, call ahead."
- **Walmart:** the 60 W Bromley Ln page shows only a generic "Money Services" label; check cashing, money orders, bill pay, and load/unload are not named, so all four flags are false. It is on the Brighton hub only, labeled to call ahead, and not on the money-order or evenings-and-weekends pages. Walmart chain fee maximums are not applied. The page does not mention Western Union.

### Held for Richard

- **Walmart Supercenter 4567, Brighton E 128th Ave Supercenter** (7101 E 128th Ave, printed Brighton CO 80602; URL https://www.walmart.com/store/4567-brighton-co, HTTP 200; 303-209-4339; Mon-Sun 6am-11pm; generic "Money Services" only, so it would be hub-only with all four flags false). The official page prints Brighton, but the Census geocoder matches 7101 E 128TH AVE, BRIGHTON, CO, 80602 in **Thornton city** on both the current file and the 2020 file (`brighton-stores-geocoder-2026-11-12.jsonl`, `brighton-geocoder-fallback-2026-11-12.jsonl`). Because the official printed city and the geocoder disagree, it is held and not listed under Brighton. **Relationship to the Thornton hold:** this is the same store held in the Thornton pass on 2026-11-11 (`docs/research/step8-thornton.md`), where it was also not added. It remains unlisted in both cities. `data/locations/thornton.csv` and the Thornton pages were not changed. Richard may decide later whether to list it under Thornton (where the geocoder places it), keep holding it, or treat the printed city as decisive.

No other hold. Every other Brighton-printed candidate with a money service geocodes inside Brighton city on the current address file, and no store or Post Office printed with another city geocodes inside Brighton.

### Left out (not held)

- Printed another city, and the geocoder agrees it is outside Brighton (already-live stores in other cities were not changed):
  - **Thornton** (Thornton city): King Soopers 00024, 00068, 00101 (13700 Colorado Blvd), 00116 (13525 Quebec St); Walmart Supercenter 1231.
  - **Commerce City** (Commerce City city): King Soopers 00092, 00114; Walmart Supercenter 2752.
  - **Broomfield** (Broomfield city): King Soopers 00086, 00089, 00118; Walmart Supercenters 4288, 5341.
  - **Westminster** (Westminster city): King Soopers 00055, 00062; Walmart Supercenters 2223, 3824, 3867.
  - **Arvada** (Arvada city): King Soopers 00003, 00036, 00121; Walmart Supercenter 4734.
  - **Aurora** (Aurora city): King Soopers 00014, 00052; Walmart Supercenters 1492, 5334.
  - **Denver-printed:** King Soopers 00005, 00083, 00093, 00115, 00123 (Denver city), 00034 (Federal Heights city); Walmart Supercenters 3533 (Denver city) and 3566 (Aurora city).
  - **Lakewood / Lakeside:** Walmart Supercenters 2125, 4284 (Lakewood city), 5957 (Lakeside town).
  - **Louisville, Longmont, Firestone, Erie** (their own cities/towns): King Soopers 00013, 00142, 00102, 00105, 00138. Erie, Louisville, and later batch cities were not built here.
  - **No current-file match, printed another city far from Brighton:** King Soopers 00129 (1891 State Highway 7, Erie 80516) and 00154 (5801 Silverstone Dr, Frederick 80504) had no match on the current or 2020 file. Neither prints Brighton and neither is near Brighton city, so neither is a reverse-check candidate.
- **Walmart Neighborhood Markets** (excluded by standing policy): Northglenn 4747, Thornton 3019, Denver 3127, Denver 3128 (Four Square Mile CDP), Aurora 4196, Centennial 3126. None prints Brighton.
- Fuel centers and fuel-only listings (King Soopers fuel features, Shell / Loaf 'N Jug fuel results, Walmart Fuel Station tags) are not separate rows.

## Not changed

- Thornton holds (Eastlake Post Office, Walmart 4567), `thornton.csv`, and every other city CSV; Grand Junction's Fruitvale hold; the Castle Rock Post Office; City Market; Littleton holds.

## Not collected

- Payday / title-loan storefronts, including ACE: omitted by policy.
- Stand-alone Western Union / MoneyGram agents and other grocery brands were not collected.
