---
title: Datasets
---

This page provides a centralized place to download some of the  datasets I have helped create, including the Historical Housing Unit and Urbanization Database v2010 (HHUUD10), Tabulated HOLC Area Description Sheet (THOLCADS) Data, and Tracts by Census Place Using Centroids.


### [HHUUD10 on Esri's Living Atlas](https://livingatlas.arcgis.com/en/browse/?q=hhuud10#q=hhuud10&d=2) | [HHUUD10 on OSF](https://osf.io/fzv5e/)

HHUUD10 provides historical housing unit counts and urbanization estimates in consistent census tract boundaries for the entire United States for each decade from 1940 to 2010 plus 2019. The data is available in csv, dta, xpt, v8xpt, shapefile, and geojson formats. It is also available as a feature service through Esri's Living Atlas. The methodology is detailed [here](https://www.nature.com/articles/s41597-022-01184-x).


### [THOLCADS Data at the Boston Public Library](https://data.leventhalmap.org/#/catalog/dkyajewyh) | [THOLCADS Data on OSF](https://osf.io/qytj8/)

THOLCADS provides tabulated Area Description sheet data from the Home Owners' Loan Corporation's (HOLC) Residential Security maps. Available in xlsx, csv, shapefile, and geojson formats, this dataset allows users to more easily conduct qualitative and quantitative assessments of the criteria used by HOLC to assign neighborhood risk scores. More background, including the methodology, is provided [here](https://osf.io/preprints/socarxiv/dktah/).

### [Tracts by Census Place Using Centroids on GitHub](https://github.com/snmarkley1/Tracts-by-Census-Place-Using-Centroids)

This repository contains R scripts that produce output csv and xlsx files that include all census tracts in the US assigned to the Census-defined [place](https://www2.census.gov/geo/pdfs/reference/GARM/Ch9GARM.pdf) (*e.g.*, city, town, village, etc.) in which their centroid is located. The scripts are written to allow users to produce this file for the whole US or for individual states. Further, they can specify which tract or place vintage (2010 or later) they would like to use. The `file_download` folder includes csv and xlsx files using 2010 and 2020 tract vintages with 2021 place vintages.
