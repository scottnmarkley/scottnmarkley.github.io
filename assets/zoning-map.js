// Map of the places my recent zoning reports and projects cover.
// Needs Leaflet and topojson-client on the page, and a <div id="zoning-map">.
// Basemap: Esri's keyless gray canvases (CARTO tiles now need an API key,
// which shouldn't sit in a public repo).
(function () {
  var el = document.getElementById("zoning-map");
  if (!el || !window.L || !window.topojson) return;

  var dark = window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches;
  var css = getComputedStyle(document.documentElement);
  var accent = css.getPropertyValue("--accent").trim() || "#a8402a";
  var blue = css.getPropertyValue("--blue").trim() || "#2f5476";

  // statewide reports, keyed by state FIPS code
  var states = {
    "08": { name: "Colorado", status: "Zoning Report: Colorado (2025)",
            url: "https://www.zoningatlas.org/zoning-report-colorado-2025" },
    "51": { name: "Virginia", status: "Zoning Report: Virginia (2025)",
            url: "https://www.zoningatlas.org/zoning-report-virginia-2025" },
    "25": { name: "Massachusetts", status: "Zoning Report: Massachusetts (2026)",
            url: "https://www.zoningatlas.org/zoning-report-massachusetts-2026" },
    "09": { name: "Connecticut", status: "Zoning Report: Connecticut (forthcoming)", forthcoming: true }
  };

  // metro and city projects
  var places = [
    { name: "Metro Kansas City", ll: [39.0997, -94.5786],
      text: "Zoning Report: Metro Kansas City (2026) and the Kauffman Foundation-funded Kansas City Zoning Atlas.",
      url: "https://www.zoningatlas.org/zoning-report-metro-kansas-city-2026" },
    { name: "Atlanta", ll: [33.749, -84.388],
      text: "Where much of my research on housing, segregation, and zoning is set, including an op-ed with Sara Bronin on metro Atlanta zoning reform.",
      url: "https://www.ajc.com/opinion/2026/04/metro-atlanta-communities-must-reform-zoning-to-create-more-affordable-housing/",
      linkText: "Read the op-ed" }
  ];

  var map = L.map(el, { scrollWheelZoom: false, zoomSnap: 0.25 }).setView([38.5, -92], 4);
  var base = dark ? "World_Dark_Gray_Base" : "World_Light_Gray_Base";
  L.tileLayer("https://server.arcgisonline.com/ArcGIS/rest/services/Canvas/" + base + "/MapServer/tile/{z}/{y}/{x}", {
    maxZoom: 16,
    attribution: "Tiles &copy; Esri &mdash; Esri, DeLorme, NAVTEQ"
  }).addTo(map);

  function popup(title, body, url, linkText) {
    return "<b>" + title + "</b><br>" + body + (url ? '<br><a href="' + url + '" target="_blank" rel="noopener">' + (linkText || "Read the report") + ' &rarr;</a>' : "");
  }

  fetch("https://cdn.jsdelivr.net/npm/us-atlas@3.0.1/states-10m.json")
    .then(function (r) { return r.json(); })
    .then(function (us) {
      var all = topojson.feature(us, us.objects.states);
      var picked = all.features.filter(function (f) { return states[f.id]; });
      var layer = L.geoJSON({ type: "FeatureCollection", features: picked }, {
        style: function (f) {
          var s = states[f.id];
          return {
            color: accent, weight: 1.5,
            fillColor: accent, fillOpacity: s.forthcoming ? 0.12 : 0.35,
            dashArray: s.forthcoming ? "4 4" : null
          };
        },
        onEachFeature: function (f, lyr) {
          var s = states[f.id];
          lyr.bindPopup(popup(s.name, s.status + (s.note ? "<br><span style='opacity:.8'>" + s.note + "</span>" : ""), s.url));
        }
      }).addTo(map);
      var bounds = layer.getBounds();
      places.forEach(function (p) { bounds.extend(p.ll); });
      map.fitBounds(bounds, { padding: [24, 24] });
    })
    .catch(function () { /* state outlines are a nice-to-have; the points still show */ });

  places.forEach(function (p) {
    L.circleMarker(p.ll, { radius: 8, color: "#fff", weight: 2, fillColor: blue, fillOpacity: 1 })
      .bindPopup(popup(p.name, p.text, p.url, p.linkText))
      .addTo(map);
  });
})();
