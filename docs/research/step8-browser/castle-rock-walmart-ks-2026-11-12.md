# Castle Rock, CO money-services store-page review — 2026-11-12

## Coverage
- Opened **49 official store detail pages**: 33 King Soopers and 16 Walmart.
- King Soopers locator search "Castle Rock, CO" returned 34 results across 4 pages (page-number buttons clicked; the `page=` URL parameter is ignored). 33 grocery detail pages were opened. The 1 remaining result was a **fuel center** (Aurora Fuel, store 00669, /stores/fuel/) — not opened, not a row.
- Walmart store finder for "Castle Rock, CO" returned **0 stores** ("couldn't find any matching results"), so used the official Walmart Colorado store directory (Castle Rock, Parker, Highlands Ranch, Monument, Centennial, Littleton, Elizabeth, Englewood, Arvada) plus the "Nearby stores" lists on store pages (Aurora, Denver, Colorado Springs, Woodland Park). Arvada directory listing seen (Arvada Supercenter #4734) but page not opened.
- Human check: Walmart "Robot or human?" press-and-hold appeared on Littleton, Elizabeth and Englewood pages; completed on first 10s hold; Englewood loaded, and later loads of Littleton and Elizabeth succeeded.
- Not opened/incomplete: Aurora E Quincy Ave NM #3740 and Aurora E Iliff Ave NM #4196 (URL guesses redirected to other stores; not recorded). Centennial NM #3126 loaded once (recorded) but a later reload showed a different store, so its Money Services status was not re-confirmed (flags False, noted in CSV).

## Printed Castle Rock
- **King Soopers (2):** Ridge Road #00132 (750 N Ridge Rd, 80104); Promenade Parkway #00125 (5544 Promenade Pkwy, 80108).
- **Walmart (1):** Castle Rock Supercenter #984 (133 Sam Walton Lane, 80104).
- Total printed Castle Rock: 3.

## Nearby/out-of-city pages opened (46), by printed city
- **Castle Pines:** KS Castle Pines.
- **Parker (5):** KS Parker (24 hours), Stroh Ranch, Crossing at Stonegate, Cottonwood Drive; Walmart Supercenter #2892.
- **Highlands Ranch (5):** KS Red Cedar Drive, University and Colorado, Quebec St Highland Ranch, Wildcat Reserve; Walmart #1252.
- **Monument:** Walmart #3227.
- **Elizabeth:** Walmart #4639.
- **Centennial (5):** KS County Line and Holly, Cherrywood Square, Smoky Hill and Himalaya; Walmart Briarwood Supercenter #3313; Walmart Smoky Hill Rd **Neighborhood Market #3126**.
- **Littleton (8):** KS Mineral and Broadway, Littleton and Broadway, Columbine Knolls Village, Coalmine and Pierce, Ken Caryl, Governors Plaza; Walmart #1308, #5049.
- **Greenwood Village (2):** KS The Orchards on Holly, Belleview Square.
- **Englewood (4):** KS Federal and Belleview, Fresh Fare, Englewood Pkwy and S Broadway; Walmart #2751.
- **Aurora (8):** KS Arapahoe Crossing, Smoky Hill and Arapahoe, Quincy Place Mission Viejo, Nine Mile, Hampden Crossing, Iliff at Buckley; Walmart #1689, #1492.
- **Denver (3):** KS Southmoor, University Hills; Walmart #3566.
- **Colorado Springs (2):** Walmart #1896, #5123 (far; opened from nearby lists).
- **Woodland Park (1):** Walmart #3805 (far).
- No Larkspur, Sedalia or Franktown stores appeared in either official source (no pages printed with those cities).
- No King Soopers pages printed as Lone Tree.

## Findings
- King Soopers: "Money Services" named on 32 of 33 pages (not on Parker #00175, which lists only Pickup). "Money Orders" named on 29 pages (not on Parker, Littleton and Broadway, Nine Mile, Fresh Fare). "Western Union" named on Cottonwood Drive (Parker) only. No page named check cashing, bill pay or prepaid reload. Account Funding, Coinstar, ATM etc. are not among the six flags and are not flagged.
- Walmart: all Supercenters show generic "Money Services" only (money orders, check cashing, bill pay, prepaid reload, Western Union not named; Englewood's expanded Other services also listed Financial Services/Academy Bank/Coinstar/ecoATM, not flagged). One Neighborhood Market (Centennial #3126) is in the CSV with note for policy exclusion.
- Hours: official store hours only (KS "Sun - Sat: 6 AM - 11 PM"; Walmart "Mon - Sun | 6am - 11pm", Castle Rock 6am - 10pm); pharmacy, fuel, sensory-friendly, holiday lines excluded.
- Unexpected grocery/retail brands in King Soopers locator results: none (only King Soopers grocery plus one King Soopers fuel center).

CSV: `/workspace/checkdesk/research/castle-rock-walmart-ks-2026-11-12.csv`
