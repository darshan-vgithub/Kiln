<script setup>
import { ref, onMounted, onUnmounted } from 'vue'

const services = [
  {
    name: 'Digital strategy',
    summary: 'Untangling priorities before any money gets spent on tools or development.',
    capabilities: ['Technology audits', 'Build-vs-buy decisions', '12-month roadmaps', 'Vendor shortlisting'],
    color: 'cobalt',
  },
  {
    name: 'Product & software consulting',
    summary: 'Turning a rough idea into a scoped, buildable plan a development team can actually run with.',
    capabilities: ['MVP definition', 'Architecture review', 'Technical due diligence', 'Delivery oversight'],
    color: 'emerald',
  },
  {
    name: 'Systems & process modernisation',
    summary: 'Replacing spreadsheets, email chains and manual handoffs with tools that fit how the team really works.',
    capabilities: ['Workflow mapping', 'Tool selection & rollout', 'Data migration planning', 'Team training'],
    color: 'ink',
  },
  {
    name: 'Fractional CTO & ongoing advisory',
    summary: 'Senior technical judgement on tap — for boards and founders who need it occasionally, not full-time.',
    capabilities: ['Monthly advisory retainer', 'Hiring & team structure', 'Investor tech due diligence', 'Roadmap accountability'],
    color: 'cobalt',
  },
]

const colorMap = {
  cobalt: { bg: 'bg-cobalt', text: 'text-cobalt', tint: 'bg-cobalt/5', border: 'border-cobalt/30' },
  emerald: { bg: 'bg-emerald', text: 'text-emerald', tint: 'bg-emerald/5', border: 'border-emerald/30' },
  ink: { bg: 'bg-ink', text: 'text-ink', tint: 'bg-ink/5', border: 'border-ink/25' },
}

const openIndex = ref(0)
function toggle(i) {
  openIndex.value = openIndex.value === i ? -1 : i
}

// --- scroll-linked progress stepper ---
const sectionRef = ref(null)
const stepProgress = ref(0)
let ticking = false

function handleScroll() {
  if (!sectionRef.value || ticking) return
  ticking = true
  requestAnimationFrame(() => {
    const rect = sectionRef.value.getBoundingClientRect()
    const viewportMid = window.innerHeight * 0.6
    const total = rect.height - viewportMid + rect.height / services.length
    const scrolled = viewportMid - rect.top
    const raw = total > 0 ? scrolled / total : 0
    stepProgress.value = Math.min(1, Math.max(0, raw))
    ticking = false
  })
}

onMounted(() => {
  window.addEventListener('scroll', handleScroll, { passive: true })
  handleScroll()
})
onUnmounted(() => {
  window.removeEventListener('scroll', handleScroll)
})

function stepState(i) {
  const activeFloat = stepProgress.value * services.length
  if (i < Math.floor(activeFloat)) return 'done'
  if (i === Math.floor(activeFloat)) return 'current'
  return 'upcoming'
}
function lineFilled(i) {
  return stepProgress.value * services.length > i + 1
}
</script>

<template>
  <section id="services" ref="sectionRef" class="border-t border-line py-20 md:py-28">
    <div class="container-content">
      <div class="grid md:grid-cols-12 gap-10 mb-14">
        <h2 class="md:col-span-5 font-serif text-4xl md:text-5xl leading-tight tracking-tight">
          What we help you figure out
        </h2>
        <p class="md:col-span-6 md:col-start-7 text-inkfade text-lg leading-relaxed self-end">
          Every engagement starts with a conversation, not a proposal template. These are the shapes that work most often takes.
        </p>
      </div>

      <div class="grid gap-x-6 md:gap-x-10 border-t border-line" style="grid-template-columns: 44px 1fr;">
        <template v-for="(service, i) in services" :key="service.name">
          <div class="relative flex flex-col items-center pt-8">
            <div class="relative flex items-center justify-center shrink-0">
              <span
                class="w-11 h-11 rounded-full flex items-center justify-center transition-colors duration-300"
                :class="stepState(i) === 'upcoming' ? 'bg-line text-inkfade' : 'bg-cobalt text-paper'"
              >
                <svg v-if="stepState(i) !== 'upcoming'" width="18" height="18" viewBox="0 0 24 24" fill="none">
                  <path d="M5 13l4 4L19 7" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>
                </svg>
                <span v-else class="text-sm font-semibold">{{ i + 1 }}</span>
              </span>
              <span
                v-if="stepState(i) === 'current'"
                class="absolute inset-0 rounded-full border-2 border-cobalt"
                style="width: 44px; height: 44px; margin: -3px;"
              ></span>
            </div>
            <div
              v-if="i < services.length - 1"
              class="w-[3px] flex-1 my-2 rounded-full transition-colors duration-300"
              :class="lineFilled(i) ? 'bg-cobalt' : 'bg-line'"
            ></div>
          </div>

          <div
            class="border-b border-line transition-colors"
            :class="openIndex === i ? colorMap[service.color].tint : ''"
          >
            <button
              class="w-full flex items-start gap-6 md:gap-10 py-8 px-4 -mx-4 text-left group"
              @click="toggle(i)"
              :aria-expanded="openIndex === i"
            >
              <span
                class="flex items-center justify-center w-14 h-14 rounded-full text-paper font-serif text-2xl shrink-0 transition-transform group-hover:scale-105"
                :class="colorMap[service.color].bg"
              >
                {{ service.name.charAt(0) }}
              </span>
              <span class="flex-1">
                <span class="flex flex-wrap items-baseline justify-between gap-x-6 gap-y-2">
                  <span class="font-serif text-2xl md:text-3xl tracking-tight transition-colors" :class="openIndex === i ? colorMap[service.color].text : ''">
                    {{ service.name }}
                  </span>
                  <span
                    class="flex items-center justify-center w-8 h-8 rounded-full border transition-transform"
                    :class="[colorMap[service.color].border, { 'rotate-45': openIndex === i }]"
                  >
                    <span class="text-lg leading-none" :class="colorMap[service.color].text">+</span>
                  </span>
                </span>
                <span class="block mt-3 text-inkfade max-w-[60ch]">{{ service.summary }}</span>

                <span
                  v-show="openIndex === i"
                  class="mt-5 flex flex-wrap gap-2"
                >
                  <span
                    v-for="cap in service.capabilities"
                    :key="cap"
                    class="text-xs font-medium rounded-full px-3 py-1.5 border"
                    :class="[colorMap[service.color].text, colorMap[service.color].border]"
                  >
                    {{ cap }}
                  </span>
                </span>
              </span>
            </button>
          </div>
        </template>
      </div>
    </div>
  </section>
</template>
