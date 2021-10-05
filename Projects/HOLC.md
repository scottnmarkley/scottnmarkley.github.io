---
title: HOLC Mapping Project
---

## City Survey Program
My ongoing dissertation project studies the New Deal-era HOLC mapping program. This initiative&mdash;officially called the "City Survey Program"&mdash;was instituted by the US federal government during the mid-1930s to map and grade thousands of neighborhoods in over 200 cities across the country (**see images below**). The infamous A-to-D grading system used to generate the maps reflected dominant ideas within the real-estate industry about how various neighborhood features impacted the investment potential of its residential properties. Among other demographic, socioeconomic, and locational characteristics, the visible presence of Black and non-white immigrants factored heavily in the grading process.

<p style="text-align: center">
  <img src="/HOLC/ATLHOLC.jpg" width="470" title="Atlanta HOLC Map"/>
  <img src="/HOLC/ATLADS.jpg" width="245" title="Sample 'Area Description' Sheet"/>
  <figcaption>Source: <a href="https://dsl.richmond.edu/panorama/redlining/#loc=4/40.886/-105.499&text=downloads"><em>Mapping Inequality</em></a></figcaption>
</p>

The Digital Scholarship at the University of Richmond has made the HOLC maps and their field notes available for download as part of their [*Mapping Inequality*](https://dsl.richmond.edu/panorama/redlining/#loc=4/40.886/-105.499) project. They also make available a [shapefile and GeoJSON file](https://dsl.richmond.edu/panorama/redlining/#loc=4/40.886/-105.499&text=downloads) to allow for easy integration with most GIS software programs. Helping this effort, I have converted the data in the HOLC "Area Description" sheets into a convenient, readable tables (available for download [here](https://osf.io/qytj8/)). HOLC variables such as the percent Black, percent "foreign born," and average building age midpoint are fully ready to be analyzed in the "ADS_FINAL.csv" file in the TABLES folder in the DATA_DOWNLOAD directory. These variables can be seen in the interactive map below.

Zoom into a city and click on one of its HOLC neighborhoods to see its attributes. You can toggle the basemap by clicking the layer icon on the lefthand side.

<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
<a href="https://snmarkley1.github.io/holc_map.html" target="_blank"><i class="fa fa-external-link"></i></a>
[Map Zoom New Tab](https://snmarkley1.github.io/holc_map.html)
<iframe
    width="800"
    height="450"
    src="/holc_map.html" >
</iframe>

For more information on how these variables were processed, please check out the *SocArXiv* preprint [here](https://osf.io/preprints/socarxiv/dktah/)
