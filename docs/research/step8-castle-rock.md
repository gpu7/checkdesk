# Step 8: Castle Rock (2026-11-12, America/Denver)

**Rows:** 3 (2 King Soopers, 1 Walmart Supercenter; no USPS row). City 5 of the batch approved on 2026-11-12 (Pueblo, Centennial, Boulder, Longmont, Castle Rock; ranked from Census Vintage 2025, SUB-IP-EST2025-POP-08). Only addresses inside the Town of Castle Rock (incorporated place, "Castle Rock town" in the Census geocoder) are listed. No businesses were contacted.

**Counts:** 3 locations; 2 money orders (2 King Soopers); 0 check cashing; 0 bill pay; 0 prepaid reload. Labels on the hub: 3 Open evenings, 3 Open weekends. The evenings/weekends page lists the 2 money-order locations (2 Open evenings, 2 Open weekends); the Walmart Supercenter is hub-only ("Money Services, call ahead"). No check-cashing or bill-pay page (zero listings).

## Method

- **USPS:** official USPS Location Finder (tools.usps.com, `locationType` PO), same method as Longmont/Boulder/Centennial/Pueblo. Searches at 5 and 15 miles around Castle Rock ZIPs (80104, 80108, 80109) returned 13 Post Office records (`docs/research/step8-browser/castle-rock-usps-locator-2026-11-12.jsonl`). The official record for the Castle Rock office (`https://tools.usps.com/locations/details/1357260`) was read on 2026-11-12. A repeat locator search with the Domestic Money Orders filter (80104, 15 miles) returned Franktown, Sedalia, Larkspur, Parker, Louviers, Elizabeth and Highlands Ranch, but not Castle Rock.
- **City limits:** every candidate address was checked with the U.S. Census Bureau Geocoder (https://geocoding.geo.census.gov/geocoder/, address endpoint, Public_AR_Current / Current_Current, Incorporated Places and Census Designated Places layers) on 2026-11-12. Raw results: `castle-rock-usps-geocoder-2026-11-12.jsonl` (all 13 Post Office records) and `castle-rock-stores-geocoder-2026-11-12.jsonl` (all 49 store pages).
- **Fallback checks** for addresses with no current-benchmark match: Census 2020 benchmark (Public_AR_Census2020) one-line lookups, plus coordinates lookups (current benchmark) of official map points. Raw results: `castle-rock-geocoder-fallback-2026-11-12.jsonl`. No listed row needed the fallback; it was used only to confirm out-of-town candidates.
- Fees reuse existing rows in `data/providers/fees.csv`. No new fee rows or brands.

## USPS

- **Castle Rock Post Office (1357260), 220 S Wilcox St 80104: not listed.** The address is inside Castle Rock town (geocoder match 220 S WILCOX ST, CASTLE ROCK, CO, 80104; its official locator point 39.36481, -104.859644 also returns Castle Rock town). Its official record lists retail hours (Mon-Fri 08:30-17:00, Sat 08:00-12:00, Sun closed; phone 303-814-6932) but its service list does not include Domestic or Inquiry Money Orders (services listed: APC, BIOIPPB, CALLREFERRAL, CONNECTLOCAL, FACTERMINALTYPERSS, GIFTCARDS, GREETINGCARDS, LBRORETAIL, LBROSSK, PARCELLOCKERS, POBOXONLINE, RTLMKTGTERMINALTYPERSS). No check cashing, bill pay, or prepaid reload either. Service flags follow only the official page, so with no tracked service the office has no row. The hub and money-order page say it is not listed and why.
- **Castle Rock Annex (1577757), 300 E Miller Ct 80104:** Castle Rock town, but a carrier/pickup unit with no retail (BUSINESS) hours and no money-order service. Not listed.
- Out of town (printed another place, and the geocoder agrees): Franktown 1364042 (Franktown CDP, unincorporated); Sedalia 1381134 (no current-file match; the 2020 file and the official locator point both return Sedalia CDP); Larkspur 1369889 (Larkspur town); Louviers 1371030 (Louviers CDP); Parker 1376837 (Parker town); Elizabeth 1362284 (no address match on the current or 2020 file; official locator point 39.36058, -104.591374 returns Elizabeth town); Highlands Ranch 1439610 and the Littleton CO Highlands SDC 1613886 at the same address (Highlands Ranch CDP); Greenwood Village 1439554 (Greenwood Village city); Centennial 1439625 and Tower 1432755 (Centennial city, already listed under Centennial; not changed). No Post Office printed with another city geocodes inside Castle Rock. USPS contract postal units and Approved Postal Providers were not collected.

## King Soopers and Walmart

Official store pages were opened in a browser on 2026-11-12 (read-only; no sign-in, no store contact). Raw results: `docs/research/step8-browser/castle-rock-walmart-ks-2026-11-12.csv` and `.md` (49 detail pages: 33 King Soopers, 16 Walmart). The King Soopers locator returned 34 results for "Castle Rock, CO"; the 34th was a fuel center (Aurora Fuel, 00669), not a row. Walmart's store finder returned no stores for "Castle Rock, CO", so Walmart's official Colorado store directory and the "Nearby stores" lists on store pages were used. No unexpected grocery or retail brands appeared. Every address was run through the Census geocoder on 2026-11-12.

### Added (3 rows)

| Store | Address | Geocoder | Services listed | Store hours |
|---|---|---|---|---|
| King Soopers 00132 Ridge Road | 750 N Ridge Rd 80104 | Castle Rock town (750 N RIDGE RD, CASTLE ROCK, CO, 80104) | Money orders (and Money Services) | Sun-Sat 6 AM-11 PM |
| King Soopers 00125 Promenade Parkway | 5544 Promenade Pkwy 80108 | Castle Rock town (5544 PROMENADE PKWY, CASTLE ROCK, CO, 80108) | Money orders (and Money Services) | Sun-Sat 6 AM-11 PM |
| Walmart Supercenter 984 (Castle Rock Supercenter) | 133 Sam Walton Lane 80104 | Castle Rock town (133 SAM WALTON LN, CASTLE ROCK, CO, 80104) | Generic "Money Services" only (hub-only) | Mon-Sun 6am-10pm |

- **Spelling/geocoder notes:** the Walmart page prints "Sam Walton Lane"; the geocoder returns "LN" (same number, street, ZIP). The row keeps the printed form.
- **Hours:** store hours only. Pharmacy, fuel, sensory-friendly, and holiday hours not used. All three are Open evenings and Open weekends.
- **King Soopers:** both Castle Rock pages tag "Money Orders" and "Money Services" (`money_orders=true`). No check cashing, bill pay, prepaid reload, Western Union, or MoneyGram named. "Account Funding" is not a tracked service and is not flagged. King Soopers fees stay "Not published, call ahead."
- **Walmart:** the Castle Rock Supercenter page shows only a generic "Money Services" label; check cashing, money orders, bill pay, and load/unload are not named, so all four flags are false. It is on the Castle Rock hub only, labeled to call ahead, and not on the money-order or evenings-and-weekends pages. Walmart chain fee maximums are not applied.

### Held for Richard

None in Castle Rock. All three Castle Rock-printed store pages geocode inside Castle Rock town on the current address file, and no candidate printed with another city geocodes inside Castle Rock. (Thornton's held Eastlake Post Office and Walmart 4567 were not touched.)

### Left out

- **Castle Pines** (separate city): King Soopers 00091 Castle Pines, 7284 Lagae Rd (Castle Pines city).
- **Parker** (Parker town): King Soopers Stroh Ranch (12959 S Parker Rd), Crossing at Stonegate (17031 Lincoln Ave), Cottonwood Drive (17761 Cottonwood Dr; the only page naming Western Union); Walmart Supercenter 2892 (11101 S Parker Rd). King Soopers 00175 Parker (6755 Prospector Ln, printed Parker; Pickup only, no money services) had no address match on the current or 2020 file; as a supplementary (non-official) check, its OpenStreetMap point (39.4592202, -104.7625073) returns unincorporated Douglas County (no place or CDP), not Castle Rock.
- **Highlands Ranch** (unincorporated CDP; official city and geocoder agree): King Soopers Red Cedar Drive, University and Colorado, Quebec St Highland Ranch, Wildcat Reserve; Walmart 1252 (6675 Business Center Dr).
- **Other places**: Monument (Walmart 3227, Monument town); Elizabeth (Walmart 4639, 2100 Legacy Cir; geocoder matched 2100 LEGACY LOOP in no place or CDP); Centennial (King Soopers County Line and Holly, Cherrywood Square, Smoky Hill and Himalaya; Walmart Briarwood 3313; Centennial is already live and unchanged); Littleton, Greenwood Village, Englewood, Aurora, Denver, Columbine/Ken Caryl/Dakota Ridge CDPs, and King Soopers Governors Plaza (9820 W Belleview Ave, printed Littleton; the geocoder matched 9820 W BELLEVIEW ST in no place or CDP). Two print one city and geocode another, neither near Castle Rock: King Soopers 7700 W Quincy Ave (printed Littleton, Denver city) and Walmart 3566, 9400 E Hampden Ave (printed Denver, Aurora city). No existing city CSV was changed.
- **Far pages (reverse check only):** Walmart 1896 (8250 Razorback Rd, Colorado Springs city); Walmart 5123 (5550 E Woodmen Rd) and 3805 (19600 E US Highway 24) had no address match, and their official store-page map points (38.942692, -104.725382; 38.970532, -105.038613) return Colorado Springs city and Woodland Park city.
- **Walmart Neighborhood Markets:** Centennial 3126 (16746 E Smoky Hill Rd) is excluded by policy (and is in Centennial). Aurora 3740 and 4196 were not opened. Fuel centers are not separate rows.
- **Larkspur, Sedalia, Franktown:** no King Soopers or Walmart store in either official source.

## Not collected

- Payday / title-loan storefronts, including ACE: omitted by policy.
- Stand-alone Western Union / MoneyGram agents and other grocery brands (Safeway, Sprouts, etc.) were not collected.
