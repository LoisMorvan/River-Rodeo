// stores/authStore.js
import { defineStore } from 'pinia';
import api from '@/axiosInstances';

export const useAuthStore = defineStore('auth', {
  id: 'auth',
  state: () => ({
    isAuthenticated: false
  }),
  actions: {
    setAuthenticated(value) {
      this.isAuthenticated = value;
    },
    checkAuthentication() {
      api
        .get('/auth/check-auth/') // Remplacez par votre endpoint de vérification de l'authentification
        .then(() => {
          useAuthStore().setAuthenticated(true); // L'utilisateur est connecté si le token est valide
        })
        .catch(() => {
          useAuthStore().setAuthenticated(false); // L'utilisateur n'est pas connecté ou le token est invalide
        });
    },
    async logout() {
      try {
        await api.post('/auth/logout/');
        localStorage.removeItem('auth_token');
        this.isAuthenticated = false;
      } catch (error) {
        console.error(error);
      }
    }
  }
});
