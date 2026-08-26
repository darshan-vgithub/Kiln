<script setup>
import { onMounted, ref } from 'vue'
import { API_BASE } from '../lib/api'

const jobs = ref([])
const loading = ref(true)
const error = ref('')

const typeLabels = {
  full_time: 'Full-time',
  part_time: 'Part-time',
  contract: 'Contract',
  internship: 'Internship',
}

async function loadJobs() {
  loading.value = true
  error.value = ''
  try {
    const res = await fetch(`${API_BASE}/jobs/`)
    if (!res.ok) throw new Error('bad response')
    jobs.value = await res.json()
  } catch {
    error.value = "Couldn't load openings. Please try again shortly."
  } finally {
    loading.value = false
  }
}

onMounted(loadJobs)
</script>

<template>
  <main class="careers">
    <div class="head">
      <span class="eyebrow">CAREERS</span>
      <h1>Come build with us</h1>
      <p class="lede">
        We're a small, hands-on team taking on client work across web and mobile.
        No account managers, no bureaucracy — just people who like shipping things.
      </p>
    </div>

    <p v-if="loading" class="hint">Loading openings…</p>
    <p v-else-if="error" class="hint error">{{ error }}</p>
    <p v-else-if="!jobs.length" class="hint">No open roles right now — check back soon.</p>

    <div v-else class="roles">
      <article v-for="job in jobs" :key="job.id" class="card">
        <span class="type">{{ typeLabels[job.employment_type] || job.employment_type }} · {{ job.location }}</span>
        <h2>{{ job.title }}</h2>
        <p>{{ job.description }}</p>
        <a class="apply" :href="`mailto:${job.apply_email}?subject=Application: ${job.title}`">Apply</a>
      </article>
    </div>

    <p class="none-fit">
      Don't see a fit but think you'd be a good addition anyway?
      <a href="mailto:careers@example.com">Reach out</a> — we're always open to hearing from good people.
    </p>
  </main>
</template>

<style scoped>
.careers {
  max-width: 56rem;
  margin: 0 auto;
  padding: clamp(2rem, 6vw, 4rem) clamp(1.25rem, 4vw, 3rem) 5rem;
}

.head {
  max-width: 40rem;
  margin-bottom: 2.5rem;
}

.eyebrow {
  display: block;
  font-family: var(--font-mono);
  font-size: 0.72rem;
  letter-spacing: 0.12em;
  color: var(--steel);
  margin-bottom: 0.6rem;
}

h1 {
  font-family: var(--font-display);
  font-weight: 700;
  font-size: clamp(2.2rem, 5vw, 3.2rem);
  margin: 0 0 0.8rem;
  letter-spacing: -0.02em;
}

.lede {
  color: var(--text-muted);
  line-height: 1.6;
  margin: 0;
}

.hint {
  color: var(--text-muted);
  margin-bottom: 2rem;
}

.hint.error {
  color: var(--ember);
}

.roles {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  margin-bottom: 2.5rem;
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

.type {
  display: inline-block;
  font-family: var(--font-mono);
  font-size: 0.7rem;
  letter-spacing: 0.06em;
  color: var(--ember);
  border: 1px solid var(--ember-dim);
  border-radius: 999px;
  padding: 0.25rem 0.65rem;
  margin-bottom: 0.8rem;
}

h2 {
  font-family: var(--font-display);
  font-size: 1.15rem;
  font-weight: 600;
  margin: 0 0 0.5rem;
}

p {
  color: var(--text-muted);
  font-size: 0.94rem;
  line-height: 1.55;
  margin: 0 0 1rem;
}

.apply {
  display: inline-block;
  text-decoration: none;
  font-weight: 600;
  font-size: 0.9rem;
  color: var(--text);
  border-bottom: 1px solid var(--steel);
}

.none-fit {
  color: var(--text-muted);
  font-size: 0.94rem;
}

.none-fit a {
  color: var(--text);
  font-weight: 600;
  text-decoration: underline;
  text-underline-offset: 3px;
}
</style>