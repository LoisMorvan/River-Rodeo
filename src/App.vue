<script setup lang="ts">
import { ref, computed } from 'vue';
import { RouterLink, RouterView, useRoute } from 'vue-router';
import Navbar from './views/Authentication/NavbarView.vue';

const showLogoutMessage = ref(false);
const route = useRoute();

const onLoggedOut = () => {
  showLogoutMessage.value = true;
  setTimeout(() => {
    showLogoutMessage.value = false;
  }, 3000);
};

const showNavbar = computed(() => {
  // Vérifiez la métadonnée pour déterminer si la navbar doit être affichée
  return route.meta.showNavbar !== false;
});


</script>

<template>
  <header>
    <Navbar v-if="showNavbar" @loggedOut="onLoggedOut" />
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