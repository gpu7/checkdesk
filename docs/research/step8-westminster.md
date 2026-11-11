# Step 8: Westminster (2026-11-11, America/Denver)

**Rows:** 7 (2 USPS, 2 King Soopers, 3 Walmart Supercenters hub-only). City 5 of the approved six-city batch (Colorado Springs, Fort Collins, Thornton, Arvada, Westminster, Greeley). Only addresses inside Westminster city limits are listed. No businesses were contacted.

**Counts:** 7 locations; 4 money orders (2 USPS, 2 King Soopers); 0 check cashing; 0 bill pay; 0 prepaid reload. Labels on the hub: 6 Open evenings, 7 Open weekends. The evenings/weekends page lists 4 (3 Open evenings, 4 Open weekends) because the three hub-only Walmart rows list no service; Harris Park closes at 17:00 on weekdays, so it is Open weekends only. No check-cashing or bill-pay page (zero listings).

## Method

- **USPS:** official USPS Location Finder (tools.usps.com, `locationType` PO). Searches at 5 and 15 miles around Westminster-area ZIPs (80030, 80031, 80003, 80020, 80021, 80023, 80005, 80234, 80260, 80221, 80233, 80241). Each candidate's official record (`https://tools.usps.com/locations/details/<id>`) was read on 2026-11-11. Retail (BUSINESS) hours, phone, and services come from that record.
- **City limits:** every candidate address was checked with the U.S. Census Bureau Geocoder (https://geocoding.geo.census.gov/geocoder/, address endpoint, Public_AR_Current / Current_Current, Incorporated Places and Census Designated Places layers) on 2026-11-11. Raw results: `docs/research/step8-browser/westminster-usps-geocoder-2026-11-11.jsonl` and `westminster-stores-geocoder-2026-11-11.jsonl`.
- Fees reuse existing rows in `data/providers/fees.csv`. No new fee rows or brands.

## USPS

| Office | Address | Geocoder | Services | Retail hours |
|---|---|---|---|---|
| Harris Park (1366303) | 7262 Meade St 80030 | Westminster city | Domestic Money Orders (Inquiry Money Orders not listed) | Mon-Fri 09:00-17:00, Sat 10:00-13:00, Sun closed |
| Westminster (1439640) | 3051 W 105th Ave 80031 | Westminster city (Census 2020 benchmark; see note) | Domestic and Inquiry Money Orders | Mon-Fri 09:00-18:00, Sat 09:00-13:00, Sun closed |

- Harris Park: Open weekends (Saturday). Not Open evenings (weekday close is 17:00, not after). Phone 303-487-0620. This is the office Arvada left off as in Westminster.
- Westminster Post Office: Open evenings and Open weekends. Phone 303-464-9941.
- **Geocoder note for 1439640:** the current benchmark (Public_AR_Current) returned no address match for 3051 W 105th Ave (parsed and one-line, with and without ZIP, and with "West ... Avenue" spelled out). The Census Bureau geocoder's Census 2020 benchmark (Public_AR_Census2020 / Census2020_Census2020) returned an exact address match, `3051 W 105TH AVE, WESTMINSTER, CO, 80031`, in Westminster city (Adams County). The official USPS locator point (39.887251, -105.026322) also falls inside Westminster city on the Census coordinates endpoint. The official city (Westminster) and the geocoder agree, so this is listed, not held. This differs from the Colorado Springs General Mail Facility, which matched on neither benchmark.

Out of city (geocoder confirmed, or other printed city): North Pecos 1375398 (1411 Cortez St, mailing Denver 80221; Sherrelwood CDP, unincorporated Adams County, same as Step 6); Northview 1375562 (850 W 112th Ave, Northglenn city); Northglenn 1439617 (Northglenn city); Broomfield 1356062 (Broomfield city); Broomfield Eagle View 1361605 (8800 W 116th Cir, printed Broomfield; no address match, locator point in Broomfield city); Indian Tree 1367908 (already on the Arvada page). Eastlake 1361915 remains held from Thornton and was not touched. USPS contract postal units and Approved Postal Providers were not collected.

## Walmart Supercenters and King Soopers

Official store pages were opened in a browser on 2026-11-11 (read-only; no sign-in, no store contact). Raw results: `docs/research/step8-browser/westminster-walmart-ks-2026-11-11.csv` and `.md` (49 detail pages: 31 King Soopers, 18 Walmart). Every address was run through the Census geocoder on 2026-11-11; all 5 Westminster-printed stores geocode inside Westminster city, and no store printed with another city geocodes inside Westminster.

### Added (5 rows)

| Store | Address | Geocoder | Services listed |
|---|---|---|---|
| King Soopers 00062 104th and Federal | 10351 Federal Blvd 80260 | Westminster city | Money orders |
| King Soopers 00055 Wadsworth and Church Ranch | 9983 Wadsworth Pkwy 80021 | Westminster city | Money orders |
| Walmart Supercenter 3824 Westminster 7155 Sheridan Blvd | 7155 Sheridan Blvd 80003 | Westminster city | Money Services only: hub only, all flags false |
| Walmart Supercenter 2223 Westminster 9499 Sheridan Blvd | 9499 Sheridan Blvd 80031 | Westminster city | Money Services only: hub only, all flags false |
| Walmart Supercenter 3867 Westminster W 136th Ave | 200 W 136th Ave 80234 | Westminster city | Money Services only: hub only, all flags false |

- **Hours:** store hours only (Walmart Mon-Sun 6am-11pm; King Soopers Sun-Sat 6 AM-11 PM). Pharmacy and fuel hours not used. All five are Open evenings and Open weekends.
- **Walmart:** each Supercenter page shows only the generic "Money Services" label; check cashing, money orders, bill pay, and load/unload are not named. All four flags false; hub-only with "call ahead" copy; chain fees not applied; Denver Supercenter tags not copied. 3824 prints ZIP 80003 (often an Arvada ZIP) with city Westminster; the geocoder agrees (Westminster city).
- **King Soopers:** both pages tag "Money Orders" and "Money Services" (`money_orders=true`). No check cashing, bill pay, prepaid reload, Western Union, or MoneyGram named. King Soopers fees stay "Not published, call ahead."

### Held for Richard

None in Westminster. Every Westminster-printed candidate matched inside Westminster city. (Thornton's held Eastlake Post Office and Walmart 4567 were not touched.)

### Left out

- Out of city (geocoder confirmed): King Soopers 00121, 00036, 00003, 00045, 00085, 00137 (Arvada); 00034 Federal Heights (1575 W 84th Ave, printed Denver; Federal Heights city, already on that page); 00024, 00068, 00101, 00116 (Thornton); 00086, 00089, 00118 (Broomfield); 00057, 00020 (Wheat Ridge); 00092 (Commerce City); 00090 (Edgewater); 00060, 00127 (Lakewood); 00142 Louisville Marketplace (Louisville; its check-cashing tag is not used here) and 00013 (Louisville); 00138 (Erie town); Denver stores. King Soopers 00129 Vista Ridge (printed Erie) had no geocoder match and is not a Westminster candidate. Walmart Supercenters 4288 and 5341 (Broomfield), 4734 (Arvada), 1231 (Thornton), 5957 (Lakeside town), 2752 (Commerce City), 4284 and 2125 (Lakewood), 5676 and 3533 (Denver), 3566 (printed Denver; Aurora city). Existing city CSVs were not changed.
- Walmart Neighborhood Markets 3019 (Thornton), 4747 (Northglenn), 3128 (Four Square Mile CDP), 3127 (Denver): omitted by policy. Fuel centers are not separate rows.

### Coverage limits

King Soopers locator: 33 results on 4 pages; 31 grocery pages opened. Walmart's Westminster finder returned "0 stores", so the browser pass used Walmart's store directory and nearby-store listings; a press-and-hold check appeared and was completed. No new-brand leads surfaced.

## Not collected

- Payday / title-loan storefronts, including ACE: omitted by policy.
- Stand-alone Western Union / MoneyGram agents and other grocery brands (Safeway, Sprouts, etc.) were not collected.
