<script setup>
import Hero from '../components/Hero.vue'
import StatementBand from '../components/StatementBand.vue'
import ScrollStory from '../components/ScrollStory.vue'
</script>

<template>
  <div>
    <Hero />
    <StatementBand />
    <ScrollStory />

    <section class="border-t border-line py-20 md:py-28 text-center">
      <div class="container-content">
        <h2 class="font-serif text-3xl md:text-4xl tracking-tight max-w-xl mx-auto text-balance">
          Not sure which of those is your problem? That's what the first call is for.
        </h2>
        <div class="mt-8 flex flex-wrap justify-center gap-4">
          <router-link
            to="/contact"
            class="inline-flex items-center gap-2 bg-cobalt text-paper text-sm font-semibold px-6 py-3.5 rounded-full hover:bg-cobaltdeep transition-colors"
          >
            Book a first call
          </router-link>
          <router-link
            to="/work"
            class="inline-flex items-center gap-2 border border-ink/20 text-sm font-semibold px-6 py-3.5 rounded-full hover:border-ink transition-colors"
          >
            See recent work
          </router-link>
        </div>
      </div>
    </section>
  </div>
</template>
