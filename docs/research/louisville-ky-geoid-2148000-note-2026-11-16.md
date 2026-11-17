# Louisville city (GEOID 2148000) and the SUMLEV 162 balance (2026-11-16, America/Denver)

Check Desk ranks and defines Louisville, Kentucky, as the Census Vintage 2025 SUMLEV 162 place “Louisville/Jefferson County metro government (balance)” (GEOID 2148006, 641,962). That Population Estimates / ACS definition includes the former Louisville city extent. OpenStreetMap was not used.

The Census geocoder’s Incorporated Places layer, and the 2025 and 2026 place gazetteers, still carry a second, non-functioning place record:

- GEOID 2148000, “Louisville city”, LSAD 25, FUNCSTAT N, about 61.465 square miles of land (2026 Gazetteer).
- GEOID 2148006, “Louisville/Jefferson County metro government (balance)”, LSAD 00, FUNCSTAT F, about 262.967 square miles of land (2026 Gazetteer).

Census Bureau, 2013 Geography Changes, “Changes to Louisville/Jefferson County Metro Government (Balance)”: in 2013, Geography Division created a new incorporated place record with a non-functioning status for the former Louisville city extent, and reduced the TIGER balance record by excluding that extent. ACS does not publish estimates for the unique Louisville city extent. For ACS and the Population Estimates Program, the SUMLEV 162 / summary-level 160 balance keeps the former definition that includes the Louisville city extent. Source: https://www.census.gov/programs-surveys/acs/technical-documentation/table-and-geography-changes/2013/geography-changes.html

Gazetteer lines (U.S. Census Bureau, 2026 Gazetteer, 2026_gaz_place_21.txt):

```
KY|2148000|1600000US2148000|02404963|Louisville city|25|N|159192984|12488302|61.465|4.822|38.224692|-85.741067
KY|2148006|1600000US2148006|01967434|Louisville/Jefferson County metro government (balance)|00|F|681080338|30150106|262.967|11.641|38.165376|-85.647377
```

Therefore, a city-limits check that looks only for TIGER GEOID 2148006 would omit offices in the former city (downtown Louisville and nearby neighborhoods), which are inside the Check Desk / Vintage 2025 balance. Classification treats a geocode leg as inside Louisville if the Incorporated Places layer returns 2148006 or 2148000. Offices that geocode in one of the 83 other Jefferson County municipalities (Jeffersontown, St. Matthews, Lyndon, Middletown, Anchorage, Watterson Park, and the rest) remain held out. This is not a map-point fallback.
