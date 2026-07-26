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

URLs are clean and extensionless, matching the live site exactly so existing
Google rankings carry over at cutover (each page is a `<slug>/index.html`
directory; any static host serves these natively):

```
/                       Home — photo hero, promises, services, why-us, FAQ
/what-we-do             Services overview (same path as the live site)
/about  /contact        Who We Are · Contact (details, hours, quote form)
/excavator-hire /bobcat-hire /tipper-hire /combo-hire
/posi-track-hire /skip-bin-hire /water-truck-hire
/earthmoving-{park-ridge,jimboomba,greenbank,yarrabilba,
              flagstone,logan-village,browns-plains}   Suburb SEO pages
404.html                Not-found page
css/ js/ assets/        Design system, interactions, logo
build.py                Static site generator (source of truth for all pages)
robots.txt sitemap.xml favicon.svg
```

Note: links are root-absolute, so preview locally with `python3 -m http.server`
(not file://), and deploy at a domain root (Netlify, Cloudflare Pages, Vercel,
cPanel — or GitHub Pages with a custom domain, not a /project subpath).

## Features

- **Structure mirrors the live site** — top location bar, Who We Are / What We Offer
  (dropdown) / Contact nav, 7 dedicated service pages, quality guarantee + price match
  promise + Zero Harm messaging, trading-hours table, photo-backed footer with rounded
  bottom bar and ABN.
- **Photography & brand** — the client's real photos, logo and favicon from the
  live site; social shares use their branded card via `og:image`.
- **SEO** — unique titles/descriptions/canonicals per page, Open Graph + og:image,
  JSON-LD (LocalBusiness, Service, FAQPage, BreadcrumbList, ItemList), sitemap.xml.
- **Mobile-first** — fluid type, full-screen menu with the services grid, icon-only
  phone button on small screens; verified zero horizontal overflow at 390px.
- **Accessibility** — skip link, ARIA states, keyboard-friendly dropdown
  (focus-within), `prefers-reduced-motion` support.

## Things to update before go-live

1. **Images** — the client's real photos from the live site are optimised to webp
   and re-hosted on the KW Innovations CDN (`IMG` in `build.py`); the real logo
   (`assets/logo.jpg`) and favicon (`favicon.ico`) are in the repo. To self-host
   the photos later, download the `IMG` URLs into `assets/img/` and point the
   dict at local paths.
2. **Reviews** — the homepage embeds the client's Elfsight Google Reviews
   widget (same account as the live site), so their real reviews render
   automatically. Static quote cards can be added via `TESTIMONIALS` in
   `build.py`; never fabricate reviews.
3. **Email** — enquiries go to `info@lvcivilcontracting.com.au` (set in `build.py`
   and `js/main.js`). Confirm this mailbox exists or update it.
4. **Stats** — hero counters (projects delivered etc.) are representative
   placeholders; set real numbers in `build_index()` and re-run `build.py`.
5. **Form backend (optional)** — the quote form opens a pre-filled email; swap in
   Formspree/Netlify Forms for server-side handling if preferred.
