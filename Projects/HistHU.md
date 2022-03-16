---
title: Historical Housing and Urbanization Project
---

Along with my colleagues Steve Holloway, Taylor Hafley, and Mathew Hauer, I have constructed a database called the Historical Housing Unit and Urbanization Database v2010, or **HHUUD10**. This dataset provides housing unit counts and urbanization year estimates in consistent census tract boundaries for every tract in the Continental US from 1940 to 2019. HHUUD10 can be used to analyze the historical geographies of housing loss and gain, urban renewal, (sub)urbanization, and more. The data, the R and Python code used to construct it, and a full write-up of the methods are all free and open access at [*Scientific Data*](https://www.nature.com/articles/s41597-022-01184-x)! Altnernatively, the data and code can be downloaded directly from [*Open Science Framework*](https://osf.io/fzv5e/).

The gif below uses HHUUD10 to depict suburbanization through time in the Atlanta region. Once a tract surpasses 200 housing units per dasymetrically refined square mile&mdash;*i.e.*, the tract surface area minus water, parks, golf courses, airports, cemeteries, and railyards&mdash;or is significantly covered by non-residential urban land uses, we consider it "urban."


<p style="text-align: center">
  <img src="/Projects/atl.gif" width="600" title="Urbanization in Metro Atlanta, 1940-2019"/>
  <figcaption>Urbanization in Metro Atlanta by 2010 Census Tracts, 1940-2019</figcaption>
</p>


<style>.embed-container {position: relative; padding-bottom: 60%; height: 0; max-width: 100%;} .embed-container iframe, .embed-container object, .embed-container iframe{position: absolute; top: 0; left: 0; width: 100%; height: 100%;} small{position: absolute; z-index: 40; bottom: 0; margin-bottom: -15px;}</style><div class="embed-container"><iframe width="700" height="420" frameborder="0" scrolling="no" marginheight="0" marginwidth="0" title="Housing Unit Change by Tract, 1940-2019" src="//usg.maps.arcgis.com/apps/Embed/index.html?webmap=02695f619dfe4cafa0defcf579896477&extent=-145.9362,14.2725,-42.3132,55.6823&zoom=true&previewImage=false&scale=true&disable_scroll=true&theme=light"></iframe></div>
