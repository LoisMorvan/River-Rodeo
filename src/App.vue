<script setup lang="ts">
import { ref } from 'vue';
import { RouterLink, RouterView } from 'vue-router';
import Navbar from './views/Authentication/NavbarView.vue';

const showLogoutMessage = ref(false);

const onLoggedOut = () => {
  showLogoutMessage.value = true;
  setTimeout(() => {
    showLogoutMessage.value = false;
  }, 3000);
};
</script>

<template>
  <header>
    <Navbar @loggedOut="onLoggedOut" />
  </header>
  <div v-if="showLogoutMessage" class="success-message">
    You have logged out successfully!
  </div>

  <RouterView />
</template>

<style scoped>
.success-message {
  background-color: green;
  color: white;
  padding: 10px;
  text-align: center;
  margin-bottom: 10px;
}
</style>