import { createRouter, createWebHistory } from 'vue-router';
import Login from '../views/Authentication/LoginView.vue';
import Register from '../views/Authentication/RegisterView.vue';
import HomePage from '../views/HomePage.vue';
import Party from '../views/Party.vue';

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
    },
    {
      path: '/party/:id',
      name: 'party',
      component: Party,
      meta: { showNavbar: false },
      props: true
    }
  ]
});

export default router;
