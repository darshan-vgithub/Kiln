<script setup>
import { onMounted, reactive, ref } from 'vue'
import { useRouter } from 'vue-router'
import { apiFetch } from '../lib/api'

const router = useRouter()
const jobs = ref([])
const loading = ref(true)
const error = ref('')
const savingId = ref(null)
const creating = ref(false)

const typeOptions = [
  { value: 'full_time', label: 'Full-time' },
  { value: 'part_time', label: 'Part-time' },
  { value: 'contract', label: 'Contract' },
  { value: 'internship', label: 'Internship' },
]

const blankForm = () => ({
  title: '',
  employment_type: 'full_time',
  location: 'Remote',
  description: '',
  apply_email: '',
  is_active: true,
})

const form = reactive(blankForm())
const showForm = ref(false)

async function load() {
  loading.value = true
  error.value = ''
  try {
    jobs.value = await apiFetch('/jobs/manage/')
  } catch (err) {
    if (err.status === 401) {
      router.push('/admin/login')
    } else {
      error.value = "Couldn't load jobs. Is the backend running?"
    }
  } finally {
    loading.value = false
  }
}

async function createJob() {
  creating.value = true
  error.value = ''
  try {
    const job = await apiFetch('/jobs/manage/', {
      method: 'POST',
      body: JSON.stringify(form),
    })
    jobs.value.unshift(job)
    Object.assign(form, blankForm())
    showForm.value = false
  } catch (err) {
    error.value = err.data?.title?.[0] || err.data?.apply_email?.[0] || "Couldn't create the posting. Check the fields."
  } finally {
    creating.value = false
  }
}

async function toggleActive(job) {
  savingId.value = job.id
  try {
    await apiFetch(`/jobs/manage/${job.id}/`, {
      method: 'PATCH',
      body: JSON.stringify({ is_active: !job.is_active }),
    })
    job.is_active = !job.is_active
  } catch {
    error.value = `Couldn't update "${job.title}".`
  } finally {
    savingId.value = null
  }
}

async function remove(job) {
  if (!confirm(`Delete "${job.title}"? This can't be undone.`)) return
  savingId.value = job.id
  try {
    await apiFetch(`/jobs/manage/${job.id}/`, { method: 'DELETE' })
    jobs.value = jobs.value.filter((j) => j.id !== job.id)
  } catch {
    error.value = `Couldn't delete "${job.title}".`
  } finally {
    savingId.value = null
  }
}

onMounted(load)
</script>

<template>
  <div class="dashboard">
    <header class="bar">
      <div>
        <span class="eyebrow">KILN ADMIN</span>
        <h1>Job postings</h1>
      </div>
      <div class="bar-actions">
        <router-link to="/admin" class="btn ghost">Inquiries</router-link>
        <button class="btn primary" type="button" @click="showForm = !showForm">
          {{ showForm ? 'Cancel' : 'New posting' }}
        </button>
      </div>
    </header>

    <p v-if="error" class="error" role="alert">{{ error }}</p>

    <form v-if="showForm" class="form" @submit.prevent="createJob">
      <div class="row">
        <label class="field">
          <span>Title</span>
          <input v-model="form.title" type="text" required />
        </label>
        <label class="field">
          <span>Type</span>
          <select v-model="form.employment_type">
            <option v-for="opt in typeOptions" :key="opt.value" :value="opt.value">{{ opt.label }}</option>
          </select>
        </label>
      </div>
      <div class="row">
        <label class="field">
          <span>Location</span>
          <input v-model="form.location" type="text" required />
        </label>
        <label class="field">
          <span>Apply email</span>
          <input v-model="form.apply_email" type="email" required />
        </label>
      </div>
      <label class="field">
        <span>Description</span>
        <textarea v-model="form.description" rows="4" required></textarea>
      </label>
      <button class="btn primary" type="submit" :disabled="creating">
        {{ creating ? 'Posting…' : 'Post job' }}
      </button>
    </form>

    <p v-if="loading" class="hint">Loading…</p>
    <p v-else-if="!jobs.length" class="hint">No postings yet.</p>

    <div v-else class="list">
      <article v-for="job in jobs" :key="job.id" class="card">
        <div class="card-top">
          <div>
            <h2>{{ job.title }}</h2>
            <span class="meta">{{ job.employment_type }} · {{ job.location }}</span>
          </div>
          <span class="status" :class="job.is_active ? 'live' : 'hidden'">
            {{ job.is_active ? 'Live' : 'Hidden' }}
          </span>
        </div>
        <p class="desc">{{ job.description }}</p>
        <div class="actions">
          <button class="btn ghost" :disabled="savingId === job.id" @click="toggleActive(job)">
            {{ job.is_active ? 'Hide from site' : 'Make live' }}
          </button>
          <button class="btn danger" :disabled="savingId === job.id" @click="remove(job)">Delete</button>
        </div>
      </article>
    </div>
  </div>
</template>

<style scoped>
.dashboard {
  max-width: 56rem;
  margin: 0 auto;
  padding: clamp(1.25rem, 4vw, 3rem);
  min-height: 100vh;
}

.bar {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
  margin-bottom: 1.5rem;
}

.eyebrow {
  display: block;
  font-family: var(--font-mono);
  font-size: 0.72rem;
  letter-spacing: 0.12em;
  color: var(--steel);
  margin-bottom: 0.4rem;
}

h1 {
  font-family: var(--font-display);
  font-weight: 600;
  font-size: 1.9rem;
  margin: 0;
}

.bar-actions {
  display: flex;
  gap: 0.7rem;
}

.error {
  color: var(--ember);
}

.hint {
  color: var(--text-muted);
}

.form {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  border: 1px solid var(--line);
  border-radius: 14px;
  background: var(--surface);
  padding: 1.4rem;
  margin-bottom: 1.5rem;
}

.row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1rem;
}

@media (max-width: 560px) {
  .row {
    grid-template-columns: 1fr;
  }
}

.field {
  display: flex;
  flex-direction: column;
  gap: 0.4rem;
  font-size: 0.88rem;
  color: var(--text-muted);
}

input,
select,
textarea {
  font-family: var(--font-body);
  font-size: 0.94rem;
  color: var(--text);
  background: var(--surface-2);
  border: 1px solid var(--line);
  border-radius: 8px;
  padding: 0.6rem 0.75rem;
}

textarea {
  resize: vertical;
}

.list {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.card {
  border: 1px solid var(--line);
  border-radius: 14px;
  background: var(--surface);
  padding: 1.4rem 1.6rem;
}

.card-top {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  gap: 0.8rem;
  margin-bottom: 0.6rem;
}

h2 {
  font-family: var(--font-display);
  font-size: 1.05rem;
  font-weight: 600;
  margin: 0 0 0.2rem;
}

.meta {
  font-size: 0.82rem;
  color: var(--text-muted);
  text-transform: capitalize;
}

.status {
  font-family: var(--font-mono);
  font-size: 0.7rem;
  letter-spacing: 0.06em;
  border-radius: 999px;
  padding: 0.25rem 0.65rem;
  white-space: nowrap;
}

.status.live {
  color: var(--steel);
  border: 1px solid var(--steel-dim);
}

.status.hidden {
  color: var(--text-muted);
  border: 1px solid var(--line);
}

.desc {
  color: var(--text-muted);
  font-size: 0.92rem;
  line-height: 1.55;
  margin: 0 0 1rem;
}

.actions {
  display: flex;
  gap: 0.7rem;
}

.btn {
  cursor: pointer;
  font-size: 0.86rem;
  padding: 0.55rem 1rem;
  border-radius: 8px;
  border: 1px solid var(--line);
}

.btn:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

.btn.ghost {
  background: transparent;
  color: var(--text);
  text-decoration: none;
}

.btn.ghost:hover {
  background: var(--surface-2);
}

.btn.primary {
  background: var(--text);
  color: var(--bg);
  border: none;
  font-weight: 600;
}

.btn.primary:hover:not(:disabled) {
  background: #fff;
}

.btn.danger {
  background: transparent;
  border-color: var(--ember-dim);
  color: var(--ember);
}

.btn.danger:hover:not(:disabled) {
  background: rgba(255, 107, 53, 0.08);
}
</style>