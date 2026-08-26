<script setup>
import BuildStrip from './BuildStrip.vue'
</script>

<template>
  <section id="top" class="hero">
    <div class="panel">
      <span class="eyebrow">SOFTWARE CONSULTANCY · REMOTE-FIRST</span>

      <div class="brand-row">
        <svg class="mark" viewBox="0 0 64 64" aria-hidden="true">
          <defs>
            <linearGradient id="heroKilnGold" x1="0" y1="0" x2="1" y2="1">
              <stop offset="0%" stop-color="#f7e2ab" />
              <stop offset="45%" stop-color="#d8a94b" />
              <stop offset="100%" stop-color="#8a6a2a" />
            </linearGradient>
          </defs>
          <path
            fill="url(#heroKilnGold)"
            d="M10,44 C6,34 8,20 20,12 C22,18 18,26 14,36 C12,40 11,42 10,44 Z"
          />
          <path
            fill="url(#heroKilnGold)"
            d="M54,44 C58,34 56,20 44,12 C42,18 46,26 50,36 C52,40 53,42 54,44 Z"
          />
          <path fill="url(#heroKilnGold)" d="M20,48 L22,30 L24,22 L26,30 L28,48 Z" />
          <path fill="url(#heroKilnGold)" d="M28,48 L30,26 L32,14 L34,26 L36,48 Z" />
          <path fill="url(#heroKilnGold)" d="M36,48 L38,30 L40,22 L42,30 L44,48 Z" />
        </svg>

        <h1 class="headline">Kiln</h1>
      </div>

      <p class="subhead">
        We take rough ideas and turn them into
        <span class="pill">shipped products</span>
      </p>

      <div class="ctas">
        <a class="btn primary" href="#contact">Start a project</a>
        <a class="btn ghost" href="#process">See our process</a>
      </div>

      <BuildStrip class="build-strip" />

      <div class="note">
        <p>
          We take on a limited number of engagements each quarter across web and mobile app
          development, MVP builds, and hands-on technical consulting.
          <a href="#contact" class="link">Get in touch</a>
          to see if there's a fit for your timeline and budget.
        </p>
      </div>
    </div>
  </section>
</template>

<style scoped>
.hero {
  padding: clamp(2rem, 6vw, 4rem) clamp(1.25rem, 4vw, 3rem) 3rem;
}

.panel {
  max-width: 74rem;
  margin: 0 auto;
  border: 1px solid var(--line);
  border-radius: 20px;
  background: radial-gradient(120% 140% at 50% 0%, #191b21 0%, var(--bg) 60%);
  padding: clamp(2.2rem, 6vw, 4.5rem) clamp(1.5rem, 5vw, 4rem) clamp(2.5rem, 5vw, 3.5rem);
  text-align: center;
}

.eyebrow {
  display: inline-block;
  font-family: var(--font-mono);
  font-size: 0.72rem;
  letter-spacing: 0.12em;
  color: var(--text-muted);
  border: 1px solid var(--line);
  border-radius: 999px;
  padding: 0.5rem 1.1rem;
}

.brand-row {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: clamp(0.6rem, 2vw, 1.2rem);
  margin: 1.8rem 0 1rem;
}

.mark {
  display: block;
  width: clamp(2.6rem, 7vw, 4.2rem);
  height: clamp(2.6rem, 7vw, 4.2rem);
  flex-shrink: 0;
}

.headline {
  font-family: 'Cormorant Garamond', 'Georgia', serif;
  font-weight: 700;
  font-size: clamp(3.2rem, 11vw, 7rem);
  line-height: 0.95;
  letter-spacing: -0.01em;
  margin: 0;
  background: linear-gradient(135deg, #f7e2ab 0%, #d8a94b 55%, #8a6a2a 100%);
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
}

.subhead {
  font-size: clamp(1.15rem, 2.4vw, 1.6rem);
  color: var(--text-muted);
  margin: 0 auto 2.2rem;
  max-width: 40rem;
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: center;
  gap: 0.55rem;
}

.pill {
  color: var(--text);
  background: var(--surface-2);
  border: 1px solid var(--line);
  border-radius: 999px;
  padding: 0.3rem 0.9rem;
  font-weight: 600;
}

.ctas {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 0.9rem;
  margin-bottom: 3rem;
}

.btn {
  display: inline-block;
  text-decoration: none;
  padding: 0.85rem 1.6rem;
  border-radius: 10px;
  font-weight: 600;
  font-size: 0.98rem;
  transition: transform 0.15s ease, background 0.15s ease;
}

.btn:hover {
  transform: translateY(-1px);
}

.btn.primary {
  background: var(--text);
  color: var(--bg);
}

.btn.primary:hover {
  background: #fff;
}

.btn.ghost {
  border: 1px solid var(--line);
  color: var(--text);
}

.btn.ghost:hover {
  background: var(--surface-2);
}

.build-strip {
  margin: 0 auto 2.6rem;
}

.note {
  max-width: 46rem;
  margin: 0 auto;
  border: 1px solid var(--line);
  border-radius: 14px;
  background: var(--surface);
  padding: 1.4rem 1.6rem;
}

.note p {
  margin: 0;
  color: var(--text-muted);
  line-height: 1.65;
  font-size: 0.98rem;
}

.link {
  color: var(--text);
  font-weight: 600;
  text-decoration: underline;
  text-underline-offset: 3px;
}
</style>