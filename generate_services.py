# generate_services.py
import os, json, datetime
from pathlib import Path

ROOT = Path('.').resolve()
SERVICES_DIR = ROOT / 'services'
SERVICES_DIR.mkdir(exist_ok=True)

SITE = {
  "brand":"SainathAI",
  "url":"https://SainathAI.github.io/sainathai-site",
  "founder":"Sainath Phani VV",
  "email":"enquiry@sainathai.com",
  "whatsapp":"+917075103333"
}

services = [
  ("ai-automation","AI Automation","Scale client operations with plug-and-play AI workflows that cut costs and increase revenue."),
  ("business-automation","Business Automation","Automate sales, billing and ops to remove manual bottlenecks and scale with same headcount."),
  ("seo-growth-systems","SEO Growth Systems","Technical and content SEO engineered for automated organic traffic and qualified leads."),
  ("content-engine","Content Engine","Automate high-ROI content production and distribution at scale."),
  ("funnels-landing-pages","Funnels & Landing Pages","High-converting funnels with automated A/B testing and analytics."),
  ("paid-ads-ai","Paid Ads + AI","Automated ad creation, bidding, and scaling powered by AI."),
  ("digital-products","Digital Products","Create subscription and info-products for recurring revenue."),
  ("whatsapp-automation","WhatsApp Automation","Lead capture and sales sequences on WhatsApp with bot + human handoff."),
  ("ecommerce-automation","Ecommerce Automation","Order, catalog and fulfillment automation for faster time-to-market."),
  ("agency-automation","Agency Automation","Standardize delivery and scale agency services with templates and automation."),
  ("data-analytics-ai","Data Analytics + AI","Dashboards, forecasts and action rules to turn data into revenue actions."),
  ("trading-automation","Trading Automation","Algorithmic trading systems for rule-based execution and risk controls.")
]

BASE_TEMPLATE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{meta_title}</title>
<meta name="description" content="{meta_desc}">
<link rel="stylesheet" href="/styles.css">
<script type="application/ld+json">{jsonld}</script>
</head>
<body>
<div class="container">
  <header class="header"><div class="brand">{brand}</div></header>

  <main class="card">
    <h1 class="h1">{h1}</h1>
    <div class="h2">{sub}</div>

    <section>
      <h3>Why this matters</h3>
      <p>{intro}</p>
      <ul>
        {benefits}
      </ul>
    </section>

    <section>
      <h3>How it works — 3 steps</h3>
      <ol>
        <li><strong>Audit & plan:</strong> We map highest-impact automations in 72 hours.</li>
        <li><strong>Build & test:</strong> Deliver production-ready flows, scripts and dashboards.</li>
        <li><strong>Scale & train:</strong> Hand-off, SOPs and performance SLAs.</li>
      </ol>
    </section>

    <section>
      <h3>Pricing (starter)</h3>
      <p>Entry audit + pilot: <strong>₹9,999</strong>. Growth package: <strong>₹49,999/month</strong>. Enterprise: custom.</p>
      <a class="btn btn-primary" href="/lead.html" id="leadCta">Get audit & pricing</a>
    </section>

    <section>
      <h3>FAQ</h3>
      <div>
        <strong>Q:</strong> How fast can you deliver?<br/>
        <strong>A:</strong> Audit in 72 hours, pilot in 7–14 days depending on scope.
      </div>
    </section>
  </main>

  <footer class="footer">© {year} {brand} — Contact: <a href="/contact.html">{email}</a></footer>
</div>
<script src="/scripts.js"></script>
</body>
</html>
"""

def make_bullets(items):
    return "\\n".join([f"<li>{x}</li>" for x in items])

for slug, title, desc in services:
    meta_title = f"{title} — {SITE['brand']}"
    meta_desc = desc
    year = datetime.date.today().year

    benefits = [
      "Cut manual work and errors, reduce cost",
      "Increase throughput and revenue without hiring",
      "Measurable KPIs and SLA-backed delivery"
    ]
    # for AI automation use deeper content
    if slug == "ai-automation":
        intro = ("AI Automation builds rule-based and ML-driven pipelines that handle customer journeys, content generation, "
                 "and operational tasks. We focus on revenue-generating automations with measurable ROI.")
        # more detailed benefits
        benefits = [
          "Automate lead scoring + routing to increase conversion",
          "Auto-generate high-CTR content and creatives for campaigns",
          "End-to-end integration: CRM, Ads, CMS, WhatsApp and Analytics"
        ]
    else:
        intro = desc

    page = BASE_TEMPLATE.format(
        meta_title=meta_title,
        meta_desc=meta_desc,
        jsonld=json.dumps({
            "@context":"https://schema.org",
            "@type":"Service",
            "name":title,
            "description":desc,
            "provider": {"@type":"Organization","name":SITE['brand'],"url":SITE['url']}
        }),
        brand=SITE['brand'],
        h1=title,
        sub=desc,
        intro=intro,
        benefits=make_bullets(benefits),
        year=year,
        email=SITE['email']
    )

    path = SERVICES_DIR / f"{slug}.html"
    path.write_text(page, encoding='utf8')

# produce one expanded flagship service (AI Automation) with longer copy
flag = SERVICES_DIR / "ai-automation.html"
flag_content = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>AI Automation — {SITE['brand']}</title>
<meta name="description" content="Full-service AI automation to scale operations and revenue; audit in 72 hours.">
<link rel="stylesheet" href="/styles.css">
<script type="application/ld+json">{json.dumps({
    "@context":"https://schema.org",
    "@type":"Service",
    "name":"AI Automation",
    "description":"AI Automation to scale operations and revenue",
    "provider":{"@type":"Organization","name":SITE['brand'],"url":SITE['url']}
})}</script>
</head><body><div class="container">
<header class="header"><div class="brand">{SITE['brand']}</div></header>
<main class="card">
<h1 class="h1">AI Automation — Deliver revenue with automation</h1>
<div class="h2">End-to-end AI workflows for marketing, ops and product—built for measurable ROI.</div>

<section>
<p><strong>Offer:</strong> 72-hour audit, pilot build, full-rollout. We prioritize automations that pay for themselves within 30–90 days.</p>

<h3>Core outcomes</h3>
<ul>
<li>+30–200% increase in lead conversion via automated lead scoring & routing</li>
<li>Reduce manual content production costs by 70% with a content engine</li>
<li>Automate order handling and customer messages to cut fulfillment time</li>
</ul>

<h3>How we work — phases</h3>
<p><strong>Phase 1 — Rapid Audit (72 hours):</strong> Technical and revenue audit focused on data, integration points, and low-hanging automation wins. Deliverable: priority roadmap + KPI targets.</p>
<p><strong>Phase 2 — Pilot build (7–14 days):</strong> Build 1–2 high-impact automations (lead capture -> scoring -> WhatsApp sequence / email / dashboard). Test with live traffic.</p>
<p><strong>Phase 3 — Scale & Run:</strong> Harden the flows, provide SOPs, training, and optional monthly operations support.</p>

<h3>Pricing and guarantees</h3>
<p>Audit + pilot: <strong>₹9,999</strong>. Growth package starts at <strong>₹49,999/month</strong> and includes monitoring and performance fine-tuning. We target measurable KPIs and deliver a rollback plan.</p>

<h3>Case study snapshot</h3>
<p>Example: Healthcare client — we automated patient lead capture and triage, reducing lead-to-booking time by 3x and increasing bookings by 42% in 30 days.</p>

<h3>FAQ</h3>
<p><strong>Q: Do you need API access?</strong> A: Yes — CRM, ad, or platform access speeds delivery. We can provide limited-scope scripts if full access is not available.</p>

<p style="margin-top:18px"><a class="btn btn-primary" href="/lead.html" id="leadCta">Request AI Audit</a></p>
</main>
<footer class="footer">© {datetime.date.today().year} {SITE['brand']} • <a href="/contact.html">{SITE['email']}</a></footer>
</div>
<script src="/scripts.js"></script></body></html>"""
flag.write_text(flag_content, encoding='utf8')

print("OK: created 12 service pages (services/*.html) and expanded ai-automation.html")
