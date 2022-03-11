---
title: Historical Housing and Urbanization Project
---

Along with my colleagues Steve Holloway, Taylor Hafley, and Mathew Hauer, I have constructed a database that contains historical housing unit and urbanization estimates in consistent 2010 census tract boundaries. These data are provided for every tract in the Continental US from 1940 to 2019. This dataset can be used to analyze the historical geographies of housing loss and gain, urban renewal, (sub)urbanization, and more. This database, the R and Python code used to construct it, and a full write-up of the methods are all free and open access at [*Scientific Data*](https://www.nature.com/articles/s41597-022-01184-x)! Altnernatively, the data and code can be downloaded directly from [*Open Science Framework*](https://osf.io/fzv5e/).

The gif below uses our dataset to depict suburbanization through time in the Atlanta region. Once a tract surpasses 200 housing units per dasymetrically refined square mile&mdash;*i.e.*, the tract surface area minus water, parks, golf courses, airports, cemeteries, and railyards&mdash;or is significantly covered by non-residential urban land uses, we consider it "urban."


<p style="text-align: center">
  <img src="/Projects/atl.gif" width="600" title="Urbanization in Metro Atlanta, 1940-2019"/>
  <figcaption>Urbanization in Metro Atlanta by 2010 Census Tracts, 1940-2019</figcaption>
</p>
