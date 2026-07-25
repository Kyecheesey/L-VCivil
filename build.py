#!/usr/bin/env python3
"""Static site generator for L&V Civil Contracting.

Run `python3 build.py` from the repo root to regenerate every HTML page from
the shared header/footer templates and the per-page content below. Keeps all
11 pages consistent without a framework.
"""

# Hosted imagery (generated for the rebrand; swap for client photography by
# replacing these URLs — see README).
IMG = {
    "hero":  "https://d2ol7oe51mr4n9.cloudfront.net/user_3ECT3zt6ovZZHX51H6T4wC5y40O/fb68d3ae-721c-4526-9ee4-37fdb38caf6b.webp",
    "trench": "https://d2ol7oe51mr4n9.cloudfront.net/user_3ECT3zt6ovZZHX51H6T4wC5y40O/a07df28b-26a4-4ab5-b740-d7e8a05611de.webp",
    "fleet": "https://d2ol7oe51mr4n9.cloudfront.net/user_3ECT3zt6ovZZHX51H6T4wC5y40O/e8e0d1bd-4648-4fc9-89d1-b18a2ddbd0bf.webp",
    "water": "https://d2ol7oe51mr4n9.cloudfront.net/user_3ECT3zt6ovZZHX51H6T4wC5y40O/578116e1-fa0a-4b0d-a8fb-904028512463.webp",
}

SITE = "https://www.lvcivilcontracting.com.au"
PHONE_DISPLAY = "0476 676 639"
PHONE_TEL = "+61476676639"
EMAIL = "info@lvcivilcontracting.com.au"
ABN = "63 661 732 869"

SERVICES = [
    ("excavator-hire",   "Excavator Hire"),
    ("bobcat-hire",      "Bobcat Hire"),
    ("tipper-hire",      "Tipper Hire"),
    ("combo-hire",       "Combo Hire"),
    ("posi-track-hire",  "Posi Track Hire"),
    ("skip-bin-hire",    "Skip Bin Hire"),
    ("water-truck-hire", "Water Truck Hire"),
]

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
  <meta property="og:image" content="{IMG['hero']}">
  <meta property="og:locale" content="en_AU">
  <meta name="twitter:card" content="summary_large_image">
  <link rel="icon" type="image/svg+xml" href="favicon.svg">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Archivo:wght@600;700;800;900&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="css/style.css">
{extra}</head>
<body>
  <a class="skip-link" href="#main">Skip to content</a>
'''


def header(active=""):
    def cls(page):
        return ' class="is-active" aria-current="page"' if page == active else ""
    drop_links = "\n".join(
        f'          <a href="{slug}.html">{name}</a>' for slug, name in SERVICES
    )
    return f'''
  <div class="topbar">{ICONS['pin'].format(s=13)}Park Ridge QLD, 4125 — Servicing Logan &amp; South East Queensland</div>
  <header class="site-header">
    <div class="container nav-bar">
      <a class="brand" href="index.html" aria-label="L&amp;V Civil Contracting — home">
        <img src="assets/logo.svg" alt="L&amp;V Civil Contracting" width="98" height="54">
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
    return f'''
  <footer class="site-footer" style="--footer-img: url('{IMG['trench']}')">
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
            <img src="assets/logo.svg" alt="L&amp;V Civil Contracting" width="156" height="86" loading="lazy">
          </a>
          <p>Family owned and operated wet hire and civil works, delivering reliable results across Logan and South East Queensland since 2022.</p>
          <div class="trust-card">
            {ICONS['shield'].format(s=26)}
            <span><strong>Fully licensed &amp; insured</strong><small>Quality guarantee · Price match promise · Zero Harm</small></span>
          </div>
        </div>
        <div>
          <h4>What We Offer</h4>
          <ul>
{offer_links}
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
        <span>Website by KW&nbsp;|&nbsp;Innovations</span>
      </div>
    </div>
  </footer>

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


# ---------------------------------------------------------------- index ----
def build_index():
    ld = f'''  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "LocalBusiness",
    "@id": "{SITE}/#business",
    "name": "L&V Civil Contracting",
    "description": "Family owned wet hire earthmoving, trenching, site preparation and civil construction services across Logan and South East Queensland.",
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
        ("tipper-hire", "Tipper Hire", "Fast, reliable haulage of spoil, fill, aggregate and demolition material — keeping your site moving.",
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
    chips_area = "\n".join(f'          <span class="chip">{s}</span>' for s in suburbs)

    body = f'''{header('home')}
  <main id="main">
    <section class="hero" style="--hero-img: url('{IMG['hero']}')">
      <div class="container hero-inner">
        <p class="hero-eyebrow"><span class="dot" aria-hidden="true"></span> Logan's Trusted Civil Contractor</p>
        <h1>Ground works, <span class="accent">done right.</span></h1>
        <p class="hero-lede">Family owned wet hire earthmoving, trenching and site preparation across Logan and South East Queensland — modern machines with skilled operators, backed by a quality guarantee and a Zero Harm safety focus.</p>
        <div class="hero-chips">{chips}</div>
        <div class="hero-actions">
          <a href="contact.html" class="btn btn-primary">Get a free quote {ICONS['arrow']}</a>
          <a href="tel:{PHONE_TEL}" class="btn btn-ghost">{ICONS['phone'].format(s=16)} {PHONE_DISPLAY}</a>
        </div>
        <div class="hero-stats reveal">
          <div><strong data-count="7">0</strong><span>Hire services</span></div>
          <div><strong data-count="250" data-suffix="+">0</strong><span>Projects delivered</span></div>
          <div><strong data-count="100" data-suffix="%">0</strong><span>Licensed &amp; insured</span></div>
          <div><strong data-count="24" data-suffix="h">0</strong><span>Quote turnaround</span></div>
        </div>
      </div>
      <div class="hero-badge reveal">
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

    <section class="section">
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

    <section class="section section-light" id="areas">
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

    <section class="section">
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
        "tipper-hire": "Spoil off site, fill on site, on time — haulage that keeps the program moving.",
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
{",".join(chr(10) + f'      {{"@type": "Service", "position": {i+1}, "name": "{name}", "areaServed": "Logan QLD", "url": "{SITE}/{slug}.html", "provider": {{"@id": "{SITE}/#business"}}}}' for i, (slug, name) in enumerate(SERVICES))}
    ]
  }}
  </script>
'''
    body = f'''{header('services')}
  <main id="main">
    <section class="page-hero" style="--hero-img: url('{IMG['water']}')">
      <div class="container">
        <nav class="breadcrumbs" aria-label="Breadcrumb"><a href="index.html">Home</a> <span aria-hidden="true">/</span> <span aria-current="page">What We Offer</span></nav>
        <p class="eyebrow-line">L&amp;V Civil Contracting</p>
        <h1>Wet hire &amp; civil works, end to end.</h1>
        <p>Every machine we send out comes with an experienced, ticketed operator — backed by a quality guarantee, price match promise and Zero Harm safety focus. Hire a single unit or bundle a combo priced for your project.</p>
        <div class="hero-actions">
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
{cta_band("Not sure which machine you need?", "Describe the job — we'll spec the right combo and quote it within 24 hours.")}  </main>
{footer()}'''
    title = "What We Offer — Wet Hire &amp; Civil Services in Logan | L&amp;V Civil Contracting"
    desc = "Excavator, bobcat, tipper, combo, posi track, skip bin and water truck hire across Logan QLD — every machine with a skilled operator. Quality guarantee, price match promise, Zero Harm safety."
    return head(title, desc, f"{SITE}/services.html", ld) + body


# ------------------------------------------------------ service detail -----
SERVICE_PAGES = {
    "excavator-hire": {
        "img": "hero",
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
        "related": ["tipper-hire", "combo-hire", "posi-track-hire"],
    },
    "bobcat-hire": {
        "img": "trench",
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
        "related": ["posi-track-hire", "tipper-hire", "skip-bin-hire"],
    },
    "tipper-hire": {
        "img": "fleet",
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
        "related": ["excavator-hire", "tipper-hire", "water-truck-hire"],
    },
    "posi-track-hire": {
        "img": "trench",
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
        "img": "fleet",
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
        "related": ["tipper-hire", "bobcat-hire", "combo-hire"],
    },
    "water-truck-hire": {
        "img": "water",
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
        "related": ["combo-hire", "excavator-hire", "tipper-hire"],
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


# ---------------------------------------------------------------- about ----
def build_about():
    ld = f'''  <script type="application/ld+json">
  {{"@context": "https://schema.org", "@type": "AboutPage", "name": "About L&V Civil Contracting", "url": "{SITE}/about.html", "about": {{"@id": "{SITE}/#business"}}}}
  </script>
'''
    body = f'''{header('about')}
  <main id="main">
    <section class="page-hero" style="--hero-img: url('{IMG['fleet']}')">
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

        <form class="contact-form reveal" id="quote-form" novalidate>
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
    urls = [("", "1.0"), ("services.html", "0.9"), ("about.html", "0.7"), ("contact.html", "0.8")]
    urls += [(f"{slug}.html", "0.8") for slug, _ in SERVICES]
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


if __name__ == "__main__":
    pages = {
        "index.html": build_index(),
        "services.html": build_services(),
        "about.html": build_about(),
        "contact.html": build_contact(),
        "404.html": build_404(),
        "sitemap.xml": build_sitemap(),
    }
    for slug, _ in SERVICES:
        pages[f"{slug}.html"] = build_service(slug)
    for fname, content in pages.items():
        with open(fname, "w") as f:
            f.write(content)
        print(f"wrote {fname}")
