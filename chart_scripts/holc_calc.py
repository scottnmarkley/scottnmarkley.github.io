# Computes the numbers behind the HOLC charts from a local copy of https://github.com/snmarkley1/THOLCADS,
# following scripts/09_bar_graphs.R in that repo.
# Usage: python holc_calc.py <path to THOLCADS clone> <output folder>   -> writes holc_numbers.json
import csv, re, json, sys, zipfile, xml.etree.ElementTree as ET
src, outdir = sys.argv[1], sys.argv[2]
# --- Sum_Stats.xlsx (sheet 1), read without openpyxl
z = zipfile.ZipFile(src + "/DATA_DOWNLOAD/TABLES/Sum_Stats.xlsx")
ns = {"m": "http://schemas.openxmlformats.org/spreadsheetml/2006/main"}
ss = [ "".join(t.text or "" for t in si.iter("{%s}t" % ns["m"])) for si in ET.fromstring(z.read("xl/sharedStrings.xml")).findall("m:si", ns)] if "xl/sharedStrings.xml" in z.namelist() else []
sheet = ET.fromstring(z.read("xl/worksheets/sheet1.xml"))
rows = []
for r in sheet.iter("{%s}row" % ns["m"]):
    vals = []
    for c in r.findall("m:c", ns):
        v = c.find("m:v", ns)
        v = None if v is None else v.text
        if c.get("t") == "s": v = ss[int(v)]
        vals.append(v)
    rows.append(vals)
hdr = rows[0]
summ = [dict(zip(hdr, r)) for r in rows[1:]]

# --- ADS_FINAL.csv
df = [r for r in csv.DictReader(open(src + "/DATA_DOWNLOAD/TABLES/ADS_FINAL.csv", encoding="utf-8")) if r["HOLC_GRADE"] != "E" and r["HOLC_ID"] not in ("", "NA")]
G = "ABCD"
def dist(col, levels):
    out = {}
    for g in G:
        sub = [r for r in df if r["HOLC_GRADE"] == g]
        out[g] = {l: round(100 * sum(1 for r in sub if r[col] == l) / len(sub), 2) for l in levels}
        other = [r[col] for r in sub if r[col] not in levels]
        if other: print("unmatched", col, g, set(other))
    return out
lv = ["Good", "Fair-Good", "Fair", "Fair-Poor", "Poor", "Other_NA"]
rep = dist("REPAIR", lv); mort = dist("MORT_AV", lv)
occ = dist("OCC_CLASS", ["Upper", "Up_Mid", "Mid_Mix", "Low_Mid", "Lower", "Other_NA"])

def has(pat, s): return re.search(pat, s or "", re.I) is not None
def num(x):
    try: return float(x)
    except: return None
groups = {
 "E. Asian/PI": lambda r: has("orient|chine|jap|filip", r["FB_GROUP"]),
 "Black": lambda r: (num(r["P_BLACK"]) or 0) > 0,
 '"Latin"': lambda r: has("latin|mex|cuba|puerto", r["FB_GROUP"]),
 "Greek": lambda r: has("greek", r["FB_GROUP"]),
 "Italian": lambda r: has("italian", r["FB_GROUP"]),
 "Polish": lambda r: has("polish|pole", r["FB_GROUP"]),
 "E. European": lambda r: has("slav|slay|hungar|russian|eastern euro|czec|bohem|yugo|slove|slova|croat|lithu", r["FB_GROUP"]),
 "Irish": lambda r: has("irish", r["FB_GROUP"]),
 "Jewish": lambda r: has("jew", r["FB_GROUP"]),
 "German": lambda r: has("german", r["FB_GROUP"]),
 "Nordic": lambda r: has("nord|norw|swed|finn|danish|dane", r["FB_GROUP"]),
 "British": lambda r: has("brit|english|welsh|scot", r["FB_GROUP"]),
 "American": lambda r: has("american", r["FB_GROUP"]) and not has("mex|latin|jew|german|native", r["FB_GROUP"]),
 "None": lambda r: num(r["P_FB"]) == 0 and num(r["P_BLACK"]) == 0,
 "Total": lambda r: True,
}
grp = {}
for name, f in groups.items():
    hits = [r for r in df if f(r)]
    grp[name] = {"n": len(hits), **{g: round(100 * sum(1 for r in hits if r["HOLC_GRADE"] == g) / len(hits), 2) for g in G}}
json.dump({"summ": summ, "rep": rep, "mort": mort, "occ": occ, "grp": grp}, open(outdir + "/holc_numbers.json", "w"), indent=1)
