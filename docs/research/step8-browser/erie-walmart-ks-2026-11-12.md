# Erie, CO money-services store-page review — 2026-11-12

## Coverage
- Opened **22 official store detail pages**: 14 King Soopers and 8 Walmart Supercenters. All King Soopers pages returned HTTP 200; all Walmart pages returned HTTP 200 (a "Robot or human?" press-and-hold appeared mid-run, was completed with a 10s mouse hold, then pages loaded normally).
- CSV rows: 24 (14 King Soopers, 8 Walmart Supercenters, 2 Walmart Neighborhood Markets excluded by policy).
- King Soopers: re-ran the official locator (`/stores/search?searchText=Erie, CO 80516`, 32 results, 4 pages) and the official Erie city directory (`/stores/grocery/co/erie`, "2 grocery stores in Erie, CO"). Opened pages for the two Erie stores plus the 12 nearest-ring stores (Frederick, Louisville x2, Broomfield x3, Thornton x2, Longmont x2, Boulder Gun Barrel, Firestone). Remaining locator results (farther than ~10.3 mi: Mission Trace, 104th and Federal, 104th and Washington, North Main, 30th St Boulder, Table Mesa, Wadsworth and Church Ranch, 4th and Bromley, Federal Heights, Arvada x5, Brighton 50th, Commerce City x3, etc.) are not carried as rows.
- Walmart: the official store directory URL for Erie redirected to the generic US directory (no Erie listing). The official store finder for 80516 (45 stores within 50 mi) was used instead; no Walmart is listed as Erie. Opened the 8 nearest Supercenters (up to ~12.5 mi).
- Not geocoded; a later pass should check town limits.

## Printed Erie
- **King Soopers (2)**
  - #00129 VISTA RIDGE, 1891 State Highway 7, Erie, CO 80516, 303-729-4161. Hours Sun - Sat: 6 AM - 11 PM. Money Services listed (generic); no money orders, check cashing, bill pay, prepaid reload, Western Union. Locator: 2.95 mi.
  - #00138 Highway 287 and Arapahoe Road, 2900 Arapahoe Rd, Erie, CO **80026**, 303-301-1150. Confirmed official printed city is Erie (page, directory and locator all say Erie), ZIP is 80026. Hours Sun - Sat: 6 AM - 11 PM. Money Services listed (generic) only. Locator: 4.34 mi. Flag for geocode (80026 is a Lafayette ZIP).
  - Account Funding (#00129) not treated as a tracked service. Both list a Gas Station / Fuel Center feature (not separate rows).
- **Walmart (0):** none printed Erie.
- Total printed Erie: 2.

## Nearby stores opened (20)
- **King Soopers (12):** Frederick #00154 (80504; no money services); Louisville #00013 (80027; Money Orders); Louisville Marketplace #00142 (80027; Money Orders + Check Cashing); Broomfield 136th and Zuni #00118 (80023), Miramonte and 287 #00089 (80020), Broomfield on Sheridan #00086 (80020) (all Money Orders); Thornton 136th and Colorado #00101, 136th and Quebec #00116 (80602) (Money Orders); Longmont Hover Street #00080 (80501), Pace Street #00102 (80504) (Money Orders); Boulder Gun Barrel #00028 (80301) (Money Orders); Firestone #00105 (80504; Money Orders).
- **Walmart Supercenters (8):** Lafayette #1045 (745 US Hwy 287, 80026, 5.52 mi); Westminster W 136th Ave #3867 (80234); Broomfield W 121st Ave #4288 (80020); Longmont E Ken Pratt #905 (80504; Walmart Fuel Station listed); Brighton E 128th Ave #4567 (80602); Broomfield Summit Blvd #5341 (80021); Brighton W Bromley Ln #1659 (80601); Longmont Main St #5370 (80504). All show generic "Money Services" only.
- Other Supercenters in the 80516 finder not opened (farther, ~11-30 mi): Thornton Grant St #1231, Westminster Sheridan #2223 and #3824, Commerce City #2752, Arvada #4734, Lakeside #5957, Denver/Aurora/Lakewood/Englewood/Littleton, Loveland #953/#1008, Greeley #980/#5051, Evergreen #2293 and others.

## Excluded by policy
- Walmart Neighborhood Markets (listed, pages not opened): #4747 Northglenn, 10755 Washington Street, 80233; #3019 Thornton E 88th Ave, 850 E 88th Ave, 80229. Also in finder (not rows): #3127 Denver Chambers Rd, #3128 Denver S Parker Rd, #4196 Aurora E Iliff, #3126 Centennial E Smoky Hill, #3740 Aurora E Quincy.
- Fuel centers appear only as features on King Soopers/Walmart pages (not separate rows). The King Soopers Fuel-filter search was not re-run this pass.

## Unexpected brands
- None seen (no City Market, Safeway, etc.) in the King Soopers locator or Walmart finder results.

## Findings
- King Soopers: "Money Services" named on 13 of 14 pages (not Frederick). "Money Orders" on 11 (not Erie #00129/#00138, not Frederick). "Check Cashing" only on Louisville Marketplace #00142. No page named bill pay, prepaid reload or Western Union. Account Funding, Coinstar, ATM, Bank not flagged.
- Walmart: all 8 are Supercenters with generic "Money Services" only; none named money orders, check cashing, bill pay, prepaid reload or Western Union.
- Hours: store hours only (King Soopers "Sun - Sat: 6 AM - 11 PM"; Walmart "Mon - Sun | 6am - 11pm"); pharmacy, fuel, sensory-friendly and holiday hours excluded.

## Coverage gaps
- Walmart Erie directory empty/redirected; relied on store finder. No Walmart in Erie found.
- Farther King Soopers/Walmart stores and Neighborhood Market pages not transcribed.

CSV: `erie-walmart-ks-2026-11-12.csv` (this folder)
