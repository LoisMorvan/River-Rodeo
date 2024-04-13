<template>
  <button v-if="!isLoggedIn" @click="goToLogin">Login</button>
  <button v-if="!isLoggedIn" @click="goToRegister">Register</button>
  <button v-if="isLoggedIn" @click="logout">Logout</button>
</template>

<script>
import api from '../../axiosInstances';

export default {
  emits: ['loggedOut'],
  data() {
    return {
      isLoggedIn: !!localStorage.getItem('auth_token'),
    };
  },
  watch: {
    '$route': function () {
      this.isLoggedIn = !!localStorage.getItem('auth_token');
    }
  },
  methods: {
    async logout() {
      try {
        await api.post('/auth/logout/');
        localStorage.removeItem('auth_token');
        this.isLoggedIn = false;
        this.$router.push('/');
        this.$emit('loggedOut');
      } catch (error) {
        console.error(error);
      }
    },
    goToLogin() {
      this.$router.push('/login');
    },
    goToRegister() {
      this.$router.push('/register');
    },
  },
};
</script>