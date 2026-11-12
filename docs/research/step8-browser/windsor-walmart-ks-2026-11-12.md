# Windsor, CO money-services store-page review — 2026-11-12

## Coverage
- Opened **20 official store detail pages**: 13 King Soopers and 7 Walmart Supercenters. All King Soopers pages returned HTTP 200; Walmart pages returned HTTP 200 (#1008 first showed a "Robot or human?" press-and-hold, completed with a 10s hold, then the official page loaded).
- Walmart: official store directory for Windsor, CO loaded but lists **0 stores**. Directories also checked for Johnstown, Evans, Severance, Eaton, Milliken, Berthoud, Firestone, Frederick (all empty), Timnath (1), Greeley (2), Loveland (2); the Fort Collins directory slug rendered empty, so the two Fort Collins stores came from the nearby-stores lists on the Timnath/Magnolia pages. The Walmart store finder was not used.
- King Soopers: opened the Windsor page plus nearby pages (Loveland, Fort Collins, Greeley, Firestone, Frederick). The King Soopers locator search itself was not re-run this pass; no King Soopers pages printed as Johnstown, Severance, Timnath, Eaton, Evans or Milliken in the related Loveland/Greeley/Fort Collins research.
- No Neighborhood Market pages and no separate fuel-only listings appeared. Fuel is only a feature on store pages (King Soopers Windsor "Fuel Center"; Walmart #5051 and #953 "Walmart Fuel Station") and not made separate rows; excluded by policy.
- Not geocoded; later geocode pass should check Greeley 47th Ave #5051/Westlake/North Gate Village and Fort Collins/Timnath/Firestone stores for position vs. Windsor town limits.

## Printed Windsor
- **King Soopers (1):** Windsor #00104, 1520 Main St, Windsor, CO 80550, 970-674-2830. Hours Sun - Sat: 6 AM - 11 PM. Money Services and Money Orders listed; no check cashing, bill pay, prepaid reload, Western Union.
- **Walmart (0):** none printed Windsor.
- Total printed Windsor: 1.

## Nearby/out-of-city pages opened (19)
- **King Soopers — Firestone (1):** Firestone #00105, 6110 Firestone Blvd, 80504, 303-682-4160.
- **King Soopers — Frederick (1):** Frederick #00154, 5801 Silverstone Dr, 80504.
- **King Soopers — Loveland (2):** Eagle Drive #00074 (80537), 29th Street #00044 (80538).
- **King Soopers — Fort Collins (5):** CEDARWOOD, JFK Parkway, Timberline, North College Marketplace, Midtown Marketplace.
- **King Soopers — Greeley (3):** North Gate Village, University Square, Westlake.
- **Walmart — Timnath (1):** Supercenter #4599, 4500 Weitzel St (nearest Walmart by listing; closest candidate for a later geocode check).
- **Walmart — Greeley (2):** 47th Ave #5051; S 23rd Ave #980.
- **Walmart — Fort Collins (2):** E Magnolia St #2729; S Mason St #3177.
- **Walmart — Loveland (2):** N Denver Ave #953; W 65th St #1008.

## Excluded by policy
- No Neighborhood Market or standalone fuel station pages found. Fuel Center / Walmart Fuel Station features noted above on King Soopers #00104 and Walmart #5051, #953.

## Unexpected brands
- None seen (no City Market, Safeway, etc.).

## Findings
- King Soopers: "Money Services" named on 12 of 13 pages (not Frederick). "Money Orders" named on the same 12. "Check Cashing" and "Western Union" named only on Midtown Marketplace (Fort Collins). No page named bill pay or prepaid reload. Account Funding, Coinstar, ATM, Bank not flagged.
- Walmart: all 7 are Supercenters showing generic "Money Services" only; money orders, check cashing, bill pay, prepaid reload, Western Union not named.
- Hours: store hours only (King Soopers "Sun - Sat: 6 AM - 11 PM"; Walmart "Mon - Sun | 6am - 11pm"); pharmacy, fuel, sensory-friendly and holiday hours excluded.

CSV: `windsor-walmart-ks-2026-11-12.csv` (this folder)
