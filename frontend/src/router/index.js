import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import AdminLogin from '../views/AdminLogin.vue'
import AdminDashboard from '../views/AdminDashboard.vue'
import AdminJobs from '../views/AdminJobs.vue'
import { isLoggedIn } from '../lib/api'
import Carrers from '../views/Carrers.vue'

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', name: 'home', component: Home, meta: { site: true } },
    { path: '/careers', name: 'careers', component: Carrers, meta: { site: true } },
    { path: '/admin/login', name: 'admin-login', component: AdminLogin, meta: { site: false } },
    {
      path: '/admin',
      name: 'admin-dashboard',
      component: AdminDashboard,
      meta: { site: false, requiresAuth: true },
    },
    {
      path: '/admin/jobs',
      name: 'admin-jobs',
      component: AdminJobs,
      meta: { site: false, requiresAuth: true },
    },
  ],
  scrollBehavior(to) {
    if (to.hash) return { el: to.hash, behavior: 'smooth' }
    return { top: 0 }
  },
})

router.beforeEach((to) => {
  if (to.meta.requiresAuth && !isLoggedIn()) {
    return { name: 'admin-login' }
  }
  return true
})

export default router