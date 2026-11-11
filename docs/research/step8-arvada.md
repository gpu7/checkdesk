# Step 8: Arvada (2026-11-11, America/Denver)

**Rows:** 10 (2 USPS, 7 King Soopers, 1 Walmart Supercenter hub-only). City 4 of the approved six-city batch (Colorado Springs, Fort Collins, Thornton, Arvada, Westminster, Greeley). Only addresses inside Arvada city limits are listed. No businesses were contacted.

**Counts:** 10 locations; 8 money orders (2 USPS, 6 King Soopers); 0 check cashing; 0 bill pay; 0 prepaid reload. Labels: 10 Open evenings, 10 Open weekends on the hub (the evenings/weekends page shows 8 because the two hub-only rows, Walmart and King Soopers Candelas, list no service). No check-cashing or bill-pay page (zero listings).

## Method

- **USPS:** official USPS Location Finder (tools.usps.com, `locationType` PO). Searches at 5 and 15 miles around Arvada-area ZIPs (80001-80007, 80403, 80033, 80212, 80221, 80030, 80031, 80020, 80021). Each candidate's official record (`https://tools.usps.com/locations/details/<id>`) was read on 2026-11-11. Retail (BUSINESS) hours are used.
- **City limits:** every candidate address was checked with the U.S. Census Bureau Geocoder (https://geocoding.geo.census.gov/geocoder/, address endpoint, Public_AR_Current / Current_Current, Incorporated Places and Census Designated Places layers) on 2026-11-11. Raw results: `docs/research/step8-browser/arvada-usps-geocoder-2026-11-11.jsonl` and `arvada-stores-geocoder-2026-11-11.jsonl`.
- Fees reuse existing rows in `data/providers/fees.csv`. No new fee rows or brands.

## USPS

| Office | Address | Geocoder | Services | Retail hours |
|---|---|---|---|---|
| Arvada (1353434) | 5885 Allison St 80004 | Arvada city | Domestic and Inquiry Money Orders | Mon-Fri 09:00-17:30, Sat 10:00-14:00, Sun closed |
| Indian Tree (1367908) | 7765 Wadsworth Blvd 80003 | Arvada city | Domestic and Inquiry Money Orders | Mon-Fri 09:00-17:30, Sat 10:00-14:00, Sun closed |

Both are Open evenings (open after 17:00 on weekdays) and Open weekends (Saturday).

Out of city: Harris Park, 7262 Meade St, Westminster 80030 (geocoder: Westminster city; Westminster is a later batch city and was not started). Wheat Ridge (4210 Wadsworth Blvd) is already on the Wheat Ridge page. Golden, Alcott (Denver), Broomfield, and other results are other cities. USPS contract postal units and Approved Postal Providers were not collected.

## Walmart Supercenters and King Soopers

Official store pages were opened in a browser on 2026-11-11 (read-only; no sign-in, no store contact). Raw results: `docs/research/step8-browser/arvada-walmart-ks-2026-11-11.csv` and `.md` (41 detail pages: 27 King Soopers, 14 Walmart). Every address was run through the Census geocoder on 2026-11-11; all 8 Arvada-printed stores geocode inside Arvada city.

### Added (8 rows)

| Store | Address | Geocoder | Services listed |
|---|---|---|---|
| Walmart Supercenter 4734 Arvada | 9400 Ralston Rd 80002 | Arvada city | Money Services only: hub only, all flags false |
| King Soopers 00022 58th and Ralston | 9731 W 58th Ave 80002 | Arvada city | Money orders |
| King Soopers 00003 Lloyd King Center | 6350 Sheridan Blvd 80003 | Arvada city (Adams County part) | Money orders |
| King Soopers 00036 Lake Arbor | 8031 Wadsworth Blvd 80003 | Arvada city | Money orders |
| King Soopers 00121 80th and Sheridan | 8055 Sheridan Blvd 80003 | Arvada city | Money orders |
| King Soopers 00045 64th and Ward | 12350 W 64th Ave 80004 | Arvada city | Money orders |
| King Soopers 00085 Westwoods | 15200 W 64th Ave 80007 | Arvada city | Money orders |
| King Soopers 00137 Candelas | 14967 Candelas Pkwy 80007 | Arvada city (matched as "Candeles Pkwy", same number and ZIP) | Money Services only: hub only, all flags false |

- **Hours:** store hours only (Walmart Mon-Sun 6am-11pm; King Soopers Sun-Sat 6 AM-11 PM). Pharmacy and fuel hours not used. All eight are Open evenings and Open weekends.
- **Walmart:** the Arvada Supercenter page shows only the generic "Money Services" label; check cashing, money orders, bill pay, and load/unload are not named. All four flags false; hub-only with "call ahead" copy; chain fees not applied; Denver Supercenter tags not copied.
- **King Soopers:** six pages tag "Money Orders" (`money_orders=true`). Candelas shows only the generic "Money Services" label, so all its flags are false (hub-only, like Aurora Nine Mile and Colorado Springs Academy and Austin Bluffs). No page tagged Check Cashing, bill pay, or prepaid reload. No Western Union or MoneyGram text recorded. King Soopers fees stay "Not published, call ahead."

### Held for Richard

None. Every Arvada-printed candidate matched on the geocoder inside Arvada city.

### Left out

- Out of city (geocoder confirmed): Walmart Supercenters 3824 (7155 Sheridan Blvd, Westminster city, printed Westminster 80003), 2223 and 3867 (Westminster), 5957 (5957 W 44th Ave, Lakeside town), 4288 and 5341 (Broomfield), 2125 and 4284 (Lakewood), 1231 (Thornton, already listed), 5676 (Denver), 2752 (Commerce City). King Soopers 00055 Wadsworth and Church Ranch and 00062 104th and Federal (Westminster), 00057 Ridge Village and 00020 Applewood (Wheat Ridge), 00090 Sloans Lake (Edgewater), 00082 Golden Road (Golden), 00086 and 00089 (Broomfield), 00034 (Federal Heights), Denver, Lakewood, Thornton, and Commerce City stores. Existing city CSVs were not changed.
- Walmart Neighborhood Markets: none inside Arvada; 3019 (Thornton) and 4747 (Northglenn) are not listed by policy. The Green Mountain fuel result was skipped (fuel centers are not separate rows).

### Coverage limits

King Soopers locator: 28 results on 4 pages; 27 grocery pages opened. Walmart's Arvada finder returned "0 stores", so the browser pass used Walmart's store directory and nearby-store listings; a press-and-hold check appeared and was completed. No new-brand leads surfaced.

## Not collected

- Payday / title-loan storefronts, including ACE: omitted by policy.
- Stand-alone Western Union / MoneyGram agents and other grocery brands (Safeway, Sprouts, etc.) were not collected.
