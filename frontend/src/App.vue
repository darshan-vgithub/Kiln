<script setup>
import { useRoute } from 'vue-router'
import NavBar from './components/NavBar.vue'
import SiteFooter from './components/SiteFooter.vue'

const route = useRoute()
</script>

<template>
  <NavBar v-if="route.meta.site" />
  <router-view />
  <SiteFooter v-if="route.meta.site" />
</template>
