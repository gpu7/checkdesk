# Step 8: Colorado Springs (2026-11-11, America/Denver)

City 1 of the approved six-city batch (Colorado Springs, Fort Collins, Thornton, Arvada, Westminster, Greeley). Only addresses inside Colorado Springs city limits are listed. No businesses were contacted.

## Method

- **USPS:** official USPS Location Finder (tools.usps.com, `locationType` PO). Searches around every Colorado Springs ZIP (80903-80911, 80915-80925, 80927, 80938, 80939, 80951) plus wider 20-mile searches from 16 of them. Each candidate's official detail page (`https://tools.usps.com/locations/details/<id>`) was opened on 2026-11-11, and the address, phone, posted retail (BUSINESS) hours, and money-order services were copied from that page.
- **City limits:** every candidate address was checked with the U.S. Census Bureau Geocoder (https://geocoding.geo.census.gov/geocoder/, Public_AR_Current / Current_Current, Incorporated Places and Census Designated Places layers) on 2026-11-11. The `city` column keeps the official mailing city.
- Fees reuse existing rows in `data/providers/fees.csv`. No new fee rows.

## USPS included (8)

| USPS id | Office | Address | Mon-Fri | Sat | Labels |
|---|---|---|---|---|---|
| 1439566 | Colorado Springs (main) | 201 E Pikes Peak Ave 80903 | 09:00-17:30 | 08:00-13:00 | Open evenings, Open weekends |
| 1355790 | Briargate | 8585 Criterion Dr 80920 | 09:00-17:30 | 09:00-15:00 | Open evenings, Open weekends |
| 1353145 | Antares | 2641 E Uintah St 80909 | 09:00-17:00 | 07:30-13:00 | Open weekends |
| 1357895 | Cheyenne Mountain | 1540 S 8th St 80905 | 09:00-17:30 | 08:00-13:00 | Open evenings, Open weekends |
| 1375306 | North End | 2940 N Prospect St 80907 | 09:00-17:00 | 09:30-13:00 | Open weekends |
| 1379690 | Rockrimmon | 5001 Centennial Blvd 80919 | 09:00-17:00 | 08:00-13:00 | Open weekends |
| 1384416 | Templeton | 4356 Montebello Dr 80918 | 09:00-17:30 | 08:30-14:00 | Open evenings, Open weekends |
| 1439639 | West End | 204 S 25th St 80904 | 09:00-17:00 | 08:30-13:00 | Open weekends |

All eight list Domestic and Inquiry Money Orders. Sunday is closed at every office. `money_orders=true`; check cashing, bill pay, and prepaid reload false (not listed).

## USPS excluded

- **Cimarron Hills 1440232** (5925 Galley Rd, mailing Colorado Springs 80915): geocoder places it in Cimarron Hills CDP (unincorporated El Paso County).
- **Security 1381131** (5755 Kittery Dr, mailing Colorado Springs 80911): Security-Widefield CDP.
- **Fort Carson 1363752** (1611 McDonald St, mailing Colorado Springs 80913): Fort Carson CDP.
- **General Mail Facility 1364595** (3655 E Fountain Blvd Ste 106, 80910; Mon-Fri 09:00-18:00, Sat 09:00-13:30; Domestic + Inquiry Money Orders): the Census geocoder returned no address match (with or without the suite, Current and Census 2020 benchmarks). The locator's own coordinates (38.812737, -104.759994) fall inside Colorado Springs city, but by the same rule used for Watkins in Step 6 it is not listed without a clean address match. **Flagged for review.**
- **West End Carrier Annex 1443285** (2410 Robinson St): no money-order services and no retail hours listed; carrier unit.
- Manitou Springs, Fountain, Monument, USAF Academy, Cadet, Cascade, Green Mountain Falls, Peyton, and other offices have non-Colorado Springs mailing cities and are outside the city.
- USPS contract postal units and Approved Postal Providers were not collected.

## Walmart Supercenters and King Soopers

STORES-RESEARCH

## Not collected

- Payday / title-loan storefronts, including ACE: omitted by policy.
- Stand-alone Western Union / MoneyGram agents and other grocery brands (for example Safeway, City Market) are not on Check Desk; no new brand was added.
