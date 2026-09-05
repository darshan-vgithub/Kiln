<script setup>
import { ref, computed, onMounted, onUnmounted } from 'vue'

const panels = [
  {
    label: 'Strategy',
    title: 'See the whole board before you move a single piece.',
    detail: 'Audits, roadmaps and build-vs-buy calls — so budget goes toward the right problem, not the loudest one.',
  },
  {
    label: 'Build',
    title: 'A plan a development team can actually pick up and run with.',
    detail: 'MVP definition, architecture review and delivery oversight, from idea to scoped brief.',
  },
  {
    label: 'Modernise',
    title: 'Replace the spreadsheet before it replaces your evening.',
    detail: 'Workflow mapping and tool rollout that fits how the team already works, not the other way round.',
  },
  {
    label: 'Advise',
    title: 'Senior judgement on tap, without a full-time hire.',
    detail: 'A fractional CTO for the decisions that are hard to make alone.',
  },
]

const wrapperRef = ref(null)
const progress = ref(0)
const reduceMotion = ref(false)

let ticking = false

function handleScroll() {
  if (!wrapperRef.value || ticking) return
  ticking = true
  requestAnimationFrame(() => {
    const rect = wrapperRef.value.getBoundingClientRect()
    const total = rect.height - window.innerHeight
    const scrolled = -rect.top
    const raw = total > 0 ? scrolled / total : 0
    progress.value = Math.min(1, Math.max(0, raw))
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

function activeIndex(p) {
  return Math.min(panels.length - 1, Math.floor(p * panels.length))
}

const contProgress = computed(() => progress.value * (panels.length - 1e-6))

function textStyle(i) {
  const delta = contProgress.value - i
  const absDelta = Math.abs(delta)
  const opacity = Math.max(0, 1 - absDelta * 1.4)
  const translateY = delta * 26
  return {
    opacity: String(opacity),
    transform: `translateY(${translateY}px)`,
    pointerEvents: absDelta < 0.5 ? 'auto' : 'none',
  }
}

function cardStyle(i) {
  const delta = contProgress.value - i
  const absDelta = Math.abs(delta)
  const translateZ = -Math.min(absDelta, 1.6) * 260
  const rotateY = Math.max(-38, Math.min(38, delta * -38))
  const translateX = delta * -60
  const scale = Math.max(0.5, 1 - absDelta * 0.32)
  const opacity = Math.max(0, 1 - absDelta * 0.85)
  return {
    transform: `translateX(${translateX}px) translateZ(${translateZ}px) rotateY(${rotateY}deg) scale(${scale})`,
    opacity: String(opacity),
    zIndex: String(Math.round(1000 - absDelta * 100)),
  }
}

const strokeProps = 'fill="none" stroke="#15171B" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"'

const dotgrid = (id) => `<pattern id="${id}" width="18" height="18" patternUnits="userSpaceOnUse"><circle cx="1.5" cy="1.5" r="1.2" fill="#15171B" opacity="0.12"/></pattern>`

const illustrations = [
  // Strategy — a route plotted across a topographic map, ending at a flag
  `<svg viewBox="0 0 280 210" width="100%" height="100%">
    <defs>${dotgrid('g1')}</defs>
    <rect width="280" height="210" fill="url(#g1)"></rect>
    <path d="M-10 150 C40 115 70 175 115 145 C155 118 185 168 230 138 C255 122 275 132 290 122" fill="none" stroke="#15171B" stroke-width="1.3" opacity="0.28"></path>
    <path d="M-10 175 C45 145 85 195 130 165 C165 140 200 185 240 158 C260 145 275 152 290 148" fill="none" stroke="#15171B" stroke-width="1.3" opacity="0.2"></path>
    <path d="M30 128 L88 92 L150 102 L212 62 L252 76" fill="none" stroke="#2438E0" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="0.5 11"></path>
    <circle cx="30" cy="128" r="6" fill="#2438E0"></circle>
    <circle cx="88" cy="92" r="3.5" fill="#15171B"></circle>
    <circle cx="150" cy="102" r="3.5" fill="#15171B"></circle>
    <circle cx="212" cy="62" r="3.5" fill="#15171B"></circle>
    <line x1="252" y1="76" x2="252" y2="34" stroke="#15171B" stroke-width="2"></line>
    <path d="M252 34 L276 42 L252 50 Z" fill="#2438E0"></path>
  </svg>`,
  // Build — isometric blocks assembling, one piece being lowered into place
  `<svg viewBox="0 0 280 210" width="100%" height="100%">
    <defs>${dotgrid('g2')}</defs>
    <rect width="280" height="210" fill="url(#g2)"></rect>
    <g stroke="#15171B" stroke-width="1.3" stroke-linejoin="round">
      <polygon points="90,120 116.1,135 90,150 63.9,135" fill="#F3F1EB"></polygon>
      <polygon points="63.9,135 90,150 90,180 63.9,165" fill="#15171B" opacity="0.12"></polygon>
      <polygon points="116.1,135 90,150 90,180 116.1,165" fill="#15171B" opacity="0.22"></polygon>
      <polygon points="150,120 176.1,135 150,150 123.9,135" fill="#F3F1EB"></polygon>
      <polygon points="123.9,135 150,150 150,180 123.9,165" fill="#15171B" opacity="0.12"></polygon>
      <polygon points="176.1,135 150,150 150,180 176.1,165" fill="#15171B" opacity="0.22"></polygon>
    </g>
    <g stroke="#2438E0" stroke-width="1.6" stroke-dasharray="3 4" stroke-linejoin="round">
      <polygon points="120,54 142.6,67 120,80 97.4,67" fill="none"></polygon>
      <polygon points="97.4,67 120,80 120,106 97.4,93" fill="none"></polygon>
      <polygon points="142.6,67 120,80 120,106 142.6,93" fill="none"></polygon>
    </g>
    <line x1="120" y1="106" x2="120" y2="119" stroke="#2438E0" stroke-width="1.6" stroke-dasharray="2 3"></line>
    <path d="M114 116 L120 124 L126 116" fill="none" stroke="#2438E0" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"></path>
  </svg>`,
  // Modernise — a tangled scribble resolving into clean parallel lines
  `<svg viewBox="0 0 280 210" width="100%" height="100%">
    <defs>${dotgrid('g3')}</defs>
    <rect width="280" height="210" fill="url(#g3)"></rect>
    <path d="M35 70 C10 90 55 100 30 122 C8 142 58 138 42 165 C28 188 68 178 55 152 C46 133 78 140 60 108 C46 84 70 92 62 68" fill="none" stroke="#15171B" stroke-width="1.6" opacity="0.55"></path>
    <circle cx="35" cy="70" r="3.5" fill="#15171B"></circle>
    <line x1="140" y1="40" x2="140" y2="190" stroke="#2438E0" stroke-width="1.4" stroke-dasharray="2 5" opacity="0.6"></line>
    <path d="M132 108 L146 115 L132 122" fill="none" stroke="#2438E0" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"></path>
    <line x1="188" y1="72" x2="256" y2="72" stroke="#0F6E5C" stroke-width="2.2" stroke-linecap="round"></line>
    <line x1="188" y1="98" x2="240" y2="98" stroke="#0F6E5C" stroke-width="2.2" stroke-linecap="round"></line>
    <line x1="188" y1="124" x2="256" y2="124" stroke="#0F6E5C" stroke-width="2.2" stroke-linecap="round"></line>
    <line x1="188" y1="150" x2="230" y2="150" stroke="#0F6E5C" stroke-width="2.2" stroke-linecap="round"></line>
    <circle cx="188" cy="72" r="3" fill="#0F6E5C"></circle>
    <circle cx="188" cy="98" r="3" fill="#0F6E5C"></circle>
    <circle cx="188" cy="124" r="3" fill="#0F6E5C"></circle>
    <circle cx="188" cy="150" r="3" fill="#0F6E5C"></circle>
  </svg>`,
  // Advise — a lighthouse beam reaching out to distant signals
  `<svg viewBox="0 0 280 210" width="100%" height="100%">
    <defs>${dotgrid('g4')}</defs>
    <rect width="280" height="210" fill="url(#g4)"></rect>
    <path d="M40 56 L258 36 L258 158 Z" fill="#2438E0" opacity="0.1"></path>
    <polygon points="26,182 56,182 47,60 35,60" fill="#15171B"></polygon>
    <rect x="30" y="96" width="22" height="4" fill="#F3F1EB"></rect>
    <rect x="31" y="130" width="20" height="4" fill="#F3F1EB"></rect>
    <rect x="24" y="182" width="34" height="7" fill="#15171B"></rect>
    <circle cx="41" cy="56" r="6" fill="#2438E0"></circle>
    <line x1="41" y1="56" x2="150" y2="88" stroke="#15171B" stroke-width="1" stroke-dasharray="1 5" opacity="0.4"></line>
    <line x1="41" y1="56" x2="205" y2="112" stroke="#15171B" stroke-width="1" stroke-dasharray="1 5" opacity="0.4"></line>
    <line x1="41" y1="56" x2="230" y2="70" stroke="#15171B" stroke-width="1" stroke-dasharray="1 5" opacity="0.4"></line>
    <circle cx="150" cy="88" r="4" fill="#15171B"></circle>
    <circle cx="205" cy="112" r="4" fill="#15171B"></circle>
    <circle cx="230" cy="70" r="3" fill="#15171B"></circle>
  </svg>`,
]


function illustration(i) {
  return illustrations[i]
}
</script>

<template>
  <section
    v-if="reduceMotion"
    class="border-t border-line py-20"
  >
    <div class="container-content space-y-16">
      <article v-for="(panel, i) in panels" :key="panel.label" class="grid md:grid-cols-2 gap-10 items-center">
        <div :class="{ 'md:order-2': i % 2 === 1 }">
          <p class="text-sm font-medium text-cobalt mb-3">{{ panel.label }}</p>
          <h3 class="font-serif text-3xl leading-tight">{{ panel.title }}</h3>
          <p class="mt-4 text-inkfade leading-relaxed max-w-[46ch]">{{ panel.detail }}</p>
        </div>
        <div class="aspect-[4/3] flex items-center justify-center">
          <div class="w-full h-full" v-html="illustration(i)"></div>
        </div>
      </article>
    </div>
  </section>

  <section v-else ref="wrapperRef" class="relative border-t border-line" style="height: 400vh;">
    <div class="sticky top-20 h-[calc(100vh-5rem)] overflow-hidden bg-paper">
      <div class="container-content h-full flex items-center">
        <div class="grid md:grid-cols-2 gap-10 items-center w-full">
          <div>
            <div class="flex gap-2 mb-8">
              <span
                v-for="(panel, i) in panels"
                :key="panel.label"
                class="h-1 flex-1 rounded-full transition-colors"
                :class="i <= activeIndex(progress) ? 'bg-cobalt' : 'bg-line'"
              />
            </div>

            <div class="relative h-64" style="perspective: 1400px;">
              <div
                v-for="(panel, i) in panels"
                :key="panel.label"
                class="absolute inset-0"
                :style="textStyle(i)"
              >
                <p class="text-sm font-medium text-cobalt mb-3">{{ panel.label }}</p>
                <h3 class="font-serif text-3xl md:text-4xl leading-tight text-balance">{{ panel.title }}</h3>
                <p class="mt-4 text-inkfade leading-relaxed max-w-[46ch]">{{ panel.detail }}</p>
              </div>
            </div>
          </div>

          <div class="aspect-[4/3] relative hidden md:block" style="perspective: 1400px;">
            <div class="absolute inset-0" style="transform-style: preserve-3d;">
              <div
                v-for="(panel, i) in panels"
                :key="panel.label"
                class="absolute inset-0 flex items-center justify-center rounded-2xl bg-paperdim border border-line p-10"
                :style="cardStyle(i)"
                v-html="illustration(i)"
              />
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

