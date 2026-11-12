# Lafayette, CO money-services store-page review — 2026-11-12

## Coverage
- Opened **10 official store detail pages**: 5 King Soopers (all HTTP 200) and 5 Walmart Supercenters (all HTTP 200; a "Robot or human?" press-and-hold appeared on first load of #1045, completed with a 10s mouse hold, then pages loaded).
- CSV rows: 13 (5 King Soopers, 5 Walmart Supercenters, 3 Walmart Neighborhood Markets excluded by policy).
- King Soopers: re-ran official locator (`/stores/search?searchText=Lafayette, CO 80026`, 31 results, 4 pages; only page 1, nearest 9, read). The city directory `/stores/grocery/co/lafayette` returned "that page doesn't exist" (no King Soopers prints Lafayette).
- Walmart: re-ran official store finder (`/store-finder?location=80026`, 45 stores within 50 mi). Only one prints Lafayette. The #1045 page's Nearby stores list was also read.
- Not geocoded.

## Printed Lafayette
- **Walmart (1):** #1045 Lafayette Supercenter ("Walmart Supercenter #1045"), 745 Us Highway 287, Lafayette, CO 80026, 303-666-0340. https://www.walmart.com/store/1045-lafayette-co. Hours Mon - Sun | 6am - 11pm (holiday, sensory-friendly, pharmacy lines excluded). Services section lists Money Services (generic tag only); page does not name money orders, check cashing, bill pay, prepaid reload or Western Union. HTTP 200. Finder: 1.02 mi.
- **King Soopers (0):** none print Lafayette.

## Nearby / geocode list
- **King Soopers #00138 Highway 287 and Arapahoe Road**, 2900 Arapahoe Rd, printed **Erie**, CO 80026, 303-301-1150 (page, locator say Erie). Hours Sun - Sat: 6 AM - 11 PM. Money Services generic only; Fuel Center feature. Locator 1.24 mi — **flag for Lafayette vs Erie geocode check**.
- King Soopers opened: Louisville #00013 (80027, 1.38 mi; Money Orders + Money Services); Louisville Marketplace #00142 (80027, 4.18 mi; Money Orders + Check Cashing + Money Services); Miramonte and 287 #00089 (Broomfield 80020, 4.27 mi; Money Orders + Money Services); VISTA RIDGE #00129 (Erie 80516, 4.76 mi; Money Services only).
- King Soopers listed in locator, not opened this run: 136th and Zuni #00118 (Broomfield 80023, 5.65 mi); Broomfield on Sheridan #00086 (80020, 5.82 mi); Gun Barrel (6550 Lookout Rd Boulder 80301, 7.59 mi); TABLE MESA (3600 Table Mesa Dr Boulder 80305, 8.08 mi). Locator pages 2–4 (22 farther stores) not read. (Erie research opened #00118 and #00086 earlier: Money Orders + Money Services.) Store number for Gun Barrel not shown in locator list; Erie research listed Gun Barrel as #00028.
- Walmart Supercenters opened: Broomfield Summit Blvd #5341 (500 Summit Blvd, 80021, 5.41 mi); Broomfield W 121st Ave #4288 (80020, 5.96 mi); Westminster W 136th Ave #3867 (80234, 6.55 mi); Westminster 9499 Sheridan Blvd #2223 (80031, 9.02 mi; phone not captured). All Mon - Sun | 6am - 11pm, generic Money Services only.
- Walmart listed, not opened (farther): Thornton Grant St #1231 (9.95), Brighton E 128th #4567 (10.76), Longmont E Ken Pratt #905 (11.41), Westminster 7155 Sheridan #3824, Arvada #4734, Brighton W Bromley #1659, Longmont Main St #5370, Lakeside #5957, Commerce City #2752, and others up to ~25 mi.

## Excluded by policy
- Walmart Neighborhood Markets (pages not opened): #4747 Northglenn (9.32 mi); #3019 Thornton E 88th Ave (11.51 mi); #3127 Denver Chambers Rd (20.71 mi); also #3128 Denver S Parker Rd.
- Fuel centers appear only as features on King Soopers pages (not separate rows); KS Fuel filter not run.

## Unexpected brands
- None seen (no City Market, Safeway, etc.).

## Findings
- Only one in-scope store prints Lafayette (Walmart #1045); no named money orders/check cashing/bill pay/prepaid reload/Western Union.
- King Soopers: Money Orders at #00013, #00142, #00089; Check Cashing only #00142; no bill pay, prepaid reload or Western Union. Account Funding, ATM, Coinstar not flagged.
- Hours are store hours only.

## Coverage gaps
- KS locator pages 2–4 unread; #00118, #00086, Boulder stores not reopened this run.
- Walmart #2223 phone not captured; Neighborhood Market pages not opened.
- Walmart's separate directory pages not used; the finder worked.

CSV: `/workspace/checkdesk/research/lafayette-walmart-ks-2026-11-12.csv`
