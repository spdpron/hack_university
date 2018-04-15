import Vue from 'vue'
import Router from 'vue-router'
import Settings from '@/components/pages/SettingsPage'
import Dashboard from '@/components/pages/DashboardPage'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/dashboard',
      component: Dashboard
    },
    {
      path: '/settings',
      component: Settings
    }
  ]
})
