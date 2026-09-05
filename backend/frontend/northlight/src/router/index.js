import { createRouter, createWebHistory } from 'vue-router'
import Home from '../pages/Home.vue'
import ServicesPage from '../pages/ServicesPage.vue'
import ProcessPage from '../pages/ProcessPage.vue'
import WorkPage from '../pages/WorkPage.vue'
import ContactPage from '../pages/ContactPage.vue'

const routes = [
  { path: '/', name: 'home', component: Home },
  { path: '/services', name: 'services', component: ServicesPage },
  { path: '/process', name: 'process', component: ProcessPage },
  { path: '/work', name: 'work', component: WorkPage },
  { path: '/contact', name: 'contact', component: ContactPage },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
  scrollBehavior() {
    return { top: 0 }
  },
})

export default router
