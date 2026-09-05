<script setup>
import { ref } from 'vue'

const open = ref(false)
const links = [
  { label: 'Services', to: '/services' },
  { label: 'Process', to: '/process' },
  { label: 'Work', to: '/work' },
  { label: 'Contact', to: '/contact' },
]
</script>

<template>
  <header class="sticky top-0 z-50 bg-paper/90 backdrop-blur-sm border-b border-line">
    <div class="container-content flex items-center justify-between h-20">
      <router-link to="/" class="flex items-baseline gap-2">
        <span class="font-serif text-2xl tracking-tight">Northlight</span>
        <span class="hidden sm:inline text-xs text-inkfade font-medium">Digital &amp; Technology Consulting</span>
      </router-link>

      <nav class="hidden md:flex items-center gap-8">
        <router-link
          v-for="link in links"
          :key="link.to"
          :to="link.to"
          class="text-sm font-medium text-ink/80 hover:text-ink transition-colors"
          active-class="text-ink font-semibold"
        >
          {{ link.label }}
        </router-link>
      </nav>

      <router-link
        to="/contact"
        class="hidden md:inline-flex items-center gap-2 bg-ink text-paper text-sm font-semibold px-5 py-2.5 rounded-full hover:bg-cobalt transition-colors"
      >
        Start a conversation
      </router-link>

      <button
        class="md:hidden p-2 -mr-2"
        @click="open = !open"
        :aria-expanded="open"
        aria-label="Toggle menu"
      >
        <svg v-if="!open" width="24" height="24" viewBox="0 0 24 24" fill="none"><path d="M3 6h18M3 12h18M3 18h18" stroke="#15171B" stroke-width="1.75" stroke-linecap="round"/></svg>
        <svg v-else width="24" height="24" viewBox="0 0 24 24" fill="none"><path d="M5 5l14 14M19 5L5 19" stroke="#15171B" stroke-width="1.75" stroke-linecap="round"/></svg>
      </button>
    </div>

    <div v-if="open" class="md:hidden border-t border-line bg-paper">
      <div class="container-content py-4 flex flex-col gap-4">
        <router-link
          v-for="link in links"
          :key="link.to"
          :to="link.to"
          class="text-base font-medium"
          active-class="text-cobalt"
          @click="open = false"
        >
          {{ link.label }}
        </router-link>
        <router-link
          to="/contact"
          class="inline-flex justify-center items-center gap-2 bg-ink text-paper text-sm font-semibold px-5 py-3 rounded-full"
          @click="open = false"
        >
          Start a conversation
        </router-link>
      </div>
    </div>
  </header>
</template>
