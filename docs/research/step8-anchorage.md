# Step 8: Anchorage, AK (2026-11-13 research, shipped 2026-11-14, America/Denver)

**Rows:** 10 (all Post Offices). First city of the approved Alaska batch (Anchorage, Juneau, Fairbanks, Wasilla, Sitka; one city at a time). Anchorage is a consolidated city-borough (Census "Anchorage municipality", GEOID 0203000; county-equivalent Anchorage Municipality, GEOID 02020). Only addresses inside the municipality whose official printed city is Anchorage are listed. No businesses were contacted. Brands in scope for non-Colorado states: USPS and Walmart Supercenters only. This PR is USPS only; Walmart rows are omitted because the official walmart.com store locator was unavailable.

**Counts:** 10 locations; 10 money orders (all ten Post Offices); 0 check cashing; 0 bill pay; 0 prepaid reload. Labels on the hub: 9 Open evenings (all except the Anchorage Postal Store), 5 Open weekends (Midtown, Muldoon, Russian Jack, Huffman, and the Anchorage Main Office). The money-orders page lists 10. The evenings/weekends page lists 9 (9 Open evenings, 5 Open weekends). No check-cashing or bill-pay page (zero listings). Holds: 4 Post Offices, none listed.

Hours are copied as published and are local Anchorage time (Alaska Time). `last_verified` is 2026-11-13 on every row. `verification_status` is `verified_official_locator` on every row.

## Method

- **USPS:** official USPS Location Finder API (`tools.usps.com`, `requestType` po), queried with curl the same way as the Alabama and Colorado cities. Pass 1: 5 and 15 miles around every Anchorage ZIP (28 USPS-city codes listed for Anchorage, AK by ZIP-Codes.com from USPS data last updated 2026-11-01) and nearby official ZIPs for Eagle River, Chugiak, Girdwood, Whittier, Hope, Wasilla / Houston, Palmer, Sutton, Willow, Trapper Creek, Talkeetna, Cooper Landing, Moose Pass, and Seward (92 queries, 28 unique records). Pass 2: 1, 2, 3, 10, and 20 miles around 20 Anchorage/edge ZIPs (added 0). Total 28 records (`step8-browser/anchorage-usps-locator-2026-11-13.jsonl`). Official location pages were fetched for all 28 records (all HTTP 200 on the first try); each page's embedded `poDetail` matched the API record. Retail hours means the BUSINESS block only. Full notes: `step8-browser/anchorage-usps-2026-11-13.md`.
- **Walmart:** not collected. The official walmart.com store locator was blocked / unavailable, so no Walmart rows are in this PR.
- **City limits:** U.S. Census Bureau Geocoder, address endpoint and coordinates endpoint, Public_AR_Current / Current_Current and Public_AR_Census2020 / Census2020_Census2020, Incorporated Places + CDPs + Counties. All 28 addresses and all 28 official locator map points on both benchmarks (`step8-browser/anchorage-usps-geocoder-2026-11-13.jsonl`). OpenStreetMap was not used.
- Fees reuse existing rows in `data/providers/fees.csv`. No new fee rows or brands. Coordinates for USPS rows are in the notes column (lat/lng columns stay blank, as in every city CSV).

## USPS (10 listed, all Domestic and Inquiry Money Orders)

| Office | Address | Phone | Retail hours (Alaska Time) | Labels | Geocoder |
|---|---|---|---|---|---|
| Eastchester (1361901) | 800 Ingra St 99501 | 907-272-8266 | Mon-Fri 10:00-17:30 | Open evenings | Address (both files) and point (61.214043, -149.867924): Anchorage municipality |
| Anchorage Postal Store (1378221) | 320 W 5th Ave Ste 348 99501 | 907-276-6790 | Mon-Fri 10:00-14:00 | none | Address (both, suite dropped) and point (61.217067, -149.889051): Anchorage municipality |
| Sand Lake (1380673) | 2200 Strawberry Rd 99502 | 907-349-2551 | Mon-Fri 10:00-17:30 | Open evenings | Address (both) and point (61.151419, -149.920535): Anchorage municipality |
| Midtown (1373018) | 3721 B St 99503 | 907-273-5877 | Mon-Fri 10:00-18:00; Sat 10:00-13:30 | Open evenings, Open weekends | Address (both) and point (61.186397, -149.881737): Anchorage municipality |
| Muldoon (1374209) | 2420 Muldoon Rd 99504 | 907-333-0053 | Mon-Fri 10:00-18:00; Sat 10:00-13:30 | Open evenings, Open weekends | Address (both) and point (61.197565, -149.735551): Anchorage municipality |
| Lake Otis (1369623) | 5855 Lake Otis Pkwy 99507 | 907-563-9643 | Mon-Fri 10:00-18:00 | Open evenings | Address (both) and point (61.168208, -149.836784): Anchorage municipality |
| Russian Jack (1380145) | 801 Northway Dr 99508 | 907-272-1356 | Mon-Fri 10:00-17:30; Sat 10:00-16:00 | Open evenings, Open weekends | Address (both) and point (61.214569, -149.810655): Anchorage municipality |
| Huffman (1367579) | 1221 Huffman Park Dr 99515 | 907-348-0491 | Mon-Fri 10:00-18:00; Sat 10:00-16:00 | Open evenings, Open weekends | Address (both) and point (61.110979, -149.859335): Anchorage municipality |
| Spenard (1382460) | 1601 W Northern Lights Blvd 99517 | 907-258-6733 | Mon-Fri 10:00-18:00 | Open evenings | Address (both) and point (61.196124, -149.915786): Anchorage municipality |
| Anchorage Main Office (1439416) | 4141 Postmark Dr 99530 | 907-266-3266 | Mon-Fri 08:00-23:00; Sat 09:00-23:00; Sun 09:00-23:00 | Open evenings, Open weekends | Current address Anchorage municipality (99530); 2020 address matched the same street with ZIP 99502, Anchorage municipality; point (61.184473, -149.986214) Anchorage municipality on both. Official BUSINESS hours, not the 24-hour APC block. |

The printed city on all ten is Anchorage, which is treated as agreeing with the Census place name "Anchorage municipality."

### Held for Richard (not listed)

1. **Fort Richardson Post Office (1439401)**, 724 Quartermaster Rd, printed **JBER**, AK 99505, 907-428-3869. Money orders; Mon-Fri 10:00-13:00/14:30-17:30, Sat/Sun closed. Address and official map point (61.256206, -149.711933) are in Anchorage municipality on both benchmarks. Printed city and geocode disagree.
2. **Eagle River Post Office (1361596)**, 11471 Business Blvd, printed **Eagle River**, AK 99577, 907-694-2732. Money orders; Mon-Fri 09:30-17:30, Sat 10:00-14:00. Address and official map point (61.324408, -149.57559) are in Anchorage municipality on both benchmarks. Printed city and geocode disagree.
3. **Chugiak Post Office (1358023)**, 22255 Dogsled Ct, printed **Chugiak**, AK 99567, 907-688-2747. Money orders; Mon-Fri 09:00-17:30, Sat 09:00-13:00. Current address and official map point (61.400859, -149.468302) are in Anchorage municipality; the 2020 address file had no match (street/city retries also no match). Printed city and geocode disagree.
4. **Girdwood Post Office (1364822)**, 118 Lindblad Ave, printed **Girdwood**, AK 99587, 907-783-2922. Money orders; Mon-Fri 09:00-12:00/13:00-17:00, Sat 10:00-12:00. Address and official map point (60.964186, -149.133523) are in Anchorage municipality on both benchmarks. Printed city and geocode disagree.

### Left off (not holds)

- **ANCHORAGE 1439369**, 1601 W Northern Lights Blvd, Anchorage 99517: BUSINESS hours Mon-Fri 10:00-17:45, but no money orders. Same address as Spenard (1382460). Use 1382460 only.
- No Indian, Bird Creek, Elmendorf, or Whittier-printed office appeared. ZIP 99693 (Whittier) returned 0 locations through 20 miles.
- Other-city offices whose printed city and geocode agree outside Anchorage municipality: Wasilla, Wasilla Annex (point in South Lakes CDP), Palmer, Houston, Willow CDP, Sutton-Alpine CDP, Chickaloon CDP, Trapper Creek CDP, Talkeetna CDP, Hope CDP, Cooper Landing CDP, Moose Pass CDP, and Seward city.

## Walmart Supercenters

Not collected in this PR. The official walmart.com store locator was unavailable. No Walmart rows, no Walmart fee citations, and no Neighborhood Markets.

## Site changes in this PR

- New `data/locations/anchorage.csv` and `/anchorage/`, `/anchorage/money-orders/`, `/anchorage/after-hours/` pages.
- Anchorage added under a new Alaska heading on the home "Start here" list and on `/cities/`, after Alabama and before Colorado (alphabetical state order). Home and `/cities/` meta descriptions now include "Anchorage, Alaska". No other city CSV or page changed. Colorado order is unchanged.

## Not changed

- Huntsville, Mobile, and every Colorado city. Juneau and the rest of the Alaska batch were not started. No Walmart rows were added.

## Not collected

- Walmart Supercenters: deferred until the official locator is available.
- Payday / title-loan storefronts, including ACE: omitted by policy.
- Stand-alone Western Union / MoneyGram agents, other grocery chains, and USPS contract postal units were not collected.
