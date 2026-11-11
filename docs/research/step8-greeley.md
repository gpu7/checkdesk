# Step 8: Greeley (2026-11-11, America/Denver)

**Rows:** 7 (2 USPS, 3 King Soopers, 2 Walmart Supercenters hub-only). City 6 of the approved six-city batch (Colorado Springs, Fort Collins, Thornton, Arvada, Westminster, Greeley). Only addresses inside Greeley city limits are listed. No businesses were contacted.

**Counts:** 7 locations; 5 money orders (2 USPS, 3 King Soopers); 0 check cashing; 0 bill pay; 0 prepaid reload. Labels on the hub: 7 Open evenings, 7 Open weekends. The evenings/weekends page lists 5 (5 Open evenings, 5 Open weekends) because the two hub-only Walmart rows list no service. Both Post Offices close at 17:30 on weekdays, so both are Open evenings. No check-cashing or bill-pay page (zero listings).

## Method

- **USPS:** official USPS Location Finder (tools.usps.com, `locationType` PO). Searches at 5 and 15 miles around Greeley-area ZIPs (80631, 80634, 80639, 80620, 80615, 80550, 80543). Each candidate's official record (`https://tools.usps.com/locations/details/<id>`) was read on 2026-11-11. Retail (BUSINESS) hours, phone, and services come from that record.
- **City limits:** every candidate address was checked with the U.S. Census Bureau Geocoder (https://geocoding.geo.census.gov/geocoder/, address endpoint, Public_AR_Current / Current_Current, Incorporated Places and Census Designated Places layers) on 2026-11-11. Raw results: `docs/research/step8-browser/greeley-usps-geocoder-2026-11-11.jsonl` and `greeley-stores-geocoder-2026-11-11.jsonl`.
- Fees reuse existing rows in `data/providers/fees.csv`. No new fee rows or brands.

## USPS

| Office | Address | Geocoder | Services | Retail hours |
|---|---|---|---|---|
| Downtown Greeley (1365513) | 925 11th Ave 80631 | Greeley city | Domestic and Inquiry Money Orders | Mon-Fri 07:30-17:30, Sat 09:00-13:00, Sun closed |
| Greeley (1365514) | 930 39th Ave 80634 | Greeley city | Domestic and Inquiry Money Orders | Mon-Fri 07:30-17:30, Sat 09:00-13:00, Sun closed |

- Downtown Greeley: Open evenings and Open weekends. Phone 970-392-2782.
- Greeley Post Office: Open evenings and Open weekends. Phone 970-392-0298.
- Both matched exactly on the current benchmark; no 2020-benchmark or locator-point fallback was needed.

Out of city (geocoder confirmed, printed another city): Evans 1362838 (3344 11th Ave, Evans city); Eaton 1361975 (Eaton town); Windsor 1387952 and WIN Carrier Annex 1560051 (Windsor town); La Salle 1369426; Kersey 1368942; Milliken 1373182; Gilcrest 1364775; Severance 1381248 (printed Severance 80546; the geocoder matched 320 1st St in ZIP 80615, Eaton town; either way not Greeley); Ault, Johnstown, Platteville, Timnath, Pierce, Nunn, Mead, Berthoud; Loveland and Valentine (Loveland city); Fort Collins, Fort Collins CO SDC, Old Town (Fort Collins city). Gill 1364780 and Galeton 1439603 are unincorporated (no place match); Lucerne 1371125 (32969 County Road 39) had no address match and prints Lucerne. No Post Office printed Greeley outside the two listed. USPS contract postal units and Approved Postal Providers were not collected.

## Walmart Supercenters and King Soopers

Official store pages were opened in a browser on 2026-11-11 (read-only; no sign-in, no store contact). Raw results: `docs/research/step8-browser/greeley-walmart-ks-2026-11-11.csv` and `.md` (29 detail pages: 22 King Soopers, 7 Walmart). Every address was run through the Census geocoder on 2026-11-11; all 5 Greeley-printed stores geocode inside Greeley city, and no store printed with another city geocodes inside Greeley.

### Added (5 rows)

| Store | Address | Geocoder | Services listed |
|---|---|---|---|
| King Soopers 00032 University Square | 2712 11th Ave 80631 | Greeley city | Money orders |
| King Soopers 00011 Westlake | 2100 35th Ave 80634 | Greeley city (matched as 2100 N 35TH AVE, same number and ZIP) | Money orders |
| King Soopers 00117 North Gate Village | 6922 W 10th St 80634 | Greeley city | Money orders |
| Walmart Supercenter 5051 Greeley 47th Ave | 920 47th Ave 80634 | Greeley city | Money Services only: hub only, all flags false |
| Walmart Supercenter 980 Greeley S 23rd Ave | 3103 S 23rd Ave 80631 | Greeley city (matched as 3103 23RD AVE, same number and ZIP) | Money Services only: hub only, all flags false |

- **Geocoder spelling variants:** Westlake (printed `2100 35Th Ave`) matched `2100 N 35TH AVE, GREELEY, CO, 80634`, and Walmart 980 (printed `3103 S 23rd Ave`) matched `3103 23RD AVE, GREELEY, CO, 80631`. Same house number, street, and ZIP, with only a directional added or dropped, and both inside Greeley city, so they are treated as matches. The row keeps the address as printed on the official store page (ordinal case normalized, e.g. 11Th -> 11th); the row notes record the match.
- **Hours:** store hours only (Walmart Mon-Sun 6am-11pm; King Soopers Sun-Sat 6 AM-11 PM). Pharmacy, fuel, and holiday hours not used. All five are Open evenings and Open weekends.
- **Walmart:** each Supercenter page shows only the generic "Money Services" label; check cashing, money orders, bill pay, and load/unload are not named. All four flags false; hub-only with "call ahead" copy; chain fees not applied. Walmart 5051 lists a Fuel Station as a department; it is not a separate row.
- **King Soopers:** all three pages tag "Money Orders" and "Money Services" (`money_orders=true`). No check cashing, bill pay, prepaid reload, Western Union, or MoneyGram named. King Soopers fees stay "Not published, call ahead."

### Held for Richard

None in Greeley. Every Greeley-printed candidate matched inside Greeley city. (Thornton's held Eastlake Post Office and Walmart 4567 were not touched.)

### Left out

- Out of city (geocoder confirmed): King Soopers 00104 Windsor (Windsor town); 00044 and 00074 (Loveland); 00097, 00073, 00099, 00009 (Fort Collins) and 00146 Midtown Marketplace (Fort Collins; its check-cashing and Western Union tags are not used here); 00105 (Firestone town); 00102, 00042, 00080 (Longmont); 00136, 00081 (Brighton); 00116, 00101 (Thornton); 00138 (Erie town). King Soopers 00154 Frederick and 00129 Vista Ridge (printed Erie) had no geocoder match and print other towns; they are not Greeley candidates. Walmart Supercenters 953 and 1008 (Loveland), 4599 (Timnath town), 2729 and 3177 (Fort Collins). Existing city CSVs were not changed.
- Longmont (2) and Brighton (2) Walmart Supercenters appeared in Walmart's directory but were not opened; they are outside Greeley and are not listed.
- No Walmart Neighborhood Market pages appeared. Fuel centers are not separate rows.

### Coverage limits

King Soopers locator ("Greeley, CO"): 22 results on 3 pages; all 22 grocery pages opened. Walmart: store directory pages for Greeley, Loveland, Timnath, and Fort Collins plus the nearby-stores list on the Greeley 47th Ave page; directories for Evans, Windsor, Eaton, Johnstown, Fort Lupton, Milliken, Berthoud, Severance, Firestone, and Frederick returned no Walmart stores. A press-and-hold check appeared and was completed. No store pages printed Evans, Garden City, Eaton, or Johnstown. No new-brand leads surfaced.

## Not collected

- Payday / title-loan storefronts, including ACE: omitted by policy.
- Stand-alone Western Union / MoneyGram agents and other grocery brands (Safeway, Sprouts, etc.) were not collected.
