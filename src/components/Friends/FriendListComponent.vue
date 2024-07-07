<template>
    <div class="friend-list">
      <h3>Friend List</h3>
      <ul>
        <li v-for="friend in friends" :key="friend.id">{{ friend.name }}</li>
        </ul>
    </div>
  </template>
  
  <script>
  export default {
    name: 'FriendListComponent',
    props: {
      friends: {
        type: Array,
        required: true
      }
    }
  }
  </script>
  
  <style scoped>
  .friend-list {
    position: absolute;
    right: 20px;
    top: 50%;
    transform: translateY(-50%);
    color: #fbf9f9;
  }
  </style>
  