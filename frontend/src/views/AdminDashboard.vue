<script setup>
import { onMounted, ref } from 'vue'
import { useRouter } from 'vue-router'
import { apiFetch, clearToken } from '../lib/api'

const router = useRouter()
const inquiries = ref([])
const loading = ref(true)
const error = ref('')
const statusFilter = ref('')
const savingId = ref(null)

const statusOptions = [
  { value: '', label: 'All statuses' },
  { value: 'new', label: 'New' },
  { value: 'reviewed', label: 'Reviewed' },
  { value: 'contacted', label: 'Contacted' },
  { value: 'archived', label: 'Archived' },
]

const projectTypeLabels = {
  new_app: 'New app build',
  existing: 'Existing product',
  mvp: 'MVP / prototype',
  consulting: 'Technical consulting',
  other: 'Other',
}

const budgetLabels = {
  under_5k: 'Under $5k',
  '5_15k': '$5k – $15k',
  '15_50k': '$15k – $50k',
  over_50k: '$50k+',
  not_sure: 'Not sure yet',
}

async function load() {
  loading.value = true
  error.value = ''
  try {
    const query = statusFilter.value ? `?status=${statusFilter.value}` : ''
    const data = await apiFetch(`/inquiries/list/${query}`)
    inquiries.value = data.results
  } catch (err) {
    if (err.status === 401) {
      router.push('/admin/login')
    } else {
      error.value = "Couldn't load inquiries. Is the backend running?"
    }
  } finally {
    loading.value = false
  }
}

async function updateStatus(inquiry, newStatus) {
  savingId.value = inquiry.id
  try {
    await apiFetch(`/inquiries/${inquiry.id}/status/`, {
      method: 'PATCH',
      body: JSON.stringify({ status: newStatus }),
    })
    inquiry.status = newStatus
  } catch {
    error.value = `Couldn't update status for ${inquiry.name}.`
  } finally {
    savingId.value = null
  }
}

function logout() {
  clearToken()
  router.push('/admin/login')
}

function formatDate(iso) {
  return new Date(iso).toLocaleString(undefined, {
    dateStyle: 'medium',
    timeStyle: 'short',
  })
}

onMounted(load)
</script>

<template>
  <div class="dashboard">
    <header class="bar">
      <div>
        <span class="eyebrow">KILN ADMIN</span>
        <h1>Inquiries</h1>
      </div>
      <div class="bar-actions">
        <select v-model="statusFilter" @change="load">
          <option v-for="opt in statusOptions" :key="opt.value" :value="opt.value">
            {{ opt.label }}
          </option>
        </select>
        <router-link to="/admin/jobs" class="btn ghost">Job postings</router-link>
        <button class="btn ghost" type="button" @click="logout">Sign out</button>
      </div>
    </header>

    <p v-if="error" class="error" role="alert">{{ error }}</p>

    <p v-if="loading" class="hint">Loading…</p>

    <p v-else-if="!inquiries.length" class="hint">No inquiries yet.</p>

    <div v-else class="list">
      <article v-for="inquiry in inquiries" :key="inquiry.id" class="card">
        <div class="card-top">
          <div>
            <h2>{{ inquiry.name }}</h2>
            <a class="email" :href="`mailto:${inquiry.email}`">{{ inquiry.email }}</a>
            <span v-if="inquiry.company"> · {{ inquiry.company }}</span>
          </div>
          <select
            class="status-select"
            :class="`status-${inquiry.status}`"
            :value="inquiry.status"
            :disabled="savingId === inquiry.id"
            @change="updateStatus(inquiry, $event.target.value)"
          >
            <option value="new">New</option>
            <option value="reviewed">Reviewed</option>
            <option value="contacted">Contacted</option>
            <option value="archived">Archived</option>
          </select>
        </div>

        <div class="tags">
          <span class="tag">{{ projectTypeLabels[inquiry.project_type] || inquiry.project_type }}</span>
          <span class="tag">{{ budgetLabels[inquiry.budget] || inquiry.budget }}</span>
          <span class="date">{{ formatDate(inquiry.created_at) }}</span>
        </div>

        <p class="message">{{ inquiry.message }}</p>
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
  margin-bottom: 2rem;
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
  align-items: center;
  gap: 0.7rem;
}

select,
.status-select {
  font-family: var(--font-body);
  font-size: 0.88rem;
  color: var(--text);
  background: var(--surface-2);
  border: 1px solid var(--line);
  border-radius: 8px;
  padding: 0.55rem 0.7rem;
}

.btn.ghost {
  cursor: pointer;
  background: transparent;
  border: 1px solid var(--line);
  color: var(--text);
  font-size: 0.88rem;
  padding: 0.55rem 1rem;
  border-radius: 8px;
}

.btn.ghost:hover {
  background: var(--surface-2);
}

.error {
  color: var(--ember);
}

.hint {
  color: var(--text-muted);
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
  flex-wrap: wrap;
  align-items: flex-start;
  justify-content: space-between;
  gap: 0.8rem;
  margin-bottom: 0.7rem;
}

h2 {
  font-family: var(--font-display);
  font-size: 1.05rem;
  font-weight: 600;
  margin: 0 0 0.2rem;
}

.email {
  color: var(--text-muted);
  font-size: 0.88rem;
  text-decoration: none;
}

.email:hover {
  text-decoration: underline;
}

.status-select.status-new {
  color: var(--ember);
  border-color: var(--ember-dim);
}

.status-select.status-contacted,
.status-select.status-reviewed {
  color: var(--steel);
  border-color: var(--steel-dim);
}

.tags {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 0.5rem;
  margin-bottom: 0.9rem;
}

.tag {
  font-family: var(--font-mono);
  font-size: 0.7rem;
  letter-spacing: 0.04em;
  color: var(--text-muted);
  border: 1px solid var(--line);
  border-radius: 999px;
  padding: 0.25rem 0.65rem;
}

.date {
  font-size: 0.78rem;
  color: var(--text-muted);
  margin-left: auto;
}

.message {
  color: var(--text);
  font-size: 0.94rem;
  line-height: 1.6;
  margin: 0;
}
</style>
