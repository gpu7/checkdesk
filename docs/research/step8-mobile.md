# Step 8: Mobile, AL (2026-11-13, America/Denver)

**Rows:** 15 (12 Post Offices, 3 Walmart Supercenters). Second city of the approved Alabama batch (Huntsville, Mobile, Birmingham, Montgomery, Tuscaloosa; one city at a time). Mobile is a city ("Mobile city", GEOID 0150000, in the Census geocoder); every listed row is in Mobile County. Only addresses inside Mobile city limits are listed. No businesses were contacted. Brands in scope for Alabama: USPS and Walmart Supercenters only.

**Counts:** 15 locations; 12 money orders (all twelve Post Offices); 0 check cashing; 0 bill pay; 0 prepaid reload. Labels on the hub: 4 Open evenings (Bel Air Post Office and the three Walmart Supercenters), 10 Open weekends (Mobile, Bel Air, Cottage Hill, Spring Hill, Towne West, Tillmans Corner, and Airport Post Offices, and the three Walmart Supercenters). Hub-only rows: 3 (Walmart Supercenters 866, 853, 4581; "Money Services, call ahead"). The money-orders page lists 12. The evenings/weekends page lists 7 (1 Open evenings, 7 Open weekends). No check-cashing or bill-pay page (zero listings). Holds: 3 (2 Post Offices, 1 Walmart Supercenter), none listed.

Hours are copied as published and are local Mobile time (Central Time). `last_verified` is 2026-11-13 on every row.

## Method

- **USPS:** official USPS Location Finder (tools.usps.com, `requestType` po), same method as Huntsville and the Colorado cities. Pass 1: 5 and 15 miles around every Mobile ZIP and nearby ZIPs for Saraland, Daphne, Spanish Fort, Semmes, Theodore, Satsuma, Axis, Grand Bay, Irvington, Bayou La Batre, Citronelle, Creola, Fairhope, Dauphin Island, Wilmer, Chunchula, Mount Vernon, and Coden (106 queries, 51 unique records). Pass 2: 1, 2, 3, 10, and 20 miles around 17 Mobile/edge ZIPs (added 0). Total 51 records (`step8-browser/mobile-usps-locator-2026-11-13.jsonl`). Official location pages were fetched for all 13 Mobile-printed records, Theodore, and the 14 nearest other-city offices (28 pages, all HTTP 200 on the first try); each page's embedded `poDetail` matched the API record. Retail hours means the BUSINESS block only. Full notes: `step8-browser/mobile-usps-2026-11-13.md`.
- **Walmart:** official walmart.com store directories (Mobile 9 stores, Prichard 0, Saraland 1, Semmes 1, Theodore 1) and store pages, opened in a browser on 2026-11-13 (read-only, no sign-in, no store contact). The Mobile store pages publish no map coordinates (only an address-based directions link), so no official map-point checks were possible for Walmart. Notes and CSV: `step8-browser/mobile-walmart-2026-11-13.md` / `.csv`.
- **City limits:** U.S. Census Bureau Geocoder, address endpoint and (for USPS) coordinates endpoint, Public_AR_Current / Current_Current and Public_AR_Census2020 / Census2020_Census2020, Incorporated Places + CDPs + Counties. USPS: all 51 addresses and all 51 official locator map points on both benchmarks (`step8-browser/mobile-usps-geocoder-2026-11-13.jsonl`). Walmart: addresses on both files for the four Mobile-printed Supercenters plus 1212 and 5174, and address variants for 991 (`step8-browser/mobile-stores-geocoder-2026-11-13.jsonl`; summary `mobile-walmart-geocode-2026-11-13.md` / `.csv`). OpenStreetMap was not used.
- Fees reuse existing rows in `data/providers/fees.csv`. No new fee rows or brands. Coordinates for USPS rows are in the notes column (lat/lng columns stay blank, as in every city CSV).

## USPS (12 listed, all Domestic and Inquiry Money Orders)

| Office | Address | Phone | Retail hours | Labels | Geocoder |
|---|---|---|---|---|---|
| Mobile (1373428) | 250 Saint Joseph St 36601 | 251-694-5969 | Mon-Fri 08:00-17:00; Sat 09:00-12:00 | Open weekends | Address (both files, matched as 250 ST JOSEPH ST, ZIP 36602) and point (30.696852, -88.0435749): Mobile city |
| Midtown (1373019) | 907 Spring Hill Ave 36604 | 251-432-0270 | Mon-Fri 09:00-16:30 | none | Address (both) and point: Mobile city |
| Loop (1370927) | 415 Dauphin Island Pkwy 36606 | 251-479-9571 | Mon-Fri 08:30-16:30 | none | Address (both) and point: Mobile city |
| Crichton (1359833) | 168 Bay Shore Ave 36607 | 251-478-5639 | Mon-Fri 09:00-16:30 | none | Address (both) and point: Mobile city |
| Bel Air (1354449) | 3410 Bel Air Mall 36606 | 251-478-8513 | Mon-Fri 11:00-18:00; Sat 12:00-17:00 | Open evenings, Open weekends | Current address no match; 2020 address Mobile city; point (30.672143, -88.121899) Mobile city on both benchmarks |
| Bayside (1354246) | 2000 Rosedale Rd 36605 | 251-479-9569 | Mon-Fri 08:30-16:30 | none | Current address Mobile city; 2020 no match; point (30.624029, -88.0839759) Mobile city on both |
| Cottage Hill (1359368) | 705 Oak Circle Dr W 36609 | 251-660-8559 | Mon-Fri 08:30-16:30; Sat 09:00-12:00 | Open weekends | Address (both) and point: Mobile city |
| Spring Hill (1382538) | 5551 Old Shell Rd 36608 | 251-341-5624 | Mon-Fri 08:30-16:30; Sat 09:30-12:00 | Open weekends | Current address no match; 2020 address Mobile city; point (30.689104, -88.170429) Mobile city on both |
| Towne West (1384895) | 5701M Moffett Rd 36618 | 251-342-8665 | Mon-Fri 09:00-16:30; Sat 09:00-12:00 | Open weekends | Address (both) and point: Mobile city |
| Plaza de Malaga (1377773) | 6157 Airport Blvd Ste 310 36608 | 251-341-6186 | Mon-Fri 08:30-16:30 | none | Address (both, suite dropped) and point: Mobile city |
| Tillmans Corner (1384671) | 5441 Highway 90 W Ste 13 36619 | 251-666-6580 | Mon-Fri 09:00-16:30; Sat 09:00-12:00 | Open weekends | **No address match** on either file; point (30.5864, -88.1677929) Mobile city on both. **Map-point include** |
| Airport (1352482) | 8400 Airport Blvd 36608 | 251-635-1743 | Mon-Fri 09:00-16:30; Sat 09:00-12:00 | Open weekends | Address (both) and point: Mobile city |

No Sunday retail anywhere. Only Bel Air is open evenings.

- **Tillmans Corner (documented include):** the official address, forms without "Ste 13", and US Hwy 90 variants had no match in the current or 2020 Census address file. The official USPS map point is in Mobile city (not Tillmans Corner CDP) on both benchmarks, so the row is included on the same map-point fallback used for Huntsville Walmart 375, Montrose Walmart 1058, and similar rows. Printed city and point agree; not a hold.
- **Bel Air, Spring Hill, Bayside:** one address file missed; the other file and the official map point on both benchmarks are Mobile city. Included on the map point with the matching file as support.

### Held for Richard (not listed)

1. **Prichard Post Office (1437776)**, 130 E Prichard Ave, prints Mobile, AL 36610, 251-457-4512. Money orders; Mon-Fri 08:30-16:30, Sat 09:00-12:00. Address match and official map point (30.730075, -88.081575) are in **Prichard city** on both benchmarks. Printed city and geocode disagree.
2. **Theodore Post Office (1384530)**, 5631 Highway 90, prints Theodore, AL 36582, 251-653-8718. Money orders; Mon-Fri 09:00-16:30, Sat 09:00-11:00. Address match (5631 US HWY 90, THEODORE, AL, 36582) and official map point (30.569951, -88.1706959) are in **Mobile city** on both benchmarks. Printed city and geocode disagree.

### Left off (not holds)

- No Mobile-printed carrier annex or no-retail record appeared. Other-city offices whose printed city and geocode agree outside Mobile: Chickasaw, Saraland, Daphne (Baldwin County), Satsuma, Semmes, Creola, Fairhope, Grand Bay CDP, Dauphin Island, Montrose (AL), Irvington, Saint Elmo, Wilmer, Axis, and farther offices listed in `mobile-usps-2026-11-13.md`.

## Walmart Supercenters (3 listed, hub-only)

All three official store pages show only a generic **Money Services** label; check cashing, money orders, bill pay, and load/unload are not named, so all four service flags are false. Store hours Mon-Sun 6 a.m.-11 p.m. (holiday closure and department hours not used). No official map coordinates on the pages.

| Store | Official name | Address | Phone | Geocoder |
|---|---|---|---|---|
| 866 | Mobile Rangeline Service Rd S Supercenter | 5245 Rangeline Service Rd S 36619 | 251-666-7972 | Matched `5245 RANGELINE RD, MOBILE, AL, 36619`; Mobile city on both files |
| 853 | Mobile Schillinger Rd S Supercenter | 685 Schillinger Rd S 36695 | 251-633-2211 | Matched exactly; Mobile city on both files |
| 4581 | Mobile Dawes Rd Supercenter | 2500 Dawes Rd 36695 | 251-633-6023 | Matched `2500 DAWES SVC RD, MOBILE, AL, 36695`; **current file Mobile city**, 2020 file no incorporated place or CDP |

- **Walmart 4581 (documented include):** the research rule flagged it as a vintage disagreement. The current Census file places the matched address in Mobile city; the 2020 file places the same address in no place (unincorporated Mobile County). This most likely reflects an annexation after 2020. There is no official map point to break the tie. Included on the current-file match per the 2026-11-13 decision; Richard was told and can ask for it to be held instead. Its hours were read from the page head (identical to the other Mobile Supercenters).

### Held for Richard (not listed)

- **Walmart Supercenter 991**, Mobile E Interstate 65 Service Rd S Supercenter, 101 E I65 Service Rd S, prints Mobile, AL 36606, 251-471-1105. Generic Money Services only. No Census address match on either file for the official form or any I-65 / Interstate 65 / Service Road / Svc / Frontage variant (address and one-line endpoints), and the store page publishes no map point, so city limits cannot be confirmed.

### Left off (not held)

- **Walmart Supercenter 1212**, 1095 Industrial Pkwy, Saraland 36571: Saraland city on both files.
- **Walmart Supercenter 5174**, 7855 Moffett Rd, Semmes 36575: Semmes city (current); no place (2020). Not in Mobile on either file.
- **Walmart Neighborhood Markets** 5740, 4210, 5098, 4648, 4657 (Mobile) and 5744 (Theodore): excluded format (policy); not opened.

## Site changes in this PR

- New `data/locations/mobile.csv` and `/mobile/`, `/mobile/money-orders/`, `/mobile/after-hours/` pages.
- Mobile added under Alabama on the home "Start here" list and on `/cities/` after Huntsville (alphabetical). `/cities/` and home meta descriptions now say "Huntsville and Mobile, Alabama". No other city CSV or page changed.

## Not changed

- Huntsville and every Colorado city. Birmingham and the rest of the Alabama batch were not started.

## Not collected

- Payday / title-loan storefronts, including ACE: omitted by policy.
- Stand-alone Western Union / MoneyGram agents, other grocery chains, and USPS contract postal units were not collected.
