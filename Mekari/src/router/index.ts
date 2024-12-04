import { createRouter, createWebHistory } from 'vue-router'

// Componentes
import Dashboard from '@/views/DashboardView.vue'
import RRHH from '@/views/RRHHViews.vue'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'Dashboard',
      component: Dashboard
    },
    {
      path: '/rrhh',
      name: 'rrhh',
      component: RRHH
    }
  ],
})

export default router
