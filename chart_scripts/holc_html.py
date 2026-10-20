# Builds the static HTML charts for Projects/HOLC.md from holc_numbers.json (see holc_calc.py).
# Usage: python holc_html.py <holc_numbers.json> <output folder>   -> writes c1.html, c2.html, c3.html
# c1 = grade/region 2x2, c2 = repair/mortgage/occupation, c3 = population groups. Paste each into its <figure>.
import json, sys
N = json.load(open(sys.argv[1]))
out = sys.argv[2]
G = "ABCD"
GN = {"A": "A &ldquo;Best&rdquo;", "B": "B &ldquo;Still desirable&rdquo;", "C": "C &ldquo;Declining&rdquo;", "D": "D &ldquo;Hazardous&rdquo;"}
REG = [("MW", "Midwest"), ("NE", "Northeast"), ("S", "South"), ("W", "West")]

def legend(items):
    return '<div class="hc-legend">' + "".join('<span><i class="%s"></i>%s</span>' % (c, t) for c, t in items) + "</div>"
grade_legend = legend([("g" + g.lower(), GN[g]) for g in G])

# ---------- 1. grouped columns, 2x2 ----------
summ = {(r["HOLC Grade"], r["Region"]): r for r in N["summ"]}
panels = [
    ("Black (%)", "Black residents", "%", 50, [0, 10, 20, 30, 40, 50], lambda v: v, lambda v: "%.1f%%" % v),
    ("Foreign Born (%)", "&ldquo;Foreign born&rdquo; residents", "%", 50, [0, 10, 20, 30, 40, 50], lambda v: v, lambda v: "%.1f%%" % v),
    ("Family Income Midpoint", "Family income midpoint", "$", 15000, [0, 5000, 10000, 15000], lambda v: v, lambda v: "$" + format(round(v, -1), ",.0f")),
    ("Building Age Midpoint", "Building age midpoint", "yrs", 40, [0, 10, 20, 30, 40], lambda v: v, lambda v: "%.0f years" % v),
]
def tick(t, unit):
    if unit == "$": return "$%dk" % (t // 1000) if t else "$0"
    return str(t)
h = ['<div class="hc" role="img" aria-label="Four grouped bar charts by region and HOLC grade. In every region, the Black share, the foreign-born share, and building age rise from grade A to grade D, and family income falls. Black shares of D neighborhoods are highest in the South, at about 48 percent; foreign-born shares of D neighborhoods are highest in the Northeast, at about 47 percent.">', grade_legend, '<div class="hc-grid2">']
for col, title, unit, mx, ticks, f, fmt in panels:
    h.append('<div class="hc-panel"><h4>%s</h4><div class="hc-cols">' % title)
    h.append('<div class="hc-yaxis">' + "".join('<i style="bottom:%.2f%%">%s</i>' % (100 * t / mx, tick(t, unit)) for t in ticks) + "</div>")
    h.append('<div class="hc-plot">' + "".join('<b style="bottom:%.2f%%"></b>' % (100 * t / mx) for t in ticks[1:]))
    for rc, rn in REG:
        h.append('<div class="hc-group">')
        for g in G:
            v = f(float(summ[(g, rc)][col]))
            h.append('<i class="g%s" style="height:%.2f%%" title="%s, grade %s: %s"></i>' % (g.lower(), min(100, 100 * v / mx), rn, g, fmt(v)))
        h.append("</div>")
    h.append("</div></div>")
    h.append('<div class="hc-xaxis">' + "".join("<span>%s</span>" % rn for _, rn in REG) + "</div></div>")
h.append("</div></div>")
open(out + "/c1.html", "w", encoding="utf-8").write("\n".join(h))

# ---------- 2. 100% stacked bars by grade, three panels ----------
ORD = ["o1", "o2", "o3", "o4", "o5", "o6"]
qual = [
    ("rep", "Home repair status", ["Good", "Fair-Good", "Fair", "Fair-Poor", "Poor", "Other_NA"], ["Good", "Fair&ndash;good", "Fair", "Fair&ndash;poor", "Poor", "No data"]),
    ("mort", "Mortgage availability", ["Good", "Fair-Good", "Fair", "Fair-Poor", "Poor", "Other_NA"], ["Ample", "Limited&ndash;ample", "Limited", "Limited&ndash;restricted", "Restricted", "No data"]),
    ("occ", "Occupation class", ["Upper", "Up_Mid", "Mid_Mix", "Low_Mid", "Lower", "Other_NA"], ["&ldquo;Upper&rdquo;", "Upper-middle", "Middle/mixed", "Lower-middle", "&ldquo;Lower&rdquo;", "No data"]),
]
def stack(vals, classes, names, label_min, prefix):
    s = []
    for v, c, n in zip(vals, classes, names):
        if v <= 0: continue
        lab = "%d" % round(v) if v >= label_min else ""
        s.append('<i class="%s" style="flex:%.2f" title="%s%s: %.1f%%">%s</i>' % (c, v, prefix, n, v, lab))
    return '<span class="hc-stack">' + "".join(s) + "</span>"
h = ['<div class="hc" role="img" aria-label="Three stacked bar charts of neighborhoods by HOLC grade. Grade A neighborhoods were overwhelmingly described as in good repair, with ample mortgage funds and upper-class residents; grade D neighborhoods were mostly described as in poor repair, with restricted mortgage funds and lower-class residents.">', '<div class="hc-grid3">']
for key, title, levels, names in qual:
    h.append('<div class="hc-panel"><h4>%s</h4>' % title)
    for g in G:
        vals = [N[key][g][l] for l in levels]
        h.append('<div class="hc-hrow"><span class="hc-lab">%s</span>%s</div>' % (g, stack(vals, ORD, names, 12, "Grade %s, " % g)))
    h.append('<div class="hc-hrow hc-ticks"><span></span><span>' + "".join('<i style="left:%d%%">%d</i>' % (t, t) for t in (0, 50, 100)) + "</span></div>")
    h.append(legend(list(zip(ORD, names))) + "</div>")
h.append("</div>")
h.append('<p class="hc-note">Bars show the share of each grade&rsquo;s neighborhoods (%), with the best category at left.</p></div>')
open(out + "/c2.html", "w", encoding="utf-8").write("\n".join(h))

# ---------- 3. population groups ----------
GRP = [("E. Asian/PI", "East Asian/Pacific Islander"), ("Black", "Black"), ('"Latin"', "&ldquo;Latin&rdquo;"), ("Greek", "Greek"),
       ("Italian", "Italian"), ("Polish", "Polish"), ("E. European", "Eastern European"), ("Irish", "Irish"), ("Jewish", "Jewish"),
       ("German", "German"), ("Nordic", "Nordic"), ("British", "British"), ("American", "&ldquo;American&rdquo;"),
       ("None", "No group noted"), ("Total", "All neighborhoods")]
h = ['<div class="hc hc-groups" role="img" aria-label="Stacked bar chart of the HOLC grades of neighborhoods where each population group is mentioned. 81 percent of neighborhoods with East Asian or Pacific Islander residents and 73 percent with Black residents were graded D, compared with 24 percent of all neighborhoods. Neighborhoods with British or American residents, or no group noted, were rarely graded D.">', grade_legend]
for key, name in GRP:
    r = N["grp"][key]
    cls = "hc-hrow" + (" hc-total" if key == "Total" else "") + (" hc-sep" if key == "None" else "")
    h.append('<div class="%s"><span class="hc-lab">%s <small>%s</small></span>%s</div>' % (
        cls, name, format(r["n"], ","), stack([r[g] for g in G], ["g" + g.lower() for g in G], ["grade " + g for g in G], 7, name.replace("&ldquo;", "").replace("&rdquo;", "") + ", ")))
h.append('<div class="hc-hrow hc-ticks"><span></span><span>' + "".join('<i style="left:%d%%">%d</i>' % (t, t) for t in (0, 25, 50, 75, 100)) + "</span></div>")
h.append('<p class="hc-note">Share of neighborhoods mentioning each group, by grade (%). Numbers after each group are neighborhoods.</p></div>')
open(out + "/c3.html", "w", encoding="utf-8").write("\n".join(h))
print("ok")
