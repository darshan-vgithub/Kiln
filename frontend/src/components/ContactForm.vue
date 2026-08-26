<script setup>
import { reactive, ref } from 'vue'

const API_BASE = import.meta.env.VITE_API_BASE || 'http://127.0.0.1:8000/api'

const form = reactive({
  name: '',
  email: '',
  company: '',
  project_type: 'new_app',
  budget: 'not_sure',
  message: '',
})

const status = ref('idle') // idle | sending | success | error
const errors = ref({})
const errorSummary = ref('')

async function submit() {
  status.value = 'sending'
  errors.value = {}
  errorSummary.value = ''

  try {
    const res = await fetch(`${API_BASE}/inquiries/`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(form),
    })

    if (res.ok) {
      status.value = 'success'
      Object.assign(form, {
        name: '',
        email: '',
        company: '',
        project_type: 'new_app',
        budget: 'not_sure',
        message: '',
      })
      return
    }

    const data = await res.json().catch(() => ({}))
    if (res.status === 429) {
      errorSummary.value = "You've hit the hourly limit for submissions. Please try again shortly."
    } else if (data && typeof data === 'object') {
      errors.value = data
      errorSummary.value = 'Please fix the highlighted fields.'
    } else {
      errorSummary.value = 'Something went wrong. Please try again.'
    }
    status.value = 'error'
  } catch (err) {
    status.value = 'error'
    errorSummary.value = "Couldn't reach the server. Check your connection and try again."
  }
}
</script>

<template>
  <section id="contact" class="contact">
    <div class="head">
      <span class="eyebrow">CONTACT</span>
      <h2>Tell us about the project</h2>
      <p class="lede">A few details help us reply with something useful instead of a form email.</p>
    </div>

    <form v-if="status !== 'success'" class="form" novalidate @submit.prevent="submit">
      <div class="row">
        <label class="field">
          <span>Name</span>
          <input v-model="form.name" type="text" name="name" required autocomplete="name" />
          <span v-if="errors.name" class="field-error">{{ errors.name[0] }}</span>
        </label>

        <label class="field">
          <span>Email</span>
          <input v-model="form.email" type="email" name="email" required autocomplete="email" />
          <span v-if="errors.email" class="field-error">{{ errors.email[0] }}</span>
        </label>
      </div>

      <div class="row">
        <label class="field">
          <span>Company <em>(optional)</em></span>
          <input v-model="form.company" type="text" name="company" autocomplete="organization" />
        </label>

        <label class="field">
          <span>Budget</span>
          <select v-model="form.budget" name="budget">
            <option value="not_sure">Not sure yet</option>
            <option value="under_5k">Under $5k</option>
            <option value="5_15k">$5k – $15k</option>
            <option value="15_50k">$15k – $50k</option>
            <option value="over_50k">$50k+</option>
          </select>
        </label>
      </div>

      <label class="field">
        <span>Project type</span>
        <select v-model="form.project_type" name="project_type">
          <option value="new_app">New app build</option>
          <option value="existing">Existing product / ongoing work</option>
          <option value="mvp">MVP / prototype</option>
          <option value="consulting">Technical consulting</option>
          <option value="other">Something else</option>
        </select>
      </label>

      <label class="field">
        <span>What are you building?</span>
        <textarea
          v-model="form.message"
          name="message"
          rows="5"
          required
          placeholder="What it does, who it's for, and roughly when you'd want to start."
        ></textarea>
        <span v-if="errors.message" class="field-error">{{ errors.message[0] }}</span>
      </label>

      <div class="submit-row">
        <button class="btn primary" type="submit" :disabled="status === 'sending'">
          {{ status === 'sending' ? 'Sending…' : 'Send inquiry' }}
        </button>
        <span v-if="errorSummary" class="error-summary" role="alert">{{ errorSummary }}</span>
      </div>
    </form>

    <div v-else class="success" role="status">
      <span class="success-mark" aria-hidden="true">✓</span>
      <h3>Thanks — that's in.</h3>
      <p>We reply to every inquiry within 1–2 business days.</p>
      <button class="btn ghost" type="button" @click="status = 'idle'">Send another</button>
    </div>
  </section>
</template>

<style scoped>
.contact {
  padding: 2rem clamp(1.25rem, 4vw, 3rem) 5rem;
  max-width: 44rem;
  margin: 0 auto;
}

.head {
  margin-bottom: 2rem;
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
  margin: 0 0 0.5rem;
  letter-spacing: -0.01em;
}

.lede {
  color: var(--text-muted);
  margin: 0;
}

.form {
  display: flex;
  flex-direction: column;
  gap: 1.1rem;
  border: 1px solid var(--line);
  border-radius: 16px;
  background: var(--surface);
  padding: clamp(1.4rem, 4vw, 2rem);
}

.row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1.1rem;
}

@media (max-width: 560px) {
  .row {
    grid-template-columns: 1fr;
  }
}

.field {
  display: flex;
  flex-direction: column;
  gap: 0.45rem;
  font-size: 0.88rem;
  color: var(--text-muted);
}

.field em {
  font-style: normal;
  opacity: 0.7;
}

input,
select,
textarea {
  font-family: var(--font-body);
  font-size: 0.95rem;
  color: var(--text);
  background: var(--surface-2);
  border: 1px solid var(--line);
  border-radius: 9px;
  padding: 0.7rem 0.85rem;
}

textarea {
  resize: vertical;
  min-height: 7rem;
}

input:focus,
select:focus,
textarea:focus {
  border-color: var(--steel);
}

.field-error {
  color: var(--ember);
  font-size: 0.82rem;
}

.submit-row {
  display: flex;
  align-items: center;
  gap: 1rem;
  margin-top: 0.4rem;
  flex-wrap: wrap;
}

.btn {
  border: none;
  cursor: pointer;
  display: inline-block;
  text-decoration: none;
  padding: 0.85rem 1.6rem;
  border-radius: 10px;
  font-weight: 600;
  font-size: 0.98rem;
}

.btn.primary {
  background: var(--text);
  color: var(--bg);
}

.btn.primary:hover:not(:disabled) {
  background: #fff;
}

.btn.primary:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

.btn.ghost {
  background: transparent;
  border: 1px solid var(--line);
  color: var(--text);
}

.error-summary {
  color: var(--ember);
  font-size: 0.9rem;
}

.success {
  text-align: center;
  border: 1px solid var(--line);
  border-radius: 16px;
  background: var(--surface);
  padding: 3rem 2rem;
}

.success-mark {
  display: inline-grid;
  place-items: center;
  width: 3rem;
  height: 3rem;
  border-radius: 50%;
  background: linear-gradient(135deg, var(--ember), var(--steel));
  color: #0b0c0f;
  font-weight: 700;
  margin-bottom: 1rem;
}

.success h3 {
  font-family: var(--font-display);
  margin: 0 0 0.4rem;
}

.success p {
  color: var(--text-muted);
  margin: 0 0 1.4rem;
}
</style>
