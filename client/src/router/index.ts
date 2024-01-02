import { createRouter, createWebHashHistory, createWebHistory, RouteRecordRaw } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import LoginView from '../views/LoginView.vue'
import PreferencesView from '@/views/PreferencesView.vue'
import SavedView from '@/views/SavedView.vue'
import PoolView from '@/views/PoolView.vue'
import GenerateView from '@/views/GenerateView.vue'
import GeneratedView from '@/views/GeneratedView.vue'
import LoadingView from '@/views/LoadingView.vue'
import AuthView from '@/views/AuthView.vue'

const isAuthenticated = () => {
  return localStorage.getItem('userEmail') !== '';
};

const authGuard = (to: any, from: any, next: any) => {
  if (isAuthenticated()) {
    next();
  } else {
    next({ name: 'login' });
  }
};

const routes: Array<RouteRecordRaw> = [
  {
    path: '/login',
    name: 'login',
    component: LoginView
  },
  {
    path: '/auth',
    name: 'auth',
    component: AuthView
  },
  {
    path: '/loading',
    name: 'loading',
    component: LoadingView
  },
  {
    path: '/home',
    name: 'home',
    component: HomeView,
    beforeEnter: authGuard
  },
  {
    path: '/preferences',
    name: 'preferences',
    component: PreferencesView,
    beforeEnter: authGuard
  },
  {
    path: '/saved',
    name: 'saved',
    component: SavedView,
    beforeEnter: authGuard
  },
  {
    path: '/pool',
    name: 'pool',
    component: PoolView,
    beforeEnter: authGuard
  },
  {
    path: '/generate',
    name: 'generate',
    component: GenerateView,
    beforeEnter: authGuard
  },
  {
    path: '/generated',
    name: 'generated',
    component: GeneratedView,
    beforeEnter: authGuard
  },
  {
    path: '/:pathMatch(.*)*',
    redirect: '/auth'
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
