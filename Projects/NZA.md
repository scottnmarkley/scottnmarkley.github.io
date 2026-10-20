---
layout: page
title: "Zoning and Land Use"
permalink: /Projects/NZA/
lede: "Zoning decides what can be built where. For most of American history, that information has been scattered across thousands of separate, hard-to-read local codes. I work to make these data public, comparable, and usable."
head: |
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.4/leaflet.min.css">
  <script defer src="https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.4/leaflet.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/topojson-client@3.1.0/dist/topojson-client.min.js"></script>
  <script defer src="/assets/zoning-map.js"></script>
  <script defer src="https://cdnjs.cloudflare.com/ajax/libs/d3/7.9.0/d3.min.js"></script>
  <script defer src="/assets/kc-maps.js"></script>
---

I am the Research Director of the [National Zoning Atlas](https://www.zoningatlas.org/) (NZA), a nonprofit building the most detailed and reliable repository of standardized zoning data in the United States. The Atlas now covers more than 11,000 jurisdictions, home to roughly 224 million people, and records over 120 variables for each zoning district, from the housing types allowed by right to minimum lot sizes, accessory dwelling unit (ADU) rules, and parking requirements. I am also Chief Data Scientist at [Land Use Labs](https://www.landuselabs.com/), where I put the same data and methods to work for the cities and states writing the rules.

<p class="btn-row"><a class="btn" href="https://www.zoningatlas.org/atlas">Explore the Atlas</a><a class="btn" href="https://www.zoningatlas.org/snapshots">Zoning snapshots</a><a class="btn" href="http://dx.doi.org/10.2139/ssrn.4476927">Methodology</a></p>

## How the Atlas is built

Every zoning code is both a text and a map, and some 33,000 jurisdictions each write their own, with no common standard. Maps and texts are amended on different schedules, source GIS layers are full of gaps and overlaps, and many maps still arrive as scanned PDFs. Overlay districts add another layer of difficulty. Boston has 287 mapped base districts and 20 mapped overlay districts, with as many as six overlays stacked on a single parcel.

<figure>
<img src="/assets/img/boston_overlays.jpg" class="narrow" alt="Map of Boston shaded by the number of mapped zoning overlays on each piece of land, from zero to six">
<figcaption><strong>Boston: number of mapped overlays on each piece of land.</strong></figcaption>
</figure>

To make places comparable, we run every jurisdiction through the same geospatial pipeline. Analysts digitize base districts and align them to jurisdiction boundaries and parcels; remove water, protected land, and rights-of-way using national layers; add overlay districts; and then flatten base and overlay districts together so that every piece of land carries one resolved set of rules.

<figure>
<img src="/assets/img/pipeline_steps.gif" alt="Animated diagram of six steps: digitize base districts, align boundaries, punch out water, protected land and rights-of-way, add overlay districts, flatten, and resolve into slices with one set of rules each" width="760" loading="lazy">
<figcaption><strong>From zoning map to analysis-ready data, step by step.</strong></figcaption>
</figure>

## Statewide and regional zoning reports

Since 2025 I have led the analysis for the NZA&rsquo;s geographic report series. Each report summarizes how much land a state or region zones for housing, what kinds of homes those rules allow, and how the rules vary from one jurisdiction to the next.

<div class="map-frame"><div id="zoning-map" role="region" aria-label="Map of states and metros covered by my zoning reports and projects"></div></div>
<div class="legend">
<span><i style="background:var(--accent);opacity:.55"></i>Statewide zoning report</span>
<span><i style="border:1.5px dashed var(--accent)"></i>Forthcoming</span>
<span><i style="background:var(--blue);border-radius:50%"></i>Metro and city projects</span>
</div>

- [Zoning Report: Massachusetts](https://www.zoningatlas.org/zoning-report-massachusetts-2026) (2026), with J. Infranca, D. Drogaris, J. Pellechia, and S. Bronin
- [Zoning Report: Metro Kansas City](https://www.zoningatlas.org/zoning-report-metro-kansas-city-2026) (2026), with D. Drogaris and S. Bronin
- [Zoning Report: Virginia](https://www.zoningatlas.org/zoning-report-virginia-2025) (2025), with M. Harris, R. Karlapalem, D. Drogaris, and S. Bronin
- [Zoning Report: Colorado](https://www.zoningatlas.org/zoning-report-colorado-2025) (2025), with S. Bronin, M. Harris, and D. Drogaris
- Zoning Report: Connecticut, with M. Harris, D. Drogaris, and S. Bronin (forthcoming)

In Massachusetts, even the older industrial Gateway Cities are zoned mostly for single-family homes. On average, 88 percent of a Gateway City&rsquo;s residential land allows single-family homes by right, compared with 10 percent for housing with four or more units. In Attleboro, Everett, Fitchburg, Springfield, Taunton, and Westfield, less than 1 percent of residential land allows apartments by right; only New Bedford, Quincy, and Worcester exceed 25 percent.

<figure class="wide">
<div class="gw" role="img" aria-label="Paired bar charts for the Statewide total and 26 Massachusetts Gateway Cities. For each, the share of residential land where 1-family housing (left) and 4-plus-family housing (right) is allowed by right, subject to a public hearing, or prohibited. 1-family housing is allowed on most land almost everywhere; 4-plus-family housing is allowed on little land in most cities.">
<div class="gw-row gw-head"><span>1-family</span><span></span><span>4+-family</span></div>
<div class="gw-row gw-state"><span class="gw-bar l" title="1-family: allowed 96%, public hearing 2%, prohibited 2%"><span class="allowed" style="width:95.6%"></span><span class="hearing" style="width:2.3%"></span><span class="prohibited" style="width:2.0%"></span></span><span class="gw-name">Statewide</span><span class="gw-bar r" title="4+-family: allowed 4%, public hearing 39%, prohibited 57%"><span class="allowed" style="width:3.5%"></span><span class="hearing" style="width:39.2%"></span><span class="prohibited" style="width:57.3%"></span></span></div>
<div class="gw-row"><span class="gw-bar l" title="1-family: allowed 98%, public hearing 0%, prohibited 2%"><span class="allowed" style="width:97.7%"></span><span class="hearing" style="width:0.0%"></span><span class="prohibited" style="width:2.3%"></span></span><span class="gw-name">Attleboro</span><span class="gw-bar r" title="4+-family: allowed 1%, public hearing 13%, prohibited 86%"><span class="allowed" style="width:0.7%"></span><span class="hearing" style="width:13.2%"></span><span class="prohibited" style="width:86.1%"></span></span></div>
<div class="gw-row"><span class="gw-bar l" title="1-family: allowed 97%, public hearing 0%, prohibited 3%"><span class="allowed" style="width:97.1%"></span><span class="hearing" style="width:0.1%"></span><span class="prohibited" style="width:2.8%"></span></span><span class="gw-name">Barnstable</span><span class="gw-bar r" title="4+-family: allowed 4%, public hearing 0%, prohibited 95%"><span class="allowed" style="width:4.5%"></span><span class="hearing" style="width:0.1%"></span><span class="prohibited" style="width:95.4%"></span></span></div>
<div class="gw-row"><span class="gw-bar l" title="1-family: allowed 87%, public hearing 0%, prohibited 13%"><span class="allowed" style="width:87.0%"></span><span class="hearing" style="width:0.0%"></span><span class="prohibited" style="width:13.0%"></span></span><span class="gw-name">Brockton</span><span class="gw-bar r" title="4+-family: allowed 9%, public hearing 11%, prohibited 80%"><span class="allowed" style="width:8.7%"></span><span class="hearing" style="width:11.2%"></span><span class="prohibited" style="width:80.1%"></span></span></div>
<div class="gw-row"><span class="gw-bar l" title="1-family: allowed 77%, public hearing 3%, prohibited 20%"><span class="allowed" style="width:76.7%"></span><span class="hearing" style="width:2.9%"></span><span class="prohibited" style="width:20.3%"></span></span><span class="gw-name">Chelsea</span><span class="gw-bar r" title="4+-family: allowed 22%, public hearing 40%, prohibited 38%"><span class="allowed" style="width:22.4%"></span><span class="hearing" style="width:39.5%"></span><span class="prohibited" style="width:38.1%"></span></span></div>
<div class="gw-row"><span class="gw-bar l" title="1-family: allowed 87%, public hearing 3%, prohibited 10%"><span class="allowed" style="width:87.4%"></span><span class="hearing" style="width:2.9%"></span><span class="prohibited" style="width:9.7%"></span></span><span class="gw-name">Chicopee</span><span class="gw-bar r" title="4+-family: allowed 5%, public hearing 11%, prohibited 84%"><span class="allowed" style="width:5.4%"></span><span class="hearing" style="width:10.8%"></span><span class="prohibited" style="width:83.9%"></span></span></div>
<div class="gw-row"><span class="gw-bar l" title="1-family: allowed 78%, public hearing 5%, prohibited 17%"><span class="allowed" style="width:78.2%"></span><span class="hearing" style="width:4.8%"></span><span class="prohibited" style="width:17.1%"></span></span><span class="gw-name">Everett</span><span class="gw-bar r" title="4+-family: allowed 0%, public hearing 50%, prohibited 50%"><span class="allowed" style="width:0.0%"></span><span class="hearing" style="width:50.3%"></span><span class="prohibited" style="width:49.7%"></span></span></div>
<div class="gw-row"><span class="gw-bar l" title="1-family: allowed 87%, public hearing 0%, prohibited 13%"><span class="allowed" style="width:87.3%"></span><span class="hearing" style="width:0.0%"></span><span class="prohibited" style="width:12.7%"></span></span><span class="gw-name">Fall River</span><span class="gw-bar r" title="4+-family: allowed 16%, public hearing 8%, prohibited 76%"><span class="allowed" style="width:16.2%"></span><span class="hearing" style="width:7.5%"></span><span class="prohibited" style="width:76.3%"></span></span></div>
<div class="gw-row"><span class="gw-bar l" title="1-family: allowed 87%, public hearing 13%, prohibited 1%"><span class="allowed" style="width:87.0%"></span><span class="hearing" style="width:12.5%"></span><span class="prohibited" style="width:0.5%"></span></span><span class="gw-name">Fitchburg</span><span class="gw-bar r" title="4+-family: allowed 1%, public hearing 20%, prohibited 79%"><span class="allowed" style="width:0.7%"></span><span class="hearing" style="width:20.2%"></span><span class="prohibited" style="width:79.1%"></span></span></div>
<div class="gw-row"><span class="gw-bar l" title="1-family: allowed 89%, public hearing 9%, prohibited 2%"><span class="allowed" style="width:89.3%"></span><span class="hearing" style="width:8.8%"></span><span class="prohibited" style="width:1.9%"></span></span><span class="gw-name">Haverhill</span><span class="gw-bar r" title="4+-family: allowed 14%, public hearing 78%, prohibited 8%"><span class="allowed" style="width:13.8%"></span><span class="hearing" style="width:78.1%"></span><span class="prohibited" style="width:8.1%"></span></span></div>
<div class="gw-row"><span class="gw-bar l" title="1-family: allowed 92%, public hearing 0%, prohibited 8%"><span class="allowed" style="width:92.0%"></span><span class="hearing" style="width:0.2%"></span><span class="prohibited" style="width:7.7%"></span></span><span class="gw-name">Holyoke</span><span class="gw-bar r" title="4+-family: allowed 17%, public hearing 6%, prohibited 77%"><span class="allowed" style="width:17.4%"></span><span class="hearing" style="width:5.8%"></span><span class="prohibited" style="width:76.8%"></span></span></div>
<div class="gw-row"><span class="gw-bar l" title="1-family: allowed 72%, public hearing 28%, prohibited 0%"><span class="allowed" style="width:72.1%"></span><span class="hearing" style="width:27.9%"></span><span class="prohibited" style="width:0.0%"></span></span><span class="gw-name">Lawrence</span><span class="gw-bar r" title="4+-family: allowed 1%, public hearing 51%, prohibited 48%"><span class="allowed" style="width:1.1%"></span><span class="hearing" style="width:50.7%"></span><span class="prohibited" style="width:48.2%"></span></span></div>
<div class="gw-row"><span class="gw-bar l" title="1-family: allowed 82%, public hearing 16%, prohibited 2%"><span class="allowed" style="width:82.0%"></span><span class="hearing" style="width:15.6%"></span><span class="prohibited" style="width:2.4%"></span></span><span class="gw-name">Leominster</span><span class="gw-bar r" title="4+-family: allowed 4%, public hearing 22%, prohibited 74%"><span class="allowed" style="width:3.9%"></span><span class="hearing" style="width:22.1%"></span><span class="prohibited" style="width:74.0%"></span></span></div>
<div class="gw-row"><span class="gw-bar l" title="1-family: allowed 74%, public hearing 9%, prohibited 17%"><span class="allowed" style="width:73.8%"></span><span class="hearing" style="width:9.2%"></span><span class="prohibited" style="width:17.0%"></span></span><span class="gw-name">Lowell</span><span class="gw-bar r" title="4+-family: allowed 8%, public hearing 17%, prohibited 74%"><span class="allowed" style="width:8.3%"></span><span class="hearing" style="width:17.2%"></span><span class="prohibited" style="width:74.5%"></span></span></div>
<div class="gw-row"><span class="gw-bar l" title="1-family: allowed 83%, public hearing 0%, prohibited 17%"><span class="allowed" style="width:83.3%"></span><span class="hearing" style="width:0.0%"></span><span class="prohibited" style="width:16.7%"></span></span><span class="gw-name">Lynn</span><span class="gw-bar r" title="4+-family: allowed 14%, public hearing 20%, prohibited 66%"><span class="allowed" style="width:14.3%"></span><span class="hearing" style="width:19.8%"></span><span class="prohibited" style="width:66.0%"></span></span></div>
<div class="gw-row"><span class="gw-bar l" title="1-family: allowed 92%, public hearing 0%, prohibited 8%"><span class="allowed" style="width:91.5%"></span><span class="hearing" style="width:0.0%"></span><span class="prohibited" style="width:8.5%"></span></span><span class="gw-name">Malden</span><span class="gw-bar r" title="4+-family: allowed 5%, public hearing 15%, prohibited 80%"><span class="allowed" style="width:5.1%"></span><span class="hearing" style="width:14.8%"></span><span class="prohibited" style="width:80.2%"></span></span></div>
<div class="gw-row"><span class="gw-bar l" title="1-family: allowed 83%, public hearing 16%, prohibited 1%"><span class="allowed" style="width:82.7%"></span><span class="hearing" style="width:16.3%"></span><span class="prohibited" style="width:1.0%"></span></span><span class="gw-name">Methuen</span><span class="gw-bar r" title="4+-family: allowed 1%, public hearing 99%, prohibited 0%"><span class="allowed" style="width:1.0%"></span><span class="hearing" style="width:99.0%"></span><span class="prohibited" style="width:0.0%"></span></span></div>
<div class="gw-row"><span class="gw-bar l" title="1-family: allowed 97%, public hearing 2%, prohibited 1%"><span class="allowed" style="width:96.9%"></span><span class="hearing" style="width:1.8%"></span><span class="prohibited" style="width:1.3%"></span></span><span class="gw-name">New Bedford</span><span class="gw-bar r" title="4+-family: allowed 27%, public hearing 3%, prohibited 71%"><span class="allowed" style="width:26.6%"></span><span class="hearing" style="width:2.5%"></span><span class="prohibited" style="width:70.9%"></span></span></div>
<div class="gw-row"><span class="gw-bar l" title="1-family: allowed 91%, public hearing 0%, prohibited 9%"><span class="allowed" style="width:91.0%"></span><span class="hearing" style="width:0.0%"></span><span class="prohibited" style="width:9.0%"></span></span><span class="gw-name">Peabody</span><span class="gw-bar r" title="4+-family: allowed 12%, public hearing 4%, prohibited 84%"><span class="allowed" style="width:12.0%"></span><span class="hearing" style="width:3.5%"></span><span class="prohibited" style="width:84.5%"></span></span></div>
<div class="gw-row"><span class="gw-bar l" title="1-family: allowed 97%, public hearing 1%, prohibited 1%"><span class="allowed" style="width:97.3%"></span><span class="hearing" style="width:1.3%"></span><span class="prohibited" style="width:1.4%"></span></span><span class="gw-name">Pittsfield</span><span class="gw-bar r" title="4+-family: allowed 6%, public hearing 1%, prohibited 92%"><span class="allowed" style="width:6.3%"></span><span class="hearing" style="width:1.5%"></span><span class="prohibited" style="width:92.3%"></span></span></div>
<div class="gw-row"><span class="gw-bar l" title="1-family: allowed 81%, public hearing 14%, prohibited 5%"><span class="allowed" style="width:80.9%"></span><span class="hearing" style="width:14.3%"></span><span class="prohibited" style="width:4.9%"></span></span><span class="gw-name">Quincy</span><span class="gw-bar r" title="4+-family: allowed 33%, public hearing 24%, prohibited 43%"><span class="allowed" style="width:32.6%"></span><span class="hearing" style="width:24.5%"></span><span class="prohibited" style="width:42.9%"></span></span></div>
<div class="gw-row"><span class="gw-bar l" title="1-family: allowed 74%, public hearing 2%, prohibited 24%"><span class="allowed" style="width:74.2%"></span><span class="hearing" style="width:2.0%"></span><span class="prohibited" style="width:23.8%"></span></span><span class="gw-name">Revere</span><span class="gw-bar r" title="4+-family: allowed 10%, public hearing 26%, prohibited 64%"><span class="allowed" style="width:10.1%"></span><span class="hearing" style="width:26.0%"></span><span class="prohibited" style="width:63.9%"></span></span></div>
<div class="gw-row"><span class="gw-bar l" title="1-family: allowed 94%, public hearing 5%, prohibited 0%"><span class="allowed" style="width:94.3%"></span><span class="hearing" style="width:5.3%"></span><span class="prohibited" style="width:0.4%"></span></span><span class="gw-name">Salem</span><span class="gw-bar r" title="4+-family: allowed 14%, public hearing 8%, prohibited 78%"><span class="allowed" style="width:14.3%"></span><span class="hearing" style="width:8.1%"></span><span class="prohibited" style="width:77.6%"></span></span></div>
<div class="gw-row"><span class="gw-bar l" title="1-family: allowed 100%, public hearing 0%, prohibited 0%"><span class="allowed" style="width:99.6%"></span><span class="hearing" style="width:0.4%"></span><span class="prohibited" style="width:0.0%"></span></span><span class="gw-name">Springfield</span><span class="gw-bar r" title="4+-family: allowed 0%, public hearing 18%, prohibited 82%"><span class="allowed" style="width:0.0%"></span><span class="hearing" style="width:18.3%"></span><span class="prohibited" style="width:81.7%"></span></span></div>
<div class="gw-row"><span class="gw-bar l" title="1-family: allowed 83%, public hearing 17%, prohibited 0%"><span class="allowed" style="width:83.3%"></span><span class="hearing" style="width:16.5%"></span><span class="prohibited" style="width:0.2%"></span></span><span class="gw-name">Taunton</span><span class="gw-bar r" title="4+-family: allowed 0%, public hearing 88%, prohibited 12%"><span class="allowed" style="width:0.2%"></span><span class="hearing" style="width:88.2%"></span><span class="prohibited" style="width:11.7%"></span></span></div>
<div class="gw-row"><span class="gw-bar l" title="1-family: allowed 100%, public hearing 0%, prohibited 0%"><span class="allowed" style="width:99.7%"></span><span class="hearing" style="width:0.0%"></span><span class="prohibited" style="width:0.3%"></span></span><span class="gw-name">Westfield</span><span class="gw-bar r" title="4+-family: allowed 0%, public hearing 17%, prohibited 83%"><span class="allowed" style="width:0.4%"></span><span class="hearing" style="width:16.9%"></span><span class="prohibited" style="width:82.7%"></span></span></div>
<div class="gw-row"><span class="gw-bar l" title="1-family: allowed 96%, public hearing 0%, prohibited 4%"><span class="allowed" style="width:96.3%"></span><span class="hearing" style="width:0.0%"></span><span class="prohibited" style="width:3.7%"></span></span><span class="gw-name">Worcester</span><span class="gw-bar r" title="4+-family: allowed 26%, public hearing 24%, prohibited 51%"><span class="allowed" style="width:25.6%"></span><span class="hearing" style="width:23.6%"></span><span class="prohibited" style="width:50.8%"></span></span></div>
<div class="gw-row gw-axis"><span class="gw-ticks"><i style="left:0%">100</i><i style="left:25%">75</i><i style="left:50%">50</i><i style="left:75%">25</i><i style="left:100%">0</i></span><span></span><span class="gw-ticks"><i style="left:0%">0</i><i style="left:25%">25</i><i style="left:50%">50</i><i style="left:75%">75</i><i style="left:100%">100</i></span></div>
<p class="gw-axis-label">% of residential land</p>
<div class="gw-legend"><span><i class="allowed"></i>Allowed by right</span><span><i class="hearing"></i>Subject to a public hearing</span><span><i class="prohibited"></i>Prohibited</span></div>
</div>
<figcaption><strong>Massachusetts Gateway Cities: how one-family and four-plus-family housing are permitted on residential land.</strong> From <em>Zoning Report: Massachusetts</em> (2026).</figcaption>
</figure>

In metro Kansas City, the most exclusionary rules follow income and race. In the highest-income tracts, 89 percent of residentially zoned land allows only single-family homes by right, compared with 31 percent in the lowest-income tracts. Minimum lot sizes of 80,000 square feet, roughly two acres, cover 69 percent of single-family land in White-majority neighborhoods and none in Black-majority neighborhoods. Statistics like these are available for any jurisdiction in the Atlas through Land Use Labs&rsquo; <a href="https://www.landuselabs.com/tables">Zoning Tables</a>.

<figure class="wide">
<div class="chart-map">
<div class="hbar blue" role="img" aria-label="Share of residentially zoned land where only single-family homes are allowed by right, by tract income quartile: highest income 89 percent, upper-middle 83, lower-middle 78, lowest income 31">
<div class="hbar-row"><span class="hbar-label">Q4 (highest income)</span><span class="hbar-track"><span class="seg a" style="width:89%"></span><span class="val in" style="left:0;width:89%">89%</span></span></div>
<div class="hbar-row"><span class="hbar-label">Q3 (upper-middle)</span><span class="hbar-track"><span class="seg a" style="width:83%"></span><span class="val in" style="left:0;width:83%">83%</span></span></div>
<div class="hbar-row"><span class="hbar-label">Q2 (lower-middle)</span><span class="hbar-track"><span class="seg a" style="width:78%"></span><span class="val in" style="left:0;width:78%">78%</span></span></div>
<div class="hbar-row"><span class="hbar-label">Q1 (lowest income)</span><span class="hbar-track"><span class="seg a" style="width:31%"></span><span class="val in" style="left:0;width:31%">31%</span></span></div>
<div class="hbar-row hbar-axis"><span></span><span class="hbar-track"><i style="left:0">0</i><i style="left:25%">25</i><i style="left:50%">50</i><i style="left:75%">75</i><i style="left:100%">100</i></span></div>
<div class="hbar-row"><span></span><span class="hbar-caption">% of residential land</span></div>
</div>
<div class="map-with-legend"><div class="kc-map" data-kc-map="sf" aria-label="Map of metro Kansas City census tracts shaded by the share of residential land that is single-family only, darkest in the outer suburbs"></div><div class="ramp-legend"><p>Share of residential land that is single-family only</p><div class="ramp" style="background:linear-gradient(to right,#d5e3eb,#9db8cd,#5a87ac,#1f618f,#003a58)"></div><div class="ticks"><span>0%</span><span>50%</span><span>100%</span></div><p class="unzoned"><i></i>Unzoned</p></div></div>
</div>
<figcaption><strong>Metro Kansas City: share of residentially zoned land where only single-family homes are allowed by right, by tract income quartile and by census tract.</strong></figcaption>
</figure>

<figure class="wide">
<div class="chart-map">
<div class="hbar green" role="img" aria-label="Share of single-family land with large minimum lot sizes, by neighborhood majority group: White 69 percent at 80,000 square feet or more plus 2 percent at 40,000 to 79,999; Black 0; Hispanic 1; no majority 5">
<div class="hbar-row"><span class="hbar-label">White</span><span class="hbar-track"><span class="seg a" style="width:69%"></span><span class="seg b" style="width:2%"></span><span class="val in" style="left:0;width:69%">69%</span></span></div>
<div class="hbar-row"><span class="hbar-label">Black</span><span class="hbar-track"><span class="seg a" style="width:0%"></span><span class="val" style="left:0%">0%</span></span></div>
<div class="hbar-row"><span class="hbar-label">Hispanic</span><span class="hbar-track"><span class="seg a" style="width:1%"></span><span class="val" style="left:1%">1%</span></span></div>
<div class="hbar-row"><span class="hbar-label">No majority</span><span class="hbar-track"><span class="seg a" style="width:5%"></span><span class="val" style="left:5%">5%</span></span></div>
<div class="hbar-row hbar-axis"><span></span><span class="hbar-track"><i style="left:0">0</i><i style="left:25%">25</i><i style="left:50%">50</i><i style="left:75%">75</i><i style="left:100%">100</i></span></div>
<div class="hbar-row"><span></span><span class="hbar-caption">% of single-family land</span></div>
<div class="hbar-row"><span></span><span class="hbar-legend"><span><i class="a"></i>80,000 sq ft or more</span><span><i class="b"></i>40,000 to 79,999 sq ft</span></span></div>
</div>
<div class="map-with-legend"><div class="kc-map" data-kc-map="mls" aria-label="Map of metro Kansas City census tracts shaded by the share of single-family land with minimum lots of 80,000 square feet or more, concentrated in the outer suburbs"></div><div class="ramp-legend"><p>Share of single-family land with a minimum lot size of 80,000+ sq ft</p><div class="ramp" style="background:linear-gradient(to right,#f8f5ea,#b2ebbd,#38ae69,#00733b,#004221)"></div><div class="ticks"><span>0%</span><span>50%</span><span>100%</span></div><p class="unzoned"><i></i>Unzoned</p></div></div>
</div>
<figcaption><strong>Metro Kansas City: share of single-family land with large minimum lot sizes, by neighborhood majority group and by census tract.</strong> From <em>Zoning Report: Metro Kansas City</em> (2026).</figcaption>
</figure>

The Colorado report was [covered by the *Colorado Sun*](https://coloradosun.com/2025/07/01/national-zoning-atlas-study-colorado-land-use-apartments-townhomes-lot-sizes-parking/) and [cited by Governor Jared Polis&rsquo;s office](https://www.colorado.gov/governor/news/governor-polis-continues-fighting-break-down-barriers-new-housing-coloradans-can-afford). Sara Bronin and I have also written op-eds on zoning reform for the [*Atlanta Journal-Constitution*](https://www.ajc.com/opinion/2026/04/metro-atlanta-communities-must-reform-zoning-to-create-more-affordable-housing/) and, with D. Drogaris, the [*Kansas City Star*](https://www.kansascity.com/opinion/article317286586.html).

## Zoning in metro Atlanta

Across the 11 counties of the Atlanta Regional Commission, 82 of 83 cities and counties have zoning, and together their codes run to about 23,900 pages and 2,238 districts. That is 291 pages per jurisdiction, well above the national average of 192. The City of Atlanta alone has 268 zoning districts, more per capita than any other major city in the Land Use Labs database. The result, as the maps below show, is a region zoned overwhelmingly for detached single-family homes on large lots.

<div class="map-grid">
<figure>
<img src="/assets/img/atl_single_family.jpg" alt="Map of metro Atlanta with land that allows single-family homes by right shaded purple, covering most of the region" loading="lazy">
<figcaption><strong>89%</strong> of residential land allows single-family homes by right.</figcaption>
</figure>
<figure>
<img src="/assets/img/atl_multifamily.jpg" alt="Map of metro Atlanta with land that allows housing of four or more units by right shaded purple, in scattered patches" loading="lazy">
<figcaption><strong>7%</strong> allows housing with four or more units by right.</figcaption>
</figure>
<figure>
<img src="/assets/img/atl_large_lots.jpg" alt="Map of metro Atlanta with single-family land requiring lots of about an acre or more shaded purple, mostly outside the urban core" loading="lazy">
<figcaption><strong>35%</strong> of single-family land requires lots of about an acre (40,000 sq ft) or more.</figcaption>
</figure>
<figure>
<img src="/assets/img/atl_adus.jpg" alt="Map of metro Atlanta with single-family land that allows accessory dwelling units without restrictions shaded purple, in a few areas" loading="lazy">
<figcaption>Only <strong>15%</strong> of single-family land allows ADUs without restrictions; 44% bans them outright.</figcaption>
</figure>
</div>
<p class="map-note"><span>National Zoning Atlas maps of the 11-county Atlanta Regional Commission area, October 2026.</span></p>

## Rethinking how zoning is measured

The Atlas also lets us question the tools researchers have long used to study land-use regulation.

- In &ldquo;[It&rsquo;s time to retire the Wharton Index](http://dx.doi.org/10.2139/ssrn.7391479),&rdquo; S. Bronin, M. Harris, and I audit the most influential measure of land use regulation in the U.S. Cited more than 1,500 times, the Wharton Index has supplied the empirical grounding for the claim that regulation drives up housing costs. We disassemble its twelve subindices and find that they say almost nothing about the content of land use rules, and we compare it against NZA data for more than 1,200 jurisdictions and find the relationship between its scores and actually existing restrictive zoning to be essentially random. (Under review.)
- In &ldquo;[Zoning and municipal data brokers: toward a political economy of &lsquo;data slop&rsquo;](https://bristoluniversitypressdigital.com/edcollchap-oa/book/9781447379362/ch009.xml),&rdquo; D. Drogaris and I locate a &ldquo;data slop&rdquo; economy in the realm of municipal data brokerage, where data brokers are selling poor-quality, AI-generated zoning summaries to planners and developers. (Bristol University Press, 2026, open access.)
- &ldquo;[A national zoning atlas to inform housing research, policy, and public participation](https://www.jstor.org/stable/48749671)&rdquo; (*Cityscape*, 2023), with W. Xu, S. Bronin, and D. Drogaris, lays out what standardized zoning data make possible.

If your organization wants to work with zoning data, I would be glad to hear from you at [scott@landuseatlas.org](mailto:scott@landuseatlas.org).
