<template>
    <div class="friend-sidebar">
      <div class="tabs">
        <button :class="{ active: activeTab === 'friends' }" @click="activeTab = 'friends'">Amis</button>
        <button :class="{ active: activeTab === 'invitations' }" @click="activeTab = 'invitations'">Invitations</button>
      </div>
      <div class="content">
        <div v-if="activeTab === 'friends'">
          <ul>
            <li v-for="friend in friends" :key="friend.id">{{ friend.name }}</li>
          </ul>
        </div>
        <div v-if="activeTab === 'invitations'">
          <ul>
            <li v-for="invitation in invitations" :key="invitation.id">{{ invitation.name }}</li>
          </ul>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'FriendSideBar',
    props: {
      friends: {
        type: Array,
        required: true
      },
      invitations: {
        type: Array,
        required: true
      }
    },
    data() {
      return {
        activeTab: 'friends'
      };
    }
  }
  </script>
  
  <style scoped>
  .friend-sidebar {
    width: 250px;
    background-color: #000000;
    padding: 10px;
    position: fixed;
    top: 100px; /* Adjust this value based on your navbar height */
    right: 0;
    height: calc(100% - 100px); /* Adjust this value based on your navbar height */
    overflow-y: auto;
  }
  
  .tabs {
    display: flex;
    justify-content: space-between;
    margin-bottom: 10px;
  }
  
  .tabs button {
    flex: 1;
    padding: 10px;
    border: none;
    cursor: pointer;
    background-color: #ddd;
  }
  
  .tabs button.active {
    background-color: #bbb;
  }
  
  .content {
    border-top: 1px solid #ccc;
    padding-top: 10px;
  }
  
  ul {
    list-style: none;
    padding: 0;
  }
  
  li {
    padding: 5px 0;
  }
  </style>
  