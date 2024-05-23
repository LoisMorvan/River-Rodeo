<template>
  <nav class="navbar">
    <div @click="goToHome" href="/" class="navbar-logo">
      <img src="@/assets/logo-navbar.svg" alt="Logo" />
      <div class="navbar-brand">River Rodeo</div>
    </div>
    <div class="navbar-links">
      <button v-if="!isLoggedIn" @click="goToLogin" class="button-login">Login</button>
      <button v-if="!isLoggedIn" @click="goToRegister" class="button-register">Register</button>
      <button v-if="isLoggedIn" @click="logout" class="button-logout">Logout</button>
    </div>
  </nav>
</template>

<script>
import api from '../../axiosInstances';

export default {
  emits: ['loggedOut'],
  data() {
    return {
      isLoggedIn: !!localStorage.getItem('auth_token')
    };
  },
  watch: {
    $route: function () {
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
    goToHome() {
      this.$router.push('/');
    },
    goToLogin() {
      this.$router.push('/login');
    },
    goToRegister() {
      this.$router.push('/register');
    }
  }
};
</script>

<style scoped>
.navbar {
  background-color: black; /* Définit la couleur de fond en noir */
  display: grid;
  grid-template-columns: 1fr 1fr;
  align-items: center;
  padding: 10px 60px;
}

.navbar-logo {
  display: flex;
  align-items: center;
  gap: 10px;
}

.navbar-brand {
  font-family: 'Jomhuria';
  color: #ffffff;
  font-size: 50px;
}

.navbar-links {
  display: flex;
  justify-content: flex-end;
  gap: 45px;
}

.navbar-links button {
  align-items: center;
  border: 0;
  border-radius: 100px;
  box-sizing: border-box;
  color: #ffffff;
  cursor: pointer;
  display: inline-flex;
  font-size: 32px;
  justify-content: center;
  line-height: 20px;
  max-width: 480px;
  min-height: 60px;
  min-width: 175px;
  overflow: hidden;
  padding: 0px;
  padding-left: 20px;
  padding-right: 20px;
  text-align: center;
  touch-action: manipulation;
  transition:
    background-color 0.167s cubic-bezier(0.4, 0, 0.2, 1) 0s,
    box-shadow 0.167s cubic-bezier(0.4, 0, 0.2, 1) 0s,
    color 0.167s cubic-bezier(0.4, 0, 0.2, 1) 0s;
  user-select: none;
  -webkit-user-select: none;
  vertical-align: middle;
}

.navbar-links button.button-register {
  background-color: #02bd9c;
}

.navbar-links button.button-register:hover,
.navbar-links button.button-register:focus {
  background-color: #089b80;
  color: #ffffff;
}

.navbar-links button.button-register:active {
  background: #05d6ae;
  color: rgb(255, 255, 255, 0.7);
}

.navbar-links button.button-login,
.navbar-links button.button-logout {
  border: 2px solid #ffffff;
  background-color: transparent;
}

.navbar-links button.button-login:hover,
.navbar-links button.button-logout:hover,
.navbar-links button.button-login:focus,
.navbar-links button.button-logout:focus {
  background-color: #999999;
  color: #ffffff;
}

.navbar-links button.button-login:active,
.navbar-links button.button-logout:active {
  background: #333333;
  color: rgb(255, 255, 255, 0.7);
}
</style>
