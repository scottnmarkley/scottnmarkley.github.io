---
layout: page
title: "Redlining and the HOLC"
permalink: /Projects/HOLC/
lede: "What were the federal &ldquo;redlining&rdquo; maps actually for? I read them as windows into the racial-spatial ideology of twentieth-century real estate, not just as tools for denying loans."
---

## The City Survey Program

This project aims to reframe how researchers and the broader public think about the processes through which racial inequities have been continuously reproduced in sub/urban spaces through time. It centers on the Home Owners&rsquo; Loan Corporation&rsquo;s (HOLC) &ldquo;City Survey&rdquo; program, which the federal government ran in partnership with the real estate industry in the late 1930s to map and grade thousands of neighborhoods in more than 200 cities. The infamous A-to-D grades reflected dominant ideas within the real estate industry about how neighborhood features affected the investment potential of residential property. Among other demographic, socioeconomic, housing, and locational characteristics, the visible presence of Black and non-white immigrant residents weighed heavily in the grading, leading many researchers to credit HOLC with spearheading the practice of &ldquo;redlining.&rdquo;

The precise impact these maps had on the sub/urban housing landscape, however, remains hotly contested. In my critical reappraisal of the redlining debates in [*Urban Studies*](https://doi.org/10.1177/00420980231182336), I contend that the maps and their accompanying &ldquo;Area Description&rdquo; sheets are better seen as windows into the governing racial-spatial ideology of twentieth-century real estate capital than as objects literally used to make lending decisions. With Steve Holloway in the [*Annals of the American Association of Geographers*](https://doi.org/10.1080/24694452.2024.2350993), I put the HOLC data to use in a statistical analysis showing that racial segregation is a more salient source of lasting injustice than map grades, work that won the IPUMS Spatial Research Award. In [*Urban Geography*](https://doi.org/10.1080/02723638.2025.2492218), A. Bonds and I used qualitative GIS to show how appraisers applied a &ldquo;racist theory of value&rdquo; that went far beyond the maps.

<figure>
<div class="fig-pair">
<img src="/HOLC/ATLHOLC.jpg" alt="HOLC Residential Security map of Atlanta">
<img src="/HOLC/ATLADS.jpg" alt="Sample HOLC Area Description sheet">
</div>
<figcaption>HOLC&rsquo;s map of Atlanta and a sample Area Description sheet. Source: <a href="https://dsl.richmond.edu/panorama/redlining/"><em>Mapping Inequality</em></a>, Digital Scholarship Lab, University of Richmond.</figcaption>
</figure>

## Tabulating the Area Descriptions

The Digital Scholarship Lab at the University of Richmond has made the HOLC maps and field notes available through *Mapping Inequality*, along with a geopackage and GeoJSON for use in GIS software. Building on that effort, I converted the data in HOLC&rsquo;s Area Descriptions into readable tables, called **THOLCADS**, available at [Open Science Framework](https://osf.io/qytj8/) and through the [Leventhal Map &amp; Education Center](https://data.leventhalmap.org/#/catalog/dkyajewyh). Variables such as the Black population percentage, &ldquo;foreign born&rdquo; percentage and group, family income, occupation class, average building age, repair status, and mortgage availability are ready for statistical analysis, and the remaining entries can be searched by keyword. The R code is on [GitHub](https://github.com/snmarkley1/HOLC_ADS), and the background and methods are in [*Environment and Planning B*](https://doi.org/10.1177/23998083221133112).

Zoom into a city and click on one of its HOLC neighborhoods to see its attributes. Switch basemaps with the layer icon on the left.

<div class="map-frame"><iframe src="/holc_map.html" title="Interactive map of HOLC neighborhoods and their Area Description attributes" loading="lazy"></iframe></div>
<p class="map-note"><span>Data: <a href="https://osf.io/qytj8/">THOLCADS on OSF</a></span><a href="/holc_map.html" target="_blank" rel="noopener">Open full-screen map &#8599;</a></p>

## What the Area Descriptions show

Despite some noteworthy regional variation, the Black population share, &ldquo;foreign born&rdquo; share, and building age rise as grades move from A to D, while family income moves the other way. That is expected: these factors all shaped how lenders, brokers, landlords, appraisers, and others in real estate judged an area&rsquo;s potential returns. The visible presence of Black residents in particular was widely assumed to harm property values. As the top-left panel shows, almost every neighborhood with any Black residents at all received a D.

<figure>
<img src="/Projects/fourplots.png" alt="Charts of percent Black, percent foreign born, family income, and building age by HOLC grade and region" width="800">
<figcaption><strong>Percent Black, percent foreign born, family income, and building age by HOLC grade</strong>, according to the Area Descriptions.</figcaption>
</figure>

Home repair status, mortgage availability, and resident occupation class break down by grade in the same way.

<figure>
<img src="/HOLC/qual_charts.png" alt="Charts of repair status, mortgage availability, and occupation class by HOLC grade" width="800">
<figcaption><strong>Repair status, mortgage availability, and occupation class by HOLC grade.</strong></figcaption>
</figure>

We can also ask how appraisers graded neighborhoods based on which &ldquo;foreign born&rdquo; groups lived there. The next chart counts the HOLC neighborhoods where each group is at least mentioned.

<figure>
<img src="/Projects/HOLC_group.png" alt="Chart of population groups mentioned in Area Descriptions by HOLC grade" width="800">
<figcaption><strong>Population groups by HOLC grade</strong>, according to the Area Descriptions.</figcaption>
</figure>

The relationship between grades and groups closely tracks the racist ranking published by the land economist Homer Hoyt in his 1933 *One Hundred Years of Land Values in Chicago*, which claimed that land values rose or fell depending on which of these populations lived nearby. Hoyt&rsquo;s book was exceptionally well regarded in the industry, and he went on to serve as chief economist of the Federal Housing Administration (FHA), where he was instrumental in the agency&rsquo;s adoption of its own redlining maps and policies.

<figure>
<img src="/Projects/hoyt.png" alt="Homer Hoyt's 1933 ranking of racial and ethnic groups by purported effect on land values" width="640">
<figcaption><strong>Homer Hoyt&rsquo;s ranking of racial and ethnic groups by their purported effect on home values in Chicago.</strong> Source: Hoyt (1933: 316).</figcaption>
</figure>

## Read more

- Markley, S. and A. Bonds. (2025). [Race and value in space and time: a critical narrative cartography of the Home Owners&rsquo; Loan Corporation&rsquo;s Area Descriptions](https://doi.org/10.1080/02723638.2025.2492218). *Urban Geography* 46(9): 1921&ndash;1942.
- Swope, C., S. Markley, S. Whittaker, and A. Hillier. (2025). [How and why does redlining matter for present-day health? Critical perspectives on causality, cartography, and capitalism](https://doi.org/10.2105/AJPH.2024.308000). *American Journal of Public Health* 115: 769&ndash;779.
- Markley, S. and S. Holloway. (2024). [Underestimating racism? Decoupling race and redlining](https://doi.org/10.1080/24694452.2024.2350993). *Annals of the American Association of Geographers* 114(7): 1464&ndash;1482.
- Markley, S. (2024). [Planning spatial obsolescence: residential segregation and the racist theory of (anti-)value](https://doi.org/10.1177/02637758241261218). *Environment &amp; Planning D: Society and Space* 42(5&ndash;6): 758&ndash;775.
- Markley, S. (2024). [Federal &lsquo;redlining&rsquo; maps: a critical reappraisal](https://doi.org/10.1177/00420980231182336). *Urban Studies* 61(2): 195&ndash;213.
- Markley, S. (2024). [Housing, socioeconomic, and racial data in consistent neighborhood geometries for 65 cities mapped by the Home Owners&rsquo; Loan Corporation, 1940&ndash;2019](https://doi.org/10.31235/osf.io/5w6jx). *SocArXiv*.
- Markley, S. (2023). [Tabulating Home Owners&rsquo; Loan Corporation area description sheet data](https://doi.org/10.1177/23998083221133112). *Environment &amp; Planning B: Urban Analytics and City Science* 50(1): 268&ndash;280.
- Markley, S. (2023). [Atlanta, Georgia](https://dsl.richmond.edu/panorama/redlining3/map/GA/Atlanta/context#loc=12/33.758/-84.3642). In *Mapping Inequality: Redlining in New Deal America*, R. Nelson and L. Winling (eds.).
