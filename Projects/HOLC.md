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
<figcaption><strong>HOLC&rsquo;s map of Atlanta and a sample Area Description sheet.</strong> Source: <a href="https://dsl.richmond.edu/panorama/redlining/"><em>Mapping Inequality</em></a>, Digital Scholarship Lab, University of Richmond.</figcaption>
</figure>

## Tabulating the Area Descriptions

The Digital Scholarship Lab at the University of Richmond has made the HOLC maps and field notes available through *Mapping Inequality*, along with a geopackage and GeoJSON for use in GIS software. Building on that effort, I converted the data in HOLC&rsquo;s Area Descriptions into readable tables, called **THOLCADS**, available at [Open Science Framework](https://osf.io/qytj8/) and through the [Leventhal Map &amp; Education Center](https://data.leventhalmap.org/#/catalog/dkyajewyh). Variables such as the Black population percentage, &ldquo;foreign born&rdquo; percentage and group, family income, occupation class, average building age, repair status, and mortgage availability are ready for statistical analysis, and the remaining entries can be searched by keyword. The R code is on [GitHub](https://github.com/snmarkley1/HOLC_ADS), and the background and methods are in [*Environment and Planning B*](https://doi.org/10.1177/23998083221133112).

Zoom into a city and click on one of its HOLC neighborhoods to see its attributes. Switch basemaps with the layer icon on the left.

<div class="map-frame"><iframe src="/holc_map.html" title="Interactive map of HOLC neighborhoods and their Area Description attributes" loading="lazy"></iframe></div>
<p class="map-note"><span>Data: <a href="https://osf.io/qytj8/">THOLCADS on OSF</a></span><a href="/holc_map.html" target="_blank" rel="noopener">Open full-screen map &#8599;</a></p>

## What the Area Descriptions show

Despite some noteworthy regional variation, the Black population share, &ldquo;foreign born&rdquo; share, and building age rise as grades move from A to D, while family income moves the other way. That is expected: these factors all shaped how lenders, brokers, landlords, appraisers, and others in real estate judged an area&rsquo;s potential returns. The visible presence of Black residents in particular was widely assumed to harm property values. As the top-left panel shows, almost every neighborhood with any Black residents at all received a D.

<figure>
<div class="hc" role="img" aria-label="Four grouped bar charts by region and HOLC grade. In every region, the Black share, the foreign-born share, and building age rise from grade A to grade D, and family income falls. Black shares of D neighborhoods are highest in the South, at about 48 percent; foreign-born shares of D neighborhoods are highest in the Northeast, at about 47 percent.">
<div class="hc-legend"><span><i class="ga"></i>A &ldquo;Best&rdquo;</span><span><i class="gb"></i>B &ldquo;Still desirable&rdquo;</span><span><i class="gc"></i>C &ldquo;Declining&rdquo;</span><span><i class="gd"></i>D &ldquo;Hazardous&rdquo;</span></div>
<div class="hc-grid2">
<div class="hc-panel"><h4>Black residents</h4><div class="hc-cols">
<div class="hc-yaxis"><i style="bottom:0.00%">0</i><i style="bottom:20.00%">10</i><i style="bottom:40.00%">20</i><i style="bottom:60.00%">30</i><i style="bottom:80.00%">40</i><i style="bottom:100.00%">50</i></div>
<div class="hc-plot"><b style="bottom:20.00%"></b><b style="bottom:40.00%"></b><b style="bottom:60.00%"></b><b style="bottom:80.00%"></b><b style="bottom:100.00%"></b>
<div class="hc-group">
<i class="ga" style="height:0.00%" title="Midwest, grade A: 0.0%"></i>
<i class="gb" style="height:0.19%" title="Midwest, grade B: 0.1%"></i>
<i class="gc" style="height:0.64%" title="Midwest, grade C: 0.3%"></i>
<i class="gd" style="height:29.88%" title="Midwest, grade D: 14.9%"></i>
</div>
<div class="hc-group">
<i class="ga" style="height:0.00%" title="Northeast, grade A: 0.0%"></i>
<i class="gb" style="height:0.08%" title="Northeast, grade B: 0.0%"></i>
<i class="gc" style="height:1.22%" title="Northeast, grade C: 0.6%"></i>
<i class="gd" style="height:31.30%" title="Northeast, grade D: 15.6%"></i>
</div>
<div class="hc-group">
<i class="ga" style="height:0.00%" title="South, grade A: 0.0%"></i>
<i class="gb" style="height:0.09%" title="South, grade B: 0.0%"></i>
<i class="gc" style="height:4.70%" title="South, grade C: 2.4%"></i>
<i class="gd" style="height:96.73%" title="South, grade D: 48.4%"></i>
</div>
<div class="hc-group">
<i class="ga" style="height:0.04%" title="West, grade A: 0.0%"></i>
<i class="gb" style="height:0.03%" title="West, grade B: 0.0%"></i>
<i class="gc" style="height:0.38%" title="West, grade C: 0.2%"></i>
<i class="gd" style="height:8.88%" title="West, grade D: 4.4%"></i>
</div>
</div></div>
<div class="hc-xaxis"><span>Midwest</span><span>Northeast</span><span>South</span><span>West</span></div></div>
<div class="hc-panel"><h4>&ldquo;Foreign born&rdquo; residents</h4><div class="hc-cols">
<div class="hc-yaxis"><i style="bottom:0.00%">0</i><i style="bottom:20.00%">10</i><i style="bottom:40.00%">20</i><i style="bottom:60.00%">30</i><i style="bottom:80.00%">40</i><i style="bottom:100.00%">50</i></div>
<div class="hc-plot"><b style="bottom:20.00%"></b><b style="bottom:40.00%"></b><b style="bottom:60.00%"></b><b style="bottom:80.00%"></b><b style="bottom:100.00%"></b>
<div class="hc-group">
<i class="ga" style="height:1.80%" title="Midwest, grade A: 0.9%"></i>
<i class="gb" style="height:7.06%" title="Midwest, grade B: 3.5%"></i>
<i class="gc" style="height:31.90%" title="Midwest, grade C: 15.9%"></i>
<i class="gd" style="height:59.00%" title="Midwest, grade D: 29.5%"></i>
</div>
<div class="hc-group">
<i class="ga" style="height:0.73%" title="Northeast, grade A: 0.4%"></i>
<i class="gb" style="height:11.60%" title="Northeast, grade B: 5.8%"></i>
<i class="gc" style="height:48.43%" title="Northeast, grade C: 24.2%"></i>
<i class="gd" style="height:94.83%" title="Northeast, grade D: 47.4%"></i>
</div>
<div class="hc-group">
<i class="ga" style="height:0.47%" title="South, grade A: 0.2%"></i>
<i class="gb" style="height:1.18%" title="South, grade B: 0.6%"></i>
<i class="gc" style="height:1.67%" title="South, grade C: 0.8%"></i>
<i class="gd" style="height:3.06%" title="South, grade D: 1.5%"></i>
</div>
<div class="hc-group">
<i class="ga" style="height:1.15%" title="West, grade A: 0.6%"></i>
<i class="gb" style="height:2.45%" title="West, grade B: 1.2%"></i>
<i class="gc" style="height:9.56%" title="West, grade C: 4.8%"></i>
<i class="gd" style="height:52.52%" title="West, grade D: 26.3%"></i>
</div>
</div></div>
<div class="hc-xaxis"><span>Midwest</span><span>Northeast</span><span>South</span><span>West</span></div></div>
<div class="hc-panel"><h4>Family income midpoint</h4><div class="hc-cols">
<div class="hc-yaxis"><i style="bottom:0.00%">$0</i><i style="bottom:33.33%">$5k</i><i style="bottom:66.67%">$10k</i><i style="bottom:100.00%">$15k</i></div>
<div class="hc-plot"><b style="bottom:33.33%"></b><b style="bottom:66.67%"></b><b style="bottom:100.00%"></b>
<div class="hc-group">
<i class="ga" style="height:62.54%" title="Midwest, grade A: $9,380"></i>
<i class="gb" style="height:27.41%" title="Midwest, grade B: $4,110"></i>
<i class="gc" style="height:14.33%" title="Midwest, grade C: $2,150"></i>
<i class="gd" style="height:8.57%" title="Midwest, grade D: $1,290"></i>
</div>
<div class="hc-group">
<i class="ga" style="height:94.27%" title="Northeast, grade A: $14,140"></i>
<i class="gb" style="height:33.06%" title="Northeast, grade B: $4,960"></i>
<i class="gc" style="height:15.46%" title="Northeast, grade C: $2,320"></i>
<i class="gd" style="height:8.65%" title="Northeast, grade D: $1,300"></i>
</div>
<div class="hc-group">
<i class="ga" style="height:74.23%" title="South, grade A: $11,130"></i>
<i class="gb" style="height:32.83%" title="South, grade B: $4,920"></i>
<i class="gc" style="height:16.91%" title="South, grade C: $2,540"></i>
<i class="gd" style="height:6.84%" title="South, grade D: $1,030"></i>
</div>
<div class="hc-group">
<i class="ga" style="height:63.94%" title="West, grade A: $9,590"></i>
<i class="gb" style="height:36.89%" title="West, grade B: $5,530"></i>
<i class="gc" style="height:14.18%" title="West, grade C: $2,130"></i>
<i class="gd" style="height:9.24%" title="West, grade D: $1,390"></i>
</div>
</div></div>
<div class="hc-xaxis"><span>Midwest</span><span>Northeast</span><span>South</span><span>West</span></div></div>
<div class="hc-panel"><h4>Building age midpoint</h4><div class="hc-cols">
<div class="hc-yaxis"><i style="bottom:0.00%">0</i><i style="bottom:25.00%">10</i><i style="bottom:50.00%">20</i><i style="bottom:75.00%">30</i><i style="bottom:100.00%">40</i></div>
<div class="hc-plot"><b style="bottom:25.00%"></b><b style="bottom:50.00%"></b><b style="bottom:75.00%"></b><b style="bottom:100.00%"></b>
<div class="hc-group">
<i class="ga" style="height:28.13%" title="Midwest, grade A: 11 years"></i>
<i class="gb" style="height:38.22%" title="Midwest, grade B: 15 years"></i>
<i class="gc" style="height:56.40%" title="Midwest, grade C: 23 years"></i>
<i class="gd" style="height:80.34%" title="Midwest, grade D: 32 years"></i>
</div>
<div class="hc-group">
<i class="ga" style="height:35.46%" title="Northeast, grade A: 14 years"></i>
<i class="gb" style="height:48.14%" title="Northeast, grade B: 19 years"></i>
<i class="gc" style="height:64.16%" title="Northeast, grade C: 26 years"></i>
<i class="gd" style="height:91.00%" title="Northeast, grade D: 36 years"></i>
</div>
<div class="hc-group">
<i class="ga" style="height:18.56%" title="South, grade A: 7 years"></i>
<i class="gb" style="height:29.44%" title="South, grade B: 12 years"></i>
<i class="gc" style="height:48.07%" title="South, grade C: 19 years"></i>
<i class="gd" style="height:61.99%" title="South, grade D: 25 years"></i>
</div>
<div class="hc-group">
<i class="ga" style="height:20.27%" title="West, grade A: 8 years"></i>
<i class="gb" style="height:28.70%" title="West, grade B: 11 years"></i>
<i class="gc" style="height:42.62%" title="West, grade C: 17 years"></i>
<i class="gd" style="height:60.99%" title="West, grade D: 24 years"></i>
</div>
</div></div>
<div class="hc-xaxis"><span>Midwest</span><span>Northeast</span><span>South</span><span>West</span></div></div>
</div></div>
<figcaption><strong>Percent Black, percent foreign born, family income, and building age by HOLC grade and region.</strong> Hover over a bar for its value. Data: <a href="https://github.com/snmarkley1/THOLCADS">THOLCADS</a>.</figcaption>
</figure>

Home repair status, mortgage availability, and resident occupation class break down by grade in the same way.

<figure>
<div class="hc" role="img" aria-label="Three stacked bar charts of neighborhoods by HOLC grade. Grade A neighborhoods were overwhelmingly described as in good repair, with ample mortgage funds and upper-class residents; grade D neighborhoods were mostly described as in poor repair, with restricted mortgage funds and lower-class residents.">
<div class="hc-grid3">
<div class="hc-panel"><h4>Home repair status</h4>
<div class="hc-hrow"><span class="hc-lab">A</span><span class="hc-stack"><i class="o1" style="flex:96.63" title="Grade A, Good: 96.6%">97</i><i class="o2" style="flex:0.84" title="Grade A, Fair&ndash;good: 0.8%"></i><i class="o3" style="flex:0.28" title="Grade A, Fair: 0.3%"></i><i class="o6" style="flex:2.24" title="Grade A, No data: 2.2%"></i></span></div>
<div class="hc-hrow"><span class="hc-lab">B</span><span class="hc-stack"><i class="o1" style="flex:71.99" title="Grade B, Good: 72.0%">72</i><i class="o2" style="flex:17.09" title="Grade B, Fair&ndash;good: 17.1%">17</i><i class="o3" style="flex:6.93" title="Grade B, Fair: 6.9%"></i><i class="o4" style="flex:0.23" title="Grade B, Fair&ndash;poor: 0.2%"></i><i class="o5" style="flex:0.35" title="Grade B, Poor: 0.3%"></i><i class="o6" style="flex:3.41" title="Grade B, No data: 3.4%"></i></span></div>
<div class="hc-hrow"><span class="hc-lab">C</span><span class="hc-stack"><i class="o1" style="flex:13.82" title="Grade C, Good: 13.8%">14</i><i class="o2" style="flex:21.54" title="Grade C, Fair&ndash;good: 21.5%">22</i><i class="o3" style="flex:44.00" title="Grade C, Fair: 44.0%">44</i><i class="o4" style="flex:13.00" title="Grade C, Fair&ndash;poor: 13.0%">13</i><i class="o5" style="flex:3.88" title="Grade C, Poor: 3.9%"></i><i class="o6" style="flex:3.77" title="Grade C, No data: 3.8%"></i></span></div>
<div class="hc-hrow"><span class="hc-lab">D</span><span class="hc-stack"><i class="o1" style="flex:1.62" title="Grade D, Good: 1.6%"></i><i class="o2" style="flex:3.00" title="Grade D, Fair&ndash;good: 3.0%"></i><i class="o3" style="flex:17.30" title="Grade D, Fair: 17.3%">17</i><i class="o4" style="flex:28.36" title="Grade D, Fair&ndash;poor: 28.4%">28</i><i class="o5" style="flex:45.03" title="Grade D, Poor: 45.0%">45</i><i class="o6" style="flex:4.68" title="Grade D, No data: 4.7%"></i></span></div>
<div class="hc-hrow hc-ticks"><span></span><span><i style="left:0%">0</i><i style="left:50%">50</i><i style="left:100%">100</i></span></div>
<div class="hc-legend"><span><i class="o1"></i>Good</span><span><i class="o2"></i>Fair&ndash;good</span><span><i class="o3"></i>Fair</span><span><i class="o4"></i>Fair&ndash;poor</span><span><i class="o5"></i>Poor</span><span><i class="o6"></i>No data</span></div></div>
<div class="hc-panel"><h4>Mortgage availability</h4>
<div class="hc-hrow"><span class="hc-lab">A</span><span class="hc-stack"><i class="o1" style="flex:88.92" title="Grade A, Ample: 88.9%">89</i><i class="o2" style="flex:4.49" title="Grade A, Limited&ndash;ample: 4.5%"></i><i class="o3" style="flex:3.93" title="Grade A, Limited: 3.9%"></i><i class="o5" style="flex:0.42" title="Grade A, Restricted: 0.4%"></i><i class="o6" style="flex:2.24" title="Grade A, No data: 2.2%"></i></span></div>
<div class="hc-hrow"><span class="hc-lab">B</span><span class="hc-stack"><i class="o1" style="flex:70.23" title="Grade B, Ample: 70.2%">70</i><i class="o2" style="flex:3.93" title="Grade B, Limited&ndash;ample: 3.9%"></i><i class="o3" style="flex:20.55" title="Grade B, Limited: 20.6%">21</i><i class="o4" style="flex:0.18" title="Grade B, Limited&ndash;restricted: 0.2%"></i><i class="o5" style="flex:1.35" title="Grade B, Restricted: 1.4%"></i><i class="o6" style="flex:3.76" title="Grade B, No data: 3.8%"></i></span></div>
<div class="hc-hrow"><span class="hc-lab">C</span><span class="hc-stack"><i class="o1" style="flex:22.98" title="Grade C, Ample: 23.0%">23</i><i class="o2" style="flex:4.10" title="Grade C, Limited&ndash;ample: 4.1%"></i><i class="o3" style="flex:54.12" title="Grade C, Limited: 54.1%">54</i><i class="o4" style="flex:1.44" title="Grade C, Limited&ndash;restricted: 1.4%"></i><i class="o5" style="flex:13.52" title="Grade C, Restricted: 13.5%">14</i><i class="o6" style="flex:3.84" title="Grade C, No data: 3.8%"></i></span></div>
<div class="hc-hrow"><span class="hc-lab">D</span><span class="hc-stack"><i class="o1" style="flex:1.50" title="Grade D, Ample: 1.5%"></i><i class="o2" style="flex:1.00" title="Grade D, Limited&ndash;ample: 1.0%"></i><i class="o3" style="flex:32.42" title="Grade D, Limited: 32.4%">32</i><i class="o4" style="flex:0.69" title="Grade D, Limited&ndash;restricted: 0.7%"></i><i class="o5" style="flex:59.40" title="Grade D, Restricted: 59.4%">59</i><i class="o6" style="flex:5.00" title="Grade D, No data: 5.0%"></i></span></div>
<div class="hc-hrow hc-ticks"><span></span><span><i style="left:0%">0</i><i style="left:50%">50</i><i style="left:100%">100</i></span></div>
<div class="hc-legend"><span><i class="o1"></i>Ample</span><span><i class="o2"></i>Limited&ndash;ample</span><span><i class="o3"></i>Limited</span><span><i class="o4"></i>Limited&ndash;restricted</span><span><i class="o5"></i>Restricted</span><span><i class="o6"></i>No data</span></div></div>
<div class="hc-panel"><h4>Occupation class</h4>
<div class="hc-hrow"><span class="hc-lab">A</span><span class="hc-stack"><i class="o1" style="flex:78.96" title="Grade A, &ldquo;Upper&rdquo;: 79.0%">79</i><i class="o2" style="flex:11.92" title="Grade A, Upper-middle: 11.9%"></i><i class="o3" style="flex:2.66" title="Grade A, Middle/mixed: 2.7%"></i><i class="o4" style="flex:0.14" title="Grade A, Lower-middle: 0.1%"></i><i class="o6" style="flex:6.31" title="Grade A, No data: 6.3%"></i></span></div>
<div class="hc-hrow"><span class="hc-lab">B</span><span class="hc-stack"><i class="o1" style="flex:43.75" title="Grade B, &ldquo;Upper&rdquo;: 43.8%">44</i><i class="o2" style="flex:30.06" title="Grade B, Upper-middle: 30.1%">30</i><i class="o3" style="flex:17.20" title="Grade B, Middle/mixed: 17.2%">17</i><i class="o4" style="flex:2.23" title="Grade B, Lower-middle: 2.2%"></i><i class="o5" style="flex:1.59" title="Grade B, &ldquo;Lower&rdquo;: 1.6%"></i><i class="o6" style="flex:5.17" title="Grade B, No data: 5.2%"></i></span></div>
<div class="hc-hrow"><span class="hc-lab">C</span><span class="hc-stack"><i class="o1" style="flex:8.94" title="Grade C, &ldquo;Upper&rdquo;: 8.9%"></i><i class="o2" style="flex:13.78" title="Grade C, Upper-middle: 13.8%">14</i><i class="o3" style="flex:32.77" title="Grade C, Middle/mixed: 32.8%">33</i><i class="o4" style="flex:17.55" title="Grade C, Lower-middle: 17.6%">18</i><i class="o5" style="flex:21.72" title="Grade C, &ldquo;Lower&rdquo;: 21.7%">22</i><i class="o6" style="flex:5.25" title="Grade C, No data: 5.2%"></i></span></div>
<div class="hc-hrow"><span class="hc-lab">D</span><span class="hc-stack"><i class="o1" style="flex:0.37" title="Grade D, &ldquo;Upper&rdquo;: 0.4%"></i><i class="o2" style="flex:1.06" title="Grade D, Upper-middle: 1.1%"></i><i class="o3" style="flex:12.12" title="Grade D, Middle/mixed: 12.1%">12</i><i class="o4" style="flex:12.99" title="Grade D, Lower-middle: 13.0%">13</i><i class="o5" style="flex:68.27" title="Grade D, &ldquo;Lower&rdquo;: 68.3%">68</i><i class="o6" style="flex:5.18" title="Grade D, No data: 5.2%"></i></span></div>
<div class="hc-hrow hc-ticks"><span></span><span><i style="left:0%">0</i><i style="left:50%">50</i><i style="left:100%">100</i></span></div>
<div class="hc-legend"><span><i class="o1"></i>&ldquo;Upper&rdquo;</span><span><i class="o2"></i>Upper-middle</span><span><i class="o3"></i>Middle/mixed</span><span><i class="o4"></i>Lower-middle</span><span><i class="o5"></i>&ldquo;Lower&rdquo;</span><span><i class="o6"></i>No data</span></div></div>
</div>
<p class="hc-note">Bars show the share of each grade&rsquo;s neighborhoods (%), with the best category at left.</p></div>
<figcaption><strong>Repair status, mortgage availability, and occupation class by HOLC grade.</strong> Data: <a href="https://github.com/snmarkley1/THOLCADS">THOLCADS</a>.</figcaption>
</figure>

We can also ask how appraisers graded neighborhoods based on which &ldquo;foreign born&rdquo; groups lived there. The next chart counts the HOLC neighborhoods where each group is at least mentioned.

<figure>
<div class="hc hc-groups" role="img" aria-label="Stacked bar chart of the HOLC grades of neighborhoods where each population group is mentioned. 81 percent of neighborhoods with East Asian or Pacific Islander residents and 73 percent with Black residents were graded D, compared with 24 percent of all neighborhoods. Neighborhoods with British or American residents, or no group noted, were rarely graded D.">
<div class="hc-legend"><span><i class="ga"></i>A &ldquo;Best&rdquo;</span><span><i class="gb"></i>B &ldquo;Still desirable&rdquo;</span><span><i class="gc"></i>C &ldquo;Declining&rdquo;</span><span><i class="gd"></i>D &ldquo;Hazardous&rdquo;</span></div>
<div class="hc-hrow"><span class="hc-lab">East Asian/Pacific Islander <small>70</small></span><span class="hc-stack"><i class="gc" style="flex:18.57" title="East Asian/Pacific Islander, grade C: 18.6%">19</i><i class="gd" style="flex:81.43" title="East Asian/Pacific Islander, grade D: 81.4%">81</i></span></div>
<div class="hc-hrow"><span class="hc-lab">Black <small>1,215</small></span><span class="hc-stack"><i class="ga" style="flex:0.08" title="Black, grade A: 0.1%"></i><i class="gb" style="flex:2.22" title="Black, grade B: 2.2%"></i><i class="gc" style="flex:24.53" title="Black, grade C: 24.5%">25</i><i class="gd" style="flex:73.17" title="Black, grade D: 73.2%">73</i></span></div>
<div class="hc-hrow"><span class="hc-lab">&ldquo;Latin&rdquo; <small>174</small></span><span class="hc-stack"><i class="ga" style="flex:1.72" title="Latin, grade A: 1.7%"></i><i class="gb" style="flex:5.75" title="Latin, grade B: 5.8%"></i><i class="gc" style="flex:31.03" title="Latin, grade C: 31.0%">31</i><i class="gd" style="flex:61.49" title="Latin, grade D: 61.5%">61</i></span></div>
<div class="hc-hrow"><span class="hc-lab">Greek <small>66</small></span><span class="hc-stack"><i class="ga" style="flex:1.52" title="Greek, grade A: 1.5%"></i><i class="gb" style="flex:4.55" title="Greek, grade B: 4.5%"></i><i class="gc" style="flex:42.42" title="Greek, grade C: 42.4%">42</i><i class="gd" style="flex:51.52" title="Greek, grade D: 51.5%">52</i></span></div>
<div class="hc-hrow"><span class="hc-lab">Italian <small>831</small></span><span class="hc-stack"><i class="ga" style="flex:0.36" title="Italian, grade A: 0.4%"></i><i class="gb" style="flex:5.29" title="Italian, grade B: 5.3%"></i><i class="gc" style="flex:47.17" title="Italian, grade C: 47.2%">47</i><i class="gd" style="flex:47.17" title="Italian, grade D: 47.2%">47</i></span></div>
<div class="hc-hrow"><span class="hc-lab">Polish <small>410</small></span><span class="hc-stack"><i class="ga" style="flex:0.73" title="Polish, grade A: 0.7%"></i><i class="gb" style="flex:6.83" title="Polish, grade B: 6.8%"></i><i class="gc" style="flex:50.73" title="Polish, grade C: 50.7%">51</i><i class="gd" style="flex:41.71" title="Polish, grade D: 41.7%">42</i></span></div>
<div class="hc-hrow"><span class="hc-lab">Eastern European <small>377</small></span><span class="hc-stack"><i class="ga" style="flex:0.27" title="Eastern European, grade A: 0.3%"></i><i class="gb" style="flex:9.81" title="Eastern European, grade B: 9.8%">10</i><i class="gc" style="flex:48.81" title="Eastern European, grade C: 48.8%">49</i><i class="gd" style="flex:41.11" title="Eastern European, grade D: 41.1%">41</i></span></div>
<div class="hc-hrow"><span class="hc-lab">Irish <small>112</small></span><span class="hc-stack"><i class="ga" style="flex:0.89" title="Irish, grade A: 0.9%"></i><i class="gb" style="flex:21.43" title="Irish, grade B: 21.4%">21</i><i class="gc" style="flex:52.68" title="Irish, grade C: 52.7%">53</i><i class="gd" style="flex:25.00" title="Irish, grade D: 25.0%">25</i></span></div>
<div class="hc-hrow"><span class="hc-lab">Jewish <small>173</small></span><span class="hc-stack"><i class="ga" style="flex:4.62" title="Jewish, grade A: 4.6%"></i><i class="gb" style="flex:26.59" title="Jewish, grade B: 26.6%">27</i><i class="gc" style="flex:43.93" title="Jewish, grade C: 43.9%">44</i><i class="gd" style="flex:24.86" title="Jewish, grade D: 24.9%">25</i></span></div>
<div class="hc-hrow"><span class="hc-lab">German <small>317</small></span><span class="hc-stack"><i class="ga" style="flex:1.26" title="German, grade A: 1.3%"></i><i class="gb" style="flex:17.67" title="German, grade B: 17.7%">18</i><i class="gc" style="flex:61.20" title="German, grade C: 61.2%">61</i><i class="gd" style="flex:19.87" title="German, grade D: 19.9%">20</i></span></div>
<div class="hc-hrow"><span class="hc-lab">Nordic <small>66</small></span><span class="hc-stack"><i class="ga" style="flex:3.03" title="Nordic, grade A: 3.0%"></i><i class="gb" style="flex:21.21" title="Nordic, grade B: 21.2%">21</i><i class="gc" style="flex:56.06" title="Nordic, grade C: 56.1%">56</i><i class="gd" style="flex:19.70" title="Nordic, grade D: 19.7%">20</i></span></div>
<div class="hc-hrow"><span class="hc-lab">British <small>75</small></span><span class="hc-stack"><i class="ga" style="flex:9.33" title="British, grade A: 9.3%">9</i><i class="gb" style="flex:30.67" title="British, grade B: 30.7%">31</i><i class="gc" style="flex:53.33" title="British, grade C: 53.3%">53</i><i class="gd" style="flex:6.67" title="British, grade D: 6.7%"></i></span></div>
<div class="hc-hrow"><span class="hc-lab">&ldquo;American&rdquo; <small>61</small></span><span class="hc-stack"><i class="ga" style="flex:13.11" title="American, grade A: 13.1%">13</i><i class="gb" style="flex:36.07" title="American, grade B: 36.1%">36</i><i class="gc" style="flex:47.54" title="American, grade C: 47.5%">48</i><i class="gd" style="flex:3.28" title="American, grade D: 3.3%"></i></span></div>
<div class="hc-hrow hc-sep"><span class="hc-lab">No group noted <small>3,276</small></span><span class="hc-stack"><i class="ga" style="flex:19.93" title="No group noted, grade A: 19.9%">20</i><i class="gb" style="flex:38.34" title="No group noted, grade B: 38.3%">38</i><i class="gc" style="flex:34.22" title="No group noted, grade C: 34.2%">34</i><i class="gd" style="flex:7.51" title="No group noted, grade D: 7.5%">8</i></span></div>
<div class="hc-hrow hc-total"><span class="hc-lab">All neighborhoods <small>6,724</small></span><span class="hc-stack"><i class="ga" style="flex:10.60" title="All neighborhoods, grade A: 10.6%">11</i><i class="gb" style="flex:25.33" title="All neighborhoods, grade B: 25.3%">25</i><i class="gc" style="flex:40.26" title="All neighborhoods, grade C: 40.3%">40</i><i class="gd" style="flex:23.81" title="All neighborhoods, grade D: 23.8%">24</i></span></div>
<div class="hc-hrow hc-ticks"><span></span><span><i style="left:0%">0</i><i style="left:25%">25</i><i style="left:50%">50</i><i style="left:75%">75</i><i style="left:100%">100</i></span></div>
<p class="hc-note">Share of neighborhoods mentioning each group, by grade (%). Numbers after each group are neighborhoods.</p></div>
<figcaption><strong>HOLC grades of neighborhoods where each population group is mentioned.</strong> Data: <a href="https://github.com/snmarkley1/THOLCADS">THOLCADS</a>.</figcaption>
</figure>

The relationship between grades and groups closely tracks the racist ranking published by the land economist Homer Hoyt in his 1933 *One Hundred Years of Land Values in Chicago*, which claimed that land values rose or fell depending on which of these populations lived nearby. Hoyt&rsquo;s book was exceptionally well regarded in the industry, and he went on to serve as chief economist of the Federal Housing Administration (FHA), where he was instrumental in the agency&rsquo;s adoption of its own redlining maps and policies.

<figure>
<img src="/Projects/hoyt.png" alt="Homer Hoyt's 1933 ranking of racial and ethnic groups by purported effect on land values">
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
