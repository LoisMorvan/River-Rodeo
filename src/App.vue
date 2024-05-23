<template>
  <div id="app" class="app-container">
    <header>
      <Navbar v-if="showNavbar" @loggedOut="onLoggedOut" />
    </header>
    <div v-if="showLogoutMessage" class="success-message">You have logged out successfully!</div>
    <RouterView />
  </div>
</template>

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

<style scoped>
.app-container {
  background-image: url('assets/background_login.png'); /* Chemin vers votre image */
  background-size: cover; /* Ajuste l'image pour couvrir toute la zone */
  background-position: center; /* Centre l'image */
  background-repeat: no-repeat; /* Empêche la répétition de l'image */
  min-height: 100vh; /* Assure que le conteneur couvre toute la hauteur de la fenêtre */
}

.success-message {
  background-color: green;
  color: white;
  padding: 10px;
  text-align: center;
  margin-bottom: 10px;
}
</style>
