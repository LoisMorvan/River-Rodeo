import { createRouter, createWebHistory } from 'vue-router';
import Login from '../views/Authentication/LoginView.vue';
import Register from '../views/Authentication/RegisterView.vue';
import HomePage from '../views/HomePage.vue';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomePage,
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
    }
  ]
});

export default router;
