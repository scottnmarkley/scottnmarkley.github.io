# scottnmarkley.github.io

Personal research site for Scott Markley, built by GitHub Pages with Jekyll. There is no local build step; pushing to `master` publishes the site.

## Layout

- `_layouts/default.html` holds the header, nav, and footer. `_layouts/page.html` wraps every interior page and reads `title`, `kicker`, and `lede` from front matter.
- `assets/site.css` is the whole stylesheet (plain CSS, light and dark mode).
- `index.html` is the home page. Interior pages are Markdown: `Projects/*.md`, `publications.md`, `Datasets.md`, `cv.md`.
- Pages that need Leaflet load it through a `head:` block in their front matter (see `index.html`).

## Common updates

- **New CV:** add the PDF to `cv/` and change the `cv:` line in `_config.yml`. Every CV link reads from it.
- **New paper:** add an `<li>` to `publications.md`.
- **Zoning report map:** the states and metros are listed at the top of `assets/zoning-map.js`.
- **Apartment demolitions map** (`apt_map.html`, embedded on the suburbs page): the sites and city boundaries are in `assets/data/atl_demolitions.json`.

## Basemaps

CARTO's free basemap tiles now draw an "API KEY REQUIRED" watermark. This is a public repo, so the maps don't use a CARTO key: anything in the HTML is readable by anyone. They use Esri's keyless tiles instead: the World Light Gray and World Dark Gray canvases, or World Imagery for the satellite view on `apt_map.html`. `holc_map.html` is still an R leaflet export, patched in place. If you re-export it from R, use `addProviderTiles("Esri.WorldGrayCanvas")` or an `addTiles()` call on the Esri canvas URL instead of `CartoDB.Positron` / `CartoDB.DarkMatter`.

## Not on the site

`r_scripts/`, `tables/`, and the `.Rproj` file are R source work. Like this README, they're kept in the repo but excluded from the build in `_config.yml`.
