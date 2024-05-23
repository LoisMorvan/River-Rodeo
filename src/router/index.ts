import { createRouter, createWebHistory } from 'vue-router';
import HomeView from '../views/HomeView.vue';
import Login from '../views/Authentication/LoginView.vue';
import Register from '../views/Authentication/RegisterView.vue';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
      meta: { showNavbar: true }
    },
    {
      path: '/login',
      name: 'login',
      component: Login,
      meta: { showNavbar: true }
    },
    {
      path: '/register',
      name: 'register',
      component: Register,
      meta: { showNavbar: true }
    },
  ]
})

export default router