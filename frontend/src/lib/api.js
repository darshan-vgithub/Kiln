export const API_BASE = import.meta.env.VITE_API_BASE || 'http://127.0.0.1:8000/api'

const TOKEN_KEY = 'kiln_admin_token'

export function getToken() {
  return localStorage.getItem(TOKEN_KEY)
}

export function setToken(token) {
  localStorage.setItem(TOKEN_KEY, token)
}

export function clearToken() {
  localStorage.removeItem(TOKEN_KEY)
}

export function isLoggedIn() {
  return !!getToken()
}

/**
 * Fetch wrapper that attaches the admin auth token when present and
 * throws a friendly error with the parsed response body on failure.
 */
export async function apiFetch(path, options = {}) {
  const token = getToken()
  const headers = {
    'Content-Type': 'application/json',
    ...(options.headers || {}),
  }
  if (token) {
    headers['Authorization'] = `Token ${token}`
  }

  const res = await fetch(`${API_BASE}${path}`, { ...options, headers })

  if (res.status === 401) {
    clearToken()
  }

  let data = null
  try {
    data = await res.json()
  } catch {
    // no JSON body
  }

  if (!res.ok) {
    const error = new Error('Request failed')
    error.status = res.status
    error.data = data
    throw error
  }

  return data
}
