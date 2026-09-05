<script setup>
const cases = [
  {
    client: 'Regional retail group',
    tag: 'Systems modernisation',
    summary: 'Replaced five disconnected spreadsheets with a single stock system, cutting weekly reconciliation time from two days to under two hours.',
    result: '~80% less admin time',
    color: 'cobalt',
  },
  {
    client: 'Manufacturing SME',
    tag: 'Digital strategy',
    summary: 'A 12-week technology roadmap that identified which of four proposed platforms was worth building — and which three were not.',
    result: '£240k avoided spend',
    color: 'emerald',
  },
  {
    client: 'Professional services firm',
    tag: 'Fractional CTO',
    summary: 'Ongoing technical advisory through a client portal rebuild, including vendor selection and a two-person hire.',
    result: '9-month engagement',
    color: 'ink',
  },
]

const colorMap = {
  cobalt: { bg: 'bg-cobalt', text: 'text-cobalt' },
  emerald: { bg: 'bg-emerald', text: 'text-emerald' },
  ink: { bg: 'bg-ink', text: 'text-ink' },
}

const icons = {
  cobalt: `<svg viewBox="0 0 60 60" width="100%" height="100%"><path d="M12 40 L24 26 L34 36 L48 18" fill="none" stroke="#F3F1EB" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/><circle cx="12" cy="40" r="3.5" fill="#F3F1EB"/><circle cx="48" cy="18" r="3.5" fill="#F3F1EB"/></svg>`,
  emerald: `<svg viewBox="0 0 60 60" width="100%" height="100%"><rect x="12" y="26" width="14" height="20" fill="none" stroke="#F3F1EB" stroke-width="3"/><rect x="30" y="14" width="14" height="32" fill="none" stroke="#F3F1EB" stroke-width="3"/></svg>`,
  ink: `<svg viewBox="0 0 60 60" width="100%" height="100%"><circle cx="30" cy="30" r="6" fill="none" stroke="#F3F1EB" stroke-width="3"/><circle cx="30" cy="30" r="18" fill="none" stroke="#F3F1EB" stroke-width="2.5" opacity="0.6"/></svg>`,
}
</script>

<template>
  <section id="work" class="py-20 md:py-28 border-b border-line">
    <div class="container-content">
      <div class="grid md:grid-cols-12 gap-10 mb-14">
        <h2 class="md:col-span-5 font-serif text-4xl md:text-5xl leading-tight tracking-tight">
          Recent engagements
        </h2>
        <p class="md:col-span-6 md:col-start-7 text-inkfade text-lg leading-relaxed self-end">
          Client names are kept confidential by request — the shape of the work is real.
        </p>
      </div>

      <div class="grid md:grid-cols-3 gap-6">
        <article
          v-for="item in cases"
          :key="item.client"
          class="border border-line rounded-2xl overflow-hidden flex flex-col transition-transform hover:-translate-y-1"
        >
          <div class="h-28 flex items-center justify-center" :class="colorMap[item.color].bg">
            <div class="w-14 h-14" v-html="icons[item.color]"></div>
          </div>
          <div class="p-7 flex flex-col flex-1 bg-paper">
            <span class="text-xs font-semibold" :class="colorMap[item.color].text">{{ item.tag }}</span>
            <h3 class="mt-3 font-serif text-2xl leading-snug">{{ item.client }}</h3>
            <p class="mt-3 text-inkfade leading-relaxed flex-1">{{ item.summary }}</p>
            <p class="mt-6 pt-5 border-t border-line font-serif text-xl" :class="colorMap[item.color].text">{{ item.result }}</p>
          </div>
        </article>
      </div>
    </div>
  </section>
</template>
