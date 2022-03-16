---
title: Historical Housing and Urbanization Project
---

Along with my colleagues Steve Holloway, Taylor Hafley, and Mathew Hauer, I have constructed a database called the Historical Housing Unit and Urbanization Database v2010, or **HHUUD10**. This dataset provides housing unit counts and urbanization year estimates in consistent census tract boundaries for every tract in the Continental US from 1940 to 2019. HHUUD10 can be used to analyze the historical geographies of housing loss and gain, urban renewal, (sub)urbanization, and more. The data, the R and Python code used to construct it, and a full write-up of the methods are all free and open access at [*Scientific Data*](https://www.nature.com/articles/s41597-022-01184-x)! Altnernatively, the data and code can be downloaded directly from [*Open Science Framework*](https://osf.io/fzv5e/).

The gif below uses HHUUD10 to depict suburbanization through time in the Atlanta region. Once a tract surpasses 200 housing units per dasymetrically refined square mile&mdash;*i.e.*, the tract surface area minus water, parks, golf courses, airports, cemeteries, and railyards&mdash;or is significantly covered by non-residential urban land uses, we consider it "urban."


<p style="text-align: center">
  <img src="/Projects/atl.gif" width="600" title="Urbanization in Metro Atlanta, 1940-2019"/>
  <figcaption>Urbanization in Metro Atlanta by 2010 Census Tracts, 1940-2019</figcaption>
</p>



HHUUD10 data can also be used to track historical housing unit changes at the tract level. The map below shows estimated housing unit changes from 1940 to 2019.

<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
<a href="https://usg.maps.arcgis.com/apps/instant/minimalist/index.html?appid=ec03ab824dcc4870aa57318a99757164" target="_blank">See Map on ArcGIS Online<i class="fa fa-external-link"></i></a>
<iframe src="https://usg.maps.arcgis.com/apps/instant/minimalist/index.html?appid=ec03ab824dcc4870aa57318a99757164" width="850" height="450" frameborder="0" style="border:0" allowfullscreen>iFrames are not supported on this page.</iframe>
