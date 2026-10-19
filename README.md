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

## Basemaps

CARTO's free basemap tiles now draw an "API KEY REQUIRED" watermark. This is a public repo, so the maps don't use a CARTO key: anything in the HTML is readable by anyone. They use Esri's keyless World Light Gray and World Dark Gray canvases instead. The R-exported maps (`holc_map.html`, `apt_map.html`, `place_map.html`) were patched in place. If you re-export one from R, use `addProviderTiles("Esri.WorldGrayCanvas")` or an `addTiles()` call on the Esri canvas URL instead of `CartoDB.Positron` / `CartoDB.DarkMatter`.

## Leftovers

The old Contrast theme (`_sass/`, `_includes/`, `_posts/`, `_data/`, `assets/katex/`, `assets/fontawesome/`, `assets/fonts/`, `assets/css/`) is still in the repo but excluded from the build in `_config.yml`, and can be deleted.
