<script setup>
const year = new Date().getFullYear()

const studioLinks = [
  { label: 'Home', to: '/' },
  { label: 'Services', to: '/services' },
  { label: 'Process', to: '/process' },
  { label: 'Work', to: '/work' },
  { label: 'Contact', to: '/contact' },
]

const serviceLinks = [
  { label: 'Digital strategy', to: '/services' },
  { label: 'Product consulting', to: '/services' },
  { label: 'Systems modernisation', to: '/services' },
  { label: 'Fractional CTO', to: '/services' },
]

const connectLinks = [
  { label: 'LinkedIn', href: 'https://linkedin.com', external: true },
  { label: 'GitHub', href: 'https://github.com', external: true },
  { label: 'hello@northlight.co', href: 'mailto:hello@northlight.co', external: true },
]
</script>

<template>
  <footer class="bg-paperdim border-t border-line pt-20">
    <div class="container-content">
      <div class="grid md:grid-cols-12 gap-12 pb-16">
        <div class="md:col-span-4">
          <div class="flex items-center gap-2.5">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none">
              <path d="M12 2 L14 10 L22 12 L14 14 L12 22 L10 14 L2 12 L10 10 Z" fill="#2438E0" />
            </svg>
            <span class="font-serif text-2xl text-ink">Northlight</span>
          </div>
          <p class="mt-5 text-inkfade leading-relaxed max-w-[34ch]">
            Independent digital &amp; technology consulting. We take unclear problems and turn them into a plan.
          </p>
          <p class="mt-6 text-xs text-ink/40 tracking-wide">
            GLASGOW · REMOTE-FRIENDLY · EST. 2026
          </p>
        </div>

        <div class="md:col-span-2 md:col-start-6">
          <p class="text-xs font-semibold text-cobalt tracking-wide mb-5">STUDIO</p>
          <ul class="space-y-3">
            <li v-for="link in studioLinks" :key="link.to">
              <router-link :to="link.to" class="text-ink/70 hover:text-ink transition-colors">
                {{ link.label }}
              </router-link>
            </li>
          </ul>
        </div>

        <div class="md:col-span-3">
          <p class="text-xs font-semibold text-cobalt tracking-wide mb-5">SERVICES</p>
          <ul class="space-y-3">
            <li v-for="link in serviceLinks" :key="link.label">
              <router-link :to="link.to" class="text-ink/70 hover:text-ink transition-colors">
                {{ link.label }}
              </router-link>
            </li>
          </ul>
        </div>

        <div class="md:col-span-3">
          <p class="text-xs font-semibold text-cobalt tracking-wide mb-5">CONNECT</p>
          <ul class="space-y-3">
            <li v-for="link in connectLinks" :key="link.label">
              <a :href="link.href" class="text-ink/70 hover:text-ink transition-colors break-words">
                {{ link.label }}
              </a>
            </li>
          </ul>
        </div>
      </div>

      <div
        class="select-none leading-none font-serif overflow-hidden whitespace-nowrap"
        style="font-size: clamp(4rem, 13vw, 11rem); color: transparent; -webkit-text-stroke: 1px rgba(21,23,27,0.08);"
        aria-hidden="true"
      >
        NORTHLIGHT
      </div>

      <div class="border-t border-line py-6 flex flex-col sm:flex-row items-start sm:items-center justify-between gap-3">
        <p class="text-sm text-ink/50">© {{ year }} Northlight Studio. All rights reserved.</p>
        <p class="text-xs text-ink/40 tracking-wide">CLARITY OVER COMPLEXITY</p>
      </div>
    </div>
  </footer>
</template>
