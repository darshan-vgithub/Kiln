<script setup>
import { reactive, ref } from 'vue'

const form = reactive({
  name: '',
  email: '',
  company: '',
  message: '',
})

const submitted = ref(false)
const error = ref('')

function handleSubmit() {
  error.value = ''
  if (!form.name || !form.email || !form.message) {
    error.value = 'Please fill in your name, email and a short message.'
    return
  }
  // Wire this up to your backend or a form service (e.g. Formspree, a serverless function).
  submitted.value = true
}
</script>

<template>
  <section id="contact" class="py-20 md:py-28">
    <div class="container-content">
      <div class="grid md:grid-cols-2 rounded-3xl overflow-hidden border border-line">
        <div class="bg-ink text-paper p-10 md:p-14 flex flex-col justify-between relative overflow-hidden">
          <div class="relative">
            <h2 class="font-serif text-3xl md:text-4xl leading-tight tracking-tight text-balance">
              Let's work out what's worth doing next.
            </h2>
            <p class="mt-6 text-paper/70 leading-relaxed max-w-[38ch]">
              Tell us roughly what's going on — a system that's slowing you down, a product idea, a decision you're stuck on. We'll reply within one working day.
            </p>
          </div>

          <dl class="mt-14 space-y-4 text-sm relative">
            <div>
              <dt class="text-paper/50">Email</dt>
              <dd class="font-medium">hello@northlight.co</dd>
            </div>
            <div>
              <dt class="text-paper/50">Phone</dt>
              <dd class="font-medium">+44 (0)141 555 0134</dd>
            </div>
            <div>
              <dt class="text-paper/50">Based in</dt>
              <dd class="font-medium">Glasgow, Scotland</dd>
            </div>
          </dl>

          <svg class="hidden md:block absolute -right-16 -bottom-16 pointer-events-none" width="260" height="260" viewBox="0 0 260 260">
            <circle cx="130" cy="130" r="100" fill="none" stroke="rgba(243,241,235,0.12)" stroke-width="1.5"></circle>
            <circle cx="130" cy="130" r="70" fill="none" stroke="rgba(243,241,235,0.18)" stroke-width="1.5"></circle>
            <circle cx="130" cy="130" r="40" fill="none" stroke="rgba(36,56,224,0.5)" stroke-width="1.5"></circle>
          </svg>
        </div>

        <div class="p-10 md:p-14 bg-paper">
          <form v-if="!submitted" class="space-y-6" @submit.prevent="handleSubmit" novalidate>
            <div class="grid sm:grid-cols-2 gap-6">
              <div>
                <label for="name" class="block text-sm font-medium mb-2">Your name</label>
                <input
                  id="name"
                  v-model="form.name"
                  type="text"
                  required
                  class="w-full border-b border-ink/25 bg-transparent py-2.5 focus:border-cobalt outline-none transition-colors"
                />
              </div>
              <div>
                <label for="company" class="block text-sm font-medium mb-2">Company</label>
                <input
                  id="company"
                  v-model="form.company"
                  type="text"
                  class="w-full border-b border-ink/25 bg-transparent py-2.5 focus:border-cobalt outline-none transition-colors"
                />
              </div>
            </div>

            <div>
              <label for="email" class="block text-sm font-medium mb-2">Email</label>
              <input
                id="email"
                v-model="form.email"
                type="email"
                required
                class="w-full border-b border-ink/25 bg-transparent py-2.5 focus:border-cobalt outline-none transition-colors"
              />
            </div>

            <div>
              <label for="message" class="block text-sm font-medium mb-2">What's on your mind?</label>
              <textarea
                id="message"
                v-model="form.message"
                rows="4"
                required
                class="w-full border-b border-ink/25 bg-transparent py-2.5 focus:border-cobalt outline-none transition-colors resize-none"
              ></textarea>
            </div>

            <p v-if="error" class="text-sm text-red-600">{{ error }}</p>

            <button
              type="submit"
              class="inline-flex items-center gap-2 bg-cobalt text-paper text-sm font-semibold px-6 py-3.5 rounded-full hover:bg-cobaltdeep transition-colors"
            >
              Send message
            </button>
          </form>

          <div v-else class="h-full flex flex-col justify-center">
            <p class="font-serif text-2xl">Thanks — that's landed with us.</p>
            <p class="mt-3 text-inkfade">We'll get back to you at {{ form.email }} within one working day.</p>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>
