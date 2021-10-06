

## Mapping Apt Demolitions


## PREPARE WORKSPACE
rm(list = ls())  # clear environment
options(scipen = 999) 
options(digits = 6)
#setwd("D:/HIST_HU_URB")  # change if desired

## Load or install packages
packages <- function(x) {
  x <- deparse(substitute(x))
  installed_packages <- as.character(installed.packages()[, 1])
  
  if (length(intersect(x, installed_packages)) == 0) {
    install.packages(pkgs = x, dependencies = TRUE, repos = "http://cran.r-project.org")
  }
  
  library(x, character.only = TRUE)
  rm(installed_packages) # Remove From Workspace
}

packages(tidyverse)
packages(sf)  # for spatial/ArcGIS Pro data
packages(tidycensus)
packages(mapview)
packages(leaflet)
packages(tigris)



#dir.create("r_scripts")


#######################################################################
##   LOAD and CONVERT JSON
#######################################################################

## read in apt data
apt_pop <- read_csv("C:/Users/scott/Dropbox/atlantaStudies/atl_suburb_apt_data.csv") %>%
  # fix NAs
  mutate_at(vars(wht10:other10), funs(ifelse(is.na(.), 0, .))) %>%
  # Calculate % Group
  mutate(
    P_White = wht10 / est_pop10 * 100,
    P_Black = blk10 / est_pop10 * 100,
    P_Asian_PI = asn10 / est_pop10 * 100,
    P_Hispanic = hisp10 / est_pop10 * 100,
    P_Other =  100 - P_White - P_Black - P_Hispanic - P_Asian_PI
  ) %>%
  print()

## Import json
apts <- rgdal::readOGR("Projects/apts.json")
print(apts)

## Convert to sf
apts_sf <- st_as_sf(apts) %>%
  left_join(apt_pop[-c(1,6,8)], by = c("apt_name", "city")) %>%
   rename(
    Apartment = 1,
    City = 2,
    Pop_2010 = 3,
    Demo_Year = 4,
    Status = 5,
    Ownership = 6,
    Units = 7,
    White = 8,
    Black = 9,
    Asian_PI = 10,
    Hispanic = 11,
    Other = 12
  ) %>%
  print()


########################################################
## Load in Census Variables for Places
#######################################################

## read in 2020 place data
cities20 <- read_csv("tables/places_race_2020.csv") %>%
  mutate(Year = 2020) %>%
  print()


## set 2010 vars
vars <- data.frame(
  vars = c("P005003", "P005004", "P005006", "P005007", "P005010"),
  var_names = c("P_White", "P_Black", "Asian", "PI", "P_Hispanic")
)
 

## read in 2010 place data
cities10 <- get_decennial(
  geography = "place",
  variables = vars$vars,
  year = 2010,
  state = "GA",
  summary_var = "P005001"
) %>%
  filter(str_detect(NAME, "Atlanta|Marietta|Smyrna|Roswell|Sandy Springs|Brookhaven")) %>%
  mutate(City = str_replace(NAME, " city, Georgia", "")) %>%
  left_join(vars, by = c("variable" = "vars")) %>%
  mutate(POP = value / summary_value * 100) %>%
  select(City, var_names, summary_value, POP) %>%
  pivot_wider(
    names_from = var_names,
    values_from = POP
  ) %>%
  mutate(
    P_Asian_PI = Asian + PI,
    P_Other = 100 - P_White - P_Black - P_Asian_PI - P_Hispanic,
    City = ifelse(str_detect(City, "North Atlanta"), "Brookhaven", City),
    Year = 2010
  ) %>%
  rename(Population = summary_value) %>%
  select(City, Population, P_White, P_Black, P_Asian_PI, P_Hispanic, P_Other, Year) %>%
  arrange(City) %>%
  print()


## Get shapes
cities_geom <- tigris::places("GA", cb = TRUE) %>%
  filter(str_detect(NAME, "Atlanta|Marietta|Smyrna|Roswell|Sandy Springs|Brookhaven")) %>%
  select(NAME, geometry) %>%
  rename(City = NAME) %>%
  print()


## Join
cities <- bind_rows(cities10, cities20) %>%
  pivot_wider(
    names_from = Year,
    values_from = Population:P_Other
  ) %>%
  rename(
    Pop_2010 = 2,
    Pop_2020 = 3
  ) %>%
  left_join(cities_geom, by = "City") %>%
  arrange(City) %>%
  st_as_sf() %>%
  print()


########################################################
## Mapview
#######################################################

## Set mapview options
mapviewOptions(fgb = FALSE, basemaps = "Esri.WorldImagery")

apt_map <- mapview(
  apts_sf,
  alpha.regions = 0.8,
  #zcol = "Status",
  col.regions = c("brown1", "lightsalmon"),
  cex = "Pop_2010",
  layer.name = "Apartment Demolitions",
  label = "Apartment"
  ) +
  mapview(
    cities, 
    alpha.regions = 0.1,
    alpha = 1,
    col.regions = "gray",
    layer.name = "Cities",
    lwd = 2,
    label = "City"
    )

apt_map2 <- apt_map@map %>%
  # add <-  map from USGS
  leaflet::addTiles(
    "https://basemap.nationalmap.gov/arcgis/rest/services/USGSImageryTopo/MapServer/tile/{z}/{y}/{x}"
    )

apt_map2

