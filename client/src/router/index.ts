import { createRouter, createWebHashHistory, RouteRecordRaw } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import LoginView from '../views/LoginView.vue'
import PreferencesView from '@/views/PreferencesView.vue'
import SavedView from '@/views/SavedView.vue'
import PoolView from '@/views/PoolView.vue'
import GenerateView from '@/views/GenerateView.vue'

const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/login',
    name: 'login',
    component: LoginView
  },
  {
    path: '/preferences',
    name: 'preferences',
    component: PreferencesView
  },
  {
    path: '/saved',
    name: 'saved',
    component: SavedView
  },
  {
    path: '/pool',
    name: 'pool',
    component: PoolView
  },
  {
    path: '/generate',
    name: 'generate',
    component: GenerateView
  },
  {
    path: '/:pathMatch(.*)*',
    redirect: '/'
  }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
