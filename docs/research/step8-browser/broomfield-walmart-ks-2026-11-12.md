# Broomfield, CO money-services store-page review — 2026-11-12

## Coverage
- Opened **37 official store detail pages**: 27 King Soopers and 10 Walmart (8 Supercenters, 2 Neighborhood Markets).
- King Soopers locator search "Broomfield, CO" returned 32 results across 4 pages. Opened all 27 detail pages from pages 1–3 (distance ≤ ~9 mi). Page 4's 5 results (Union Station Denver, Sloans Lake Edgewater, Quail Street Lakewood, Frederick, Speer Blvd Denver; 12+ mi) were not opened as out of range. Fuel centers do not appear as separate listings; they show only as a feature on store pages.
- Walmart store finder was not used; used Walmart's official store directories: Broomfield (2), Westminster (3), Thornton (2), Northglenn (1), Arvada (1), Lafayette (1) — all 10 opened. Directories for Louisville, Superior, Erie, Commerce City, Boulder, Federal Heights, Wheat Ridge returned no Walmart stores.
- Human check: Walmart "Robot or human?" press-and-hold appeared once (Thornton Grant St #1231); completed with a ~9s hold and the page loaded.
- No loaded store pages were left incomplete.
- Skips (earlier 2026-11-12 complete official-page rows): Walmart Longmont #5370 and #905 — see `docs/research/step8-browser/longmont-walmart-ks-2026-11-12.csv`. Westminster/Thornton/Arvada Walmarts (earlier files dated 11-11) were re-opened. Lakewood Walmarts (directory lists 2) not opened.

## Printed Broomfield
- **King Soopers (3):** Miramonte and 287 (1150 Us Highway 287, 80020); Broomfield on Sheridan (12167 Sheridan Blvd, 80020); 136th and Zuni (2355 W 136Th Ave, 80023).
- **Walmart (2):** W 121st Ave Supercenter #4288 (4651 W 121st Ave, 80020); Summit Blvd Supercenter #5341 (500 Summit Blvd, 80021).
- Total printed Broomfield: 5.

## Nearby/out-of-city pages opened (32), by printed city
- **Westminster:** KS Wadsworth and Church Ranch; KS 104th and Federal; Walmart #3867 (W 136th Ave), #2223 (9499 Sheridan), #3824 (7155 Sheridan).
- **Louisville:** KS LOUISVILLE; KS Louisville Marketplace.
- **Arvada:** KS Lake Arbor, 80th and Sheridan, Candelas, Lloyd King Center, 64th and Ward, 58th and Ralston, Westwoods; Walmart #4734 Supercenter.
- **Erie:** KS Highway 287 and Arapahoe Road; KS Vista Ridge.
- **Thornton:** KS 104th and Washington, Mission Trace, 136th and Colorado Blvd, 136th and Quebec; Walmart #1231 Supercenter; Walmart #3019 Neighborhood Market.
- **Denver (printed):** KS Federal Heights (printed "Denver, CO 80260").
- **Boulder:** KS Table Mesa, 30th Street Boulder, Gun Barrel.
- **Wheat Ridge:** KS Ridge Village on 38th Ave; KS Applewood.
- **Commerce City:** KS Commerce City Plaza.
- **Northglenn:** Walmart #4747 Neighborhood Market.
- **Lafayette:** Walmart #1045 Supercenter.
- No King Soopers pages printed Superior, Lafayette, or Northglenn in the results.

## Findings
- **King Soopers:** every page shows a "Money Services" tag; "Money Orders" is explicitly tagged on 24 of 27 (not on Erie Hwy 287/Arapahoe, Candelas, Vista Ridge). "Check Cashing" is tagged only at Louisville Marketplace. No Bill Pay, prepaid reload, or Western Union tag on any page. Most pages also tag "Account Funding"; it is not a named prepaid-reload service, so prepaid_reload is False (noted in the CSV).
- **Walmart:** the 8 Supercenters show only a generic "Money Services" label (money_services_generic True; others False). The two Neighborhood Markets (#3019, #4747) show no Money Services tag and are recorded with a Neighborhood Market note.
- **Hours rule:** only store hours (KS "Sun - Sat: 6 AM - 11 PM"; Walmart "Mon - Sun | 6am - 11pm"); pharmacy, fuel, sensory-friendly, and holiday lines excluded.
- **Fuel:** several King Soopers pages (Miramonte, Broomfield on Sheridan, 136th and Zuni, Louisville, Louisville Marketplace, 80th and Sheridan) list a gas station/fuel center; noted only, no separate rows.
- **Unexpected brands in the King Soopers locator results:** none (all results were King Soopers).

## CSV
`docs/research/step8-browser/broomfield-walmart-ks-2026-11-12.csv`
