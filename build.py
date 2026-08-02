#!/usr/bin/env python3
"""Static site generator for L&V Civil Contracting.

Run `python3 build.py` from the repo root to regenerate every HTML page from
the shared header/footer templates and the per-page content below. Keeps all
11 pages consistent without a framework.
"""

# Client photography from the live site, optimised to webp and re-hosted on the
# KW Innovations CDN. Keys map to where each image sat on the original site.
IMG = {
    "hero":      "https://d2ol7oe51mr4n9.cloudfront.net/user_3ECT3zt6ovZZHX51H6T4wC5y40O/f10a3951-3ce4-47b2-8eeb-8f75a4ba282c.webp",  # live homepage hero (loader)
    "work":      "https://d2ol7oe51mr4n9.cloudfront.net/user_3ECT3zt6ovZZHX51H6T4wC5y40O/148aaf25-9c24-4f60-9ba8-7a43ea1f332a.webp",  # IMG_9318 — client machine photo
    "machine":   "https://d2ol7oe51mr4n9.cloudfront.net/user_3ECT3zt6ovZZHX51H6T4wC5y40O/ef8c78a5-8e3b-421c-91db-c7a770162721.webp",  # IMG_9442 — client machine photo
    "excavator": "https://d2ol7oe51mr4n9.cloudfront.net/user_3ECT3zt6ovZZHX51H6T4wC5y40O/46362802-7b01-45e1-bb00-3bf21efd263f.webp",  # live excavator-hire hero
    "site1":     "https://d2ol7oe51mr4n9.cloudfront.net/user_3ECT3zt6ovZZHX51H6T4wC5y40O/2e013edc-6bdd-44b3-b473-7546423d722c.webp",
    "site2":     "https://d2ol7oe51mr4n9.cloudfront.net/user_3ECT3zt6ovZZHX51H6T4wC5y40O/3060894c-f138-4f55-adab-d0f18d2dea69.webp",
    "pano":      "https://d2ol7oe51mr4n9.cloudfront.net/user_3ECT3zt6ovZZHX51H6T4wC5y40O/b6806a97-d72a-4818-a428-99fa3df390bb.webp",  # wide tipper panorama
    "og":        "https://d2ol7oe51mr4n9.cloudfront.net/user_3ECT3zt6ovZZHX51H6T4wC5y40O/0189b932-a3b3-4591-8ae9-d686d63f85a4.png",   # branded social card
}
IMG["trench"] = IMG["work"]
IMG["fleet"] = IMG["machine"]
IMG["water"] = IMG["site2"]

SITE = "https://www.lvcivilcontracting.com.au"
PHONE_DISPLAY = "0476 676 639"
PHONE_TEL = "+61476676639"
EMAIL = "info@lvcivilcontracting.com.au"
# Recipient for the homepage "Reach Out" form (per client request). NB: this is
# a different domain to the site (lvcivilconstruction vs lvcivilcontracting) —
# confirm the mailbox exists before go-live.
HOME_FORM_EMAIL = "admin@lvcivilconstruction.com.au"
ABN = "63 661 732 869"

SERVICES = [
    ("excavator-hire",   "Excavator Hire"),
    ("bobcat-hire",      "Bobcat Hire"),
    ("tipper-truck-hire",      "Tipper Hire"),
    ("combo-hire",       "Combo Hire"),
    ("posi-track-hire",  "Posi Track Hire"),
    ("skip-bin-hire",    "Skip Bin Hire"),
    ("water-truck-hire", "Water Truck Hire"),
]

# Civil project services from the live site's "Our Services" section, each with
# a dedicated content page. (slug, name, card desc, icon)
CIVIL_SERVICES = [
    ("renewable-energy-subdivisions", "Renewable Energy Subdivision Works",
     "Earthworks, trenching, access roads and service installation for reliable, future-ready energy subdivisions of any size.",
     '<path d="M13 2 3 14h9l-1 8 10-12h-9z"/>'),
    ("site-preparation", "Site Preparation",
     "We clear, level, grade and stabilise land to create safe, accessible and compliant sites for all types of construction work.",
     '<path d="m12 2 10 6-10 6L2 8z"/><path d="m2 14 10 6 10-6"/>'),
    ("wind-farms", "Wind Farms",
     "Crane pads, internal roads and trench networks constructed to support smooth wind turbine transport and installation.",
     '<path d="M9.6 4.6A2 2 0 1 1 11 8H2"/><path d="M12.6 19.4A2 2 0 1 0 14 16H2"/><path d="M17.7 7.7a2.5 2.5 0 1 1 1.8 4.3H2"/>'),
    ("solar-farms", "Solar Farms",
     "Power your solar project with precision groundwork — we shape, stabilise and trench land to support arrays, inverters and access routes that last.",
     '<circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.93 4.93l1.41 1.41M17.66 17.66l1.41 1.41M2 12h2M20 12h2M6.34 17.66l-1.41 1.41M19.07 4.93l-1.41 1.41"/>'),
    ("pipe-and-gas-lines", "Pipe & Gas Lines",
     "Safe trenching, backfilling and reinstatement services that keep your pipeline and gas infrastructure protected and compliant.",
     '<circle cx="6" cy="19" r="3"/><path d="M9 19h8.5a3.5 3.5 0 0 0 0-7h-11a3.5 3.5 0 0 1 0-7H15"/><circle cx="18" cy="5" r="3"/>'),
    ("gas-gathering", "Gas Gatherings",
     "We trench, grade and form access routes to support efficient, safe transport of extracted gas to processing.",
     '<path d="M8.5 14.5A2.5 2.5 0 0 0 11 12c0-1.38-.5-2-1-3-1.072-2.143-.224-4.054 2-6 .5 2.5 2 4.9 4 6.5 2 1.6 3 3.5 3 5.5a7 7 0 1 1-14 0c0-1.153.433-2.294 1-3a2.5 2.5 0 0 0 2.5 2.5z"/>'),
]
CIVIL_NAMES = {slug: name for slug, name, _, _ in CIVIL_SERVICES}

# Real client reviews only — populate from Google/verbal testimonials supplied by
# the client. Leave empty to hide the testimonials section entirely. Fields:
# (quote, name, suburb/job)
TESTIMONIALS = []

# Suburb landing pages for local SEO. slug -> (display name, intro paras, highlights)
SUBURBS = {
    "park-ridge": ("Park Ridge", [
        "Park Ridge is home base. Our yard is right here in 4125, which means the shortest float times, the sharpest call-out rates and machines that can be on your site quickly.",
        "From house pads and footings to trenching, driveways and site cleanups, we handle Park Ridge's mix of established blocks and new development with gear sized to fit.",
    ], ["Fastest response times", "House pads & footings", "Trenching & driveways"]),
    "jimboomba": ("Jimboomba", [
        "Acreage country. Jimboomba blocks mean long driveways, dams, shed pads and serious clearing — exactly the work our excavators, posi tracks and tippers are set up for.",
        "We know the local soil and the long access runs, and our combo packages keep multi-day acreage jobs on one booking and one invoice.",
    ], ["Dams & shed pads", "Long driveways", "Acreage clearing"]),
    "greenbank": ("Greenbank", [
        "Greenbank's semi-rural blocks call for flexible gear: land clearing, house pads, trenching for services that run a long way from the street, and tracked machines for soft paddocks.",
        "We service the whole corridor regularly, so mobilisation is quick and quotes come back fast.",
    ], ["Land clearing", "House pads", "Soft-ground posi tracks"]),
    "yarrabilba": ("Yarrabilba", [
        "One of Queensland's fastest growing communities — and tight new estate lots need machines and operators that work clean and precise next to finished homes.",
        "We handle cut and fill, detailed excavation, backyard access jobs and final-grade levelling for builders and new homeowners across Yarrabilba.",
    ], ["Tight-access work", "Cut & fill", "Final-grade levelling"]),
    "flagstone": ("Flagstone", [
        "Flagstone is building fast, and we're in the estates every week: site cuts, footings, service trenching and spoil cart-away for builders working to program.",
        "Book a dig-and-cart combo and your excavation never waits on a truck.",
    ], ["Site cuts & footings", "Service trenching", "Dig & cart combos"]),
    "logan-village": ("Logan Village", [
        "Acreage lifestyle blocks with real earthworks needs — driveways, dams, pads, clearing and trenching that suburban-sized operators struggle to cover.",
        "Our fleet is built for exactly this mix, with wet hire operators who've worked Logan Village ground for years.",
    ], ["Driveways & pads", "Dams", "Rural trenching"]),
    "browns-plains": ("Browns Plains", [
        "The commercial heart of Logan. We support Browns Plains businesses and homeowners with site preparation, tight-access digs, waste removal and water trucks for dust control.",
        "Established suburbs mean careful work around services and neighbours — that's where experienced operators earn their keep.",
    ], ["Commercial site prep", "Tight-access digs", "Dust control"]),
}

ICONS = {
    "phone": '<svg width="{s}" height="{s}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.127.96.361 1.903.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0 1 22 16.92z"/></svg>',
    "arrow": '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M12 5l7 7-7 7"/></svg>',
    "tick": '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 6 9 17l-5-5"/></svg>',
    "shield": '<svg width="{s}" height="{s}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="m9 12 2 2 4-4"/></svg>',
    "pin": '<svg width="{s}" height="{s}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0z"/><circle cx="12" cy="10" r="3"/></svg>',
}


def head(title, desc, canonical, extra=""):
    return f'''<!DOCTYPE html>
<html lang="en-AU">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <link rel="canonical" href="{canonical}">
  <meta name="robots" content="index, follow">
  <meta name="theme-color" content="#0b0f14">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="L&amp;V Civil Contracting">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:url" content="{canonical}">
  <meta property="og:image" content="{IMG['og']}">
  <meta property="og:locale" content="en_AU">
  <meta name="twitter:card" content="summary_large_image">
  <link rel="icon" href="favicon.ico" sizes="16x16">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Archivo:wght@600;700;800;900&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="css/style.css">
  <script type="speculationrules">
  {{"prerender": [{{"where": {{"href_matches": "/*"}}, "eagerness": "moderate"}}]}}
  </script>
{extra}</head>
<body>
  <a class="skip-link" href="#main">Skip to content</a>
'''


def header(active=""):
    def cls(page):
        return ' class="is-active" aria-current="page"' if page == active else ""
    drop_links = '          <span class="drop-label">Wet Hire</span>\n'
    drop_links += "\n".join(
        f'          <a href="{slug}.html">{name}</a>' for slug, name in SERVICES
    )
    drop_links += '\n          <span class="drop-label">Civil Works</span>\n'
    drop_links += "\n".join(
        f'          <a href="{slug}.html">{name}</a>' for slug, name, _, _ in CIVIL_SERVICES
    )
    return f'''
  <div class="topbar">{ICONS['pin'].format(s=13)}Park Ridge QLD, 4125 — Servicing Logan &amp; South East Queensland</div>
  <header class="site-header">
    <div class="container nav-bar">
      <a class="brand" href="index.html" aria-label="L&amp;V Civil Contracting — home">
        <img src="assets/logo.jpg" alt="L&amp;V Civil Contracting" width="54" height="54">
      </a>
      <nav class="nav-links" id="nav-links" aria-label="Main navigation">
        <a href="index.html"{cls('home')}>Home</a>
        <a href="about.html"{cls('about')}>Who We Are</a>
        <div class="nav-drop">
          <button type="button" aria-haspopup="true">What We Offer
            <svg class="caret" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m6 9 6 6 6-6"/></svg>
          </button>
          <div class="drop-menu">
{drop_links}
          <a class="drop-all" href="services.html">All Services →</a>
          </div>
        </div>
        <a href="contact.html"{cls('contact')}>Contact</a>
        <a href="contact.html" class="btn btn-primary btn-sm">Get a Quote</a>
      </nav>
      <div class="nav-cta">
        <a href="contact.html" class="btn btn-ghost btn-sm">Contact</a>
        <a href="tel:{PHONE_TEL}" class="btn btn-primary btn-sm nav-phone">{ICONS['phone'].format(s=15)} <span class="ph-num">{PHONE_DISPLAY}</span></a>
        <button class="nav-toggle" aria-expanded="false" aria-controls="nav-links" aria-label="Toggle menu">
          <span></span><span></span><span></span>
        </button>
      </div>
    </div>
  </header>
'''


def footer():
    offer_links = "\n".join(
        f'            <li><a href="{slug}.html">{name}</a></li>' for slug, name in SERVICES
    )
    civil_links = "\n".join(
        f'            <li><a href="{slug}.html">{name}</a></li>' for slug, name, _, _ in CIVIL_SERVICES
    )
    return f'''
  <footer class="site-footer" style="--footer-img: url('{IMG['pano']}')">
    <div class="container">
      <div class="footer-cta">
        <h2>Powering projects with skill &amp; safety.</h2>
        <a href="contact.html" class="btn btn-primary">Get in touch {ICONS['arrow']}</a>
      </div>
      <nav class="footer-nav" aria-label="Footer navigation">
        <a href="index.html">Home</a>
        <a href="about.html">Who We Are</a>
        <a href="services.html">What We Offer</a>
        <a href="contact.html">Contact Us</a>
      </nav>
      <div class="footer-grid">
        <div class="footer-about">
          <a class="brand" href="index.html">
            <img src="assets/logo.jpg" alt="L&amp;V Civil Contracting" width="86" height="86" loading="lazy">
          </a>
          <p>Family owned and operated wet hire and civil works, delivering reliable results across Logan and South East Queensland since 2022.</p>
          <div class="trust-card">
            {ICONS['shield'].format(s=26)}
            <span><strong>Fully licensed &amp; insured</strong><small>Quality guarantee · Price match promise · Zero Harm</small></span>
          </div>
        </div>
        <div>
          <h4>Wet Hire</h4>
          <ul>
{offer_links}
          </ul>
        </div>
        <div>
          <h4>Civil Works</h4>
          <ul>
{civil_links}
          </ul>
        </div>
        <div>
          <h4>Contact</h4>
          <ul>
            <li><a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></li>
            <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
            <li>Park Ridge QLD, 4125</li>
          </ul>
        </div>
        <div>
          <h4>Trading Hours</h4>
          <table class="hours">
            <tr><td>Monday</td><td>9:00 am – 5:00 pm</td></tr>
            <tr><td>Tuesday</td><td>9:00 am – 5:00 pm</td></tr>
            <tr><td>Wednesday</td><td>9:00 am – 5:00 pm</td></tr>
            <tr><td>Thursday</td><td>9:00 am – 5:00 pm</td></tr>
            <tr><td>Friday</td><td>9:00 am – 5:00 pm</td></tr>
            <tr class="closed"><td>Saturday</td><td>Closed</td></tr>
            <tr class="closed"><td>Sunday</td><td>Closed</td></tr>
          </table>
        </div>
      </div>
      <div class="footer-bottom">
        <span>© <span data-year>2026</span> | L&amp;V Civil Contracting · ABN: {ABN}</span>
        <span>Website by <a href="https://kwinnovations.com.au" target="_blank" rel="noopener" class="kw-credit">KW&nbsp;|&nbsp;Innovations</a></span>
      </div>
    </div>
  </footer>

  <div class="mobile-cta" aria-hidden="false">
    <a href="tel:{PHONE_TEL}" class="btn btn-primary">{ICONS['phone'].format(s=16)} Call now</a>
    <a href="contact.html" class="btn btn-ghost">Get a quote</a>
  </div>

  <script src="js/main.js" defer></script>
</body>
</html>
'''


def cta_band(h, p):
    return f'''
    <section class="section-tight">
      <div class="container">
        <div class="cta-band reveal">
          <div>
            <h2>{h}</h2>
            <p>{p}</p>
          </div>
          <div style="display:flex; gap:1rem; flex-wrap:wrap;">
            <a href="tel:{PHONE_TEL}" class="btn btn-dark">{ICONS['phone'].format(s=16)} {PHONE_DISPLAY}</a>
            <a href="contact.html" class="btn btn-ghost" style="border-color: rgba(11,15,20,0.4); color: var(--ink-950);">Request a quote</a>
          </div>
        </div>
      </div>
    </section>
'''


def tickline():
    seg = "".join(
        f'{name} <em class="sep">◆</em> ' for _, name in SERVICES
    ) + 'Trenching &amp; Civil Works <em class="sep">◆</em> '
    return f'''
    <div class="marquee" aria-hidden="true">
      <div class="marquee-track">
        <span>{seg}</span>
        <span>{seg}</span>
      </div>
    </div>
'''


def civil_section(tint="section-light"):
    cards = []
    for i, (slug, name, desc, icon) in enumerate(CIVIL_SERVICES):
        delay = f' style="--delay:.{(i % 3) * 6:02d}s"' if i % 3 else ""
        cards.append(f'''          <article class="service-card reveal"{delay}>
            <span class="card-num" aria-hidden="true">{i+1:02d}</span>
            <div class="service-icon" aria-hidden="true"><svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">{icon}</svg></div>
            <h3>{name}</h3>
            <p>{desc}</p>
            <a class="card-link" href="{slug}.html">Learn more {ICONS['arrow'].replace('width="16" height="16"', 'width="14" height="14"')}</a>
          </article>''')
    cards_html = "\n".join(cards)
    return f'''    <section class="section {tint}" id="civil-works">
      <div class="container">
        <div class="section-head reveal">
          <span class="eyebrow">Our services</span>
          <h2>Civil works, from subdivisions to solar.</h2>
          <p>Beyond wet hire, we deliver full civil project works — renewable energy subdivisions, wind and solar farms, pipelines and gas gathering infrastructure — from a homeowner's site prep to broadacre energy developments.</p>
        </div>
        <div class="card-grid">
{cards_html}
        </div>
      </div>
    </section>

'''


def gallery_section():
    shots = [
        ("hero",      "L&amp;V Civil loader working at sunrise on a Logan site", "g-feature"),
        ("work",      "Excavator trenching on a residential block", ""),
        ("machine",   "Posi track loader on soft ground", ""),
        ("excavator", "Excavator on site cut works", ""),
        ("site2",     "Water truck dust suppression on a civil site", ""),
        ("pano",      "Tipper truck panorama across a Logan worksite", "g-wide"),
    ]
    figs = "\n".join(
        f'''          <figure class="g-item {cls} reveal"{f' style="--delay:.{(i % 3) * 6:02d}s"' if i % 3 else ''}>
            <img src="{IMG[key]}" alt="{alt}" loading="lazy" width="900" height="675">
          </figure>''' for i, (key, alt, cls) in enumerate(shots)
    )
    return f'''    <section class="section" id="gallery">
      <div class="container">
        <div class="section-head reveal">
          <span class="eyebrow">On the tools</span>
          <h2>Real machines. Real Logan sites.</h2>
          <p>No stock photos — this is our gear and our crew at work across the Logan region.</p>
        </div>
        <div class="gallery">
{figs}
        </div>
      </div>
    </section>

'''


def testimonials_section():
    # The client's Elfsight Google Reviews widget (same embed as the live site)
    # renders their real reviews; TESTIMONIALS adds static quote cards if supplied.
    widget = '''    <section class="section section-tint">
      <div class="container">
        <div class="section-head center reveal">
          <span class="eyebrow">What clients say</span>
          <h2>Rated by real Logan clients.</h2>
        </div>
        <script src="https://static.elfsight.com/platform/platform.js" async></script>
        <div class="elfsight-app-e981435c-4cda-4718-a82a-4d8280ea8cf5" data-elfsight-app-lazy></div>
      </div>
    </section>
'''
    if not TESTIMONIALS:
        return widget
    cards = "\n".join(
        f'''          <figure class="quote-card reveal">
            <blockquote>&ldquo;{q}&rdquo;</blockquote>
            <figcaption><strong>{n}</strong><span>{j}</span></figcaption>
          </figure>''' for q, n, j in TESTIMONIALS
    )
    return f'''    <section class="section section-tint">
      <div class="container">
        <div class="section-head center reveal">
          <span class="eyebrow">What clients say</span>
          <h2>Word gets around Logan.</h2>
        </div>
        <div class="card-grid">
{cards}
        </div>
      </div>
    </section>
'''


# ---------------------------------------------------------------- index ----
def build_index():
    ld = f'''  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "LocalBusiness",
    "@id": "{SITE}/#business",
    "name": "L&V Civil Contracting",
    "description": "Family owned wet hire for site preparation, landscaping, construction and civil works across Logan and South East Queensland.",
    "url": "{SITE}/",
    "telephone": "{PHONE_TEL}",
    "email": "{EMAIL}",
    "image": "{IMG['hero']}",
    "address": {{"@type": "PostalAddress", "addressLocality": "Park Ridge", "addressRegion": "QLD", "postalCode": "4125", "addressCountry": "AU"}},
    "areaServed": ["Logan", "Park Ridge", "South East Queensland"],
    "openingHoursSpecification": {{"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday"], "opens": "09:00", "closes": "17:00"}},
    "priceRange": "$$"
  }}
  </script>
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {{"@type": "Question", "name": "What does wet hire mean?", "acceptedAnswer": {{"@type": "Answer", "text": "Wet hire means the machine comes with a skilled, ticketed operator included — you get production from the first hour without needing your own plant tickets."}}}},
      {{"@type": "Question", "name": "Which areas do you service?", "acceptedAnswer": {{"@type": "Answer", "text": "We are based in Park Ridge QLD 4125 and service all major suburbs across Logan and wider South East Queensland."}}}},
      {{"@type": "Question", "name": "How fast can I get a quote?", "acceptedAnswer": {{"@type": "Answer", "text": "Call 0476 676 639 or send your project details — we aim to have a clear, itemised quote back to you within 24 hours."}}}},
      {{"@type": "Question", "name": "Are you licensed and insured?", "acceptedAnswer": {{"@type": "Answer", "text": "Yes — every job runs with full licensing, insurance, documented SWMS and a Zero Harm safety focus."}}}}
    ]
  }}
  </script>
'''
    cards = []
    card_data = [
        ("excavator-hire", "Excavator Hire", "Precision digging, trenching, footings and site cuts with operators who read the ground as well as the plans.",
         '<path d="M3 17h13l2 3H5z"/><path d="M8 17v-5h4l3 5"/><path d="M12 12 9 5l6 2 3 6"/><circle cx="6.5" cy="20" r="1"/><circle cx="15.5" cy="20" r="1"/>'),
        ("bobcat-hire", "Bobcat Hire", "Tight-access clearing, levelling and spreading for blocks where bigger machines simply can't work.",
         '<rect x="3" y="10" width="12" height="7" rx="1.5"/><path d="M15 13h4l2 3v1h-6z"/><circle cx="7" cy="19" r="1.6"/><circle cx="17" cy="19" r="1.6"/>'),
        ("tipper-truck-hire", "Tipper Hire", "Fast, reliable haulage of spoil, fill, aggregate and demolition material — keeping your site moving.",
         '<path d="M2 15V9h11l3-4h3v10"/><path d="M2 15h20v2h-3"/><circle cx="7" cy="18.5" r="1.7"/><circle cx="15" cy="18.5" r="1.7"/>'),
        ("combo-hire", "Combo Hire", "Machines, trucks and operators bundled into one package — one booking, one invoice, one crew.",
         '<rect x="3" y="3" width="8" height="8" rx="2"/><rect x="13" y="3" width="8" height="8" rx="2"/><rect x="3" y="13" width="8" height="8" rx="2"/><rect x="13" y="13" width="8" height="8" rx="2"/>'),
        ("posi-track-hire", "Posi Track Hire", "Tracked loaders that keep working where wheels bog down — soft, wet or sloped ground sorted.",
         '<rect x="3" y="9" width="13" height="7" rx="2"/><path d="M16 12h3l2 3v1h-5z"/><path d="M4 19h16"/><circle cx="7" cy="19" r="1.4"/><circle cx="12" cy="19" r="1.4"/><circle cx="17" cy="19" r="1.4"/>'),
        ("skip-bin-hire", "Skip Bin Hire", "Site waste handled in the same booking — bins delivered, filled and taken away on your schedule.",
         '<path d="M4 8h16l-2 12H6z"/><path d="M2 8h20M9 4h6l1 4H8z"/>'),
        ("water-truck-hire", "Water Truck Hire", "Dust suppression and compaction watering that keeps your site compliant and your program on track.",
         '<path d="M12 3v3M12 3c-4 4-7 7.5-7 11a7 7 0 0 0 14 0c0-3.5-3-7-7-11z"/><path d="M9 15a3 3 0 0 0 3 3"/>'),
    ]
    for i, (slug, name, desc, icon) in enumerate(card_data):
        delay = f' style="--delay:.{(i % 3) * 6:02d}s"' if i % 3 else ""
        cards.append(f'''          <article class="service-card reveal"{delay}>
            <span class="card-num" aria-hidden="true">{i+1:02d}</span>
            <div class="service-icon" aria-hidden="true"><svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">{icon}</svg></div>
            <h3>{name}</h3>
            <p>{desc}</p>
            <a class="card-link" href="{slug}.html">Learn more {ICONS['arrow'].replace('width="16" height="16"', 'width="14" height="14"')}</a>
          </article>''')
    cards_html = "\n".join(cards)

    chips = "".join(f"<span>{n}</span>" for _, n in SERVICES[:5])
    suburbs = ["Park Ridge", "Logan Village", "Jimboomba", "Greenbank", "Browns Plains", "Crestmead",
               "Marsden", "Waterford", "Beenleigh", "Springwood", "Shailer Park", "Loganholme",
               "Loganlea", "Yarrabilba", "Flagstone", "Chambers Flat", "Munruben", "Boronia Heights"]
    page_slugs = {v[0]: k for k, v in SUBURBS.items()}
    chips_area = "\n".join(
        (f'          <a class="chip chip-link" href="earthmoving-{page_slugs[s]}.html">{s}</a>'
         if s in page_slugs else f'          <span class="chip">{s}</span>')
        for s in suburbs
    )

    ld = f'  <link rel="preload" as="image" href="{IMG["hero"]}" fetchpriority="high">\n' + ld
    body = f'''{header('home')}
  <main id="main">
    <section class="hero" style="--hero-img: url('{IMG['hero']}')">
      <div class="container hero-inner">
        <p class="hero-eyebrow rise"><span class="dot" aria-hidden="true"></span> Logan's Trusted Civil Contractor</p>
        <h1 class="rise" style="--delay:.08s">Ground works, <span class="accent">done right.</span></h1>
        <p class="hero-lede rise" style="--delay:.16s">Family owned wet hire for site preparation, landscaping, construction and civil works across Logan and South East Queensland — modern machines with skilled operators, backed by a quality guarantee and a Zero Harm safety focus.</p>
        <div class="hero-chips rise" style="--delay:.24s">{chips}</div>
        <div class="hero-actions rise" style="--delay:.32s">
          <a href="contact.html" class="btn btn-primary">Get a free quote {ICONS['arrow']}</a>
          <a href="tel:{PHONE_TEL}" class="btn btn-ghost">{ICONS['phone'].format(s=16)} {PHONE_DISPLAY}</a>
        </div>
        <div class="hero-stats rise" style="--delay:.4s">
          <div><strong data-count="100" data-suffix="%">0</strong><span>Wet hire</span></div>
          <div><strong data-count="0">0</strong><span>Harm record</span></div>
          <div><strong data-count="100" data-suffix="%">0</strong><span>Compliant operations</span></div>
        </div>
      </div>
      <div class="hero-badge rise" style="--delay:.55s">
        <div class="hb-top"><span class="dot"></span> Our promise</div>
        <strong>Quality guarantee &amp; price match promise</strong>
        <small>Family owned · Zero Harm safety focus</small>
      </div>
    </section>
{tickline()}
    <section class="section-tight">
      <div class="container promises">
        <div class="promise reveal">
          <div class="service-icon" aria-hidden="true">{ICONS['shield'].format(s=24)}</div>
          <div><strong>Quality guarantee</strong><p>Dug to depth, compacted to spec and finished properly — we stand behind every job we deliver.</p></div>
        </div>
        <div class="promise reveal" style="--delay:.07s">
          <div class="service-icon" aria-hidden="true"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 1v22M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg></div>
          <div><strong>Price match promise</strong><p>Straight-up quotes with no hidden extras — and if you find a sharper like-for-like price, talk to us.</p></div>
        </div>
        <div class="promise reveal" style="--delay:.14s">
          <div class="service-icon" aria-hidden="true"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87M16 3.13a4 4 0 0 1 0 7.75"/></svg></div>
          <div><strong>Zero Harm safety</strong><p>SWMS, inductions and maintained plant on every site — nobody gets hurt on our watch.</p></div>
        </div>
      </div>
    </section>

    <section class="section" id="services">
      <div class="container">
        <div class="section-head reveal">
          <span class="eyebrow">What we offer</span>
          <h2>One crew. Every stage of your ground works.</h2>
          <p>Every machine arrives with a skilled, safety-focused operator — that's the wet hire difference. Hire a single unit or bundle a combo package sized to your site.</p>
        </div>
        <div class="card-grid">
{cards_html}
        </div>
      </div>
    </section>

    <section class="section section-tint">
      <div class="container split">
        <div class="split-media reveal">
          <img src="{IMG['trench']}" alt="Excavator digging a trench on a residential site in Logan at golden hour" loading="lazy" width="1200" height="896">
          <div class="badge-float">{ICONS['shield'].format(s=26)} Fully licensed &amp; insured</div>
        </div>
        <div class="reveal">
          <span class="eyebrow">Why L&amp;V Civil</span>
          <h2 style="font-size: var(--fs-h2); font-weight: 800;">The local crew that treats your site like their own.</h2>
          <p style="margin-top:1rem;">L&amp;V Civil Contracting is family owned and operated — the kind of crew that answers the phone, shows up on time and stands behind every job, with flexible wet hire options sized to any project.</p>
          <ul class="check-list">
            <li><span class="tick">{ICONS['tick']}</span><div><strong>Operators included, always</strong><span>Wet hire means every machine comes with an experienced, ticketed operator.</span></div></li>
            <li><span class="tick">{ICONS['tick']}</span><div><strong>Safety without shortcuts</strong><span>Zero Harm focus with SWMS, site inductions and maintained plant on every job.</span></div></li>
            <li><span class="tick">{ICONS['tick']}</span><div><strong>Straight-up pricing</strong><span>Clear quotes, a price match promise, and combo packages that save you money.</span></div></li>
            <li><span class="tick">{ICONS['tick']}</span><div><strong>Local knowledge</strong><span>Based in Park Ridge — we know Logan's soil, councils and site conditions inside out.</span></div></li>
          </ul>
        </div>
      </div>
    </section>

{civil_section()}    <section class="section">
      <div class="container">
        <div class="section-head center reveal">
          <span class="eyebrow">How it works</span>
          <h2>From first call to final compaction.</h2>
        </div>
        <div class="steps">
          <div class="step reveal"><h3>Tell us the job</h3><p>Call or send the details — site, scope, timeframe. We'll ask the right questions up front.</p></div>
          <div class="step reveal" style="--delay:.07s"><h3>Get a clear quote</h3><p>A straightforward price within 24 hours, with the right machines and combos for the work.</p></div>
          <div class="step reveal" style="--delay:.14s"><h3>We do the work</h3><p>Our operators arrive on time, inducted and ready — and keep you updated as the job progresses.</p></div>
          <div class="step reveal" style="--delay:.21s"><h3>Site left right</h3><p>Clean finish, spoil removed, ground reinstated. We're not done until you're happy.</p></div>
        </div>
      </div>
    </section>

{gallery_section()}    <section class="section section-light" id="areas">
      <div class="container">
        <div class="section-head reveal">
          <span class="eyebrow">Where we work</span>
          <h2>Servicing Logan &amp; South East Queensland.</h2>
          <p>Based in Park Ridge, we cover all major suburbs across the Logan region — and travel further for the right project.</p>
        </div>
        <div class="chip-cloud reveal">
{chips_area}
        </div>
      </div>
    </section>

{testimonials_section()}    <section class="section">
      <div class="container">
        <div class="section-head center reveal">
          <span class="eyebrow">Good to know</span>
          <h2>Questions we get asked a lot.</h2>
        </div>
        <div class="faq reveal">
          <details>
            <summary>What does wet hire actually mean?</summary>
            <p>Wet hire means the machine comes with a skilled, ticketed operator included in the rate. You get production from the first hour — no plant tickets, no learning curve, no extra insurance headaches on your side.</p>
          </details>
          <details>
            <summary>Which areas do you service?</summary>
            <p>We're based in Park Ridge QLD 4125 and service all major suburbs across Logan — Jimboomba, Greenbank, Yarrabilba, Flagstone, Loganlea and beyond — plus wider South East Queensland for the right project.</p>
          </details>
          <details>
            <summary>How fast can I get a quote?</summary>
            <p>Call {PHONE_DISPLAY} or send your project details through the contact page — we aim to have a clear, itemised quote back to you within 24 hours.</p>
          </details>
          <details>
            <summary>Are you licensed and insured?</summary>
            <p>Yes. Every job runs with full licensing and insurance, documented SWMS and site inductions, under our Zero Harm safety focus.</p>
          </details>
          <details>
            <summary>Can I bundle machines together?</summary>
            <p>Absolutely — that's our combo hire. Excavator plus tipper, loader plus water truck, or a full site-prep crew: one booking, one invoice, machines that are used to working together.</p>
          </details>
        </div>
      </div>
    </section>

    <section class="section section-light" id="reach-out">
      <div class="container split">
        <div class="reveal">
          <span class="eyebrow">Reach out</span>
          <h2 style="font-size: var(--fs-h2); font-weight: 800;">Tell us about your project.</h2>
          <p style="margin-top:1rem;">Send the details and we'll come back with a clear, itemised quote — usually within 24 hours. Prefer to talk it through? Call us on <a href="tel:{PHONE_TEL}" style="color: var(--amber-500); font-weight: 600;">{PHONE_DISPLAY}</a>.</p>
          <ul class="check-list" style="margin-top:1.5rem;">
            <li><span class="tick">{ICONS['tick']}</span><div><strong>Free quotes</strong><span>No obligation, no call-out fee to price a job.</span></div></li>
            <li><span class="tick">{ICONS['tick']}</span><div><strong>24-hour turnaround</strong><span>Most quotes are back the next business day.</span></div></li>
            <li><span class="tick">{ICONS['tick']}</span><div><strong>Straight answers</strong><span>The right machine and combo for the job — not the dearest one.</span></div></li>
          </ul>
        </div>
        <form class="contact-form reveal" id="home-form" data-mailto="{HOME_FORM_EMAIL}" novalidate>
          <h3 style="margin-bottom:1.5rem;">Reach out</h3>
          <div class="form-row">
            <div class="field"><label for="h-name">Name</label><input id="h-name" name="name" type="text" autocomplete="name" required></div>
            <div class="field"><label for="h-phone">Phone</label><input id="h-phone" name="phone" type="tel" autocomplete="tel" required></div>
          </div>
          <div class="field"><label for="h-email">Email</label><input id="h-email" name="email" type="email" autocomplete="email" required></div>
          <div class="field"><label for="h-message">Message</label><textarea id="h-message" name="message" placeholder="Tell us about the site, scope and timeframe…"></textarea></div>
          <button type="submit" class="btn btn-primary" style="width:100%;">Send message <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M22 2 11 13M22 2l-7 20-4-9-9-4 20-7z"/></svg></button>
          <p class="form-note">Submitting opens your email app with the details pre-filled — or just call us on {PHONE_DISPLAY}.</p>
        </form>
      </div>
    </section>
{cta_band("Ready to break ground?", "Free quotes. 24-hour turnaround. Operators included with every machine.")}  </main>
{footer()}'''
    title = "Civil Construction &amp; Wet Hire in Logan QLD | L&amp;V Civil Contracting"
    desc = "Family owned wet hire earthmoving in Logan QLD — excavators, bobcats, tippers, posi tracks, water trucks and skip bins with skilled operators. Quality guarantee, price match promise and Zero Harm safety. Free quotes: 0476 676 639."
    return head(title, desc, f"{SITE}/", ld) + body


# ------------------------------------------------------------- services ----
def build_services():
    rows = []
    data = {
        "excavator-hire": "Footings, trenches, site cuts, dams and detailed excavation with precision operators.",
        "bobcat-hire": "Tight-access clearing, levelling, spreading and site cleanups on any block.",
        "tipper-truck-hire": "Spoil off site, fill on site, on time — haulage that keeps the program moving.",
        "combo-hire": "Machines and trucks bundled into one package, priced for your project.",
        "posi-track-hire": "Tracked loaders with traction and control for soft, wet or sloped ground.",
        "skip-bin-hire": "Bins delivered, filled and removed in the same booking as your machines.",
        "water-truck-hire": "Dust suppression, compaction watering and haul-road maintenance.",
    }
    for i, (slug, name) in enumerate(SERVICES):
        rows.append(f'''          <article class="service-card reveal">
            <span class="card-num" aria-hidden="true">{i+1:02d}</span>
            <h3>{name}</h3>
            <p>{data[slug]}</p>
            <a class="card-link" href="{slug}.html">View {name} {ICONS['arrow'].replace('width="16" height="16"', 'width="14" height="14"')}</a>
          </article>''')
    rows_html = "\n".join(rows)
    ld = f'''  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "ItemList",
    "name": "Civil contracting services in Logan",
    "itemListElement": [
{",".join([chr(10) + f'      {{"@type": "Service", "position": {i+1}, "name": "{name}", "areaServed": "Logan QLD", "url": "{SITE}/{slug}.html", "provider": {{"@id": "{SITE}/#business"}}}}' for i, (slug, name) in enumerate(SERVICES)] + [chr(10) + f'      {{"@type": "Service", "position": {len(SERVICES)+i+1}, "name": "{name}", "areaServed": "Logan QLD", "url": "{SITE}/{slug}.html", "provider": {{"@id": "{SITE}/#business"}}}}' for i, (slug, name, _, _) in enumerate(CIVIL_SERVICES)])}
    ]
  }}
  </script>
'''
    body = f'''{header('services')}
  <main id="main">
    <section class="page-hero" style="--hero-img: url('{IMG['site1']}')">
      <div class="container">
        <nav class="breadcrumbs" aria-label="Breadcrumb"><a href="index.html">Home</a> <span aria-hidden="true">/</span> <span aria-current="page">What We Offer</span></nav>
        <p class="eyebrow-line">L&amp;V Civil Contracting</p>
        <h1>Wet hire &amp; civil works, end to end.</h1>
        <p>Every machine we send out comes with an experienced, ticketed operator — backed by a quality guarantee, price match promise and Zero Harm safety focus. Hire a single unit or bundle a combo priced for your project.</p>
        <div class="hero-actions rise" style="--delay:.32s">
          <a href="contact.html" class="btn btn-primary">Get a free quote {ICONS['arrow']}</a>
          <a href="tel:{PHONE_TEL}" class="btn btn-ghost">{ICONS['phone'].format(s=16)} Call now</a>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="card-grid">
{rows_html}
        </div>
      </div>
    </section>

{civil_section("section-tint")}{cta_band("Not sure which machine you need?", "Describe the job — we'll spec the right combo and quote it within 24 hours.")}  </main>
{footer()}'''
    title = "What We Offer — Wet Hire &amp; Civil Services in Logan | L&amp;V Civil Contracting"
    desc = "Wet hire across Logan QLD — excavators, bobcats, tippers, posi tracks, skip bins and water trucks — plus civil works for renewable energy subdivisions, wind and solar farms, pipelines and gas gathering."
    return head(title, desc, f"{SITE}/services.html", ld) + body


# ------------------------------------------------------ service detail -----
SERVICE_PAGES = {
    "excavator-hire": {
        "img": "excavator",
        "h1": "Excavator Hire in Logan",
        "desc": "Fully operated excavator hire across Logan QLD — trenching, footings, site cuts and detailed excavation with a quality guarantee and Zero Harm safety focus. Free quotes on 0476 676 639.",
        "intro": [
            "From tight residential digs to bulk earthworks, our operated excavators handle footings, trenches, dams, site cuts, detailed excavation and material handling across Logan — including Park Ridge, Jimboomba, Greenbank and surrounding suburbs.",
            "Every hire is wet hire: an experienced, ticketed operator is included with the machine, so you get production from the first hour instead of a learning curve. Backed by our quality guarantee, price match promise and Zero Harm safety focus.",
        ],
        "includes": [
            ("Experienced operator included", "Ticketed, inducted and ready to work from the first hour."),
            ("The right attachments", "Buckets, augers and rippers matched to your ground conditions."),
            ("Clean, to-spec finish", "Dug to depth, batters trimmed, spoil managed properly."),
        ],
        "tags": ["Trenching", "Footings", "Site cuts", "Dams", "Detailed excavation"],
        "related": ["tipper-truck-hire", "combo-hire", "posi-track-hire"],
    },
    "bobcat-hire": {
        "img": "work",
        "h1": "Bobcat Hire in Logan",
        "desc": "Operated bobcat hire in Logan QLD for tight-access clearing, levelling, spreading and site cleanups. Family owned, fully insured, free quotes on 0476 676 639.",
        "intro": [
            "When the block is tight and the tolerances are tighter, our operated bobcats deliver: clearing, levelling, spreading soil and gravel, backfilling and site cleanups across Logan's residential and commercial sites.",
            "Skid steers shine where bigger machines can't fit — driveways, backyards, between-builds access. Pair one with a tipper for a dig-and-cart package that keeps waste moving off site as fast as it's loaded.",
        ],
        "includes": [
            ("Tight-access capability", "Compact machines sized for suburban blocks and narrow entries."),
            ("Finishing-grade work", "Levelling and spreading to the grades your slab or turf needs."),
            ("Fast site cleanups", "Rubbish, green waste and spoil loaded out efficiently."),
        ],
        "tags": ["Tight access", "Levelling", "Spreading", "Backfilling", "Cleanups"],
        "related": ["posi-track-hire", "tipper-truck-hire", "skip-bin-hire"],
    },
    "tipper-truck-hire": {
        "img": "pano",
        "h1": "Tipper Hire in Logan",
        "desc": "Tipper truck hire across Logan QLD — spoil removal, material delivery and dig-and-cart packages with experienced drivers. Free quotes on 0476 676 639.",
        "intro": [
            "Spoil off site, fill on site, on time. Our tippers move earth, aggregate, green waste and demolition material across Logan — efficiently, legally loaded and driven by experienced operators.",
            "Tippers pair naturally with our excavators and loaders: book a dig-and-cart combo and the whole cycle runs as one crew, so your excavation never waits on a truck.",
        ],
        "includes": [
            ("Experienced drivers", "Load management and site access handled properly."),
            ("Flexible scheduling", "One-off loads or all-day cart-away programs."),
            ("Combo-ready", "Seamless pairing with our excavators, bobcats and posi tracks."),
        ],
        "tags": ["Spoil removal", "Material delivery", "Dig & cart", "Demolition cart-away"],
        "related": ["excavator-hire", "combo-hire", "skip-bin-hire"],
    },
    "combo-hire": {
        "img": "hero",
        "h1": "Combo Hire in Logan",
        "desc": "Combo plant hire packages in Logan QLD — excavator and tipper, loader and water truck, or a full site-prep crew. One booking, one invoice. Free quotes on 0476 676 639.",
        "intro": [
            "Most jobs need more than one machine — so we price them that way. Combo hire bundles machines, trucks and operators into a single package sized for your project: excavator plus tipper, loader plus water truck, or a full site-preparation crew.",
            "One booking, one invoice, one crew that's used to working together. Combos are how our regular builders and contractors get the sharpest rates and the smoothest programs.",
        ],
        "includes": [
            ("Package pricing", "Bundled rates that beat hiring each unit separately."),
            ("A crew that clicks", "Operators who work together every week, not strangers on site."),
            ("Sized to the job", "From a two-machine dig-and-cart to full site prep."),
        ],
        "tags": ["Excavator + tipper", "Loader + water truck", "Full site prep", "One invoice"],
        "related": ["excavator-hire", "tipper-truck-hire", "water-truck-hire"],
    },
    "posi-track-hire": {
        "img": "machine",
        "h1": "Posi Track Hire in Logan",
        "desc": "Fully operated posi track hire across Logan QLD — traction and control on soft, wet or sloped ground. Family owned with a Zero Harm safety focus. Free quotes on 0476 676 639.",
        "intro": [
            "When soft ground and unstable surfaces stop wheeled machines, tracked loaders keep working. Our fully operated posi tracks deliver traction, flotation and control on wet, sandy or sloped sites across Logan — Park Ridge, Loganlea, Jimboomba and beyond.",
            "Lower ground pressure means less damage to lawns, driveways and finished surfaces, and more working days when the weather turns. Backed by our quality guarantee, price match promise and Zero Harm safety focus.",
        ],
        "includes": [
            ("All-terrain traction", "Rubber tracks that work soft, wet and sloped ground safely."),
            ("Surface-friendly", "Low ground pressure protects finished areas and access routes."),
            ("Weather resilience", "Keep the program moving when wheels would bog."),
        ],
        "tags": ["Soft ground", "Wet sites", "Slopes", "Low ground pressure"],
        "related": ["bobcat-hire", "excavator-hire", "combo-hire"],
    },
    "skip-bin-hire": {
        "img": "excavator",
        "h1": "Skip Bin Hire in Logan",
        "desc": "Skip bin hire across Logan QLD — bins delivered, filled and removed in the same booking as your earthmoving. Free quotes on 0476 676 639.",
        "intro": [
            "Site waste shouldn't need a second phone call. Our skip bins are delivered, swapped and removed on your schedule — and because they're booked alongside our machines, waste handling becomes part of the same job, not an extra one.",
            "Green waste, demolition material, general site waste — sized to the job and placed where your crew actually needs them.",
        ],
        "includes": [
            ("Delivered & removed on time", "Bins arrive when the job starts and leave when it's done."),
            ("One booking with your machines", "Waste handled inside the same hire package."),
            ("Right size, right spot", "Placed for your workflow, not the truck's convenience."),
        ],
        "tags": ["Green waste", "Demolition waste", "Site waste", "Bin swaps"],
        "related": ["tipper-truck-hire", "bobcat-hire", "combo-hire"],
    },
    "water-truck-hire": {
        "img": "site2",
        "h1": "Water Truck Hire in Logan",
        "desc": "Water truck hire in Logan QLD — dust suppression, compaction watering and haul-road maintenance that keeps sites compliant. Free quotes on 0476 676 639.",
        "intro": [
            "Keep dust down and compaction up. Our water trucks handle dust suppression, compaction watering, haul-road maintenance and general site wet-down across Logan's civil and construction sites.",
            "Dust management isn't just neighbourly — it's a compliance condition on most sites. A scheduled water truck keeps you covered without slowing the program, and pairs naturally with our rollers-and-earthworks combos.",
        ],
        "includes": [
            ("Dust suppression runs", "Scheduled or on-call wet-downs that keep you compliant."),
            ("Compaction watering", "Moisture conditioning for spec-ready compaction results."),
            ("Haul-road maintenance", "Safer, cleaner running surfaces for your site traffic."),
        ],
        "tags": ["Dust suppression", "Compaction", "Haul roads", "Site wet-down"],
        "related": ["combo-hire", "excavator-hire", "tipper-truck-hire"],
    },
}


def build_service(slug):
    d = SERVICE_PAGES[slug]
    name = dict(SERVICES)[slug]
    inc = "\n".join(
        f'''            <li><span class="tick">{ICONS['tick']}</span><div><strong>{t}</strong><span>{s}</span></div></li>'''
        for t, s in d["includes"]
    )
    tags = "".join(f'<span class="tag">{t}</span>' for t in d["tags"])
    rel = "\n".join(
        f'            <a href="{r}.html">{dict(SERVICES)[r]}</a>' for r in d["related"]
    )
    intro = "\n".join(f"          <p>{p}</p>" for p in d["intro"])
    ld = f'''  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Service",
    "name": "{name} in Logan",
    "serviceType": "{name}",
    "areaServed": "Logan QLD",
    "url": "{SITE}/{slug}.html",
    "provider": {{"@id": "{SITE}/#business"}}
  }}
  </script>
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [
      {{"@type": "ListItem", "position": 1, "name": "Home", "item": "{SITE}/"}},
      {{"@type": "ListItem", "position": 2, "name": "What We Offer", "item": "{SITE}/services.html"}},
      {{"@type": "ListItem", "position": 3, "name": "{name}"}}
    ]
  }}
  </script>
'''
    body = f'''{header('services')}
  <main id="main">
    <section class="page-hero" style="--hero-img: url('{IMG[d['img']]}')">
      <div class="container">
        <nav class="breadcrumbs" aria-label="Breadcrumb"><a href="index.html">Home</a> <span aria-hidden="true">/</span> <a href="services.html">What We Offer</a> <span aria-hidden="true">/</span> <span aria-current="page">{name}</span></nav>
        <p class="eyebrow-line">L&amp;V Civil Contracting</p>
        <h1>{d['h1']}</h1>
        <p>Backed by a quality guarantee, price match promise and Zero Harm safety focus — our family owned crew delivers reliable results every time.</p>
        <div class="hero-actions">
          <a href="tel:{PHONE_TEL}" class="btn btn-primary">{ICONS['phone'].format(s=16)} Call now</a>
          <a href="contact.html" class="btn btn-ghost">Request a quote</a>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container split">
        <div class="service-body reveal">
          <span class="eyebrow">Wet hire</span>
          <h2>Logan {name}</h2>
{intro}
          <div class="tag-row">{tags}</div>
        </div>
        <div class="split-media reveal">
          <img src="{IMG[d['img']]}" alt="{name} — L&amp;V Civil Contracting machine working on a Logan site" loading="lazy" width="1200" height="800">
          <div class="badge-float">{ICONS['shield'].format(s=26)} Operator included</div>
        </div>
      </div>
    </section>

    <section class="section section-tint">
      <div class="container split">
        <div class="reveal">
          <span class="eyebrow">What's included</span>
          <h2 style="font-size: var(--fs-h2); font-weight: 800;">Everything the job needs, nothing it doesn't.</h2>
          <ul class="check-list">
{inc}
          </ul>
        </div>
        <div class="reveal">
          <span class="eyebrow">Keep exploring</span>
          <h2 style="font-size: clamp(1.3rem, 2.6vw, 1.8rem); font-weight: 800;">Pairs well with</h2>
          <div class="related">
{rel}
            <a href="services.html">All services →</a>
          </div>
          <p style="margin-top:1.75rem; color: var(--steel-400); font-size: 0.95rem;">Most projects combine two or more services — ask about a <a href="combo-hire.html" style="color: var(--amber-500); font-weight: 600;">combo package</a> and save on the bundle.</p>
        </div>
      </div>
    </section>
{cta_band(f"Need {name.lower()} this week?", "Call now or send the details — quotes back within 24 hours.")}  </main>
{footer()}'''
    title = f"{d['h1']} | L&amp;V Civil Contracting"
    return head(title, d["desc"], f"{SITE}/{slug}.html", ld) + body


# ------------------------------------------------------- civil projects ----
CIVIL_PAGES = {
    "renewable-energy-subdivisions": {
        "img": "pano",
        "h1": "Renewable Energy Subdivision Works",
        "desc": "Civil works for renewable energy subdivisions across Logan and South East Queensland — earthworks, trenching, access roads and service installation. Free quotes on 0476 676 639.",
        "intro": [
            "Efficient infrastructure supports every renewable build. We deliver earthworks, trenching, access roads and service installation for reliable, future-ready energy subdivisions of any size.",
            "From the first cut to the last service trench, our crew works to program alongside your engineers and project managers — with documented SWMS, maintained plant and a Zero Harm safety focus on every stage.",
        ],
        "includes": [
            ("Bulk & detailed earthworks", "Cut, fill and shaping to design levels across the subdivision."),
            ("Trenching & service installation", "Power, comms and water runs trenched, bedded and reinstated to spec."),
            ("Access roads & hardstands", "All-weather routes built for construction traffic and ongoing operations."),
        ],
        "tags": ["Earthworks", "Trenching", "Access roads", "Service installation"],
        "related": ["wind-farms", "solar-farms", "site-preparation"],
    },
    "site-preparation": {
        "img": "site1",
        "h1": "Site Preparation in Logan",
        "desc": "Site preparation across Logan QLD — clearing, levelling, grading and stabilising for safe, accessible and compliant construction sites. Free quotes on 0476 676 639.",
        "intro": [
            "Getting ready to build? We clear, level, grade and stabilise land to create safe, accessible and compliant sites for all types of construction work.",
            "Whether it's a single house pad or a staged commercial development, foundations done right start with ground done right — and our operators know Logan's soils, falls and council requirements inside out.",
        ],
        "includes": [
            ("Clearing & grubbing", "Vegetation, stumps and rubbish removed and carted away."),
            ("Levelling & grading", "Pads, batters and falls cut to the levels your build needs."),
            ("Stabilising & compaction", "Ground conditioned and compacted for a compliant, build-ready site."),
        ],
        "tags": ["Clearing", "Levelling", "Grading", "Stabilising"],
        "related": ["excavator-hire", "bobcat-hire", "water-truck-hire"],
    },
    "wind-farms": {
        "img": "machine",
        "h1": "Wind Farm Civil Works",
        "desc": "Wind farm civil works — crane pads, internal roads and trench networks supporting smooth turbine transport and installation. L&V Civil Contracting: 0476 676 639.",
        "intro": [
            "Strong access and stable foundations are key. We construct crane pads, internal roads and trench networks to support smooth wind turbine transport and installation.",
            "Turbine components don't wait for bad ground — our crews build the all-weather access and lay-down areas that keep oversize transport, cranage and cabling works moving to program.",
        ],
        "includes": [
            ("Crane pads & hardstands", "Engineered pads built and compacted for heavy-lift cranage."),
            ("Internal road networks", "Haul and access roads shaped for oversize turbine transport."),
            ("Trench networks", "Collector and comms trenching, bedded and reinstated to spec."),
        ],
        "tags": ["Crane pads", "Internal roads", "Trench networks", "Turbine access"],
        "related": ["renewable-energy-subdivisions", "solar-farms", "water-truck-hire"],
    },
    "solar-farms": {
        "img": "site2",
        "h1": "Solar Farm Civil Works",
        "desc": "Solar farm civil works — we shape, stabilise and trench land to support arrays, inverters and access routes that last. L&V Civil Contracting: 0476 676 639.",
        "intro": [
            "Power your solar project with precision groundwork. We shape, stabilise, and trench land to support arrays, inverters, and access routes that last.",
            "Solar sites live or die on drainage, levels and access. We grade array areas to tolerance, trench cable runs cleanly and build the roads that keep construction and maintenance traffic moving in any weather.",
        ],
        "includes": [
            ("Array area shaping", "Ground graded and stabilised to the tolerances your racking needs."),
            ("Cable & service trenching", "DC, AC and comms runs trenched, bedded and backfilled properly."),
            ("Access routes & drainage", "Roads and drainage that protect the asset for the long haul."),
        ],
        "tags": ["Array areas", "Cable trenching", "Access routes", "Drainage"],
        "related": ["renewable-energy-subdivisions", "wind-farms", "posi-track-hire"],
    },
    "pipe-and-gas-lines": {
        "img": "work",
        "h1": "Pipe &amp; Gas Line Works",
        "desc": "Pipeline and gas line civil works — safe trenching, backfilling and reinstatement that keeps your infrastructure protected and compliant. Call 0476 676 639.",
        "intro": [
            "Installing pipelines or gas lines? We offer safe trenching, backfilling and reinstatement services to keep your infrastructure protected and compliant.",
            "Linear works demand consistency: trench to depth, bed properly, backfill and compact in lifts, reinstate the surface. Our operators run that cycle day in, day out — safely, and to your inspection and test plan.",
        ],
        "includes": [
            ("Trenching to spec", "Depth, width and bedding to your alignment drawings."),
            ("Backfill & compaction", "Select fill placed and compacted in lifts, tested as required."),
            ("Reinstatement", "Surfaces returned to condition — pavements, topsoil and turf."),
        ],
        "tags": ["Trenching", "Backfilling", "Reinstatement", "Compliance"],
        "related": ["gas-gathering", "excavator-hire", "water-truck-hire"],
    },
    "gas-gathering": {
        "img": "hero",
        "h1": "Gas Gathering Works",
        "desc": "Gas gathering civil works — trenching, grading and access routes supporting efficient, safe transport of extracted gas to processing. Call 0476 676 639.",
        "intro": [
            "Connect sites with expert gas gathering works. We trench, grade, and form access routes to support efficient, safe transport of extracted gas to processing.",
            "From site clearing for gathering networks to trench and access programs across multiple wellsites, we bring the plant, operators and safety systems that field work demands.",
        ],
        "includes": [
            ("Gathering trench networks", "Flowline and service trenching across the gathering field."),
            ("Grading & pads", "Wellsite and facility pads cut, shaped and compacted."),
            ("Access routes", "Formed access that stands up to field traffic year-round."),
        ],
        "tags": ["Trench networks", "Grading", "Well pads", "Access routes"],
        "related": ["pipe-and-gas-lines", "renewable-energy-subdivisions", "excavator-hire"],
    },
}


def build_civil(slug):
    d = CIVIL_PAGES[slug]
    name = CIVIL_NAMES[slug]
    all_names = {**dict(SERVICES), **CIVIL_NAMES}
    inc = "\n".join(
        f'''            <li><span class="tick">{ICONS['tick']}</span><div><strong>{t}</strong><span>{s}</span></div></li>'''
        for t, s in d["includes"]
    )
    tags = "".join(f'<span class="tag">{t}</span>' for t in d["tags"])
    rel = "\n".join(
        f'            <a href="{r}.html">{all_names[r]}</a>' for r in d["related"]
    )
    intro = "\n".join(f"          <p>{p}</p>" for p in d["intro"])
    ld = f'''  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Service",
    "name": "{name}",
    "serviceType": "{name}",
    "areaServed": "Logan QLD",
    "url": "{SITE}/{slug}.html",
    "provider": {{"@id": "{SITE}/#business"}}
  }}
  </script>
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [
      {{"@type": "ListItem", "position": 1, "name": "Home", "item": "{SITE}/"}},
      {{"@type": "ListItem", "position": 2, "name": "What We Offer", "item": "{SITE}/services.html"}},
      {{"@type": "ListItem", "position": 3, "name": "{name}"}}
    ]
  }}
  </script>
'''
    body = f'''{header('services')}
  <main id="main">
    <section class="page-hero" style="--hero-img: url('{IMG[d['img']]}')">
      <div class="container">
        <nav class="breadcrumbs" aria-label="Breadcrumb"><a href="index.html">Home</a> <span aria-hidden="true">/</span> <a href="services.html">What We Offer</a> <span aria-hidden="true">/</span> <span aria-current="page">{name}</span></nav>
        <p class="eyebrow-line">L&amp;V Civil Contracting</p>
        <h1>{d['h1']}</h1>
        <p>Backed by a quality guarantee, price match promise and Zero Harm safety focus — our family owned crew delivers reliable results every time.</p>
        <div class="hero-actions">
          <a href="tel:{PHONE_TEL}" class="btn btn-primary">{ICONS['phone'].format(s=16)} Call now</a>
          <a href="contact.html" class="btn btn-ghost">Request a quote</a>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container split">
        <div class="service-body reveal">
          <span class="eyebrow">Civil works</span>
          <h2>{name}</h2>
{intro}
          <div class="tag-row">{tags}</div>
        </div>
        <div class="split-media reveal">
          <img src="{IMG[d['img']]}" alt="{name} — L&amp;V Civil Contracting working on site" loading="lazy" width="1200" height="800">
          <div class="badge-float">{ICONS['shield'].format(s=26)} Licensed &amp; insured</div>
        </div>
      </div>
    </section>

    <section class="section section-tint">
      <div class="container split">
        <div class="reveal">
          <span class="eyebrow">What we deliver</span>
          <h2 style="font-size: var(--fs-h2); font-weight: 800;">Scoped, staged and done to spec.</h2>
          <ul class="check-list">
{inc}
          </ul>
        </div>
        <div class="reveal">
          <span class="eyebrow">Keep exploring</span>
          <h2 style="font-size: clamp(1.3rem, 2.6vw, 1.8rem); font-weight: 800;">Pairs well with</h2>
          <div class="related">
{rel}
            <a href="services.html">All services →</a>
          </div>
          <p style="margin-top:1.75rem; color: var(--steel-400); font-size: 0.95rem;">Every machine on our civil projects is wet hire — skilled, ticketed operators included. Ask about a <a href="combo-hire.html" style="color: var(--amber-500); font-weight: 600;">combo package</a> for multi-machine programs.</p>
        </div>
      </div>
    </section>
{cta_band("Ready to scope your project?", "Send the drawings or describe the job — quotes back within 24 hours.")}  </main>
{footer()}'''
    title = f"{d['h1']} | L&amp;V Civil Contracting"
    return head(title, d["desc"], f"{SITE}/{slug}.html", ld) + body


# ------------------------------------------------------------ suburbs ------
def build_suburb(slug):
    name, paras, highlights = SUBURBS[slug]
    page = f"earthmoving-{slug}.html"
    intro = "\n".join(f"          <p>{p}</p>" for p in paras)
    tags = "".join(f'<span class="tag">{t}</span>' for t in highlights)
    others = "\n".join(
        f'            <a href="earthmoving-{k}.html">{v[0]}</a>'
        for k, v in SUBURBS.items() if k != slug
    )
    svc_links = "\n".join(
        f'            <a href="{sslug}.html">{sname}</a>' for sslug, sname in SERVICES
    )
    ld = f'''  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Service",
    "name": "Earthmoving and wet hire in {name}",
    "serviceType": "Earthmoving and plant hire",
    "areaServed": {{"@type": "Place", "name": "{name} QLD"}},
    "url": "{SITE}/{page}",
    "provider": {{"@id": "{SITE}/#business"}}
  }}
  </script>
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [
      {{"@type": "ListItem", "position": 1, "name": "Home", "item": "{SITE}/"}},
      {{"@type": "ListItem", "position": 2, "name": "Service Areas", "item": "{SITE}/#areas"}},
      {{"@type": "ListItem", "position": 3, "name": "{name}"}}
    ]
  }}
  </script>
'''
    body = f'''{header('services')}
  <main id="main">
    <section class="page-hero" style="--hero-img: url('{IMG['hero']}')">
      <div class="container">
        <nav class="breadcrumbs" aria-label="Breadcrumb"><a href="index.html">Home</a> <span aria-hidden="true">/</span> <a href="index.html#areas">Service Areas</a> <span aria-hidden="true">/</span> <span aria-current="page">{name}</span></nav>
        <p class="eyebrow-line">L&amp;V Civil Contracting</p>
        <h1>Excavator Hire &amp; Earthmoving in {name}</h1>
        <p>Wet hire machines with skilled operators, servicing {name} from our Park Ridge base — backed by a quality guarantee, price match promise and Zero Harm safety focus.</p>
        <div class="hero-actions">
          <a href="tel:{PHONE_TEL}" class="btn btn-primary">{ICONS['phone'].format(s=16)} Call now</a>
          <a href="contact.html" class="btn btn-ghost">Request a quote</a>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container split">
        <div class="service-body reveal">
          <span class="eyebrow">Local wet hire</span>
          <h2>Earthmoving in {name}, done by locals.</h2>
{intro}
          <div class="tag-row">{tags}</div>
        </div>
        <div class="split-media reveal">
          <img src="{IMG['trench']}" alt="L&amp;V Civil Contracting excavator working in {name} QLD" loading="lazy" width="1200" height="896">
          <div class="badge-float">{ICONS['pin'].format(s=24)} Servicing {name} from Park Ridge</div>
        </div>
      </div>
    </section>

    <section class="section section-tint">
      <div class="container split">
        <div class="reveal">
          <span class="eyebrow">What we offer in {name}</span>
          <h2 style="font-size: var(--fs-h2); font-weight: 800;">Every machine, operator included.</h2>
          <div class="related">
{svc_links}
          </div>
        </div>
        <div class="reveal">
          <span class="eyebrow">Nearby areas</span>
          <h2 style="font-size: clamp(1.3rem, 2.6vw, 1.8rem); font-weight: 800;">We also service</h2>
          <div class="related">
{others}
          </div>
        </div>
      </div>
    </section>
{cta_band(f"Working on a {name} project?", "Free quotes within 24 hours. Machines with operators included.")}  </main>
{footer()}'''
    title = f"Excavator Hire &amp; Earthmoving {name} | L&amp;V Civil Contracting"
    desc = f"Local wet hire earthmoving in {name} QLD — excavators, bobcats, tippers, posi tracks and water trucks with skilled operators, servicing {name} from Park Ridge. Free quotes: {PHONE_DISPLAY}."
    return head(title, desc, f"{SITE}/{page}", ld) + body


# ---------------------------------------------------------------- about ----
def build_about():
    ld = f'''  <script type="application/ld+json">
  {{"@context": "https://schema.org", "@type": "AboutPage", "name": "About L&V Civil Contracting", "url": "{SITE}/about.html", "about": {{"@id": "{SITE}/#business"}}}}
  </script>
'''
    body = f'''{header('about')}
  <main id="main">
    <section class="page-hero" style="--hero-img: url('{IMG['pano']}')">
      <div class="container">
        <nav class="breadcrumbs" aria-label="Breadcrumb"><a href="index.html">Home</a> <span aria-hidden="true">/</span> <span aria-current="page">Who We Are</span></nav>
        <p class="eyebrow-line">L&amp;V Civil Contracting</p>
        <h1>The family crew behind Logan's ground works.</h1>
        <p>Built job by job, referral by referral. Family owned and operated since 2022 — and still answering every call ourselves.</p>
      </div>
    </section>

    <section class="section">
      <div class="container split">
        <div class="reveal">
          <span class="eyebrow">Our story</span>
          <h2 style="font-size: var(--fs-h2); font-weight: 800;">Built by family. Proven on site.</h2>
          <p style="margin-top:1rem;">L&amp;V Civil Contracting started in early 2022 as a family owned and operated outfit in Park Ridge, delivering wet hire earthmoving and civil works across the Logan region. The formula was simple: turn up on time, do the job properly, and leave the site better than you found it.</p>
          <p style="margin-top:1rem;">What started with a single machine has grown into a versatile fleet covering everything from tight-access residential digs to gas gathering and renewable energy project works. The formula hasn't changed: straight-up pricing, safety without shortcuts, and a site left better than we found it.</p>
          <ul class="check-list">
            <li><span class="tick">{ICONS['tick']}</span><div><strong>Same operators, same standards</strong><span>The people who built the reputation are still on the machines.</span></div></li>
            <li><span class="tick">{ICONS['tick']}</span><div><strong>Growing fleet, broader reach</strong><span>From residential digs to energy projects across South East Queensland.</span></div></li>
            <li><span class="tick">{ICONS['tick']}</span><div><strong>Modern systems</strong><span>Digital quoting, scheduling and safety management — no paperwork black holes.</span></div></li>
          </ul>
        </div>
        <div class="split-media reveal">
          <img src="{IMG['fleet']}" alt="L&amp;V Civil Contracting earthmoving fleet lined up at dawn" loading="lazy" width="1200" height="896">
          <div class="badge-float">{ICONS['shield'].format(s=26)} Family owned &amp; operated · Est. 2022</div>
        </div>
      </div>
    </section>

    <section class="section section-light">
      <div class="container">
        <div class="section-head center reveal">
          <span class="eyebrow">What we stand for</span>
          <h2>The values behind every job.</h2>
        </div>
        <div class="value-grid">
          <div class="value-card reveal">
            <div class="service-icon" aria-hidden="true">{ICONS['shield'].format(s=26)}</div>
            <h3>Zero Harm, always</h3>
            <p>Every job runs on documented SWMS, inducted crews and maintained plant. Nobody gets hurt on our watch.</p>
          </div>
          <div class="value-card reveal" style="--delay:.07s">
            <div class="service-icon" aria-hidden="true"><svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6 9 17l-5-5"/></svg></div>
            <h3>Do it once, do it right</h3>
            <p>Rework costs everyone. We dig to depth, compact to spec and reinstate properly the first time — guaranteed.</p>
          </div>
          <div class="value-card reveal" style="--delay:.14s">
            <div class="service-icon" aria-hidden="true"><svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87M16 3.13a4 4 0 0 1 0 7.75"/></svg></div>
            <h3>Local, and proud of it</h3>
            <p>We live where we work. Logan builders, plumbers and homeowners aren't just clients — they're neighbours.</p>
          </div>
          <div class="value-card reveal" style="--delay:.21s">
            <div class="service-icon" aria-hidden="true"><svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M13 2 3 14h9l-1 8 10-12h-9l1-8z"/></svg></div>
            <h3>Fair, honest pricing</h3>
            <p>Clear quotes, no hidden extras, and a price match promise we actually honour.</p>
          </div>
        </div>
      </div>
    </section>
{cta_band("Let's talk about your next project.", "Free quotes, straight answers and a crew that shows up.")}  </main>
{footer()}'''
    title = "Who We Are | L&amp;V Civil Contracting — Family Owned Civil Crew, Logan QLD"
    desc = "L&V Civil Contracting is a family owned wet hire and civil works crew based in Park Ridge QLD, servicing Logan and South East Queensland since 2022. Quality guarantee, price match promise, Zero Harm safety."
    return head(title, desc, f"{SITE}/about.html", ld) + body


# -------------------------------------------------------------- contact ----
def build_contact():
    ld = f'''  <script type="application/ld+json">
  {{"@context": "https://schema.org", "@type": "ContactPage", "name": "Contact L&V Civil Contracting", "url": "{SITE}/contact.html", "about": {{"@id": "{SITE}/#business"}}}}
  </script>
'''
    services_opts = "\n".join(f"              <option>{n}</option>" for _, n in SERVICES)
    body = f'''{header('contact')}
  <main id="main">
    <section class="page-hero" style="--hero-img: url('{IMG['trench']}')">
      <div class="container">
        <nav class="breadcrumbs" aria-label="Breadcrumb"><a href="index.html">Home</a> <span aria-hidden="true">/</span> <span aria-current="page">Contact</span></nav>
        <p class="eyebrow-line">L&amp;V Civil Contracting</p>
        <h1>Tell us about the job. We'll quote it in 24 hours.</h1>
        <p>Call, email or drop your project details below — the more you can tell us about the site and scope, the sharper the quote.</p>
      </div>
    </section>

    <section class="section">
      <div class="container contact-grid">
        <div class="reveal">
          <span class="eyebrow">Reach us directly</span>
          <h2 style="font-size: var(--fs-h2); font-weight: 800;">Talk to the crew.</h2>
          <div class="info-tiles">
            <div class="info-tile">
              <div class="service-icon" aria-hidden="true">{ICONS['phone'].format(s=22)}</div>
              <div><strong>Phone</strong><a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></div>
            </div>
            <div class="info-tile">
              <div class="service-icon" aria-hidden="true"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-10 6L2 7"/></svg></div>
              <div><strong>Email</strong><a href="mailto:{EMAIL}">{EMAIL}</a></div>
            </div>
            <div class="info-tile">
              <div class="service-icon" aria-hidden="true">{ICONS['pin'].format(s=22)}</div>
              <div><strong>Base of operations</strong><span>Park Ridge QLD, 4125 — servicing all of Logan &amp; SE QLD</span></div>
            </div>
            <div class="info-tile">
              <div class="service-icon" aria-hidden="true"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6M16 13H8M16 17H8M10 9H8"/></svg></div>
              <div><strong>Business</strong><span>L&amp;V Civil Contracting · ABN {ABN}</span></div>
            </div>
            <div class="info-tile" style="display:block;">
              <strong style="display:block; color: var(--white); margin-bottom: 0.6rem;">Trading hours</strong>
              <table class="hours">
                <tr><td>Monday – Friday</td><td>9:00 am – 5:00 pm</td></tr>
                <tr class="closed"><td>Saturday – Sunday</td><td>Closed</td></tr>
              </table>
            </div>
          </div>
        </div>

        <form class="contact-form reveal" id="quote-form" data-mailto="{EMAIL}" novalidate>
          <h3 style="margin-bottom:1.5rem;">Request a free quote</h3>
          <div class="form-row">
            <div class="field"><label for="f-name">Name</label><input id="f-name" name="name" type="text" autocomplete="name" required></div>
            <div class="field"><label for="f-phone">Phone</label><input id="f-phone" name="phone" type="tel" autocomplete="tel" required></div>
          </div>
          <div class="form-row">
            <div class="field"><label for="f-email">Email</label><input id="f-email" name="email" type="email" autocomplete="email" required></div>
            <div class="field"><label for="f-suburb">Site suburb</label><input id="f-suburb" name="suburb" type="text" placeholder="e.g. Jimboomba"></div>
          </div>
          <div class="field">
            <label for="f-service">Service needed</label>
            <select id="f-service" name="service">
{services_opts}
              <option>Something else</option>
            </select>
          </div>
          <div class="field"><label for="f-message">Project details</label><textarea id="f-message" name="message" placeholder="Tell us about the site, scope and timeframe…"></textarea></div>
          <button type="submit" class="btn btn-primary" style="width:100%;">Send quote request <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M22 2 11 13M22 2l-7 20-4-9-9-4 20-7z"/></svg></button>
          <p class="form-note">Submitting opens your email app with the details pre-filled — or just call us on {PHONE_DISPLAY}.</p>
        </form>
      </div>
    </section>
  </main>
{footer()}'''
    title = "Contact &amp; Free Quotes | L&amp;V Civil Contracting — Logan QLD"
    desc = "Get a free quote for excavation, trenching, wet hire and civil works in Logan QLD. Call L&V Civil Contracting on 0476 676 639 — quotes within 24 hours."
    return head(title, desc, f"{SITE}/contact.html", ld) + body


# ------------------------------------------------------------------ 404 ----
def build_404():
    body = f'''{header()}
  <main id="main">
    <section class="page-hero" style="--hero-img: url('{IMG['hero']}'); min-height: 70vh; display:flex; align-items:center;">
      <div class="container" style="text-align:center;">
        <p class="eyebrow-line" style="justify-content:center;">Error 404</p>
        <h1 style="margin-inline:auto;">Looks like we dug too deep.</h1>
        <p style="margin-inline:auto;">The page you're after doesn't exist or has been moved. Head back to solid ground.</p>
        <div class="hero-actions" style="justify-content:center;">
          <a href="index.html" class="btn btn-primary">Back to home</a>
          <a href="contact.html" class="btn btn-ghost">Contact us</a>
        </div>
      </div>
    </section>
  </main>
{footer()}'''
    out = head("Page Not Found | L&amp;V Civil Contracting", "Page not found.", f"{SITE}/404.html") + body
    return out.replace('<meta name="robots" content="index, follow">', '<meta name="robots" content="noindex">')


# -------------------------------------------------------------- sitemap ----
def build_sitemap():
    urls = [("", "1.0"), ("what-we-do", "0.9"), ("about", "0.7"), ("contact", "0.8")]
    urls += [(slug, "0.8") for slug, _ in SERVICES]
    urls += [(slug, "0.8") for slug, _, _, _ in CIVIL_SERVICES]
    urls += [(f"earthmoving-{slug}", "0.7") for slug in SUBURBS]
    entries = "\n".join(
        f'''  <url>
    <loc>{SITE}/{path}</loc>
    <lastmod>2026-07-25</lastmod>
    <changefreq>monthly</changefreq>
    <priority>{pr}</priority>
  </url>''' for path, pr in urls
    )
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{entries}
</urlset>
'''


import os
import re


def transform(html):
    """Rewrite template links to clean, root-absolute URLs matching the live
    site's structure (/about, /what-we-do, /posi-track-hire, ...)."""
    html = html.replace('href="index.html#areas"', 'href="/#areas"')
    html = html.replace('href="index.html"', 'href="/"')
    html = html.replace('href="services.html"', 'href="/what-we-do"')
    html = re.sub(r'href="([a-z0-9-]+)\.html"', r'href="/\1"', html)
    html = html.replace('href="css/style.css"', 'href="/css/style.css"')
    html = html.replace('href="favicon.svg"', 'href="/favicon.svg"')
    html = html.replace('src="js/main.js"', 'src="/js/main.js"')
    html = html.replace('src="assets/logo.svg"', 'src="/assets/logo.svg"')
    html = html.replace('src="assets/logo.jpg"', 'src="/assets/logo.jpg"')
    html = html.replace('href="favicon.ico"', 'href="/favicon.ico"')
    html = html.replace(f'{SITE}/services.html', f'{SITE}/what-we-do')
    html = re.sub(re.escape(SITE) + r'/([a-z0-9-]+)\.html', SITE + r'/\1', html)
    return html


if __name__ == "__main__":
    pages = {
        "index.html": build_index(),
        "what-we-do/index.html": build_services(),
        "about/index.html": build_about(),
        "contact/index.html": build_contact(),
        "404.html": build_404(),
    }
    for slug, _ in SERVICES:
        pages[f"{slug}/index.html"] = build_service(slug)
    for slug in CIVIL_PAGES:
        pages[f"{slug}/index.html"] = build_civil(slug)
    for slug in SUBURBS:
        pages[f"earthmoving-{slug}/index.html"] = build_suburb(slug)
    for fname, content in pages.items():
        d = os.path.dirname(fname)
        if d:
            os.makedirs(d, exist_ok=True)
        with open(fname, "w") as f:
            f.write(transform(content))
        print(f"wrote {fname}")
    with open("sitemap.xml", "w") as f:
        f.write(build_sitemap())
    print("wrote sitemap.xml")
