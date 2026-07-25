# L&V Civil Contracting — Website

Redesigned website for **L&V Civil Contracting** (Park Ridge QLD, servicing Logan &
South East Queensland) — a client project by **KW | Innovations**.

## Stack

Pure static site — no build step, no framework, no dependencies. Deploy the repository
root to any static host (GitHub Pages, Netlify, Vercel, Cloudflare Pages, cPanel, S3…).

```
index.html      Home — hero, service ticker, services overview, why us, process,
                service areas, CTA
services.html   Full service detail (excavators, bobcats, tippers, water trucks,
                trenching, gas gathering, renewables civil, combos & skip bins)
about.html      Company story + values
contact.html    Contact details + quote request form (opens a pre-filled email)
404.html        Not-found page
css/style.css   Design system (dark graphite + safety amber, fluid type, animations)
js/main.js      Nav, scroll reveals, counters, card spotlight, ticker, progress bar,
                parallax, form handler
favicon.svg     L&V brand mark (placeholder — swap for the client's real favicon)
robots.txt / sitemap.xml
```

## Features

- **Mobile-first responsive** — fluid `clamp()` typography, full-screen mobile nav,
  single-column collapses, touch-friendly targets.
- **SEO** — unique titles/descriptions per page, canonical URLs, Open Graph tags,
  JSON-LD structured data (`LocalBusiness`, `Service` list, `AboutPage`,
  `ContactPage`), semantic HTML, sitemap.xml and robots.txt. Canonicals point at the
  existing `www.lvcivilcontracting.com.au` domain to retain its search equity.
- **Performance** — no frameworks, no image downloads (all graphics are inline SVG),
  one CSS file, one deferred JS file, font preconnect.
- **Accessibility** — skip link, ARIA labels/expanded states, keyboard-closable menu,
  `prefers-reduced-motion` support, semantic landmarks.

## Things to update before go-live

1. **Images & favicon** — the original site's images and favicon could not be
   downloaded from the build environment (the domain is behind bot protection and
   blocked by the sandbox network policy). All visuals are currently inline SVG
   illustrations and `favicon.svg` is an L&V placeholder mark. To use the client's
   real assets: save the photos/favicon from the live site or the client's files,
   drop them into an `assets/img/` folder, and swap the `<svg>` blocks /
   `<link rel="icon">` references. Compressed `.webp` with descriptive `alt` text
   recommended.
2. **Email** — enquiries go to `info@lvcivilcontracting.com.au` (in the four HTML
   pages and `js/main.js`). Confirm this mailbox exists or update it — the original
   site's public email could not be verified.
3. **Form backend (optional)** — the quote form opens the visitor's email app
   pre-filled (no backend needed). Swap in Formspree/Netlify Forms/etc. for
   server-side handling if preferred.
4. **Stats** — the animated counters on the home hero (machines, projects) are
   representative placeholders; adjust `data-count` values in `index.html` to the
   client's real numbers.
