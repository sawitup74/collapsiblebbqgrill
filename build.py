"""collapsiblebbqgrill.com build. Run: python3 build.py
To switch on visit counting, replace collapsiblebbqgrill in GOATCOUNTER below with the real GoatCounter code, then rebuild."""
GOATCOUNTER = "https://collapsiblebbqgrill.goatcounter.com/count"
DOMAIN = "https://collapsiblebbqgrill.com"
UTM_SOURCE = "collapsiblebbqgrill"
SITE_NAME = "Collapsible BBQ Grill"
LASTMOD = "2026-10-31"
THEME_COLOR = "#1f2a36"
HOME_IMG = "both16"
HOME_TITLE = "Collapsible BBQ Grill: Flat Pack Charcoal Grill Guides, Setup & Recipes"
HOME_DESC = "How collapsible flat pack charcoal grills work, how to set one up, season it, cook on it and pack it away, with recipes and honest sizing advice."
BRAND_HTML = '<span class="mark" aria-hidden="true"><i></i><i></i><i></i></span><span class="wm">collapsible<b>bbq</b>grill</span>'
FOOTER_BLURB = "<b>Collapsible BBQ Grill</b> is a guide site about flat pack charcoal grills: how they go together, how to run a fire in one, and how to care for raw carbon steel. It is published by Slot Grill, and every guide is written around the Slot Grill Compact and Full Size."
NOTE = "Specs and prices on this site come from SlotGrill.com. Grill outdoors only, on a stable, level, non-combustible surface, and follow local fire rules and burn bans."
CATS = {
 "basics": ("how-collapsible-grills-work", "How Collapsible Grills Work", "Tab-and-slot construction, carbon steel, steel gauge, airflow and what separates a flat pack grill from other portable charcoal grills.", "How they work"),
 "setup": ("setup-and-fire", "Setup &amp; Fire", "Putting a flat pack grill together, lighting it, building heat zones, feeding the fire and cooking on grates, griddle plates and cast iron.", "Setup &amp; fire"),
 "recipes": ("recipes", "Recipes", "Recipes written for the cooking area of a collapsible grill, with fire setup, timing and safe internal temperatures.", "Recipes"),
 "care": ("care-and-storage", "Care &amp; Storage", "Seasoning, cleaning, rust, ash and packing a carbon steel grill flat for the shelf or the trunk.", "Care"),
 "choosing": ("choosing-a-collapsible-grill", "Choosing a Collapsible Grill", "Who a collapsible charcoal grill suits, what to look for, how to size one and how the two Slot Grills compare.", "Choosing"),
 "about": ("about-this-site", "About &amp; Reference", "About this site, Slot Grill, the glossary and the full FAQ.", "About"),
}
NAV_CATS = ["basics", "setup", "recipes", "care", "choosing"]
FAVICON = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="12" fill="#1f2a36"/><path d="M12 22h40M12 32h40M12 42h40" stroke="#d7894a" stroke-width="5" stroke-linecap="round"/><path d="M20 50l12-8 12 8" stroke="#e9eef3" stroke-width="4" fill="none" stroke-linecap="round"/></svg>'
CSS = """
:root{--slate:#1f2a36;--slate2:#2c3a4a;--steel:#5b6b7c;--copper:#c96f32;--copper2:#d7894a;--bg:#f2f4f6;--card:#fff;--ink:#17202a;--mute:#5a6673;--line:#d9dfe5}
*{box-sizing:border-box}html{-webkit-text-size-adjust:100%}
body{margin:0;font:17px/1.7 'Avenir Next',Avenir,'Segoe UI',Helvetica,Arial,sans-serif;color:var(--ink);background:var(--bg)}
h1,h2,h3{font-family:'Avenir Next Condensed','Arial Narrow','Segoe UI',Helvetica,sans-serif;font-weight:700;letter-spacing:-.01em;line-height:1.15}
a{color:var(--copper)}img{max-width:100%;height:auto;display:block}
.top{background:var(--slate);position:sticky;top:0;z-index:9;box-shadow:0 2px 0 var(--copper)}
.nav{max-width:1120px;margin:auto;display:flex;align-items:center;gap:1.2rem;padding:.65rem 1rem}
.brand{display:flex;align-items:center;gap:.55rem;text-decoration:none;color:#e9eef3}
.mark{display:inline-flex;flex-direction:column;gap:3px}.mark i{display:block;width:22px;height:4px;background:var(--copper2);border-radius:2px}.mark i:nth-child(2){width:16px;background:#e9eef3}
.wm{font-weight:600;font-size:1.05rem;letter-spacing:.01em}.wm b{color:var(--copper2);font-weight:800}
.nav nav{flex:1;display:flex;gap:1.1rem;justify-content:flex-end}.nav nav a{color:#c5cfd8;text-decoration:none;font-size:.93rem}.nav nav a:hover{color:#fff}
.btn{display:inline-block;background:var(--copper);color:#fff!important;text-decoration:none;font-weight:700;padding:.75rem 1.15rem;border-radius:4px;letter-spacing:.02em}
.btn:hover{background:#b35f27}.btn.small{padding:.45rem .8rem;font-size:.88rem}.btn.ghost{background:transparent;border:2px solid var(--copper);color:var(--copper)!important}
main{max-width:780px;margin:auto;padding:1.2rem 1rem 2rem}main.wide{max-width:1120px}
.crumbs{font-size:.83rem;color:var(--mute)}.crumbs a{color:var(--mute)}
h1{font-size:clamp(1.9rem,4.4vw,2.7rem);margin:.4rem 0 .6rem}h2{margin-top:2.3rem;font-size:1.55rem;border-top:1px solid var(--line);padding-top:1.4rem}
.lede{font-size:1.12rem;color:var(--mute)}
.hero-img{border-radius:4px;margin:1rem 0 1.4rem;aspect-ratio:16/9;object-fit:cover;width:100%}
.facts{display:flex;flex-wrap:wrap;gap:.5rem 1.4rem;background:var(--card);border:1px solid var(--line);border-left:4px solid var(--copper);padding:.7rem 1rem;margin:1rem 0}
.tbl{overflow-x:auto;margin:1rem 0}table{border-collapse:collapse;width:100%;background:var(--card);font-size:.94rem}th,td{border:1px solid var(--line);padding:.55rem .65rem;text-align:left;vertical-align:top}th{background:var(--slate);color:#fff;font-weight:600}
.note{background:#fbf1e8;border:1px solid #efcfb4;border-radius:4px;padding:.8rem 1rem}
details{background:var(--card);border:1px solid var(--line);border-radius:4px;margin:.5rem 0;padding:.6rem .9rem}summary{cursor:pointer;font-weight:700}
.product{display:grid;grid-template-columns:190px 1fr;gap:1.2rem;align-items:center;background:var(--card);border:1px solid var(--line);border-top:4px solid var(--slate);border-radius:4px;padding:1.1rem;margin:2rem 0}
.product img{border-radius:3px;aspect-ratio:1;object-fit:cover}.product h3{margin:.1rem 0 .3rem;font-size:1.3rem}.kicker{text-transform:uppercase;letter-spacing:.14em;font-size:.72rem;color:var(--copper);font-weight:800;margin:0}
.price{font-weight:800;font-size:1.25rem}.price s{color:var(--mute);font-weight:400;font-size:.95rem;margin-left:.5rem}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:1rem}
.card{background:var(--card);border:1px solid var(--line);border-radius:4px;text-decoration:none;color:var(--ink);overflow:hidden;transition:transform .15s}.card:hover{transform:translateY(-3px);border-color:var(--copper)}
.card img{aspect-ratio:3/2;object-fit:cover;width:100%}.card div{padding:.8rem .95rem}.card h3{margin:0 0 .3rem;font-size:1.08rem}.card p{margin:0;font-size:.9rem;color:var(--mute)}
.hero{background:linear-gradient(120deg,var(--slate) 0%,var(--slate2) 60%,#3b4d61 100%);color:#e9eef3;border-radius:6px;display:grid;grid-template-columns:1.1fr 1fr;gap:2rem;align-items:center;padding:2.2rem;margin:.5rem 0 1rem}
.hero h1{color:#fff;font-size:clamp(2rem,4.8vw,3.1rem)}.hero p{color:#c5cfd8}.hero img{border-radius:4px}.hero .kicker{color:var(--copper2)}
.hsec h2 a{color:inherit;text-decoration:none}.related ul{columns:2;gap:2rem}
footer{background:var(--slate);color:#a9b5c1;padding:2.2rem 1rem;margin-top:3rem;font-size:.9rem}footer .in{max-width:1120px;margin:auto}footer a{color:#e3e9ee}.fbrand{margin-bottom:.6rem}.fbrand .wm{color:#e9eef3}
.small-note{font-size:.85rem;color:var(--mute)}
@media(max-width:780px){.nav nav{display:none}.nav{justify-content:space-between}.hero{grid-template-columns:1fr;padding:1.4rem}.product{grid-template-columns:1fr}.related ul{columns:1}body{font-size:16.5px}}
"""
# ---------------- engine (shared by all guide sites; config is at the top of this file) ----------------
import json, html, os, sys, re, glob


# --- Search Console schema helpers ---
# Guide sites do not sell products and have no reviews. Do not emit Product
# JSON-LD (Search Console flags missing aggregateRating/review). Use Brand.
def product_schema_compact(valid_from="2026-11-04"):
    return {"@type":"Brand","name":"Slot Grill","url":"https://slotgrill.com/"}
def product_schema_aggregate(valid_from="2026-11-04"):
    return {"@type":"Brand","name":"Slot Grill","url":"https://slotgrill.com/"}
# --- end schema helpers ---
SG = "https://slotgrill.com"
UTM = "utm_source=%s&amp;utm_medium=referral&amp;utm_campaign=guide-site" % UTM_SOURCE
def sg(path=""):
    return SG + path + ("&amp;" if "?" in path else "?") + UTM
COMPACT = sg("/products/slot-grill-compact-carbon-steel-free-shipping")
FULL = sg("/products/slot-grill-carbon-steel-collapsible-bbq-grill")
GRID = sg("/products/slot-grill-griddle-plancha")
BALM = sg("/products/seasoning-balm-for-slot-grill")
THERMO = sg("/products/slot-grill-instant-read-digital-meat-thermometer")
BUNDLE = sg("/products/seasoning-balm-meat-thermometer-bundle")
SHOP = sg("/collections/all")
SPECS = sg("/pages/slot-grill-specs-setup-care")
ABOUTSG = sg("/pages/about-slot-grill")
MADE = sg("/pages/made-in-usa")
SGFAQ = sg("/pages/faq-frequently-asked-questions")
CONTACT = sg("/pages/contact")
HOME = sg("/")
CDN = "https://cdn.shopify.com/s/files/1/0721/8833/0172/files/"
IMG = {k: CDN + v for k, v in dict(
    c07="compact-07.jpg?v=1792382833", c28="compact-28.jpg?v=1792382861", c08="compact-08.jpg?v=1792382834",
    c13="compact-13.jpg?v=1792382834", both16="both-16.jpg?v=1792382825", both02="both-02.jpg?v=1792382824",
    full01="full-size-01.jpg?v=1792382862", full08="full-size-08.jpg?v=1792382863", full10="full-size-10.jpg?v=1792382864",
    full13="full-size-13.jpg?v=1792382866", grid1="griddle-add-on.jpg?v=1793024225", grid2="griddle-add-on-two.jpg?v=1793024983",
    balm="seasoning-balm-main.jpg?v=1791978819", thermo="thermometer-red-clean.jpg?v=1791939312",
    bundle="balm-thermometer-bundle-v3.jpg?v=1791943793").items()}
# Product facts below are copied from slotgrill.com product and specs pages (checked 2026-10-31).
PRODUCTS = {
 "compact": dict(name="Slot Grill Compact", url=COMPACT, img="c07", alt="Slot Grill Compact carbon steel charcoal grill",
    facts='12-gauge carbon steel · about 14 lb · 16.25" × 9" cooking area · packs about 1" thick · made in the USA (Texas)',
    price="$89.97", was="$99.97", btn="See the Compact at SlotGrill.com"),
 "full": dict(name="Slot Grill Full Size", url=FULL, img="full01", alt="Slot Grill Full Size carbon steel charcoal grill",
    facts='10-gauge carbon steel · about 27.6 lb · 20.5" × 11.25" cooking area · packs about 1.25" thick · made in the USA (Texas)',
    price="$149.97", was="$159.97", btn="See the Full Size at SlotGrill.com"),
 "griddle": dict(name="Slot Grill Griddle Add-On", url=GRID, img="grid1", alt="Slot Grill griddle plancha add-on plates",
    facts="Carbon steel flat-top plates made for the Slot Grill two-piece top. One or two plates, for the Compact or the Full Size. Stacks flat with the grill. Grill not included.",
    price="from $20.00", was="", btn="See the griddle at SlotGrill.com"),
}
PAGES = []
def page(slug, title, desc, img, body, cat, faq=None):
    global PAGES
    PAGES = [p for p in PAGES if p[0] != slug]
    PAGES.append((slug, title, desc, img, body, cat, faq or []))
def esc(s): return html.escape(s, quote=True)
def L(slug, text): return '<a href="/%s.html">%s</a>' % (slug, text)
def X(url, text): return '<a href="%s">%s</a>' % (url, text)
def ul(items): return "<ul>" + "".join("<li>%s</li>" % i for i in items) + "</ul>"
def ol(items): return "<ol>" + "".join("<li>%s</li>" % i for i in items) + "</ol>"
def table(head, rows):
    return '<div class="tbl"><table><tr>' + "".join("<th>%s</th>" % h for h in head) + "</tr>" + "".join(
        "<tr>" + "".join("<td>%s</td>" % c for c in r) + "</tr>" for r in rows) + "</table></div>"
def tip(t): return '<p class="note">%s</p>' % t
TEMPS_ROWS = [("Beef, pork, lamb and veal steaks, chops and roasts", "145°F, then rest 3 minutes"),
    ("Ground beef, pork, lamb and veal (burgers, fresh sausage)", "160°F"),
    ("Chicken and turkey, whole, pieces or ground", "165°F"),
    ("Fish and shellfish", "145°F, or flesh opaque and flakes with a fork"),
    ("Egg dishes", "160°F; cook eggs until yolks and whites are firm"),
    ("Precooked sausage, hot dogs and leftovers", "Reheat to 165°F")]
def temps():
    return ("<h2>Safe internal temperatures</h2><p>Check the thickest part with an instant-read thermometer, away from bone. These are USDA minimum safe temperatures; tougher cuts like brisket and ribs are cooked well past them for tenderness.</p>"
            + table(["Food", "Minimum internal temperature"], TEMPS_ROWS))
def recipe(intro, serves, time, ingr, steps, tips=None, extra="", size="compact"):
    p = PRODUCTS[size]
    h = intro + '<div class="facts"><span><b>Serves</b> %s</span><span><b>Time</b> %s</span><span><b>Grill</b> <a href="%s">%s</a></span></div>' % (serves, time, p["url"], p["name"])
    h += "<h2>Ingredients</h2>" + ul(ingr) + "<h2>Method</h2>" + ol(steps) + extra
    if tips: h += "<h2>Tips</h2>" + ul(tips)
    return h + temps()
def faqld(faq):
    if not faq: return ""
    return '<script type="application/ld+json">' + json.dumps({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": html.unescape(re.sub("<[^>]+>", "", q)), "acceptedAnswer": {"@type": "Answer", "text": html.unescape(re.sub("<[^>]+>", "", a))}} for q, a in faq]}) + "</script>"
def faqhtml(faq, h="Questions people ask"):
    return ("<h2>%s</h2>" % h + "".join('<details><summary>%s</summary><p>%s</p></details>' % (q, a) for q, a in faq)) if faq else ""
def productbox(kind="compact"):
    p = PRODUCTS[kind]
    was = "<s>%s</s>" % p["was"] if p["was"] else ""
    return ('<aside class="product"><img src="%s" alt="%s" loading="lazy"><div><p class="kicker">From the maker in Buna, Texas</p><h3>%s</h3><p>%s</p><p class="price">%s%s</p><a class="btn" href="%s">%s</a></div></aside>'
            % (IMG[p["img"]], esc(p["alt"]), p["name"], p["facts"], p["price"], was, p["url"], p["btn"]))
def crumbs(items):
    return '<p class="crumbs">' + " › ".join(('<a href="%s">%s</a>' % (u, t)) if u else t for t, u in items) + "</p>"
def shell(title, desc, slug, inner, img=None, faq=None, kind="Article", trail=None, wide=False):
    canon = DOMAIN + ("/" if slug == "index" else "/%s.html" % slug)
    img = img or IMG["c07"]
    ld = [{"@context": "https://schema.org", "@type": "WebSite" if slug == "index" else kind, "name": html.unescape(title),
           "url": canon, "description": html.unescape(desc), "image": img,
           "publisher": {"@type": "Organization", "name": SITE_NAME, "url": DOMAIN + "/"},
           "about": product_schema_aggregate()}]
    if kind == "Article" and slug != "index": ld[0]["headline"] = html.unescape(title)
    if trail:
        ld.append({"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": html.unescape(re.sub("<[^>]+>", "", t)), "item": DOMAIN + (u if u else "/%s.html" % slug)} for i, (t, u) in enumerate(trail)]})
    lds = "".join('<script type="application/ld+json">%s</script>' % json.dumps(x) for x in ld)
    nav = "".join('<a href="/%s.html">%s</a>' % (CATS[k][0], CATS[k][3]) for k in NAV_CATS) + '<a href="/faq.html">FAQ</a>'
    foot = " · ".join('<a href="/%s.html">%s</a>' % (c[0], c[1]) for c in CATS.values()) + ' · <a href="/faq.html">FAQ</a> · <a href="/glossary.html">Glossary</a> · <a href="/about.html">About</a> · <a href="/compact-vs-full-size-slot-grill.html">Compact vs Full Size</a>'
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(html.unescape(title))}</title><meta name="description" content="{esc(html.unescape(desc))}"><link rel="canonical" href="{canon}">
<meta property="og:type" content="{'website' if slug=='index' else 'article'}"><meta property="og:site_name" content="{SITE_NAME}"><meta property="og:title" content="{esc(html.unescape(title))}"><meta property="og:description" content="{esc(html.unescape(desc))}"><meta property="og:url" content="{canon}"><meta property="og:image" content="{img}">
<meta name="theme-color" content="{THEME_COLOR}"><link rel="icon" href="/favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="/style.css">{lds}{faqld(faq)}</head><body>
<header class="top"><div class="nav"><a class="brand" href="/" aria-label="{SITE_NAME} home">{BRAND_HTML}</a><nav>{nav}</nav><a class="btn small" href="{HOME}">SlotGrill.com</a></div></header>
<main class="{'wide' if wide else ''}">{inner}</main>
<footer><div class="in"><div class="fbrand">{BRAND_HTML}</div><p>{FOOTER_BLURB}</p><p>Slot Grill is a collapsible carbon steel charcoal grill made in the USA by Keith in Buna, Texas. Slot Grill® is a registered trademark. Genuine Slot Grills are sold at <a href="{HOME}">SlotGrill.com</a>, the @SlotGrill TikTok Shop and @SlotGrill on the Shop app. Questions about an order or the grill? Use the <a href="{CONTACT}">Slot Grill contact form</a>.</p><p class="flinks"><a href="/">Home</a> · {foot}</p></div></footer>
<script data-goatcounter="{GOATCOUNTER}" async src="//gc.zgo.at/count.js"></script><script>document.addEventListener("click",function(e){{var a=e.target.closest&&e.target.closest('a[href*="//slotgrill.com"]');if(a&&window.goatcounter&&window.goatcounter.count){{window.goatcounter.count({{path:"click-to-slotgrill/"+location.pathname,title:"Click to slotgrill.com",event:true}})}}}});</script></body></html>
'''
def related(slug, cat):
    rel = [p for p in PAGES if p[5] == cat and p[0] != slug][:8]
    if not rel: return ""
    c = CATS[cat]
    return '<nav class="related"><h2>More in %s</h2><ul>' % c[1] + "".join('<li><a href="/%s.html">%s</a></li>' % (p[0], p[1]) for p in rel) + '</ul><p><a href="/%s.html">All %s →</a></p></nav>' % (c[0], c[1])
def article(slug, title, desc, img, body, cat, faq):
    c = CATS[cat]
    wc = lambda b: len(re.sub("<[^>]+>", " ", b).split())
    for blk in globals().get("EXTRA", {}).get(cat, []):
        if wc(body) >= 520: break
        if blk[:60] not in body: body += blk
    trail = [("Home", "/"), (c[1], "/%s.html" % c[0]), (title, None)]
    kind = "big" if "full" in img else "compact"
    box = productbox("full" if kind == "big" else "compact")
    if "griddle" in body.lower() and cat != "about": box += productbox("griddle")
    inner = (crumbs(trail) + '<article><h1>%s</h1><p class="lede">%s</p><img class="hero-img" src="%s" alt="%s">' % (title, desc, IMG[img], esc(html.unescape(title)) + " – Slot Grill")
             + body + (faqhtml(faq) if slug != "faq" else "") + "</article>" + box + related(slug, cat) + '<p class="small-note">%s</p>' % NOTE)
    return shell(title, desc, slug, inner, img=IMG[img], faq=faq, trail=trail)
def cardgrid(ps):
    return '<div class="grid">' + "".join('<a class="card" href="/%s.html"><img src="%s" alt="" loading="lazy"><div><h3>%s</h3><p>%s</p></div></a>' % (s, IMG[i], t, d) for s, t, d, i, *_ in ps) + "</div>"
REDIRECTS = {"flat-pack-vs-folding-vs-fixed-grills": "flat-pack-vs-hinged-vs-fixed-grills"}
def build():
    open("style.css", "w").write(CSS)
    open("favicon.svg", "w").write(FAVICON)
    open("CNAME", "w").write(DOMAIN.split("//")[1] + "\n")
    for f in sorted(glob.glob("content_*.py")): exec(open(f).read(), globals())
    # FAQ page aggregates every page's questions
    allq = [(q, a, p) for p in PAGES for q, a in p[6] if p[0] != "faq"]
    base = [p for p in PAGES if p[0] == "faq"]
    if base:
        b = base[0]
        body = b[4] + "".join('<h2>%s</h2>' % CATS[k][1] + "".join('<details><summary>%s</summary><p>%s <a href="/%s.html">Read: %s</a></p></details>' % (q, a, p[0], p[1]) for q, a, p in allq if p[5] == k) for k in CATS)
        page("faq", b[1], b[2], b[3], body, b[5], b[6])
    for f in glob.glob("*.html"): os.remove(f)
    for p in PAGES: open(p[0] + ".html", "w").write(article(*p))
    for k, c in CATS.items():
        ps = [p for p in PAGES if p[5] == k]
        trail = [("Home", "/"), (c[1], None)]
        open(c[0] + ".html", "w").write(shell(c[1] + " | " + SITE_NAME, c[2], c[0], crumbs(trail) + "<h1>%s</h1><p class=\"lede\">%s</p>" % (c[1], c[2]) + cardgrid(ps) + productbox(), kind="CollectionPage", trail=trail, wide=True))
    for o, n in REDIRECTS.items():
        open(o + ".html", "w").write('<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><title>Moved</title><link rel="canonical" href="%s/%s.html"><meta name="robots" content="noindex"><meta http-equiv="refresh" content="0; url=/%s.html"></head><body><p>This page moved to <a href="/%s.html">/%s.html</a>.</p></body></html>' % (DOMAIN, n, n, n, n))
    open("index.html", "w").write(shell(HOME_TITLE, HOME_DESC, "index", home_html(), img=IMG[HOME_IMG], wide=True))
    open("404.html", "w").write(shell("Page not found | " + SITE_NAME, "That page isn't here. Browse the guides instead.", "404",
        "<h1>That page isn't here</h1><p>The link may be old or mistyped. Try one of these:</p>" + ul(['<a href="/">Home</a>'] + ['<a href="/%s.html">%s</a>' % (c[0], c[1]) for c in CATS.values()] + ['<a href="/faq.html">FAQ</a>']), kind="WebPage"))
    urls = [DOMAIN + "/"] + ["%s/%s.html" % (DOMAIN, c[0]) for c in CATS.values()] + ["%s/%s.html" % (DOMAIN, p[0]) for p in PAGES]
    open("sitemap.xml", "w").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join("  <url><loc>%s</loc><lastmod>%s</lastmod></url>\n" % (u, LASTMOD) for u in urls) + "</urlset>\n")
    open("robots.txt", "w").write("User-agent: *\nAllow: /\nSitemap: %s/sitemap.xml\n" % DOMAIN)
    print(len(PAGES), "articles +", len(CATS), "hubs + home")
def home_html():
    secs = "".join('<section class="hsec"><h2><a href="/%s.html">%s</a></h2><p>%s</p>%s</section>' % (c[0], c[1], c[2], cardgrid([p for p in PAGES if p[5] == k][:6])) for k, c in CATS.items())
    return HOME_HERO + secs + '<section class="hsec"><h2>The two Slot Grills, side by side</h2><p>Both are tab-and-slot, carbon steel, made in Texas. ' + L("compact-vs-full-size-slot-grill", "Full comparison →") + "</p>" + productbox("compact") + productbox("full") + "</section>"
if __name__ == "__main__":
    build()

# Indexing post-process (2026-11-09): 404 noindex, redirect stubs without noindex, real sitemap lastmod
import subprocess as _sp, sys as _sys
_sp.run([_sys.executable, "postfix_indexing.py"])
