# Step 8: Longmont (2026-11-12, America/Denver)

**Rows:** 6 (1 USPS, 3 King Soopers, 2 Walmart Supercenters). City 4 of the batch approved on 2026-11-12 (Pueblo, Centennial, Boulder, Longmont, Castle Rock; ranked from Census Vintage 2025, SUB-IP-EST2025-POP-08). Only addresses inside Longmont city limits are listed. No businesses were contacted.

**Counts:** 6 locations; 4 money orders (1 USPS, 3 King Soopers); 0 check cashing; 0 bill pay; 0 prepaid reload. Labels on the hub: 6 Open evenings, 6 Open weekends. The evenings/weekends page lists the 4 money-order locations (4 Open evenings, 4 Open weekends); the two Walmart Supercenters are hub-only ("Money Services, call ahead"). No check-cashing or bill-pay page (zero listings).

## Method

- **USPS:** official USPS Location Finder (tools.usps.com, `locationType` PO), same method as Boulder/Centennial/Pueblo. Searches at 5 and 15 miles around Longmont ZIPs (80501, 80502, 80503, 80504) returned 23 Post Office records. The official record for the one Longmont-printed office (`https://tools.usps.com/locations/details/1370889`) was read on 2026-11-12. Retail (BUSINESS) hours, phone, and services come from that record; lobby, passport, and collection hours are not used.
- **City limits:** every candidate address was checked with the U.S. Census Bureau Geocoder (https://geocoding.geo.census.gov/geocoder/, address endpoint, Public_AR_Current / Current_Current, Incorporated Places and Census Designated Places layers) on 2026-11-12. Raw results: `docs/research/step8-browser/longmont-usps-geocoder-2026-11-12.jsonl` (all 23 Post Office records) and `longmont-stores-geocoder-2026-11-12.jsonl` (all 36 store pages).
- **Fallback checks** for addresses with no current-benchmark match: Census 2020 benchmark (Public_AR_Census2020) and current-benchmark one-line retries, plus coordinates lookups (current benchmark) of map points. Raw results: `longmont-geocoder-fallback-2026-11-12.jsonl`. Only one listed row needed the fallback (Walmart 5370, below).
- Fees reuse existing rows in `data/providers/fees.csv`. No new fee rows or brands.

## USPS

| Office | Address | Geocoder | Services | Retail hours |
|---|---|---|---|---|
| Longmont (1370889) | 201 Coffman St 80501 | Longmont city (201 COFFMAN ST, LONGMONT, CO, 80501) | Domestic and Inquiry Money Orders | Mon-Fri 09:00-17:30, Sat 09:00-13:00, Sun closed |

- Longmont Post Office: Open evenings and Open weekends. Phone 303-776-2387.
- No other Longmont-printed Post Office (and no duplicate record at 201 Coffman St) appeared in the locator results.

Out of city (printed another place, and the geocoder agrees or found no match): Niwot 1375136 (Niwot CDP, unincorporated); Hygiene 1367788 (no address match on the current or 2020 file; its official locator point 40.189394, -105.17769 is in no incorporated place or CDP); Mead 1372465 (Mead town); Erie 1362695 and Erie Carrier Annex 1546616 (Erie town); Firestone 1363406 (Firestone town); Frederick 1364064 (Frederick town); Dacono 1360137 (Dacono city); Lyons 1371280 (Lyons town); Berthoud 1354778 (Berthoud town); Boulder 1355494, High Mar 1366905, Valmont 1385692 and Boulder CO SDC 1612987 (Boulder city); Lafayette 1369494 and Lafayette Carrier Annex 1369484 (Lafayette city); Louisville 1371024 (printed Superior, Louisville city); Jamestown, Platteville, Fort Lupton, Johnstown and Milliken farther out. No Post Office printed with another city geocodes inside Longmont. USPS contract postal units and Approved Postal Providers were not collected.

## King Soopers and Walmart

Official store pages were opened in a browser on 2026-11-12 (read-only; no sign-in, no store contact). Raw results: `docs/research/step8-browser/longmont-walmart-ks-2026-11-12.csv` and `.md` (36 detail pages: 29 King Soopers, 7 Walmart Supercenters). Walmart's store finder returned no stores for "Longmont, CO", so Walmart's official city store directories were used (Longmont lists 2; Erie, Firestone, Frederick, Boulder, Louisville, Mead, Niwot and Lyons list none). No Neighborhood Market pages appeared. No unexpected grocery or retail brands appeared. Every address was run through the Census geocoder on 2026-11-12.

### Added (5 rows)

| Store | Address | Geocoder | Services listed |
|---|---|---|---|
| King Soopers 00102 Pace Street | 1611 Pace St 80504 | Longmont city (1611 PACE ST, LONGMONT, CO, 80504) | Money orders (and Money Services) |
| King Soopers 00080 Hover Street | 995 S Hover St 80501 | Longmont city (995 HOVER ST, LONGMONT, CO, 80501) | Money orders (and Money Services) |
| King Soopers 00042 North Main | 2255 Main St 80501 | Longmont city (2255 MAIN ST, LONGMONT, CO, 80501) | Money orders (and Money Services) |
| Walmart Supercenter 905 (E Ken Pratt Blvd) | 2285 E Ken Pratt Blvd 80504 | Longmont city (2285 KEN PRATT BLVD, LONGMONT, CO, 80501) | Generic "Money Services" only (hub-only) |
| Walmart Supercenter 5370 (Main St) | 2514 Main St 80504 | No address match (current and 2020); official store-page map point in Longmont city | Generic "Money Services" only (hub-only) |

- **Spelling/geocoder notes:** the Hover Street match drops the "S" prefix (same number, street, ZIP). The Ken Pratt match drops the "E" prefix and returns ZIP 80501 where the official page prints 80504 (same number and street, Longmont city either way).
- **Walmart 5370 fallback (2514 Main St):** the Census geocoder found no address match for 2514 Main St on the current benchmark or the 2020 benchmark (variants tried: `2514 Main St, Longmont, CO 80504`, `2514 N Main St, Longmont, CO 80501`, `2514 Main St, Longmont, CO 80501`). The official page prints Longmont, CO 80504, and the store's map point embedded in its official Walmart store page (40.205153, -105.098807, read 2026-11-12) returns **Longmont city** (Boulder County, no CDP) in a Census coordinates lookup on the current benchmark. Printed city and map point agree, so the row is included under the same fallback used for the Westminster Post Office and Pueblo Midtown/Belmont, and the row's notes say so.
- **Hours:** store hours only (King Soopers Sun-Sat 6 AM-11 PM; Walmart Mon-Sun 6am-11pm). Pharmacy, fuel, sensory-friendly, and holiday hours not used. All five are Open evenings and Open weekends.
- **King Soopers:** all three Longmont pages tag "Money Orders" and "Money Services" (`money_orders=true`). No check cashing, bill pay, prepaid reload, Western Union, or MoneyGram named. "Account Funding" is not a tracked service and is not flagged. King Soopers fees stay "Not published, call ahead."
- **Walmart:** both Longmont Supercenter pages show only a generic "Money Services" label; check cashing, money orders, bill pay, and load/unload are not named, so all four flags are false. They are on the Longmont hub only, labeled to call ahead, and not on the money-order or evenings-and-weekends pages. Walmart chain fee maximums are not applied to them.

### Held for Richard

None in Longmont. Every Longmont-printed candidate is inside Longmont city (four on the current address match, Walmart 5370 on the documented map-point fallback), and no candidate printed with another city geocodes inside Longmont. (Thornton's held Eastlake Post Office and Walmart 4567 were not touched.)

### Left out

- **Other incorporated places nearby** (printed and geocoded elsewhere): Boulder (King Soopers 00028 Gun Barrel, 00061, 00033), Firestone (King Soopers 00105, 6110 Firestone Blvd; the geocoder matched 6110 FIRESTONE TRL in Firestone town), Erie (King Soopers Highway 287 and Arapahoe Road, 2900 Arapahoe Rd; Erie town), Louisville (LOUISVILLE and Louisville Marketplace, which tags check cashing), Broomfield (3 King Soopers, 2 Walmart Supercenters), Loveland (2 King Soopers, 2 Walmart Supercenters), Thornton, Westminster, Brighton, Arvada, and Federal Heights (King Soopers printed Denver). None is a Longmont candidate, and no existing city CSV was changed.
- **No address match, printed elsewhere:** King Soopers Frederick (5801 Silverstone Dr, Frederick 80504) and VISTA RIDGE (1891 State Highway 7, Erie) had no match on the current or 2020 file; Walmart 1045 (745 US Highway 287, Lafayette) had no address match, and its official store-page map point (40.005992, -105.105136) returns Lafayette city. As a supplementary (non-official) check, OpenStreetMap points for the Frederick store (40.0898221, -104.9442011) and for State Highway 7 near Erie return Frederick town and Erie town in Census coordinates lookups. None of these points falls inside Longmont, and none of these pages prints Longmont.
- Fuel centers are not separate rows. Walmart Neighborhood Markets are excluded by policy (none appeared for Longmont).

## Not collected

- Payday / title-loan storefronts, including ACE: omitted by policy.
- Stand-alone Western Union / MoneyGram agents and other grocery brands (Safeway, Sprouts, etc.) were not collected.
