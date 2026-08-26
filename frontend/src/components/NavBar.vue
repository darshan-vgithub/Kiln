<script setup>
import { ref } from 'vue'

const open = ref(false)

const links = [
  { label: 'Services', to: { path: '/', hash: '#services' } },
  { label: 'About', to: { path: '/', hash: '#about' } },
  { label: 'Process', to: { path: '/', hash: '#process' } },
  { label: 'Contact', to: { path: '/', hash: '#contact' } },
  { label: 'Careers', to: '/careers' },
]

function close() {
  open.value = false
}
</script>

<template>
  <header class="nav">
    <router-link class="brand" to="/" @click="close">
      <svg class="brand-mark" viewBox="0 0 64 64" aria-hidden="true">
        <defs>
          <linearGradient id="kilnGold" x1="0" y1="0" x2="1" y2="1">
            <stop offset="0%" stop-color="#f7e2ab" />
            <stop offset="45%" stop-color="#d8a94b" />
            <stop offset="100%" stop-color="#8a6a2a" />
          </linearGradient>
        </defs>
        <!-- left horn -->
        <path
          fill="url(#kilnGold)"
          d="M10,44 C6,34 8,20 20,12 C22,18 18,26 14,36 C12,40 11,42 10,44 Z"
        />
        <!-- right horn -->
        <path
          fill="url(#kilnGold)"
          d="M54,44 C58,34 56,20 44,12 C42,18 46,26 50,36 C52,40 53,42 54,44 Z"
        />
        <!-- three rising flames -->
        <path fill="url(#kilnGold)" d="M20,48 L22,30 L24,22 L26,30 L28,48 Z" />
        <path fill="url(#kilnGold)" d="M28,48 L30,26 L32,14 L34,26 L36,48 Z" />
        <path fill="url(#kilnGold)" d="M36,48 L38,30 L40,22 L42,30 L44,48 Z" />
      </svg>

      <span class="brand-text">
        <span class="brand-name">Kiln</span>
        <span class="brand-caption">EST. 2026</span>
      </span>
    </router-link>

    <nav class="links" :class="{ open }" aria-label="Primary">
      <router-link v-for="link in links" :key="link.label" :to="link.to" @click="close">
        {{ link.label }}
      </router-link>
      <router-link class="cta" :to="{ path: '/', hash: '#contact' }" @click="close">
        Start a project
      </router-link>
    </nav>

    <button class="toggle" :aria-expanded="open" aria-label="Toggle menu" @click="open = !open">
      <span></span><span></span><span></span>
    </button>
  </header>
</template>

<style scoped>
.nav {
  position: sticky;
  top: 0;
  z-index: 40;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 1.1rem clamp(1.25rem, 4vw, 3rem);
  background: rgba(11, 12, 15, 0.85);
  backdrop-filter: blur(10px);
  border-bottom: 1px solid var(--line);
}

.brand {
  display: flex;
  align-items: center;
  gap: 0.7rem;
  text-decoration: none;
  color: var(--text);
}

.brand-mark {
  width: 2.3rem;
  height: 2.3rem;
  flex-shrink: 0;
}

.brand-text {
  display: flex;
  flex-direction: column;
  line-height: 1;
}

.brand-name {
  font-family: 'Cormorant Garamond', 'Georgia', serif;
  font-weight: 700;
  font-size: 1.5rem;
  letter-spacing: 0.02em;
  background: linear-gradient(135deg, #f7e2ab 0%, #d8a94b 55%, #8a6a2a 100%);
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
}

.brand-caption {
  font-family: var(--font-mono);
  font-size: 0.58rem;
  letter-spacing: 0.18em;
  color: #b9924f;
  margin-top: 0.2rem;
}

.links {
  display: flex;
  align-items: center;
  gap: 2rem;
  font-size: 0.94rem;
}

.links a {
  text-decoration: none;
  color: var(--text-muted);
  transition: color 0.15s ease;
}

.links a:hover {
  color: var(--text);
}

.links .cta {
  color: var(--bg);
  background: var(--text);
  padding: 0.5rem 1.05rem;
  border-radius: 999px;
  font-weight: 600;
}

.links .cta:hover {
  color: var(--bg);
  background: #fff;
}

.toggle {
  display: none;
  flex-direction: column;
  justify-content: center;
  gap: 5px;
  width: 2.1rem;
  height: 2.1rem;
  background: none;
  border: 1px solid var(--line);
  border-radius: 8px;
}

.toggle span {
  display: block;
  height: 2px;
  margin: 0 6px;
  background: var(--text);
  border-radius: 2px;
}

@media (max-width: 780px) {
  .toggle {
    display: flex;
  }

  .links {
    position: absolute;
    top: 100%;
    left: 0;
    right: 0;
    flex-direction: column;
    align-items: flex-start;
    gap: 1.1rem;
    padding: 1.5rem;
    background: var(--surface);
    border-bottom: 1px solid var(--line);
    display: none;
  }

  .links.open {
    display: flex;
  }

  .links .cta {
    align-self: flex-start;
  }
}
</style>