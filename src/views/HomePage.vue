<template>
  <div class="home-view" :style="{ backgroundImage: `url(${backgroundImage})` }">
    <div class="header"></div>
    <div class="content">
      <button v-if="isAuthenticated" class="main-button bordered-button" @click="openPlayPopup">
        Play
      </button>
      <button
        v-if="isAuthenticated"
        class="main-button bordered-button"
        @click="openSearchPartyPopup"
      >
        Search Party
      </button>
      <button v-if="isAuthenticated" class="main-button bordered-button" @click="goToMyAccount">
        My Account
      </button>
      <button v-if="isAuthenticated" class="main-button bordered-button" @click="goToSettings">
        Settings
      </button>
    </div>
    <FriendSideBarComponent v-if="isAuthenticated" :friends="friends" :invitations="invitations" />
    <div v-if="showSearchPartyPopup" class="popup">
      <div class="popup-content">
        <h3>Search Party</h3>
        <input type="text" v-model="searchPartyId" placeholder="Enter ID" />
        <button @click="confirmSearchParty">Confirm</button>
        <button @click="showSearchPartyPopup = false">Cancel</button>
      </div>
    </div>
    <div v-if="showPlayPopup" class="popup">
      <div class="popup-content">
        <h3>Play Party</h3>
        <input type="number" v-model="minAmount" placeholder="Enter Min Amount" />
        <button @click="confirmPlayParty">Confirm</button>
        <button @click="showPlayPopup = false">Cancel</button>
      </div>
    </div>
  </div>
</template>

<script>
import { useAuthStore } from '@/stores/authStore';
import FriendSideBarComponent from '@/components/Friends/FriendSideBarComponent.vue';
import api from '@/axiosInstances';

export default {
  components: {
    FriendSideBarComponent
  },
  data() {
    return {
      backgroundImage: 'assets/background_home.png',
      showSearchPartyPopup: false,
      showPlayPopup: false,
      searchPartyId: '',
      minAmount: '',
      friends: [
        { id: 1, name: 'Friend 1' },
        { id: 2, name: 'Friend 2' },
        { id: 3, name: 'Friend 3' }
      ],
      invitations: [
        { id: 1, name: 'Invitation 1' },
        { id: 2, name: 'Invitation 2' }
      ]
    };
  },
  computed: {
    isAuthenticated() {
      return useAuthStore().isAuthenticated; // Accès au state isAuthenticated du store
    }
  },

  methods: {
    openSearchPartyPopup() {
      this.showSearchPartyPopup = true;
    },
    openPlayPopup() {
      this.showPlayPopup = true;
    },
    confirmSearchParty() {
      console.log('Search Party ID:', this.searchPartyId);
      this.showSearchPartyPopup = false;
    },
    confirmPlayParty() {
      const payload = { min_amount: this.minAmount };
      api
        .post('/party/create/', payload)
        .then(() => {
          console.log('Party created successfully');
        })
        .catch((error) => {
          console.error('Error creating party:', error);
        });

      console.log('Min Amount:', this.minAmount);
      this.showPlayPopup = false;
    },
    goToMyAccount() {
      // TODO: Logique pour naviguer vers My Account
      console.log('Navigating to My Account');
    },
    goToSettings() {
      // TODO: Logique pour naviguer vers Settings
      console.log('Navigating to Settings');
    }
  },
  mounted() {
    useAuthStore().checkAuthentication();
  }
};
</script>
<style scoped>
.home-view {
  display: flex;
  flex-direction: column;
  align-items: center;
  background-size: cover;
  background-position: center;
  width: 100vw;
}

.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  width: 100%;
  padding: 20px;
}

.logo {
  width: 50px;
  height: 50px;
}

.title {
  font-size: 2rem;
  color: #ffffff;
}

.content {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  margin-top: 100px;
}

.main-button {
  font-size: 1.5rem;
  padding: 10px 20px;
  margin: 10px;
  background-color: #060606;
  color: #ffffff;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.2);
  width: 300px;
  height: 50px;
  border-radius: 50% 50% 52% 48% / 43% 49% 51% 57%;
}

.main-button:hover {
  background-color: #b12317;
}

.bordered-button {
  border: 2px solid red;
}

.popup {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
}

.popup-content {
  background: #ffffff;
  padding: 20px;
  border-radius: 5px;
  text-align: center;
}

.popup-content input {
  margin-bottom: 10px;
  padding: 5px;
  width: 80%;
}

.popup-content h3 {
  color: #505050;
}
</style>
