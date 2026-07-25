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

  // Contact form -> pre-filled email (no backend required)
  const form = document.getElementById("quote-form");
  if (form) {
    form.addEventListener("submit", (e) => {
      e.preventDefault();
      const data = new FormData(form);
      const subject = encodeURIComponent(
        `Quote request — ${data.get("service") || "Civil works"}`
      );
      const body = encodeURIComponent(
        [
          `Name: ${data.get("name") || ""}`,
          `Phone: ${data.get("phone") || ""}`,
          `Email: ${data.get("email") || ""}`,
          `Suburb: ${data.get("suburb") || ""}`,
          `Service: ${data.get("service") || ""}`,
          "",
          "Project details:",
          data.get("message") || "",
        ].join("\n")
      );
      window.location.href = `mailto:info@lvcivilcontracting.com.au?subject=${subject}&body=${body}`;
    });
  }

  // Footer year
  document.querySelectorAll("[data-year]").forEach((el) => {
    el.textContent = new Date().getFullYear();
  });
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
})();
