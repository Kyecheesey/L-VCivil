/* L&V Civil Contracting: site interactions */
(function () {
  "use strict";

  // Sticky header state
  const header = document.querySelector(".site-header");
  if (header) {
    const onScroll = () => header.classList.toggle("is-scrolled", window.scrollY > 24);
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
  }

  // Mobile navigation
  const toggle = document.querySelector(".nav-toggle");
  const links = document.querySelector(".nav-links");
  if (toggle && links) {
    const setOpen = (open) => {
      toggle.setAttribute("aria-expanded", String(open));
      links.classList.toggle("is-open", open);
      document.body.classList.toggle("nav-locked", open);
    };
    toggle.addEventListener("click", () => {
      setOpen(toggle.getAttribute("aria-expanded") !== "true");
    });
    links.querySelectorAll("a").forEach((a) => a.addEventListener("click", () => setOpen(false)));
    document.addEventListener("keydown", (e) => {
      if (e.key === "Escape") setOpen(false);
    });
  }

  // Scroll reveal
  const revealEls = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window && revealEls.length) {
    const io = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            entry.target.classList.add("is-visible");
            io.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.12, rootMargin: "0px 0px -40px 0px" }
    );
    revealEls.forEach((el) => io.observe(el));
  } else {
    revealEls.forEach((el) => el.classList.add("is-visible"));
  }

  // Spotlight hover on service cards
  document.querySelectorAll(".service-card").forEach((card) => {
    card.addEventListener("pointermove", (e) => {
      const r = card.getBoundingClientRect();
      card.style.setProperty("--mx", `${e.clientX - r.left}px`);
      card.style.setProperty("--my", `${e.clientY - r.top}px`);
    });
  });

  // Animated counters in the hero stat strip
  const counters = document.querySelectorAll("[data-count]");
  if ("IntersectionObserver" in window && counters.length) {
    const cio = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (!entry.isIntersecting) return;
          const el = entry.target;
          const target = parseFloat(el.dataset.count);
          const suffix = el.dataset.suffix || "";
          const dur = 1400;
          const t0 = performance.now();
          const tick = (t) => {
            const p = Math.min((t - t0) / dur, 1);
            const eased = 1 - Math.pow(1 - p, 3);
            el.textContent = Math.round(target * eased) + suffix;
            if (p < 1) requestAnimationFrame(tick);
          };
          requestAnimationFrame(tick);
          cio.unobserve(el);
        });
      },
      { threshold: 0.6 }
    );
    counters.forEach((el) => cio.observe(el));
  }

  // Multi-step "instant quote" wizard
  document.querySelectorAll(".quote-wizard").forEach((form) => {
    const steps = Array.from(form.querySelectorAll(".form-step"));
    const dots = Array.from(form.querySelectorAll(".wp-step"));
    let current = 1;

    const paint = (dir) => {
      steps.forEach((s) => {
        const n = Number(s.dataset.step);
        s.classList.toggle("is-active", n === current);
      });
      dots.forEach((d) => {
        const n = Number(d.dataset.wp);
        d.classList.toggle("is-active", n === current);
        d.classList.toggle("is-done", n < current);
      });
      const active = form.querySelector(`.form-step[data-step="${current}"]`);
      if (active) {
        active.classList.remove("step-in-l", "step-in-r");
        void active.offsetWidth;
        active.classList.add(dir === "back" ? "step-in-l" : "step-in-r");
        const focusable = active.querySelector("input, select, textarea");
        if (focusable) focusable.focus({ preventScroll: true });
      }
    };

    form.querySelectorAll(".wizard-next").forEach((btn) => {
      btn.addEventListener("click", () => {
        const step = btn.closest(".form-step");
        const invalid = step.querySelector(":invalid");
        if (invalid) {
          invalid.reportValidity();
          return;
        }
        current = Math.min(current + 1, steps.length);
        paint("next");
      });
    });
    form.querySelectorAll(".wizard-back").forEach((btn) => {
      btn.addEventListener("click", () => {
        current = Math.max(current - 1, 1);
        paint("back");
      });
    });
  });

  // Enquiry forms -> pre-filled email (no backend required). Each form sets
  // its recipient via data-mailto; fields not present are skipped.
  document.querySelectorAll("form[data-mailto]").forEach((form) => {
    form.addEventListener("submit", (e) => {
      e.preventDefault();
      const data = new FormData(form);
      const subject = encodeURIComponent(
        `Quote request — ${data.get("service") || "Civil works"}`
      );
      const lines = [];
      [["Name", "name"], ["Phone", "phone"], ["Email", "email"], ["Suburb", "suburb"], ["Service", "service"], ["Timeframe", "timeframe"]]
        .forEach(([label, key]) => {
          if (data.has(key)) lines.push(`${label}: ${data.get(key) || ""}`);
        });
      lines.push("", "Project details:", data.get("message") || "");
      const body = encodeURIComponent(lines.join("\n"));
      window.location.href = `mailto:${form.dataset.mailto}?subject=${subject}&body=${body}`;
    });
  });

  // Gallery filter pills
  const filterRow = document.querySelector(".filter-row");
  const gallery = document.querySelector("[data-gallery]");
  if (filterRow && gallery) {
    const items = gallery.querySelectorAll(".g-item");
    filterRow.addEventListener("click", (e) => {
      const btn = e.target.closest(".filter-pill");
      if (!btn) return;
      filterRow.querySelectorAll(".filter-pill").forEach((p) => p.classList.remove("is-active"));
      btn.classList.add("is-active");
      const filter = btn.dataset.filter;
      items.forEach((item) => {
        const show = filter === "all" || item.dataset.cat === filter;
        item.classList.toggle("is-hidden", !show);
        if (show) {
          item.classList.remove("is-filtering");
          void item.offsetWidth;
          item.classList.add("is-filtering");
        }
      });
    });
  }

  // Ops-style map: pin / legend / route sync, hover highlights, and an
  // auto-cycling spotlight that hands over control on first interaction.
  const pmapWrap = document.querySelector(".pmap-wrap");
  if (pmapWrap) {
    const pins = Array.from(pmapWrap.querySelectorAll(".pmap-pin"));
    const legend = Array.from(pmapWrap.querySelectorAll(".pmap-item"));
    const routes = Array.from(pmapWrap.querySelectorAll(".pmap-route"));
    const ids = legend.map((l) => l.dataset.id);
    let idx = 0;
    let auto = null;

    const paint = (id) => {
      pins.forEach((p) => p.classList.toggle("is-active", p.dataset.id === id));
      legend.forEach((l) => l.classList.toggle("is-active", l.dataset.id === id));
      routes.forEach((r) => r.classList.toggle("is-active", r.dataset.id === id));
    };
    const stopAuto = () => {
      if (auto) {
        clearInterval(auto);
        auto = null;
      }
    };
    const activate = (id) => {
      stopAuto();
      idx = Math.max(0, ids.indexOf(id));
      paint(id);
    };

    pins.forEach((p) => {
      p.addEventListener("click", () => activate(p.dataset.id));
      p.addEventListener("pointerenter", () => activate(p.dataset.id));
      p.addEventListener("keydown", (e) => {
        if (e.key === "Enter" || e.key === " ") {
          e.preventDefault();
          activate(p.dataset.id);
        }
      });
    });
    legend.forEach((l) => {
      l.addEventListener("click", () => activate(l.dataset.id));
      l.addEventListener("pointerenter", () => activate(l.dataset.id));
    });

    if (ids.length) {
      paint(ids[0]);
      if (window.matchMedia("(prefers-reduced-motion: no-preference)").matches) {
        auto = setInterval(() => {
          idx = (idx + 1) % ids.length;
          paint(ids[idx]);
        }, 3200);
      }
    }
  }

  // Interactive service-area map: click a suburb to expand its details and
  // re-centre the embedded map, without needing a paid Maps API key.
  const areaCards = document.querySelectorAll(".area-card");
  const areaMap = document.querySelector("[data-area-map]");
  if (areaCards.length) {
    areaCards.forEach((card) => {
      const toggle = card.querySelector(".area-card-top");
      if (!toggle) return;
      toggle.addEventListener("click", () => {
        const already = card.classList.contains("is-active");
        areaCards.forEach((c) => c.classList.remove("is-active"));
        if (!already) {
          card.classList.add("is-active");
          if (areaMap && card.dataset.q) {
            areaMap.src = `https://maps.google.com/maps?q=${card.dataset.q}&z=13&output=embed`;
          }
        }
      });
    });
  }

  // Footer year
  document.querySelectorAll("[data-year]").forEach((el) => {
    el.textContent = new Date().getFullYear();
  });

  // Hover prefetch fallback for browsers without the Speculation Rules API,
  // so page-to-page navigation stays instant everywhere.
  if (!HTMLScriptElement.supports || !HTMLScriptElement.supports("speculationrules")) {
    const prefetched = new Set();
    document.addEventListener("pointerenter", (e) => {
      const a = e.target.closest && e.target.closest('a[href^="/"]');
      if (!a) return;
      const href = a.getAttribute("href");
      if (prefetched.has(href)) return;
      prefetched.add(href);
      const link = document.createElement("link");
      link.rel = "prefetch";
      link.href = href;
      document.head.appendChild(link);
    }, true);
  }
})();

/* Polish pass: scroll progress bar + hero parallax */
(function () {
  "use strict";

  var bar = document.createElement("div");
  bar.className = "scroll-progress";
  document.body.appendChild(bar);
  var onProg = function () {
    var h = document.documentElement;
    var max = h.scrollHeight - h.clientHeight;
    bar.style.width = (max ? (h.scrollTop / max) * 100 : 0) + "%";
  };
  window.addEventListener("scroll", onProg, { passive: true });
  onProg();

  // Smart header: tuck away on scroll down, return on scroll up
  var hdr = document.querySelector(".site-header");
  var lastY = window.scrollY;
  if (hdr) {
    window.addEventListener("scroll", function () {
      var y = window.scrollY;
      if (document.body.classList.contains("nav-locked")) {
        hdr.classList.remove("nav-hidden");
      } else if (y > 320 && y > lastY + 6) {
        hdr.classList.add("nav-hidden");
      } else if (y < lastY - 6 || y <= 320) {
        hdr.classList.remove("nav-hidden");
      }
      lastY = y;
    }, { passive: true });
  }

  var bp = document.querySelector(".hero-blueprint");
  if (bp && window.matchMedia("(prefers-reduced-motion: no-preference)").matches) {
    window.addEventListener(
      "scroll",
      function () {
        bp.style.transform = "translateY(" + window.scrollY * 0.14 + "px)";
      },
      { passive: true }
    );
  }

  // Hero background video: only autoplay for users who haven't asked for
  // reduced motion; everyone else keeps the static poster frame.
  var heroVideo = document.querySelector(".hero-video");
  if (heroVideo && window.matchMedia("(prefers-reduced-motion: no-preference)").matches) {
    heroVideo.play().catch(function () {});
  }
})();
