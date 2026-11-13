# Huntsville, AL — Walmart Supercenter Census geocodes (2026-11-12 research; lookups run 2026-11-13)

Research only. Nothing was built, committed, or deployed. No business was contacted. OpenStreetMap was not used. last_verified (Census lookups): 2026-11-13, about 9:50 AM America/Denver.

Official store addresses and map coordinates for the five Huntsville-printed Supercenters come from the 2026-11-12 official walmart.com store-page research (`huntsville-walmart-2026-11-12.md`). Three nearby Supercenters that print other cities were added to the same geocoding check.

## Method

U.S. Census Bureau Geocoder only, geographies endpoint, two files each time:

- Current: `benchmark=Public_AR_Current`, `vintage=Current_Current`
- 2020 Census: `benchmark=Public_AR_Census2020`, `vintage=Census2020_Census2020`
- Layers: Incorporated Places, Census Designated Places, Counties
- Address: `https://geocoding.geo.census.gov/geocoder/geographies/address`
- Official map point: `https://geocoding.geo.census.gov/geocoder/geographies/coordinates` (`x` = longitude, `y` = latitude)

Place names below are Census NAME values (`Huntsville city` GEOID 0137000; `Madison city` GEOID 0145784). Every row is in Madison County (GEOID 01089) in both files. No CDP was returned for any lookup.

## Inclusion rule applied

- Huntsville-printed stores: include only if the printed city is Huntsville and an address match **or** the official map point lands in Huntsville city. If the address match and the official map point disagree, flag as HOLD.
- Other-city-printed stores: if they do not print Huntsville but an address match or official map point lands in Huntsville city, flag as HOLD (printed city vs geocode disagreement). If they geocode in their printed city, mark **left off, other city**.

## Decision table

| Store | Printed city | Official address | Current address (place / county) | 2020 address (place / county) | Official point current | Official point 2020 | Decision |
|---|---|---|---|---|---|---|---|
| 375 | Huntsville | 3031 Memorial Pkwy SW, Huntsville, AL 35801 | no match | no match | Huntsville city, Madison County | Huntsville city, Madison County | **include** (map point) |
| 433 | Huntsville | 2200 Sparkman Dr NW, Huntsville, AL 35810 | 2200 SPARKMAN DR NW, HUNTSVILLE, AL, 35810 — Huntsville city, Madison County | same matched address — Huntsville city, Madison County | Huntsville city, Madison County | Huntsville city, Madison County | **include** |
| 332 | Huntsville | 6140a University Dr NW, Huntsville, AL 35806 | 6140A UNIVERSITY DR NW, HUNTSVILLE, AL, 35806 — Huntsville city, Madison County | same matched address — Huntsville city, Madison County | Huntsville city, Madison County | Huntsville city, Madison County | **include** |
| 434 | Huntsville | 11610 Memorial Pkwy SW, Huntsville, AL 35803 | 11610 MEMORIAL PKWY SW, HUNTSVILLE, AL, 35803 — Huntsville city, Madison County | same matched address — Huntsville city, Madison County | Huntsville city, Madison County | Huntsville city, Madison County | **include** |
| 7324 | Huntsville | 2165 Winchester Rd NE, Huntsville, AL 35811 | 2165 WINCHESTER RD NE, HUNTSVILLE, AL, 35811 — Huntsville city, Madison County | same matched address — Huntsville city, Madison County | Huntsville city, Madison County | Huntsville city, Madison County | **include** |
| 2690 | Madison | 8650 Madison Blvd, Madison, AL 35758 | 8650 MADISON BLVD, MADISON, AL, 35758 — Madison city, Madison County | same matched address — Madison city, Madison County | Madison city, Madison County | Madison city, Madison County | **left off, other city** |
| 5703 | Madison | 8580 Hwy 72 W, Madison, AL 35758 | 8580 US HWY 72, MADISON, AL, 35758 — **Huntsville city**, Madison County | same matched address — **Huntsville city**, Madison County | **Huntsville city**, Madison County | **Huntsville city**, Madison County | **HOLD** (printed Madison, geocodes in Huntsville city) |
| 5197 | Owens Cross Roads | 330 Sutton Rd SE, Owens Cross Roads, AL 35763 | 330 SUTTON RD, OWENS CROSS ROADS, AL, 35763 — **Huntsville city**, Madison County | same matched address — **Huntsville city**, Madison County | **Huntsville city**, Madison County | **Huntsville city**, Madison County | **HOLD** (printed Owens Cross Roads, geocodes in Huntsville city) |

Official map points used: 375 (34.703017, -86.585392); 433 (34.765271, -86.592518); 332 (34.747008, -86.675822); 434 (34.615879, -86.570722); 7324 (34.820138, -86.492473); 2690 (34.683846, -86.741089); 5703 (34.751176, -86.773609); 5197 (34.657641, -86.485439).

## Notes by store

### Includes (5), all Huntsville-printed

- **#375.** No address match in either Census file. The official map point is in Huntsville city, Madison County, on both the current and 2020 benchmarks. Included on the map point. The same street abbreviation (`Memorial Pkwy SW`) did match for store 434, so this is likely a missing TIGER address range for 3031, not a street-name problem. No printed-city disagreement.
- **#433, #434, #7324.** Address match and official map point are Huntsville city, Madison County, in both files.
- **#332.** Official `6140a University Dr NW` matched as `6140A UNIVERSITY DR NW` in both files. The fallback `6140 University Dr NW` was not required. Address match and official map point are Huntsville city, Madison County, in both files.

### HOLD (2), other printed city but inside Huntsville city

- **#5703**, 8580 Hwy 72 W, printed **Madison**, AL 35758. Census matched the street as `8580 US HWY 72, MADISON, AL, 35758`. The matched-address city string still says Madison (postal city), but the incorporated place for that match is **Huntsville city**, and the official map point is also **Huntsville city**, on both benchmarks, all in Madison County. HOLD: do not list in Huntsville unless a later decision overrides the hold.
- **#5197**, 330 Sutton Rd SE, printed **Owens Cross Roads**, AL 35763. Census matched the street as `330 SUTTON RD` (directional SE dropped), city string Owens Cross Roads. The incorporated place for that match is **Huntsville city**, and the official map point is also **Huntsville city**, on both benchmarks, all in Madison County. HOLD: do not list in Huntsville unless a later decision overrides the hold.

### Left off, other city (1)

- **#2690**, 8650 Madison Blvd, printed **Madison**, AL 35758. Address match and official map point are **Madison city**, Madison County, in both files. Geocodes in its printed city, not in Huntsville city. Left off as another city's store.

## Files

- This note: `/workspace/checkdesk/research/huntsville-walmart-geocode-2026-11-12.md`
- Spreadsheet of the same rows: `/workspace/checkdesk/research/huntsville-walmart-geocode-2026-11-12.csv`
