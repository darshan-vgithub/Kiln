<script setup>
import { ref, onMounted, onUnmounted } from 'vue'

const industries = ['Retail & e-commerce', 'Professional services', 'Manufacturing', 'Healthcare', 'Education']

const sectionRef = ref(null)
const tiltStyle = ref({})
const reduceMotion = ref(false)
let ticking = false

function handleScroll() {
  if (!sectionRef.value || ticking) return
  ticking = true
  requestAnimationFrame(() => {
    const rect = sectionRef.value.getBoundingClientRect()
    const raw = -rect.top / (rect.height || 1)
    const progress = Math.min(1, Math.max(0, raw))
    tiltStyle.value = {
      transform: `perspective(1200px) rotateX(${progress * -16}deg) translateY(${progress * 60}px) scale(${1 - progress * 0.1})`,
      opacity: String(1 - progress * 0.5),
    }
    ticking = false
  })
}

onMounted(() => {
  reduceMotion.value = window.matchMedia('(prefers-reduced-motion: reduce)').matches
  if (!reduceMotion.value) {
    window.addEventListener('scroll', handleScroll, { passive: true })
    handleScroll()
  }
})

onUnmounted(() => {
  window.removeEventListener('scroll', handleScroll)
})
</script>

<template>
  <section ref="sectionRef" class="relative overflow-hidden bg-paper">
    <div
      class="hidden md:block absolute inset-y-0 right-0 w-[46%] bg-ink"
      style="clip-path: polygon(22% 0, 100% 0, 100% 100%, 0% 100%);"
    ></div>

    <div class="container-content pt-16 pb-24 md:pt-24 md:pb-32 relative">
      <div class="grid md:grid-cols-12 gap-10 items-start">
        <div class="md:col-span-7">
          <span class="inline-flex items-center gap-2 bg-cobalt text-paper text-xs font-semibold px-3.5 py-1.5 rounded-full mb-7">
            Independent technology advisory · Glasgow
          </span>
          <h1 class="font-serif italic text-[2.6rem] leading-[1.08] sm:text-6xl md:text-[4rem] md:leading-[1.03] tracking-tight text-ink text-balance">
            Technology decisions, made clear.
          </h1>
          <p class="mt-8 max-w-[46ch] text-lg text-inkfade leading-relaxed">
            Northlight helps growing businesses make sense of software, systems and strategy — without the jargon, the sales pitch, or the guesswork.
          </p>

          <div class="mt-10 flex flex-wrap items-center gap-4">
            <router-link
              to="/contact"
              class="inline-flex items-center gap-2 bg-cobalt text-paper text-sm font-semibold px-6 py-3.5 rounded-full hover:bg-cobaltdeep transition-colors"
            >
              Book a first call
            </router-link>
            <router-link
              to="/services"
              class="inline-flex items-center gap-2 border border-ink/20 text-sm font-semibold px-6 py-3.5 rounded-full hover:border-ink transition-colors"
            >
              See how we help
            </router-link>
          </div>
        </div>

        <div class="md:col-span-5 md:pl-6 relative" :style="tiltStyle" style="transform-origin: center top;">
          <p class="text-sm text-paper/70 leading-relaxed">
            We work with leadership teams who know something needs to change, but aren't sure what to build, buy, or fix first.
          </p>
          <ul class="mt-6 flex flex-wrap gap-2">
            <li
              v-for="item in industries"
              :key="item"
              class="text-xs text-paper/85 border border-paper/25 rounded-full px-3 py-1.5"
            >
              {{ item }}
            </li>
          </ul>

          <div class="mt-8 hidden lg:block">
            <svg viewBox="0 0 280 220" width="100%" height="auto">
              <rect x="30" y="30" width="180" height="130" rx="6" fill="none" stroke="rgba(243,241,235,0.18)" stroke-width="1.5" transform="translate(20,10) rotate(-4 120 95)"></rect>
              <rect x="30" y="30" width="180" height="130" rx="6" fill="none" stroke="rgba(243,241,235,0.35)" stroke-width="1.5" transform="translate(10,30) rotate(2 120 95)"></rect>
              <rect x="30" y="30" width="180" height="130" rx="6" fill="none" stroke="#F3F1EB" stroke-width="2" transform="translate(0,60)"></rect>
              <path d="M70 190 L120 160 L160 200 L210 150" fill="none" stroke="#2438E0" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" transform="translate(0,0)"></path>
              <circle cx="70" cy="190" r="4.5" fill="#2438E0"></circle>
              <circle cx="120" cy="160" r="4.5" fill="#2438E0"></circle>
              <circle cx="160" cy="200" r="4.5" fill="#2438E0"></circle>
              <circle cx="210" cy="150" r="4.5" fill="#2438E0"></circle>
            </svg>
          </div>
        </div>
      </div>
    </div>

    <div class="border-t border-line bg-paperdim relative">
      <div class="container-content grid grid-cols-2 sm:grid-cols-4 gap-y-8 py-10">
        <div>
          <p class="font-serif text-4xl text-cobalt">40+</p>
          <p class="mt-1 text-sm text-inkfade">Advisory engagements delivered</p>
        </div>
        <div>
          <p class="font-serif text-4xl text-cobalt">12yrs</p>
          <p class="mt-1 text-sm text-inkfade">Average team experience</p>
        </div>
        <div>
          <p class="font-serif text-4xl text-cobalt">6wks</p>
          <p class="mt-1 text-sm text-inkfade">Typical roadmap turnaround</p>
        </div>
        <div>
          <p class="font-serif text-4xl text-cobalt">0</p>
          <p class="mt-1 text-sm text-inkfade">Products sold on commission</p>
        </div>
      </div>
    </div>
  </section>
</template>
