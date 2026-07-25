# KW | Innovations Civil — Website

Rebranded website for the civil contracting business formerly operating as **L&V Civil
Contracting** (Park Ridge QLD, servicing Logan & South East Queensland), now part of
**KW | Innovations**.

## Stack

Pure static site — no build step, no framework, no dependencies. Deploy the repository
root to any static host (GitHub Pages, Netlify, Vercel, Cloudflare Pages, cPanel, S3…).

```
index.html      Home — hero, services overview, why us, process, service areas, CTA
services.html   Full service detail (excavators, bobcats, tippers, water trucks,
                trenching, gas gathering, renewables civil, combos & skip bins)
about.html      Company story (takeover of L&V Civil) + values
contact.html    Contact details + quote request form (opens a pre-filled email)
404.html        Not-found page
css/style.css   Design system (dark graphite + safety amber, fluid type, animations)
js/main.js      Nav, scroll reveals, counters, card spotlight, form handler
favicon.svg     KW brand mark
robots.txt / sitemap.xml
```

## Features

- **Mobile-first responsive** — fluid `clamp()` typography, full-screen mobile nav,
  single-column collapses, touch-friendly targets.
- **SEO** — unique titles/descriptions per page, canonical URLs, Open Graph tags,
  JSON-LD structured data (`LocalBusiness`, `Service` list, `AboutPage`,
  `ContactPage`), semantic HTML, sitemap.xml and robots.txt.
- **Performance** — no frameworks, no image downloads (all graphics are inline SVG),
  one CSS file, one deferred JS file, font preconnect.
- **Accessibility** — skip link, ARIA labels/expanded states, keyboard-closable menu,
  `prefers-reduced-motion` support, semantic landmarks.

## Things to update before go-live

1. **Domain** — canonical URLs, `sitemap.xml` and `robots.txt` currently point at
   `www.lvcivilcontracting.com.au` (keeping the existing domain preserves its search
   ranking). Search-and-replace if the site moves to a KW Innovations domain, and
   set 301 redirects from the old domain if so.
2. **Email** — the site uses `info@kwinnovations.com.au`; change in the four HTML
   pages and `js/main.js` if a different inbox should receive enquiries.
3. **Form backend (optional)** — the quote form currently opens the visitor's email
   app pre-filled (no backend needed). Swap in Formspree/Netlify Forms/etc. for
   server-side handling if preferred.
4. **Stats** — the animated counters on the home hero (machines, projects) are
   representative placeholders; adjust `data-count` values in `index.html` to the
   real numbers.
5. **Photos** — the illustrated SVG scenes can be replaced with real site/fleet
   photography (use compressed `.webp` files and keep `alt` text descriptive).
