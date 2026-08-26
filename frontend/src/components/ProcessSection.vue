<script setup>
const steps = [
  {
    n: '01',
    title: 'Discover',
    body: 'A short call to understand the problem, your users, and what "done" looks like for this stage.',
  },
  {
    n: '02',
    title: 'Design',
    body: 'We scope the build, map the data model, and agree on a fixed timeline and price before writing code.',
  },
  {
    n: '03',
    title: 'Build',
    body: 'Weekly check-ins and a staging environment you can poke at from the first working version onward.',
  },
  {
    n: '04',
    title: 'Ship',
    body: 'Deployed, documented, and handed over with a walkthrough of how everything fits together.',
  },
  {
    n: '05',
    title: 'Support',
    body: 'Optional ongoing time for fixes and new features once real users are on the product.',
  },
]
</script>

<template>
  <section id="process" class="process">
    <div class="head">
      <span class="eyebrow">PROCESS</span>
      <h2>How an engagement runs</h2>
    </div>

    <ol class="steps">
      <li v-for="s in steps" :key="s.n" class="step">
        <span class="n">{{ s.n }}</span>
        <div class="body">
          <h3>{{ s.title }}</h3>
          <p>{{ s.body }}</p>
        </div>
      </li>
    </ol>
  </section>
</template>

<style scoped>
.process {
  padding: 2rem clamp(1.25rem, 4vw, 3rem) 4rem;
  max-width: 56rem;
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

.steps {
  list-style: none;
  margin: 0;
  padding: 0;
  border-top: 1px solid var(--line);
}

.step {
  display: flex;
  gap: 1.6rem;
  padding: 1.5rem 0;
  border-bottom: 1px solid var(--line);
}

.n {
  font-family: var(--font-mono);
  font-size: 0.95rem;
  color: var(--ember);
  min-width: 2.2rem;
  padding-top: 0.15rem;
}

h3 {
  font-family: var(--font-display);
  font-size: 1.1rem;
  font-weight: 600;
  margin: 0 0 0.35rem;
}

p {
  color: var(--text-muted);
  font-size: 0.94rem;
  line-height: 1.6;
  margin: 0;
  max-width: 38rem;
}
</style>
