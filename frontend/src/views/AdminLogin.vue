<script setup>
import { reactive, ref } from 'vue'
import { useRouter } from 'vue-router'
import { API_BASE, setToken } from '../lib/api'

const router = useRouter()
const form = reactive({ username: '', password: '' })
const error = ref('')
const loading = ref(false)

async function submit() {
  error.value = ''
  loading.value = true
  try {
    const res = await fetch(`${API_BASE}/auth/login/`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(form),
    })

    if (!res.ok) {
      error.value = 'Wrong username or password.'
      return
    }

    const data = await res.json()
    setToken(data.token)
    router.push('/admin')
  } catch {
    error.value = "Couldn't reach the server. Is the backend running?"
  } finally {
    loading.value = false
  }
}
</script>

<template>
  <div class="login-page">
    <form class="login-card" @submit.prevent="submit">
      <span class="eyebrow">KILN ADMIN</span>
      <h1>Sign in</h1>
      <p class="lede">Use your Django account to view submitted inquiries.</p>

      <label class="field">
        <span>Username</span>
        <input v-model="form.username" type="text" autocomplete="username" required />
      </label>

      <label class="field">
        <span>Password</span>
        <input v-model="form.password" type="password" autocomplete="current-password" required />
      </label>

      <p v-if="error" class="error" role="alert">{{ error }}</p>

      <button class="btn" type="submit" :disabled="loading">
        {{ loading ? 'Signing in…' : 'Sign in' }}
      </button>
    </form>
  </div>
</template>

<style scoped>
.login-page {
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 2rem;
}

.login-card {
  width: 100%;
  max-width: 24rem;
  border: 1px solid var(--line);
  border-radius: 16px;
  background: var(--surface);
  padding: 2.2rem;
  display: flex;
  flex-direction: column;
  gap: 1.1rem;
}

.eyebrow {
  font-family: var(--font-mono);
  font-size: 0.72rem;
  letter-spacing: 0.12em;
  color: var(--steel);
}

h1 {
  font-family: var(--font-display);
  font-weight: 600;
  font-size: 1.7rem;
  margin: 0.2rem 0 0;
}

.lede {
  color: var(--text-muted);
  font-size: 0.92rem;
  margin: 0 0 0.4rem;
}

.field {
  display: flex;
  flex-direction: column;
  gap: 0.4rem;
  font-size: 0.88rem;
  color: var(--text-muted);
}

input {
  font-family: var(--font-body);
  font-size: 0.95rem;
  color: var(--text);
  background: var(--surface-2);
  border: 1px solid var(--line);
  border-radius: 9px;
  padding: 0.7rem 0.85rem;
}

input:focus {
  border-color: var(--steel);
}

.error {
  color: var(--ember);
  font-size: 0.88rem;
  margin: 0;
}

.btn {
  border: none;
  cursor: pointer;
  background: var(--text);
  color: var(--bg);
  font-weight: 600;
  font-size: 0.98rem;
  padding: 0.85rem;
  border-radius: 10px;
  margin-top: 0.3rem;
}

.btn:hover:not(:disabled) {
  background: #fff;
}

.btn:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}
</style>
