<script setup>
const steps = [
  {
    title: 'Listen',
    detail: 'A working session with the people closest to the problem — not just the person who wrote the brief.',
    color: '#2438E0',
  },
  {
    title: 'Diagnose',
    detail: "Mapping where technology is genuinely helping, and where it's quietly costing time and money.",
    color: '#0F6E5C',
  },
  {
    title: 'Plan',
    detail: 'A written roadmap with priorities, rough costs and trade-offs spelled out — no black box.',
    color: '#2438E0',
  },
  {
    title: 'Support',
    detail: 'Staying involved through delivery, or handing off a plan a team can run with on their own.',
    color: '#0F6E5C',
  },
]
</script>

<template>
  <section id="process" class="bg-ink text-paper py-20 md:py-28">
    <div class="container-content">
      <h2 class="font-serif text-4xl md:text-5xl leading-tight tracking-tight max-w-xl">
        A process built to leave you with answers, not more homework
      </h2>

      <ol class="mt-16 grid sm:grid-cols-2 lg:grid-cols-4 gap-x-8 gap-y-14">
        <li v-for="(step, i) in steps" :key="step.title" class="pt-6 relative">
          <div class="absolute top-0 left-0 h-[3px] w-10" :style="{ backgroundColor: step.color }"></div>
          <span class="font-serif text-lg" :style="{ color: step.color }">{{ String(i + 1).padStart(2, '0') }}</span>
          <h3 class="mt-3 font-serif text-2xl">{{ step.title }}</h3>
          <p class="mt-3 text-paper/70 leading-relaxed">{{ step.detail }}</p>
        </li>
      </ol>
    </div>
  </section>
</template>
