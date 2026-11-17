# Grand Rapids, Michigan USPS research (2026-11-17, America/Denver)

Second Michigan city (ship order: Detroit, Grand Rapids, Warren, Sterling Heights, Ann Arbor). Post Offices only. Hours labeled Eastern Time (49 CFR 71.4; the Eastern–Central boundary in 49 CFR 71.5(a) does not reach Grand Rapids). Census place is Grand Rapids city, GEOID 2634000, Vintage 2025 population 201,183, in Kent County (GEOID 26081). This is Grand Rapids, Michigan, not Grand Junction, Colorado, and not East Grand Rapids, Grand Rapids charter township, Wyoming, or Kentwood. Detroit stays on a separate list. OpenStreetMap was not used.

Official Grand Rapids self ZIPs are 49501, 49502, 49503, 49504, 49505, 49506, 49507, 49508, 49510, 49512, 49514, 49515, 49516, 49518, 49523, 49525, 49528, 49530, 49534, 49544, 49546, 49548, 49555, 49560, 49588, and 49599 (26 self). The Grand Rapids search.asp page also lists Wyoming 49509 and 49519, which are not Grand Rapids self ZIPs. Locator passes and official pages are the shared Michigan sweep (500 offices, all geocoded on the current and 2020 Census files, 0 errors).

## Listed (5)

All print Grand Rapids, MI, list money orders, and match Grand Rapids city on all four Census legs.

- Eastown (1361876, 1451 Lake Dr SE, 49506). Weekdays 09:00-17:00; Saturday 09:00-14:00.
- Ledyard (1437880, 120 Monroe Center St NW, 49503). Weekdays 10:00-16:30; Saturday closed.
- Northeast (1375511, 1765 3 Mile Rd NE, 49505). Weekdays 08:30-17:30; Saturday 09:00-12:00.
- Northwest (1375583, 1625 Walker Ave NW, 49504). Weekdays 08:30-17:00; Saturday 09:00-12:30.
- Seymour Square (1381278, 2017 Eastern Ave SE Ste A, 49507). Weekdays 10:00-17:00; Saturday 09:30-12:00.

Evenings: 1 (Northeast, until 17:30). Weekends: 4 (all Saturday, none Sunday). Eastown, Northwest, and Seymour Square weekday retail closes at 17:00, which does not count as Open evenings. Ledyard weekday retail closes at 16:30 and does not publish weekend hours.

## Holds (5)

No money-order tags, but print Grand Rapids and geocode in Grand Rapids city:

- Centerpointe Postal Store (1441674, 3665 28th St SE Ste 6F, 49512).
- Grand Rapids (1365329, 225 Michigan St NW, 49501).
- Grand River Carrier Annex (1462245, 630 Division Ave S, 49503). The official BUSINESS block lists no retail hours.

Print Grand Rapids, but the Census geocoder places both the address and the official map point in Kentwood city on the current and 2020 files:

- East Paris (1433034, 3970 S Greenbrooke Dr SE, 49512). Lists money orders.
- Kentwood (1437872, 1680 44th St SE, 49508). Lists money orders.

No other office in the Michigan locator sweep geocodes into Grand Rapids city. No map-point fallback.

## Result

5 listed Post Offices, all with money orders. 1 Open evenings. 4 Open weekends, all Saturday, none Sunday. Hours labeled Eastern Time. 5 holds (3 no money-order tags, 2 geocode in Kentwood city). No map-point fallback.

## Site changes in this PR

- New `data/locations/grand-rapids.csv` and `/grand-rapids/`, `/grand-rapids/money-orders/`, and `/grand-rapids/after-hours/` pages.
- Grand Rapids is inserted under Michigan after Detroit on the home page and `/cities/`. Detroit remains 17. The `/grand-junction/` Colorado pages are not touched. No other city CSV or page changed except those meta and list lines.
