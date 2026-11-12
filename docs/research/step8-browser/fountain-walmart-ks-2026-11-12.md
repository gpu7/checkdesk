# Fountain, CO money-services store-page review — 2026-11-12

## Coverage
- Opened **7 official store detail pages**: 3 King Soopers (all HTTP 200) and 4 Walmart Supercenters (all HTTP 200). No press-and-hold challenge appeared this run.
- CSV rows: 9 (3 King Soopers, 4 Walmart Supercenters, 2 Walmart Neighborhood Markets excluded by policy).
- King Soopers: re-ran official locator (`/stores/search?searchText=Fountain, CO 80817`, 13 results, 2 pages; page 1 of 9 read) and the city directory `/stores/grocery/co/fountain` ("1 grocery store in Fountain, CO"). Opened the printed-Fountain store plus the two nearest Colorado Springs stores.
- Walmart: re-ran official store finder (`/store-finder?location=80817`, 20 stores within 50 mi; loaded after a few seconds). Opened both Fountain Supercenters plus the two nearest Colorado Springs Supercenters (from #3018's Nearby section).
- Not geocoded.

## Printed Fountain
- **Walmart (2)**
  - #1273 "Fountain S South Us Hwy 85 87 Supercenter" ("Walmart Supercenter #1273"), 6310 S Us Highway 85-87, Fountain, CO 80817, 719-391-1700. https://www.walmart.com/store/1273-fountain-co. Hours Mon - Sun | 6am - 11pm (holiday, sensory-friendly, pharmacy excluded). Money Services listed (generic tag only); no money orders, check cashing, bill pay, prepaid reload or Western Union named. HTTP 200. Finder: 6.36 mi.
  - #3018 "Fountain Venetucci Blvd Supercenter", 4425 Venetucci Blvd, Fountain, CO **80906**, 719-313-4378. https://www.walmart.com/store/3018-fountain-co. Hours Mon - Sun | 6am - 11pm. Money Services generic only; nothing else named. HTTP 200. Finder: 9.27 mi. ZIP 80906 is a Colorado Springs ZIP — flag for city-limit geocode check.
- **King Soopers (1)**
  - #00153 "Fountain King Soopers", 6255 Sawcut Pt, Fountain, CO 80817, 719-359-9070. https://www.kingsoopers.com/stores/grocery/co/fountain/fountain-king-soopers/620/00153. Hours Sun - Sat: 6 AM - 11 PM (pharmacy and fuel hours excluded). **No Money Services or money orders listed** in Specialties & Departments (lists Gas Station, Starbucks, Pharmacy etc.); no check cashing, bill pay, prepaid reload, Western Union. HTTP 200. Locator: 3.68 mi.
- Total printed Fountain: 3.

## Nearby / geocode list
- **King Soopers opened:** Hancock Plaza #00103, 2910 S Academy Blvd, Colorado Springs 80916, 719-393-9622 (9.17 mi; Money Orders + Money Services); Cheyenne Meadows Center #00058, 815 Cheyenne Meadows Rd, Colorado Springs 80906, 719-527-1590 (9.93 mi; Money Orders + Money Services). Hours Sun - Sat: 6 AM - 11 PM.
- **Walmart Supercenters opened:** Colorado Springs S 8th St #1434, 707 S 8th St, 80905, 719-633-0736 (finder 14.13 mi; 4.58 mi from #3018); Colorado Springs E Platte Ave #1200, 3201 E Platte Ave, 80909, 719-578-9164 (13.23 mi). Both Mon - Sun | 6am - 11pm, generic Money Services only.
- King Soopers listed, not opened (locator page 1): Constitution Avenue #00134 (7915 Constitution Ave 80951, 13.48 mi); Westside Uintah #00006 (1750 W Uintah St 80904, 15.05); Academy and Austin Bluffs #00130 (3620 Austin Bluffs Pkwy 80918, 15.79); Centennial Blvd and Fillmore #00133 (3250 Centennial Blvd 80907, 16.72); Stetson Hills #00098 (6030 Stetson Hills Blvd 80923, 16.73); Woodmen and Academy #00053 (6930 N Academy Blvd 80918, 18.92). Locator page 2 (4 more) not read.
- Walmart Supercenters listed, not opened: Colorado Springs Space Center Dr #3582 (1575 Space Center Dr 80915, 13.68 mi); Falcon #4335 (11550 Meridian Market Vw 80831, 19.72); Colorado Spgs Ne Co #5123 (5550 E Woodmen Rd 80920, 19.74); Razorback Rd #1896 (8250 Razorback Rd 80920, 21.07); Pueblo West #3382, Pueblo Dillon Dr #842, Woodland Park #3805, Pueblo W Northern #1001, Monument #3227 (29.66), Canon City #1019, Elizabeth #4639.
- No stores printed Security, Widefield, Fort Carson, or Peyton appeared in either locator; the Walmart/KS stores nearest those areas are #1273 (Fountain, near Security-Widefield) and #00153. Any Security/Widefield-area store would be one of the printed-Fountain stores above.

## Excluded by policy
- Walmart Neighborhood Markets (listed, pages not opened): #3082 Colorado Springs S Academy Blvd, 1622 S Academy Blvd, 80916 (11.07 mi); #3083 N Murray Blvd, 665 N Murray Blvd, 80915 (13.19 mi); also in finder: #3176 N Union Blvd, #3175 Austin Bluffs Pkwy, Pueblo S Prairie Ave #5828.
- Fuel centers appear only as features on pages (not separate rows); KS Fuel filter not re-run.

## Unexpected brands
- None seen (no City Market, Safeway, etc.) in the King Soopers locator or Walmart finder results.

## Findings
- Fountain King Soopers #00153 lists no money services at all; the two Colorado Springs King Soopers opened list Money Orders + Money Services; none list Check Cashing, bill pay, prepaid reload or Western Union. Account Funding, Coinstar, ATM, Bank not flagged.
- Walmart: all 4 opened are Supercenters with generic "Money Services" only; none named money orders, check cashing, bill pay, prepaid reload or Western Union.
- Hours are store hours only.

## Coverage gaps
- KS locator page 2 and six farther KS stores not opened; farther Walmarts not opened; Neighborhood Market pages not opened.
- Walmart store directory pages not used; the finder worked.
- Walmart #3018's ZIP 80906 vs Fountain city name needs geocode check.

CSV: `/workspace/checkdesk/research/fountain-walmart-ks-2026-11-12.csv`
