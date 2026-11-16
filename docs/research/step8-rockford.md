# Step 8: Rockford, IL (2026-11-16, America/Denver)

Prepared 2026-11-16 (America/Denver). Fifth Illinois city in the standing 50-state run (ship order: Chicago, Aurora, Illinois, Naperville, Joliet, Rockford). Post Offices only. Hours on the Rockford pages are Central Time. Census place: Rockford city, GEOID 1765000, in Winnebago County (GEOID 17201; Vintage 2025 place-county population 147,384) with an Ogle County remainder of 0. July 1, 2025 population 147,384 (Vintage 2025, SUMLEV 162). This is Rockford, Illinois, in Winnebago County, not a Rockford in another state, and not Loves Park or Machesney Park. Official printed-Rockford ZIPs from search.asp: 14 (search 15; Machesney Park 61115 excluded). OpenStreetMap was not used.

Shared Illinois sweep raw files: `/workspace/step8il/`. All 591 official pages returned HTTP 200 and `match_api`, and all 591 records were geocoded on current and 2020 address and coordinate lookups with 0 errors.

Listed (4), all with money-order tags and printed city Rockford. Both address files and both official map points are in Rockford city, in Winnebago County. No map-point fallback:

- Broadway (1379655, 1140 Broadway, Rockford, 61104; Census matched 1140 BROADWAY, ROCKFORD, IL, 61104). Phone 815-968-9522. Weekdays 09:30–12:00 and 12:30–17:00, Saturday closed, Sunday closed.
- Downtown Rockford (1379657, 401 S Main St Fl 1, Rockford, 61101; Census matched 401 S MAIN ST, ROCKFORD, IL, 61101). Phone 815-962-5940. Weekdays 08:30–17:00, Saturday closed, Sunday closed.
- East Rockford (1361831, 111 N 6th St, Rockford, 61107; Census matched 111 N 6TH ST, ROCKFORD, IL, 61107). Phone 815-962-8565. Weekdays 08:30–17:00, Saturday 08:30–12:30, Sunday closed.
- Kilburn Rockford (1435502, 2440 Kilburn Ave, Rockford, 61101; Census matched 2440 KILBURN AVE, ROCKFORD, IL, 61101). Phone 815-962-8359. Weekdays 09:00–17:00, Saturday 09:00–14:30, Sunday closed.

Holds (2), both at 5225 Harrison Ave, printed Rockford, no money-order tags:

- Rockford (1434900, 5225 Harrison Ave, Rockford, 61125). The official page does not list money orders and has no BUSINESS hours. The current address file matched 5225 HARRISON AVE, ROCKFORD, IL, 61125 in Rockford city, and both official map points fall there. The 2020 address file snapped to a different street, 5225 HARRISON RD, ROCKFORD, IL, 61101, about 10 miles away; that snap was discarded.
- Rockford IL S&DC (1579665, 5225 Harrison Ave, Rockford, 61125). The official page publishes BUSINESS hours but does not list money orders. The current address file and both official map points are in Rockford city, with the same discarded 2020 Harrison Road snap.

Held because the official pages do not list money orders. No other office in the Illinois locator sweep geocodes into Rockford city.

Evenings: 0. Weekends: 2 (East Rockford Saturday 08:30–12:30; Kilburn Rockford Saturday 09:00–14:30). No Sunday hours. A 17:00 close does not count as Open evenings.

## Result

4 listed Post Offices, all with money orders. 0 Open evenings. 2 Open weekends. Hours labeled Central Time.

## Site changes in this PR

- New `data/locations/rockford.csv` and `/rockford/`, `/rockford/money-orders/`, and `/rockford/after-hours/` pages.
- Rockford is inserted under Illinois after Joliet on the home page and `/cities/`. Home and `/cities/` meta now say Chicago, Aurora, Naperville, Joliet, and Rockford, Illinois. No other city CSV or page changed except those meta and list lines. This finishes Illinois's five. Do not start Indiana in this PR.
