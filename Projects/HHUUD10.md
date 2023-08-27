---
title: Historical Housing and Urbanization Project
---

Along with my colleagues Steve Holloway, Taylor Hafley, and Mathew Hauer, I have constructed a database called the Historical Housing Unit and Urbanization Database v2010, or **HHUUD10**. This dataset provides housing unit counts and urbanization year estimates in consistent census tract boundaries for every tract in the Continental US from 1940 to 2019. HHUUD10 can be used to analyze the historical geographies of housing loss and gain, urban renewal, (sub)urbanization, and more. The data, the R and Python code used to construct it, and a full write-up of the methods are all free and open access at [*Scientific Data*](https://www.nature.com/articles/s41597-022-01184-x)! Altnernatively, the data and code can be downloaded directly from [Open Science Framework](https://osf.io/fzv5e/) or from [Esri's Living Atlas](https://www.arcgis.com/home/item.html?id=98efddc0d7b84ddea6d211f7958447d8).


HHUUD10 data can be used to track historical housing unit changes at the tract level. The map below shows estimated housing unit changes from 1940 to 2019.

<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
<a href="https://usg.maps.arcgis.com/apps/instant/minimalist/index.html?appid=d2e0f6f161c547b9b82696e6d36c7207" target="_blank">See Map on ArcGIS Online <i class="fa fa-external-link"></i></a>

<style>.embed-container {position: relative; padding-bottom: 53%; height: 0; max-width: 100%;} .embed-container iframe, .embed-container object, .embed-container iframe{position: absolute; top: 0; left: 0; width: 100%; height: 100%;} small{position: absolute; z-index: 40; bottom: 0; margin-bottom: -15px;}</style><div class="embed-container"><iframe width="850" height="450" frameborder="0" scrolling="no" marginheight="0" marginwidth="0" title="Tract-level Housing Unit Changes, 1940-2019" src="//usg.maps.arcgis.com/apps/Embed/index.html?webmap=998602f24b114562a7cef6408eeabdde&extent=-84.6318,33.6105,-84.1247,33.8438&zoom=true&previewImage=false&scale=true&legend=true&disable_scroll=false&theme=light"></iframe></div>

HHUUD10 data can also be used to capture sub/urbanization through time. The graphic below shows this process in the Atlanta region. Once a tract surpasses 200 housing units per dasymetrically refined square mile&mdash;*i.e.*, the tract surface area minus water, parks, golf courses, airports, cemeteries, and railyards&mdash;or is significantly covered by non-residential urban land uses, we consider it "urban."


<p style="text-align: center">
  <img src="/Projects/atl.gif" width="600" title="Urbanization in Metro Atlanta, 1940-2019"/>
  <figcaption>Urbanization in Metro Atlanta by 2010 Census Tracts, 1940-2019</figcaption>
</p>



