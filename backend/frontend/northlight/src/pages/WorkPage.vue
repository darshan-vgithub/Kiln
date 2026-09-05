<script setup>
import Work from '../components/Work.vue'
import Testimonials from '../components/Testimonials.vue'
</script>

<template>
  <div>
    <section class="pt-16 pb-4 md:pt-24">
      <div class="container-content">
        <p class="text-sm font-medium text-cobalt mb-4">Work</p>
        <h1 class="font-serif text-4xl md:text-5xl leading-tight tracking-tight max-w-2xl">
          Recent engagements and what came out of them
        </h1>
      </div>
    </section>
    <Work />
    <Testimonials />
  </div>
</template>
