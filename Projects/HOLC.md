---
title: HOLC Mapping Project
---

## City Survey Program
My current research project studies the New Deal-era HOLC mapping program. This initiative&mdash;officially called the "City Survey" program&mdash;was instituted by the US federal government in partnership with the real estate industry during the late 1930s to map and grade thousands of neighborhoods in over 200 cities across the country (**see images below**). The infamous A-to-D grading system used to generate the maps reflected dominant ideas within the real estate industry about how various neighborhood features impacted the investment potential of its residential properties. Among other demographic, socioeconomic, and locational characteristics, the visible presence of Black and non-white immigrants factored heavily in the grading process.

<p style="text-align: center">
  <img src="/HOLC/ATLHOLC.jpg" width="470" title="Atlanta HOLC Map"/>
  <img src="/HOLC/ATLADS.jpg" width="245" title="Sample 'Area Description' Sheet"/>
  <figcaption>Source: <a href="https://dsl.richmond.edu/panorama/redlining/#loc=4/40.886/-105.499&text=downloads"><em>Mapping Inequality</em></a></figcaption>
</p>

The Digital Scholarship Lab at the University of Richmond has made the HOLC maps and their field notes available for download as part of their [*Mapping Inequality*](https://dsl.richmond.edu/panorama/redlining/#loc=4/40.886/-105.499) project. They also make available a [shapefile and GeoJSON file](https://dsl.richmond.edu/panorama/redlining/#loc=4/40.886/-105.499&text=downloads) to allow for easy integration with most GIS software programs. Assisting this effort, I have converted the data in the HOLC "Area Description" sheets into convenient, readable tables (available for download at [Open Science Framework](https://osf.io/qytj8/)). HOLC variables such as the Black population percentage, "foreign born" population percentage and group, family income, occupation class, average building age, home repair status, and mortgage availability are fully ready to be downloaded and incorporated into statistical analyses [here](https://osf.io/28vup/). These variables can be seen in the interactive map below. All R code used to generate these files are available through [GitHub](https://github.com/snmarkley1/HOLC_ADS/tree/main), and a description of the background and methods is available at [*Environment and Planning B*](https://osf.io/preprints/socarxiv/dktah/).

Zoom into a city and click on one of its HOLC neighborhoods to see its attributes. You can toggle the basemap by clicking the layer icon on the lefthand side. All variables used to populate these attribute tables are available [here](https://osf.io/qytj8/).

<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
<a href="https://snmarkley1.github.io/holc_map.html" target="_blank">Map Zoom <i class="fa fa-external-link"></i></a>
<iframe
    width="800"
    height="450"
    src="/holc_map.html" >
</iframe>

Using the data provided in the map, I graphed the HOLC grading breakdown by variable and region. (a) shows the average building age midpoint; (b) shows the Black population percentage; and (c) shows the "foreign born" population percentage. Despite some noteworthy regional variation, all variables tend to increase as the neighborhood grade goes from A to D. This is expected, as these factors all played an important role in how lenders, real estate brokers, landlords, appraisers, and others dealing in real estate perceived an area's potential returns on property investment. Specifically, the visible presence of Black residents in a neighborhood was widely assumed to be detrimental to property values. Thus, as (b) suggests, the presence of nearly any number of Black residents was enough for a place to receive a D grade.

<p style="text-align: center">
  <img src="/Projects/fourplots.png" width="800" title="HOLC Variables by Region"/>
  <figcaption>(All bar graphs on this page are from <a href="https://osf.io/preprints/socarxiv/dktah/"><em>SocArXiv</em></a>)</figcaption>
</p>

We might also wonder about how HOLC appraisers issued neighborhood grades based on the presence of different "foreign born" groups. That is shown in the graph here. Notably, the relationship between grades and "foreign born" groups closely tracks the racist ranking system published by the influential land-use economist Homer Hoyt in his 1933 *One Hundred Years of Land Values in Chicago*. Here, Hoyt asserted that land values in an area went up or down depending on which of these populations lived nearby. Hoyt's book was exceptionally well-regarded within the industry, and he would later serve as the head economist of the Federal Housing Administration (FHA). There, he was instrumental in the agency's adoption of its own redlining maps and policies that were used to deny mortgages to non-white applicants.

<p style="text-align: center">
  <img src="/Projects/HOLC_group.png" width="800" title="HOLC Grade by Group"/>
</p>

<p style="text-align: center">
    <img src="/Projects/hoyt.png" width="600" title="Hoyt's ranking"/>
    <figcaption>Source: <a href="https://chipublib.bibliocommons.com/v2/record/S126C844620">Hoyt (1933: 316)</a></figcaption>
</p>

It is worth noting that these breakdowns include any "Area Description" sheets where the population group in question was mentioned. It does not take the size of that group into account. We can use the data in the [tables](https://osf.io/28vup/) to get a better picture of this. 

<p style="text-align: center">
  <img src="/Projects/HOLC_pblk.png" width="700" title="HOLC Grade by % Black"/>
</p>

Again we see that higher Black population shares in a neighborhood translated into lower HOLC grades. This is not surprising. The leading real estate appraisal theorists of the day&mdash;including Homer Hoyt&mdash;taught that Black presence was detrimental to an area's property values. This conviction was largely predicated on the belief that once a neighborhood transitioned from white to Black, it would never transition back because white people would be viscerally opposed to occupying a former Black living space. Although there is some debate about how widely the HOLC maps circulated, it is important to keep in mind that regardless of how and if they were used, the maps and their description sheets reflect the governing ideology of an industry that would fundamentally transform the US sub/urban landscape. They are, in that regard, an indispensable window into the twentieth-century real-estate mind.
