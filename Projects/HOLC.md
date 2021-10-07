---
title: HOLC Mapping Project
---

## City Survey Program
My ongoing dissertation project studies the New Deal-era HOLC mapping program. This initiative&mdash;officially called the "City Survey Program"&mdash;was instituted by the US federal government in partnership with the real-estate industry during the mid-1930s to map and grade thousands of neighborhoods in over 200 cities across the country (**see images below**). The infamous A-to-D grading system used to generate the maps reflected dominant ideas within the real-estate industry about how various neighborhood features impacted the investment potential of its residential properties. Among other demographic, socioeconomic, and locational characteristics, the visible presence of Black and non-white immigrants factored heavily in the grading process.

<p style="text-align: center">
  <img src="/HOLC/ATLHOLC.jpg" width="470" title="Atlanta HOLC Map"/>
  <img src="/HOLC/ATLADS.jpg" width="245" title="Sample 'Area Description' Sheet"/>
  <figcaption>Source:<em> Mapping Inequality</em></figcaption>
</p>

The Digital Scholarship at the University of Richmond has made the HOLC maps and their field notes available for download as part of their [*Mapping Inequality*](https://dsl.richmond.edu/panorama/redlining/#loc=4/40.886/-105.499) project. They also make available a [shapefile and GeoJSON file](https://dsl.richmond.edu/panorama/redlining/#loc=4/40.886/-105.499&text=downloads) to allow for easy integration with most GIS software programs. Assisting this effort, I have converted the data in the HOLC "Area Description" sheets into convenient, readable tables (available for download at [Open Science Framework](https://osf.io/qytj8/)). HOLC variables such as the percent Black, percent "foreign born," and average building age midpoint are fully ready to be downloaded and incorporated into statistical analyses [here](https://osf.io/28vup/). These variables can be seen in the interactive map below. All R code used to generate these files are available through [GitHub](https://github.com/snmarkley1/HOLC_ADS/tree/main), and a description of the background and methods is available at [*SocArXiv*](https://osf.io/preprints/socarxiv/dktah/).

Zoom into a city and click on one of its HOLC neighborhoods to see its attributes. You can toggle the basemap by clicking the layer icon on the lefthand side. All variables used to populate these attribute tables are available [here](https://osf.io/28vup/).

<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
<a href="https://snmarkley1.github.io/holc_map.html" target="_blank">Map Zoom <i class="fa fa-external-link"></i></a>
<iframe
    width="800"
    height="450"
    src="/holc_map.html" >
</iframe>

Using the data provided in the map, I graphed the HOLC grading breakdown by variable and region. (a) shows the average building age midpoint; (b) shows the Black population percentage; and (c) shows the "foreign born" population percentage. Despite some noteworthy regional variation, all variables tend to increase as the neighborhood grade goes from A to D. This is expected, as these factors all played an important role in how lenders, real estate brokers, landlords, appraisers, and others dealing in real estate perceived an area's potential returns on property investment. Specifically, the visible presence of Black residents in a neighborhood was widely assumed to be detrimental to property values. Thus, as (b) suggests, the presence of nearly any number of Black residents was enough for a place to receive a D grade.

![](/Projects/holc_regions.png)

We might also wonder about how HOLC neighborhood appraisers issued their grades based on the presence of different "foreign born" groups. That is shown in the graph here.

![](/Projects/pct_group.tif)
