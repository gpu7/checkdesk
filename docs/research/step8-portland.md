# Portland, ME — community-named office added 2026-11-19

The Cliff Island Post Office is now listed on the Portland, Maine pages, under the rule approved 2026-11-19: the official page prints a community name, both the current and 2020 Census address files place the address inside Portland city (GEOID 2360545), money-order tags are present, and the displayed city stays the official printed USPS city. Official map points also fall in Portland city on both files. The original Portland-printed rows are unchanged.

Added office (printed city in parentheses): Cliff Island (Cliff Island). Cliff Island is a community inside Portland city, not a separately incorporated place. The official address is 11 Sunset Rd Unit 1; both Census address files matched 11 SUNSET RD, CLIFF ISLAND, ME, 04019.

The Portland, Maine list is now 3 Post Offices, all with money orders (one Open evenings, unchanged: Downtown Station until 5:30 p.m.; three Open weekends, Saturday only, including Cliff Island 8:30 a.m. to 12:15 p.m.). Cliff Island weekday retail closes at 4:45 p.m. after a 1:00–2:00 p.m. midday closure, so it is not labeled Open evenings. Hours stay Eastern Time. Peaks Island stays held (no money-order tags). Two Portland-printed offices remain held for no money-order tags. Portland, Oregon and South Portland were not changed.

The body below is the original 2026-11-16 memo and is superseded for listed and hold counts.

# Portland, Maine USPS research (2026-11-16, America/Denver)

First Maine city (ship order: Portland, Lewiston, Bangor, South Portland, Auburn). Post Offices only. Hours labeled Eastern Time (49 CFR 71.4). Census place is Portland city, GEOID 2360545, Vintage 2025 population 69,911, in Cumberland County (GEOID 23005). This is Portland, Maine, not Portland, Oregon, and not South Portland, Westbrook, Falmouth, or Cape Elizabeth. OpenStreetMap was not used.

ZIP inventory used zip-codes.com county pages for Cumberland, Androscoggin, and Penobscot Counties plus Census-adjacent Maine counties (437 in-scope ZIPs), and the official Portland, ME search.asp list. Official Portland self ZIPs are 04101, 04102, 04103, 04104, 04109, 04112, and 04122. The Portland search also lists Falmouth, South Portland, Cape Elizabeth, Peaks Island, Cumberland Foreside, and New Portland; those are not Portland self ZIPs. Locator pass 1 (5 and 15 miles) and pass 2 (1, 2, 3, 10, and 20 miles) found 466 unique offices. Official USPS location pages were fetched for all 466 (all HTTP 200). All 466 were geocoded on the Census current and 2020 address and coordinate files, 0 errors.

## Listed (2)

Both print Portland, ME, list money orders, and match Portland city on all four Census legs.

- Downtown Station (1361208, 400 Congress St Ste 9998, 04101). Weekdays 08:30-17:30; Saturday 09:00-13:00.
- Station A (1383436, 622 Congress St Ste 9998, 04101). Weekdays 08:30-17:00; Saturday 09:00-12:00.

Evenings: 1 (Downtown Station; a 17:00 close does not count). Weekends: 2 (both Saturday, none Sunday).

## Holds (4)

### Official page does not list money orders, inside the city (2)

- Portland (1434511, 125 Forest Ave, 04101). No BUSINESS hours block on the official page.
- Portland ME SDC (1582837, 151 Forest Ave, 04101). BUSINESS hours 07:30-19:00 weekdays and 07:30-17:00 Saturday; no money-order tags.

### Prints a different city, all four Census legs in Portland city (2)

- Cliff Island (1358348, 11 Sunset Rd Unit 1, Cliff Island 04019). Lists money orders. Official page prints Cliff Island, ME. All four Census legs fall in Portland city (GEOID 2360545).
- Peaks Island (1601591, 70 Island Ave, Peaks Island 04108). Official page does not list money orders and has no BUSINESS hours block. Official page prints Peaks Island, ME. All four Census legs fall in Portland city (GEOID 2360545).

## Result

2 listed, both with money orders. 1 Open evenings. 2 Open weekends. 4 holds (2 no money-order tags inside the city; 2 printed-city vs Portland city). No map-point fallback. Hours labeled Eastern Time.

## Site changes in this PR

- New `data/locations/portland.csv` and `/portland/`, `/portland/money-orders/`, and `/portland/after-hours/` pages.
- Portland is added as the first Maine city, after Louisiana, on the home page and `/cities/`. Home and `/cities/` meta now end with Lake Charles, Louisiana, and Portland, Maine. The Maine Census Vintage 2025 ranking memo is added under `docs/research/`. No other city CSV or page changed except those meta and list lines. `/augusta/` remains Augusta, Georgia.
