<script>
export default {
  data() {
    return {
      friends: [
        { id: 1, name: 'Friend 1' },
        { id: 2, name: 'Friend 2' },
        { id: 3, name: 'Friend 3' }
      ],
      showSearchPartyPopup: false,
      showPlayPopup: false,
      searchPartyId: '',
      minAmount: ''
    };
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
      console.log('Min Amount:', this.minAmount);
      this.showPlayPopup = false;
    }
  }
};
</script>

<template>
  <div class="home-view" :style="{ backgroundImage: `url(${backgroundImage})` }">
    <div class="header"></div>
    <div class="content">
      <button class="main-button bordered-button" @click="openPlayPopup">Play</button>
      <button class="main-button bordered-button" @click="openSearchPartyPopup">
        Search Party
      </button>
    </div>
    <div class="friend-list">
      <h3>Friend List</h3>
      <ul>
        <li v-for="friend in friends" :key="friend.id">{{ friend.name }}</li>
      </ul>
    </div>
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

.friend-list {
  position: absolute;
  right: 20px;
  top: 50%;
  transform: translateY(-50%);
  color: #fbf9f9;
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
</style>
