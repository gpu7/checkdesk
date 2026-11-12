# Step 8: Broomfield (2026-11-12, America/Denver)

**Rows:** 7 (2 Post Offices, 3 King Soopers, 2 Walmart Supercenters). City 2 of the batch approved on 2026-11-12 (Loveland, Broomfield, Grand Junction, Parker, Littleton; ranked from Census Vintage 2025, SUB-IP-EST2025-POP-08). Only addresses inside the City and County of Broomfield (incorporated place, "Broomfield city" / Broomfield County in the Census geocoder) are listed. No businesses were contacted.

**Counts:** 7 locations; 5 money orders (2 Post Offices, 3 King Soopers); 0 check cashing; 0 bill pay; 0 prepaid reload. Labels on the hub: 7 Open evenings, 7 Open weekends. The evenings/weekends page lists the 5 money-order locations (5 Open evenings, 5 Open weekends). Both Walmart Supercenters are hub-only ("Money Services, call ahead"). No check-cashing or bill-pay page (zero listings).

## Method

- **USPS:** official USPS Location Finder (tools.usps.com, `locationType` PO), same method as Loveland/Castle Rock/Longmont. Searches at 5 and 15 miles around Broomfield ZIPs (80020, 80021, 80023, 80038) returned 52 Post Office records (`docs/research/step8-browser/broomfield-usps-locator-2026-11-12.jsonl`). Rows link the official location pages (`https://tools.usps.com/locations/details/<id>`); hours and services come from the same official locator record those pages display. Both listed offices' official location pages were also loaded on 2026-11-12 and show Money Orders.
- **City limits:** every candidate address was checked with the U.S. Census Bureau Geocoder (https://geocoding.geo.census.gov/geocoder/, address endpoint, Public_AR_Current / Current_Current, Incorporated Places, Census Designated Places and Counties layers) on 2026-11-12. Raw results: `broomfield-usps-geocoder-2026-11-12.jsonl` (all 52 Post Office records) and `broomfield-stores-geocoder-2026-11-12.jsonl` (all 37 store pages).
- **Fallback checks** for addresses with no current-benchmark match: Census 2020 benchmark (Public_AR_Census2020) one-line lookups, plus coordinates lookups (current benchmark) of official USPS locator points. For one out-of-area King Soopers page with no address match and no official map point in the research file (Vista Ridge, Erie), an OpenStreetMap point was used as a supplementary, non-official check. Raw results: `broomfield-geocoder-fallback-2026-11-12.jsonl`. One listed row used the fallback (Eagle View Post Office, below).
- Fees reuse existing rows in `data/providers/fees.csv`. No new fee rows or brands.

## USPS

| Office | Address | Geocoder | Services | Retail hours |
|---|---|---|---|---|
| Broomfield (1356062) | 280 E 1st Ave 80020 | Broomfield city (280 E 1ST AVE, BROOMFIELD, CO, 80020; Broomfield County) | Domestic and Inquiry Money Orders | Mon-Fri 08:00-18:00, Sat 09:00-13:00, Sun closed |
| Eagle View (1361605) | 8800 W 116th Cir 80021 | No address match (current or 2020 file); official locator point (39.902597, -105.097138) is in Broomfield city, Broomfield County | Domestic and Inquiry Money Orders | Mon-Fri 09:00-17:30, Sat 09:00-13:00, Sun closed |

- Broomfield Post Office: Open evenings and Open weekends. Phone 303-438-0035. Its official locator point also returns Broomfield city.
- Eagle View Post Office: Open evenings and Open weekends. Phone 303-466-9669. Official locator name "BROOMFIELD EAGLE VIEW", printed city Broomfield. **Fallback:** the Census geocoder found no match for 8800 W 116th Cir on the current or 2020 address file; the official printed city is Broomfield and the official USPS locator point falls inside Broomfield city on the Census coordinates lookup (current benchmark). Included the same way as the Westminster Post Office and Longmont Walmart 5370.
- No other Broomfield-printed Post Office, and no duplicate record at either address, appeared in the locator results. No Broomfield-printed office was found without money orders.

Out of city (printed another place, and the geocoder or fallback agrees it is outside Broomfield): Westminster 1439640 (no current match; 2020 file and official locator point return Westminster city; already live and unchanged) and Harris Park 1366303 (Westminster city); Northglenn 1439617 and Northview 1375562 (Northglenn city; Northview has no retail hours or money orders); Louisville 1371024 (printed Superior, 566 S McCaslin Blvd; geocoder returns Louisville city); Lafayette 1369494 and Lafayette Carrier Annex 1369484 (Lafayette city); Erie 1362695 and Erie Carrier Annex 1546616 (Erie town); Arvada 1353434 and Indian Tree 1367908 (Arvada city); Eastlake 1361915 (no current or 2020 match; official locator point returns Thornton city; this is the Thornton hold, untouched); Niwot 1375136 (Niwot CDP); Eldorado Springs 1362237 (no address match; official point in Eldorado Springs CDP); North Pecos 1375398 (Sherrelwood CDP); Dupont 1361498 (Derby CDP); Henderson 1366713 (in no place or CDP); Boulder, High Mar, Valmont and Boulder CO SDC (Boulder city); Commerce City and Adams City (Commerce City city); Edgewater 1439601 (Edgewater city); Wheat Ridge (Wheat Ridge city); Golden, Downtown Golden, Golden CO S&DC (Golden city); Lakewood and Lakewood CO SDC (no current match; 2020 file and official points return Lakewood city); Brighton and Brighton Carrier Annex (Brighton city); Dacono, Frederick, Firestone, Fort Lupton, Longmont (their own places); and the Denver offices (Denver city). No Post Office printed with another city geocodes inside Broomfield. USPS contract postal units and Approved Postal Providers were not collected.

## King Soopers and Walmart

Official store pages were opened in a browser on 2026-11-12 (read-only; no sign-in, no store contact). Raw results: `docs/research/step8-browser/broomfield-walmart-ks-2026-11-12.csv` and `.md` (37 detail pages: 27 King Soopers, 10 Walmart). The King Soopers locator returned 32 stores for "Broomfield, CO" over 4 pages; the 27 on pages 1-3 were opened. Page 4 (Union Station Denver, Sloans Lake Edgewater, Quail Street Lakewood, Frederick, Speer Blvd Denver; 12+ miles out, none printed Broomfield) was not opened. Walmart's store finder was not run; Walmart's official store directories for Broomfield, Westminster, Thornton, Northglenn, Arvada and Lafayette were used (directories for Louisville, Superior, Erie, Commerce City, Boulder, Federal Heights and Wheat Ridge list no Walmart store). The two Longmont Walmart Supercenters (5370, 905) were not re-opened; they are in `longmont-walmart-ks-2026-11-12.csv` and already geocoded in Longmont city. No unexpected grocery or retail brands appeared. Every address was run through the Census geocoder on 2026-11-12.

### Added (5 store rows)

| Store | Address | Geocoder | Services listed | Store hours |
|---|---|---|---|---|
| King Soopers 00089 Miramonte and 287 | 1150 US Highway 287 80020 | Broomfield city (1150 US HWY 287, BROOMFIELD, CO, 80020) | Money orders (and Money Services) | Sun-Sat 6 AM-11 PM |
| King Soopers 00086 Broomfield on Sheridan | 12167 Sheridan Blvd 80020 | Broomfield city (12167 SHERIDAN BLVD, BROOMFIELD, CO, 80020) | Money orders (and Money Services) | Sun-Sat 6 AM-11 PM |
| King Soopers 00118 136th and Zuni | 2355 W 136th Ave 80023 | Broomfield city (2355 W 136TH AVE, BROOMFIELD, CO, 80023) | Money orders (and Money Services) | Sun-Sat 6 AM-11 PM |
| Walmart Supercenter 4288 (Broomfield W 121st Ave Supercenter) | 4651 W 121st Ave 80020 | Broomfield city (4651 W 121ST AVE, BROOMFIELD, CO, 80020) | Generic "Money Services" only (hub-only) | Mon-Sun 6am-11pm |
| Walmart Supercenter 5341 (Broomfield Summit Blvd Supercenter) | 500 Summit Blvd 80021 | Broomfield city (500 SUMMIT BLVD, BROOMFIELD, CO, 80021) | Generic "Money Services" only (hub-only) | Mon-Sun 6am-11pm |

- **Spelling/geocoder notes:** King Soopers prints "1150 Us Highway 287" and "2355 W 136Th Ave"; the rows use "1150 US Highway 287" and "2355 W 136th Ave" (same addresses as the geocoder matches).
- **Hours:** store hours only. Pharmacy, fuel, sensory-friendly, and holiday hours not used. All five stores are Open evenings and Open weekends.
- **King Soopers:** all three Broomfield pages tag "Money Orders" and "Money Services" (`money_orders=true`). No check cashing, bill pay, prepaid reload, Western Union, or MoneyGram named. "Account Funding" is not a tracked service and is not flagged. All three pages list a fuel center; it is not a separate row. King Soopers fees stay "Not published, call ahead."
- **Walmart:** both Broomfield Supercenter pages show only a generic "Money Services" label; check cashing, money orders, bill pay, and load/unload are not named, so all four flags are false. They are on the Broomfield hub only, labeled to call ahead, and not on the money-order or evenings-and-weekends pages. Walmart chain fee maximums are not applied.

### Held for Richard

None in Broomfield. All five Broomfield-printed store pages geocode inside Broomfield city on the current address file; the Broomfield Post Office matches on the current file and the Eagle View Post Office is inside Broomfield by its official locator point (documented fallback above). No candidate printed with another city geocodes inside Broomfield. (Thornton's held Eastlake Post Office and Walmart 4567, and the Castle Rock Post Office, were not touched.)

### Left out

- **Westminster** (Westminster city; already live and unchanged): King Soopers Wadsworth and Church Ranch (9983 Wadsworth Pkwy, ZIP 80021) and 104th and Federal; Walmart 3867 (200 W 136th Ave), 2223 (9499 Sheridan Blvd), 3824 (7155 Sheridan Blvd).
- **Thornton** (Thornton city; already live and unchanged): King Soopers 104th and Washington, Mission Trace, 136th and Colorado Blvd, 136th and Quebec; Walmart 1231 (9901 Grant St).
- **Arvada** (Arvada city; already live and unchanged): King Soopers Lake Arbor, 80th and Sheridan, Candelas (geocoder matched 14967 CANDELES PKWY), Lloyd King Center, 64th and Ward, 58th and Ralston, Westwoods; Walmart 4734 (9400 Ralston Rd).
- **Federal Heights:** King Soopers Federal Heights prints "1575 W 84Th Ave, Denver, CO 80260"; the geocoder places it in Federal Heights city. Official city and geocoder both put it outside Broomfield, so it is left off, not held.
- **Louisville** (Louisville city): King Soopers LOUISVILLE and Louisville Marketplace (the only page in this pass tagging Check Cashing).
- **Erie** (Erie town): King Soopers Highway 287 and Arapahoe Road. King Soopers VISTA RIDGE (1891 State Highway 7) had no address match on the current or 2020 file; its OpenStreetMap point (supplementary, non-official) returns Erie town, matching the printed city.
- **Lafayette** (Lafayette city): Walmart 1045 (745 US Highway 287) had no address match on the current or 2020 file; its official store-page point, checked for Longmont on 2026-11-12, returns Lafayette city.
- **Boulder** (Boulder city; already live and unchanged): King Soopers Table Mesa, 30th Street Boulder, Gun Barrel. **Wheat Ridge** (Wheat Ridge city): King Soopers Ridge Village on 38th Ave, APPLEWOOD. **Commerce City** (Commerce City city): King Soopers Commerce City Plaza.
- **Walmart Neighborhood Markets:** Thornton 3019 (850 E 88th Ave; Thornton city) and Northglenn 4747 (10755 Washington St; Northglenn city) show no Money Services tag and are excluded by policy. Northglenn is not in the approved batch.
- **Longmont:** Walmart 5370 and 905 (Longmont city; already live and unchanged).
- Fuel centers are not separate rows.

## Not collected

- Payday / title-loan storefronts, including ACE: omitted by policy.
- Stand-alone Western Union / MoneyGram agents and other grocery brands (Safeway, Sprouts, etc.) were not collected.
