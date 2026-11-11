# Step 8: Fort Collins (2026-11-11, America/Denver)

**Rows:** 9 (2 USPS, 2 Walmart Supercenters hub-only, 5 King Soopers). City 2 of the approved six-city batch (Colorado Springs, Fort Collins, Thornton, Arvada, Westminster, Greeley). Only addresses inside Fort Collins city limits are listed. No businesses were contacted.

**Counts:** 9 locations; 7 money orders (2 USPS, 5 King Soopers); 1 check cashing (King Soopers Midtown Marketplace); 0 bill pay; 0 prepaid reload. Labels: 8 Open evenings, 9 Open weekends (the evenings/weekends page shows 7 because the two hub-only Walmart rows list no service).

## Method

- **USPS:** official USPS Location Finder (tools.usps.com, `locationType` PO). Searches at 5 and 15 miles around every Fort Collins ZIP (80521-80528, 80553). Each candidate's official record (`https://tools.usps.com/locations/details/<id>`) was read on 2026-11-11, and the address, phone, posted retail (BUSINESS) hours, and money-order services were copied from it.
- **City limits:** every candidate address was checked with the U.S. Census Bureau Geocoder (https://geocoding.geo.census.gov/geocoder/, address endpoint, Public_AR_Current / Current_Current, Incorporated Places and Census Designated Places layers) on 2026-11-11. The `city` column keeps the official mailing city.
- Fees reuse existing rows in `data/providers/fees.csv`. No new fee rows or brands.

## USPS included (2)

| USPS id | Office | Address | Mon-Fri | Sat | Labels |
|---|---|---|---|---|---|
| 1363754 | Fort Collins (main) | 301 Boardwalk Dr 80525 | 09:00-18:00 | 09:00-13:00 | Open evenings, Open weekends |
| 1376040 | Old Town | 301 S Howes St (Fl 1) 80521 | 09:00-17:00 | 10:00-14:00 | Open weekends |

Both list Domestic and Inquiry Money Orders. Sunday is closed. `money_orders=true`; check cashing, bill pay, and prepaid reload false (not listed). The geocoder matched 301 Boardwalk Dr as 301 E Boardwalk Dr (same number, street, ZIP).

## USPS not listed separately or excluded

- **Fort Collins CO SDC 1601572**: same address (301 Boardwalk Dr), phone, and retail hours as 1363754; a second locator entry for the same building. Not listed twice.
- Laporte, Bellvue, Timnath, Wellington, Windsor, Loveland, Valentine (Loveland), Masonville, Severance, Johnstown, Berthoud, Milliken, Drake, and the Windsor Carrier Annex have non-Fort Collins mailing cities and are outside the city.
- USPS contract postal units and Approved Postal Providers were not collected.

## Walmart Supercenters and King Soopers

Official store pages were opened in a browser on 2026-11-11 (read-only; no sign-in, no store contact). Raw results: `docs/research/step8-browser/fort-collins-walmart-ks-2026-11-11.csv` and `.md` (28 detail pages: 11 King Soopers from a 19-result, 3-page locator search; 17 Walmart Supercenters from the Walmart finder's 50-mile set for ZIP 80524, no Neighborhood Markets). Every Fort Collins, Timnath, Windsor, and Loveland address was run through the Census geocoder on 2026-11-11.

### Added (7 rows)

| Store | Address | Geocoder | Services listed |
|---|---|---|---|
| Walmart Supercenter 2729 | 1250 E Magnolia St 80524 | Fort Collins city | Money Services / Financial Services only: hub only, all flags false |
| Walmart Supercenter 3177 | 4625 S Mason St 80525 | Fort Collins city | Money Services / Financial Services only: hub only, all flags false |
| King Soopers 00099 North College Marketplace | 1842 N College Ave 80524 | Fort Collins city | Money orders |
| King Soopers 00009 Cedarwood | 1015 S Taft Hill Rd 80521 | Fort Collins city | Money orders |
| King Soopers 00146 Midtown Marketplace | 2535 S College Ave 80525 | Fort Collins city | Check cashing, money orders (also lists Western Union, not mapped) |
| King Soopers 00097 Timberline | 2602 S Timberline Rd 80525 | Fort Collins city | Money orders |
| King Soopers 00073 JFK Parkway | 4503 John F Kennedy Pkwy 80525 | Fort Collins city | Money orders |

- **Hours:** Walmart rows use store hours (Mon-Sun 6am-11pm). King Soopers rows use store hours (Sun-Sat 6 AM-11 PM), never pharmacy or fuel hours. All seven are labeled Open evenings and Open weekends; the Walmart rows do not appear on the evenings/weekends page because they list no service.
- **Walmart:** both Fort Collins Supercenter pages show only the generic "Money Services" feature and "Financial Services" under other services; check cashing, money orders, bill pay, and load/unload are not named. All four flags are false; hub-only with "call ahead" copy. Chain fees are not applied.
- **King Soopers:** `money_orders=true` only where the page tagged "Money Orders" (all five). Midtown Marketplace is the only page that tagged "Check Cashing", so it is the only `check_cashing=true` row and the only entry on `/fort-collins/check-cashing/`. No page tagged bill pay or prepaid reload, so there is no bill-pay page.
- No new fee rows. King Soopers fees stay "Not published, call ahead."

### Held for Richard

None. All seven printed-Fort Collins store addresses matched inside Fort Collins city on the Census geocoder; no city disagreements and no unmatched addresses.

### Left out

- Out of city (geocoder confirmed): Walmart 4599 Timnath (4500 Weitzel St, Timnath town), Walmart 1008 and 953 Loveland, King Soopers 00104 Windsor (Windsor town), 00044 and 00074 Loveland. Greeley, Longmont, Lafayette, Brighton, Westminster, Broomfield, and Cheyenne WY results are other cities (Greeley and Westminster are later batch cities and were not started).
- Walmart Neighborhood Markets: none in the Fort Collins finder results. Fuel centers are not separate rows.

### Coverage limits

King Soopers locator: 19 results on 3 pages; every Fort Collins, Windsor, Loveland, and Greeley result was opened. Walmart finder: one 50-mile result set of 17, all opened. The browser pass reported a brief Walmart "Robot or human?" challenge that cleared; no targeted page remained incomplete.

## Not collected

- Payday / title-loan storefronts, including ACE: omitted by policy.
- Stand-alone Western Union / MoneyGram agents and other grocery brands (City Market, Safeway, etc.) were not collected; no other-brand leads were recorded by the browser pass.
