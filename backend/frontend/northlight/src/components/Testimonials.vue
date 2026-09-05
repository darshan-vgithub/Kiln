<script setup>
const quotes = [
  {
    quote: "They didn't try to sell us a platform. They told us our spreadsheet was fine for another year and to spend the budget elsewhere.",
    name: 'Operations Director',
    org: 'Regional retail group',
    tint: 'bg-cobalt/5 border-cobalt/20',
    mark: 'text-cobalt',
  },
  {
    quote: 'The roadmap was the first technology document our board actually finished reading. Clear costs, clear trade-offs, no fluff.',
    name: 'Managing Director',
    org: 'Manufacturing SME',
    tint: 'bg-emerald/5 border-emerald/20',
    mark: 'text-emerald',
  },
  {
    quote: "Having someone senior to call before a decision, rather than after, changed how confidently we've been able to move.",
    name: 'Founder',
    org: 'Professional services firm',
    tint: 'bg-ink/5 border-ink/15',
    mark: 'text-ink',
  },
]
</script>

<template>
  <section id="testimonials" class="py-20 md:py-28">
    <div class="container-content">
      <h2 class="font-serif text-4xl md:text-5xl leading-tight tracking-tight max-w-xl mb-14">
        What that looks like from the other side of the table
      </h2>

      <div class="grid md:grid-cols-3 gap-6">
        <figure
          v-for="q in quotes"
          :key="q.name"
          class="flex flex-col p-7 rounded-2xl border"
          :class="q.tint"
        >
          <span class="font-serif text-6xl leading-none" :class="q.mark">"</span>
          <blockquote class="font-serif text-xl leading-snug text-ink text-balance -mt-4">
            {{ q.quote }}
          </blockquote>
          <figcaption class="mt-6 pt-6 border-t border-ink/10 text-sm">
            <span class="font-semibold text-ink">{{ q.name }}</span>
            <span class="block text-inkfade">{{ q.org }}</span>
          </figcaption>
        </figure>
      </div>
    </div>
  </section>
</template>
