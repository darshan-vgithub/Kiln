<script setup>
const services = [
  {
    tag: 'WEB + MOBILE',
    title: 'Custom app development',
    body: 'Full-stack builds for web and mobile, from data model to deployed product, in the stack that fits your team.',
  },
  {
    tag: '0 → 1',
    title: 'MVP & prototyping',
    body: 'A scoped, working version of your idea fast enough to put in front of real users or investors.',
  },
  {
    tag: 'ADVISORY',
    title: 'Technical consulting',
    body: 'Architecture reviews, stack decisions, and hands-on guidance for teams building in-house.',
  },
  {
    tag: 'MAINTENANCE',
    title: 'Ongoing product support',
    body: 'Bug fixes, new features, and steady iteration once your product is live and growing.',
  },
]
</script>

<template>
  <section id="services" class="services">
    <div class="head">
      <span class="eyebrow">SERVICES</span>
      <h2>What we take on</h2>
    </div>

    <div class="grid">
      <article v-for="s in services" :key="s.title" class="card">
        <span class="tag">{{ s.tag }}</span>
        <h3>{{ s.title }}</h3>
        <p>{{ s.body }}</p>
      </article>
    </div>
  </section>
</template>

<style scoped>
.services {
  padding: 3rem clamp(1.25rem, 4vw, 3rem) 4rem;
  max-width: 74rem;
  margin: 0 auto;
}

.head {
  margin-bottom: 2.2rem;
}

.eyebrow {
  display: block;
  font-family: var(--font-mono);
  font-size: 0.72rem;
  letter-spacing: 0.12em;
  color: var(--steel);
  margin-bottom: 0.6rem;
}

h2 {
  font-family: var(--font-display);
  font-weight: 600;
  font-size: clamp(1.7rem, 3vw, 2.3rem);
  margin: 0;
  letter-spacing: -0.01em;
}

.grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(15.5rem, 1fr));
  gap: 1.1rem;
}

.card {
  border: 1px solid var(--line);
  border-radius: 14px;
  background: var(--surface);
  padding: 1.6rem;
  transition: border-color 0.15s ease, background 0.15s ease;
}

.card:hover {
  border-color: rgba(255, 107, 53, 0.35);
  background: var(--surface-2);
}

.tag {
  display: inline-block;
  font-family: var(--font-mono);
  font-size: 0.68rem;
  letter-spacing: 0.08em;
  color: var(--ember);
  border: 1px solid var(--ember-dim);
  border-radius: 999px;
  padding: 0.25rem 0.65rem;
  margin-bottom: 0.9rem;
}

h3 {
  font-family: var(--font-display);
  font-size: 1.15rem;
  font-weight: 600;
  margin: 0 0 0.5rem;
}

p {
  color: var(--text-muted);
  font-size: 0.92rem;
  line-height: 1.55;
  margin: 0;
}
</style>
