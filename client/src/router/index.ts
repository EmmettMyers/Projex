import { createRouter, createWebHashHistory, createWebHistory, RouteRecordRaw } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import LoginView from '../views/LoginView.vue'
import PreferencesView from '@/views/PreferencesView.vue'
import SavedView from '@/views/SavedView.vue'
import PoolView from '@/views/PoolView.vue'
import GenerateView from '@/views/GenerateView.vue'
import GeneratedView from '@/views/GeneratedView.vue'

const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    name: 'login',
    component: LoginView
  },
  {
    path: '/home',
    name: 'home',
    component: HomeView
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
    path: '/generated',
    name: 'generated',
    component: GeneratedView
  },
  {
    path: '/:pathMatch(.*)*',
    redirect: '/'
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
