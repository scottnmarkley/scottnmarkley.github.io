---
layout: page
title: "Historical Housing and Urbanization"
permalink: /Projects/HHUUD10/
lede: "Housing unit counts and urbanization estimates for every census tract in the continental United States, decade by decade from 1940 to 2019, all in consistent 2010 boundaries."
---

With my colleagues Steve Holloway, Taylor Hafley, and Mathew Hauer, I built the **Historical Housing Unit and Urbanization Database v2010**, or **HHUUD10**. It can be used to analyze the historical geographies of housing loss and gain, urban renewal, sub/urbanization, and land-use and environmental change. The data, the R and Python code used to build it, and a full write-up of the methods are free and open access in [*Scientific Data*](https://www.nature.com/articles/s41597-022-01184-x).

<p class="btn-row"><a class="btn primary" href="https://osf.io/fzv5e/">Download on OSF</a><a class="btn" href="https://www.arcgis.com/home/item.html?id=98efddc0d7b84ddea6d211f7958447d8">Esri Living Atlas</a><a class="btn" href="https://www.nature.com/articles/s41597-022-01184-x">Methods paper</a></p>

## Housing unit change, 1940&ndash;2019

HHUUD10 tracks housing unit change at the tract level. The map below shows estimated change from 1940 to 2019.

<div class="map-frame"><iframe src="https://usg.maps.arcgis.com/apps/Embed/index.html?webmap=998602f24b114562a7cef6408eeabdde&amp;extent=-84.6318,33.6105,-84.1247,33.8438&amp;zoom=true&amp;previewImage=false&amp;scale=true&amp;legend=true&amp;disable_scroll=false&amp;theme=light" title="Tract-level housing unit changes, 1940-2019" loading="lazy"></iframe></div>
<p class="map-note"><span>Map: ArcGIS Online</span><a href="https://usg.maps.arcgis.com/apps/instant/minimalist/index.html?appid=d2e0f6f161c547b9b82696e6d36c7207" target="_blank" rel="noopener">Open full-screen map &#8599;</a></p>

## Sub/urbanization through time

HHUUD10 also captures sub/urbanization. Once a tract passes 200 housing units per dasymetrically refined square mile (the tract area minus water, parks, golf courses, airports, cemeteries, and railyards), or is substantially covered by non-residential urban land uses, we consider it &ldquo;urban.&rdquo; The animation shows that process unfolding across metro Atlanta.

<figure>
<img src="/Projects/atl.gif" class="narrow" alt="Animated map of urbanization in metro Atlanta by census tract, 1940 to 2019">
<figcaption><strong>Urbanization in metro Atlanta by 2010 census tract, 1940&ndash;2019.</strong></figcaption>
</figure>

## Read more

- Markley, S., S. Holloway, T. Hafley, and M. Hauer. (2022). [Housing unit and urbanization estimates for the Continental U.S. in consistent tract boundaries, 1940&ndash;2019](https://www.nature.com/articles/s41597-022-01184-x). *Scientific Data* 9: 82.
- Beauvais, J., S. Markley, and J.E. Byers. (2024). [Exponential growth of private coastal infrastructure influenced by geography and race in South Carolina, USA](https://www.nature.com/articles/s41598-024-59740-x). *Scientific Reports* 14: 9114.
