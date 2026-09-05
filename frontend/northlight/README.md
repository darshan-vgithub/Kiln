# Northlight — consultancy website (Vue 3 + Vite + Tailwind)

## Run it locally

```bash
npm install
npm run dev
```

Then open the local URL Vite prints (usually http://localhost:5173).

## Build for production

```bash
npm run build
```

Output goes to `dist/` — upload that folder to any static host (Netlify, Vercel, Cloudflare Pages, S3, etc).

**Important — this is a multi-page app using client-side routing (Vue Router with `createWebHistory`).** Your host needs to be configured to serve `index.html` for unknown paths (an "SPA fallback" or "rewrite rule"), otherwise a hard refresh on `/services` will 404. Netlify and Vercel do this automatically for Vite projects; other hosts may need a `_redirects` or rewrite config — check your host's docs if you hit 404s on refresh.

## Pages & routes

- `/` — Home: hero + a pinned scroll-driven overview of the four service pillars
- `/services` — full services list (expandable)
- `/process` — the four-step working process
- `/work` — case studies + testimonials
- `/contact` — contact form

## What's here

- `src/router/index.js` — route definitions
- `src/App.vue` — nav, footer, and the `<router-view>` with a fade transition between pages
- `src/pages/*.vue` — one file per route, each composing the components below
- `src/components/NavBar.vue` — sticky header with mobile menu, using `router-link`
- `src/components/Hero.vue` — headline, CTAs, stats strip (used on Home)
- `src/components/ScrollStory.vue` — the pinned scroll effect on Home; falls back to a static stacked layout if the visitor has "reduce motion" enabled
- `src/components/Services.vue` — expandable list of services
- `src/components/Process.vue` — the four-step working process
- `src/components/Work.vue` — case study cards
- `src/components/Testimonials.vue` — client quotes
- `src/components/ContactSection.vue` — contact form (client-side only — see below)
- `src/components/SiteFooter.vue`

## About the graphics

The illustrations in the scroll section are hand-coded original line-art SVGs (no stock imagery), so there's nothing to license or attribute. If you'd rather use real photography — team photos, office shots, product screenshots — drop image files into `src/assets/` and swap them into `Hero.vue` / `ScrollStory.vue` in place of the SVGs.

## Things to customise before launch

- **Business name & copy**: everything currently says "Northlight" — a placeholder name. Swap in your real name, tagline and service descriptions throughout the `src/components/*.vue` files.
- **Contact form**: `ContactSection.vue` validates and shows a success state, but doesn't actually send anywhere yet. Wire the `handleSubmit` function up to a form backend (e.g. Formspree, Resend, or your own API route).
- **Case studies & testimonials**: currently invented placeholder content — replace with real client work once you have it (or keep them anonymised if that's your preference).
- **Colours & fonts**: defined as tokens in `tailwind.config.js` (`paper`, `ink`, `cobalt`, `emerald`) and loaded via Google Fonts in `index.html` (Fraunces + Archivo). Easy to swap.
