<script>
export default {
  data() {
    return {
      friends: [
        { id: 1, name: 'Friend 1' },
        { id: 2, name: 'Friend 2' },
        { id: 3, name: 'Friend 3' }
      ]
    };
  }
};
</script>

<template>
  <div class="home-view" :style="{ backgroundImage: `url(${backgroundImage})` }">
    <div class="header"></div>
    <div class="content">
      <button class="main-button bordered-button">Play</button>
      <button class="main-button bordered-button">Search Party</button>
      <button class="main-button bordered-button">My Account</button>
      <button class="main-button bordered-button">Settings</button>
    </div>
    <div class="friend-list">
      <h3>Friend List</h3>
      <ul>
        <li v-for="friend in friends" :key="friend.id">{{ friend.name }}</li>
      </ul>
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
</style>
