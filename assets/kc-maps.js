// Kansas City tract maps on the zoning page, drawn with d3 from assets/data/kc_tracts.json.
// Each map is a <div data-kc-map="sf"> or <div data-kc-map="mls"> holding an <svg>.
// Colors match the HTML legends under each map. Tracts with no value draw as unzoned.
(function () {
  var maps = document.querySelectorAll("[data-kc-map]");
  if (!maps.length || !window.d3) return;

  var ramps = {
    sf:  { stops: ["#d5e3eb", "#9db8cd", "#5a87ac", "#1f618f", "#003a58"], label: "single-family only" },
    mls: { stops: ["#f8f5ea", "#b2ebbd", "#38ae69", "#00733b", "#004221"], label: "with 80,000+ sq ft minimum lots" }
  };
  var UNZONED = "#dcdcdc";

  d3.json("/assets/data/kc_tracts.json").then(function (geo) {
    maps.forEach(function (el) {
      var key = el.getAttribute("data-kc-map"), ramp = ramps[key];
      var color = d3.scaleLinear().domain([0, 25, 50, 75, 100]).range(ramp.stops).clamp(true);
      // frame the map on the tracts that have data, as the report maps do;
      // unzoned tracts around the edge still draw, clipped by the SVG frame
      var withData = { type: "FeatureCollection", features: geo.tracts.features.filter(function (d) { return d.properties[key] != null; }) };
      var W = 600, pad = 6;
      var proj = d3.geoMercator().fitWidth(W - 2 * pad, withData);
      var path = d3.geoPath(proj);
      var b = path.bounds(withData);
      proj.translate([proj.translate()[0] - b[0][0] + pad, proj.translate()[1] - b[0][1] + pad]);
      var H = Math.ceil(b[1][1] - b[0][1] + 2 * pad);
      var svg = d3.select(el).append("svg")
        .attr("viewBox", "0 0 " + W + " " + H)
        .attr("role", "img")
        .attr("aria-label", el.getAttribute("aria-label") || "");

      svg.append("g").selectAll("path").data(geo.tracts.features).join("path")
        .attr("class", "kc-tract")
        .attr("d", path)
        .attr("fill", function (d) { var v = d.properties[key]; return v == null ? UNZONED : color(v); })
        .append("title")
        .text(function (d) {
          var v = d.properties[key];
          return "Tract " + d.properties.g + ": " + (v == null ? "no zoned residential land" : Math.round(v) + "% " + ramp.label);
        });

      svg.append("g").selectAll("path").data(geo.counties.features).join("path")
        .attr("class", "kc-county").attr("d", path);
      // city outlines: a contrasting halo under the line keeps them visible on light and dark fills
      svg.append("g").selectAll("path").data(geo.cities.features).join("path")
        .attr("class", "kc-city-halo").attr("d", path);
      svg.append("g").selectAll("path").data(geo.cities.features).join("path")
        .attr("class", "kc-city").attr("d", path);
    });
  });
})();
