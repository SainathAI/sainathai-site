# generate_site.py
import os, shutil, json, datetime
from pathlib import Path

ROOT = Path('.').resolve()
ASSETS = ROOT / 'assets'
OUT = ROOT

# Basic site config
SITE = {
  "title":"SainathAI",
  "brand":"SainathAI",
  "name":"Sainath Phani VV",
  "email":"enquiry@sainathai.com",
  "whatsapp":"+917075103333",
  "description":"AI Automation, SEO & Growth systems for revenue scale",
  "url":"https://www.sainathai.com"
}

# Ensure folders
(OUT / 'services').mkdir(exist_ok=True)
(OUT / 'blog').mkdir(exist_ok=True)

# HTML template (simple, responsive, SEO-ready)
BASE_TEMPLATE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{meta_title}</title>
<meta name="description" content="{meta_desc}">
<link rel="icon" href="/assets/favicon.png">
<meta property="og:title" content="{meta_title}">
<meta property="og:description" content="{meta_desc}">
<meta property="og:type" content="website">
<meta property="og:url" content="{page_url}">
<script type="application/ld+json">{jsonld}</script>
<style>
:root{{--accent:#1A73E8;--bg:#0b0b0b;--muted:#9aa;}}
body{{margin:0;font-family:Inter,system-ui,Arial;background:var(--bg);color:#eee;}}
.container{{max-width:1100px;margin:40px auto;padding:30px;}}
.header{{display:flex;align-items:center;gap:20px}}
.logo{{font-weight:700;font-size:28px;color:var(--accent)}}
.cta{{background:var(--accent);color:#fff;padding:10px 14px;border-radius:8px;text-decoration:none}}
.card{{background:rgba(255,255,255,0.03);padding:18px;border-radius:12px;margin:18px 0}}
a{{color:var(--accent)}}
footer{{margin-top:60px;color:var(--muted)}}
img.founder{{max-width:220px;border-radius:8px;box-shadow:0 8px 30px rgba(0,0,0,0.6)}}
</style>
</head>
<body>
<div class="container">
  <header class="header">
    <div class="logo">{brand}</div>
    <nav style="margin-left:auto"><a class="cta" href="/lead.html">Get 72-hour Growth System</a></nav>
  </header>

  <main>
    <h1 style="margin-top:24px">{page_h1}</h1>
    <div class="card">{content}</div>
  </main>

  <footer>
    <p>Founder — {name} • <a href="/contact.html">Contact</a></p>
    <p>© {year} {brand}</p>
  </footer>
</div>
</body>
</html>"""

# JSON-LD helpers
def org_schema(site):
    return {
      "@context":"https://schema.org",
      "@type":"Organization",
      "name": site["brand"],
      "url": site["url"],
      "email": site["email"]
    }

# create homepage
home_content = f"""
<p style="font-size:18px">{SITE['description']}</p>
<p><strong>Offer:</strong> 72-hour AI Growth System — Lead magnet, audit and automated funnel.</p>
<p><a class='cta' href='/lead.html'>Download free blueprint</a></p>
"""

with open(OUT / 'index.html','w',encoding='utf8') as f:
    jsonld = json.dumps(org_schema(SITE))
    f.write(BASE_TEMPLATE.format(
      meta_title=f"{SITE['brand']} — AI Automation & Revenue Systems",
      meta_desc=SITE['description'],
      page_url=SITE['url'],
      jsonld=jsonld,
      brand=SITE['brand'],
      page_h1="AI Automation • SEO • Revenue Systems",
      content=home_content,
      name=SITE['name'],
      year=datetime.date.today().year
    ))

# create founder / contact page
founder_html = f"""
<div style='display:flex;gap:24px;align-items:flex-start'>
  <div><img class='founder' src='/assets/founder.png' alt='Founder photo'></div>
  <div>
    <h2>{SITE['name']}</h2>
    <p>15+ years IT industry experience. Consultant to Wipro, Polaris, Microsoft, HSBC. Expert in Healthcare & Banking domain systems.</p>
    <p><a href='/services/ai-automation.html'>AI Automation</a> • <a href='/services/seo-growth-systems.html'>SEO Growth</a></p>
    <p>WhatsApp: <a href='https://wa.me/{SITE['whatsapp'].replace('+','')}' id='wa'>{SITE['whatsapp']}</a></p>
    <p>Email: <a href='mailto:{SITE['email']}'>{SITE['email']}</a></p>
  </div>
</div>
"""
with open(OUT / 'about.html','w',encoding='utf8') as f:
    f.write(BASE_TEMPLATE.format(
      meta_title=f"{SITE['name']} — Founder, {SITE['brand']}",
      meta_desc=f"{SITE['name']} — founder profile and experience",
      page_url=SITE['url'] + '/about.html',
      jsonld=json.dumps({"@context":"https://schema.org","@type":"Person","name":SITE['name']}),
      brand=SITE['brand'],
      page_h1="Founder — " + SITE['name'],
      content=founder_html,
      name=SITE['name'],
      year=datetime.date.today().year
    ))

# services list (12)
services = [
  ("ai-automation","AI Automation","Scale client operations with AI workflows and automation"),
  ("business-automation","Business Automation","Automate revenue operations"),
  ("seo-growth-systems","SEO Growth Systems","Technical & content SEO that converts"),
  ("content-engine","Content Engine","Automate high-ROI content production"),
  ("funnels-landing-pages","Funnels & Landing Pages","Conversion-first funnels"),
  ("paid-ads-ai","Paid Ads + AI","Automated ad creation and bidding"),
  ("digital-products","Digital Products","Create subscription products & info-products"),
  ("whatsapp-automation","WhatsApp Automation","Lead capture, sequences and bot flows"),
  ("ecommerce-automation","Ecommerce Automation","Catalog, orders, fulfillment automation"),
  ("agency-automation","Agency Automation","Scale agency delivery with scripts & templates"),
  ("data-analytics-ai","Data Analytics + AI","Actionable dashboards & forecasting"),
  ("trading-automation","Trading Automation","Algorithmic trading workflows")
]

for slug, title, desc in services:
    content = f"<p>{desc}</p><p><strong>Benefits:</strong><ul><li>Rapid ROI</li><li>Repeatable system</li></ul></p><p><a class='cta' href='/lead.html'>Get audit</a></p>"
    with open(OUT / 'services' / f"{slug}.html",'w',encoding='utf8') as f:
        f.write(BASE_TEMPLATE.format(
          meta_title=f"{title} — {SITE['brand']}",
          meta_desc=desc,
          page_url=SITE['url']+f"/services/{slug}.html",
          jsonld=json.dumps({"@context":"https://schema.org","@type":"Service","name":title,"description":desc,"provider":org_schema(SITE)}),
          brand=SITE['brand'],
          page_h1=title,
          content=content,
          name=SITE['name'],
          year=datetime.date.today().year
        ))

# generate 30 blog stubs
for i in range(1,31):
    slug = f"blog-post-{i:02d}"
    title = f"Blog Post {i:02d} — {['AI Workflows','Pinterest growth','SEO tips','72-hour blueprint'][i%4]}"
    excerpt = f"Actionable guide {i}"
    content = f"<p>{excerpt}</p><p>Long form content placeholder — replace with 800-1500 word article using target keywords.</p>"
    with open(OUT / 'blog' / f"{slug}.html",'w',encoding='utf8') as f:
        f.write(BASE_TEMPLATE.format(
          meta_title=title,
          meta_desc=excerpt,
          page_url=SITE['url']+f"/blog/{slug}.html",
          jsonld=json.dumps({"@context":"https://schema.org","@type":"BlogPosting","headline":title}),
          brand=SITE['brand'],
          page_h1=title,
          content=content,
          name=SITE['name'],
          year=datetime.date.today().year
        ))

# sitemap
urls = []
for p in (OUT.glob('*.html')):
    urls.append(SITE['url'] + '/' + p.name)
for p in (OUT / 'services').glob('*.html'):
    urls.append(SITE['url'] + '/services/' + p.name)
for p in (OUT / 'blog').glob('*.html'):
    urls.append(SITE['url'] + '/blog/' + p.name)

sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
for u in urls:
    sitemap += f"  <url><loc>{u}</loc></url>\n"
sitemap += '</urlset>'
with open(OUT / 'sitemap.xml','w',encoding='utf8') as f:
    f.write(sitemap)

print("Generated site: index, about, services (12), blog (30), sitemap.xml")
