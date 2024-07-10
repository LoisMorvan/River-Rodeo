<template>
    <div class="friend-sidebar">
      <div class="tabs">
        <button :class="{ active: activeTab === 'friends' }" @click="activeTab = 'friends'">Amis</button>
        <button :class="{ active: activeTab === 'invitations' }" @click="activeTab = 'invitations'">Invitations</button>
      </div>
      <div class="content">
        <div v-if="activeTab === 'friends'">
          <ul>
            <li v-for="friend in friends" :key="friend.id">{{ friend }}</li>
          </ul>
          <div class="add-friend">
        <input type="text" v-model="newFriendUsername" placeholder="Username">
        <button @click="sendFriendRequest">+</button>
    </div>
        </div>
        <div v-if="activeTab === 'invitations'">
          <ul>
            <li v-for="invitation in invitations" :key="invitation.id"><span>{{ invitation.from_user }}</span>
              <button class="ignore-button" @click="ignoreInvitation(invitation.id)">Ignorer</button>
              <button class="accept-button" @click="acceptInvitation(invitation.id)">Accepter</button>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import api from '@/axiosInstances';
  export default {
    name: 'FriendSideBar',
    props: {
    },
    data() {
      return {
        activeTab: 'friends',
        invitations: [],
        friends: [],
        newFriendUsername: ''
      };
    },
    created() {
    this.fetchInvitations();
    this.fetchFriends();
  },
  methods: {
    fetchFriends() {
      api.get('/auth/friendship/amis/')
        .then(response => {
          this.friends = response.data;
        })
        .catch(error => {
          console.error('Error fetching invitations:', error);
        });
    },
    fetchInvitations() {
      api.get('/auth/friendship/invitations/')
        .then(response => {
          this.invitations = response.data;
        })
        .catch(error => {
          console.error('Error fetching invitations:', error);
        });
    },
    acceptInvitation(invitationId) {
      api.post(`/auth/friendship/invitations/${invitationId}/accept/`)
        .then(response => {
          console.log('Invitation accepted successfully:', response.data);
          // Optionally update UI or fetch invitations again
          this.fetchInvitations();
        })
        .catch(error => {
          console.error('Error accepting invitation:', error);
        });
        this.fetchFriends();
    },
    ignoreInvitation(invitationId) {
      api.post(`/auth/friendship/invitations/${invitationId}/reject/`)
        .then(response => {
          console.log('Invitation rejected successfully:', response.data);
          // Optionally update UI or fetch invitations again
          this.fetchInvitations();
        })
        .catch(error => {
          console.error('Error rejecting invitation:', error);
        });
    },
    sendFriendRequest() {
      const username = this.newFriendUsername.trim();
      if (username) {
        api.post('/auth/friendship/requests/', { username })
          .then(response => {
            console.log('Friend request sent successfully:', response.data);
            this.newFriendUsername = ''; // Clear the input field
            // Optionally update UI or fetch friends/invitations again
            this.fetchFriends();
            this.fetchInvitations();
          })
          .catch(error => {
            console.error('Error sending friend request:', error);
          });
      }
    }
  }
  };
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

  .ignore-button,
.accept-button {
  padding: 5px 10px;
  cursor: pointer;
  transition: background-color 0.3s, border-width 0.3s;
}

.ignore-button {
  background-color: transparent;
  color: white;
  border: none;
}

.ignore-button:hover {
  background-color: #5c5c5c;
}

.accept-button {
  background-color: #007bff;
  color: white;
  border: 2px solid #007bff;
  border-radius: 50%;
}

.accept-button:hover {
  background-color: #0056b3;
  border-width: 4px;
}
.add-friend {
  margin-top: 20px;
  display: flex;
  align-items: center;
}

.add-friend input {
  flex: 1;
  padding: 8px;
  margin-right: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
}

.add-friend button {
  padding: 8px;
  background-color: #007bff;
  color: white;
  border: none;
  cursor: pointer;
  transition: background-color 0.3s;
}

.add-friend button:hover {
  background-color: #0056b3;
}
  </style>
  