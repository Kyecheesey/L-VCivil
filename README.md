# L&V Civil Contracting — Website

Redesigned website for **L&V Civil Contracting** (Park Ridge QLD 4125, servicing Logan &
South East Queensland) — a client project by **KW | Innovations**.

## Stack

Pure static site — no framework, no dependencies. Deploy the repository root to any
static host (GitHub Pages, Netlify, Vercel, Cloudflare Pages, cPanel, S3…).

Pages are generated from `build.py` (shared header/footer + per-page content). To
change nav, footer, or any page copy, edit `build.py` and run:

```
python3 build.py
```

```
index.html            Home — photo hero, promises, services, why-us, process, areas, FAQ
services.html         What We Offer — overview of all 7 hire services
excavator-hire.html   ┐
bobcat-hire.html      │
tipper-hire.html      │ Dedicated service pages (same slugs as the
combo-hire.html       │ original site, matching its nav dropdown)
posi-track-hire.html  │
skip-bin-hire.html    │
water-truck-hire.html ┘
about.html            Who We Are — story + values
contact.html          Contact — details, trading hours, quote form
404.html              Not-found page
css/style.css         Design system (dark graphite + safety amber)
js/main.js            Nav, dropdown, reveals, counters, ticker, progress bar
build.py              Static site generator (source of truth for all pages)
favicon.svg           L&V mark (placeholder — swap for the client's real favicon)
robots.txt / sitemap.xml
```

## Features

- **Structure mirrors the live site** — top location bar, Who We Are / What We Offer
  (dropdown) / Contact nav, 7 dedicated service pages, quality guarantee + price match
  promise + Zero Harm messaging, trading-hours table, photo-backed footer with rounded
  bottom bar and ABN.
- **Photography** — hero and section imagery hosted on the KW Innovations Higgsfield
  CDN (see `IMG` in `build.py`).
- **SEO** — unique titles/descriptions/canonicals per page, Open Graph + og:image,
  JSON-LD (LocalBusiness, Service, FAQPage, BreadcrumbList, ItemList), sitemap.xml.
- **Mobile-first** — fluid type, full-screen menu with the services grid, icon-only
  phone button on small screens; verified zero horizontal overflow at 390px.
- **Accessibility** — skip link, ARIA states, keyboard-friendly dropdown
  (focus-within), `prefers-reduced-motion` support.

## Things to update before go-live

1. **Images & favicon** — imagery is AI-generated placeholder photography hosted at
   the CDN URLs in `build.py`. Swap for the client's real site/fleet photos when
   available: download them, drop into `assets/img/`, update the `IMG` dict to local
   paths and re-run `build.py`. Same for `favicon.svg` → the client's real favicon.
2. **Email** — enquiries go to `info@lvcivilcontracting.com.au` (set in `build.py`
   and `js/main.js`). Confirm this mailbox exists or update it.
3. **Stats** — hero counters (projects delivered etc.) are representative
   placeholders; set real numbers in `build_index()` and re-run `build.py`.
4. **Form backend (optional)** — the quote form opens a pre-filled email; swap in
   Formspree/Netlify Forms for server-side handling if preferred.
