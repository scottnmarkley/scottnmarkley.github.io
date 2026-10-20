# Cumulative residents displaced by apartment demolitions, by year and group, as static HTML columns,
# for the figure on Projects/suburbs.md.
# Usage: python sub_html.py ../assets/data/atl_demolitions.json <output folder>   -> writes c4.html
import json, sys
d = json.load(open(sys.argv[1]))["sites"]
out = sys.argv[2]
GR = [("Hispanic", "Hispanic", "dh"), ("Black", "Black", "db"), ("White", "White", "dw"), ("Asian & P.I.", "Asian &amp; P.I.", "da"), ("Other", "Other", "do")]
years = list(range(2010, 2018))
cum = {y: {k: sum(s["race"][k] for s in d if s["year"] <= y) for k, _, _ in GR} for y in years}
tot = {y: sum(cum[y].values()) for y in years}
T = tot[2017]
mx = 10000
h = ['<div class="hc dc" role="img" aria-label="Stacked column chart of the cumulative number of residents displaced by apartment demolitions, 2010 to 2017, by race and ethnicity. The total reaches %s by 2017, %d percent of them Hispanic and %d percent Black.">' % (format(T, ","), round(100 * cum[2017]["Hispanic"] / T), round(100 * cum[2017]["Black"] / T)),
     '<div class="hc-legend">' + "".join('<span><i class="%s"></i>%s</span>' % (c, n) for _, n, c in GR) + "</div>",
     '<div class="hc-cols dc-cols">',
     '<div class="hc-yaxis">' + "".join('<i style="bottom:%d%%">%s</i>' % (t / 100, format(t, ",")) for t in range(0, mx + 1, 2500)) + "</div>",
     '<div class="hc-plot">' + "".join('<b style="bottom:%d%%"></b>' % (t / 100) for t in range(2500, mx + 1, 2500))]
for y in years:
    segs = "".join('<i class="%s" style="height:%.2f%%" title="%d, %s: %s"></i>' % (c, 100 * cum[y][k] / mx, y, n.replace("&amp;", "&"), format(cum[y][k], ",")) for k, n, c in reversed(GR) if cum[y][k] > 0)
    h.append('<div class="dc-col"><span class="dc-val" style="bottom:%.2f%%">%s</span>%s</div>' % (100 * tot[y] / mx, format(tot[y], ","), segs))
h.append("</div></div>")
h.append('<div class="hc-xaxis dc-x">' + "".join("<span>%d</span>" % y for y in years) + "</div>")
h.append('<p class="hc-note">Cumulative residents of demolished complexes, estimated from 2010 census data.</p></div>')
open(out + "/c4.html", "w", encoding="utf-8").write("\n".join(h))
