<template>
  <div class="account-form">
    <div class="form-group">
      <label for="email">Email:</label>
      <input
        type="email"
        id="email"
        v-model="email"
        :disabled="!isEditing"
        placeholder="Enter your email"
      />
    </div>
    <div class="form-group">
      <label for="username">Username:</label>
      <input
        type="text"
        id="username"
        v-model="username"
        :disabled="!isEditing"
        placeholder="Enter your username"
      />
    </div>
    <div class="form-group">
      <label for="password">Password:</label>
      <input
        type="password"
        id="password"
        v-model="password"
        :placeholder="isEditing ? 'Enter your new password' : '********'"
        :disabled="!isEditing"
      />
    </div>
    <div class="button-group">
      <button @click="toggleEdit">{{ isEditing ? 'Save' : 'Edit' }}</button>
      <button v-if="isEditing" @click="cancelEdit">Cancel</button>
      <button @click="deleteAccount">Delete</button>
    </div>
  </div>
</template>

<script>
import api from '@/axiosInstances';

export default {
  data() {
    return {
      email: '',
      username: '',
      password: '********',
      isEditing: false,
      originalEmail: '',
      originalUsername: '',
    };
  },

  mounted() {
    this.fetchUser();
  },

  methods: {
    toggleEdit() {
      if (this.isEditing) {
        this.saveAccount();
      } else {
        this.isEditing = true;
        this.password = '';
      }
    },

    cancelEdit() {
      this.isEditing = false;
      this.email = this.originalEmail;
      this.username = this.originalUsername;
      this.password = '********';
    },

    saveAccount() {
      const data = {
        email: this.email,
        username: this.username,
      };

      if (this.password) {
        data.password = this.password;
      }

      api
        .put('/auth/user/', data)
        .then((response) => {
          this.isEditing = false;
          this.password = '********';
          this.fetchUser();
        })
        .catch((error) => {
          console.error('Error updating account:', error);
        });
    },

    deleteAccount() {
      console.log('Delete account');
      // Here you would add the API call to delete the account
    },

    fetchUser() {
      api.get('/auth/user/').then((response) => {
        this.email = response.data.email;
        this.username = response.data.username;
        this.originalEmail = response.data.email;
        this.originalUsername = response.data.username;
      });
    },
  },
};
</script>

<style scoped>
.account-form {
  max-width: 400px;
  margin: 0 auto;
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 5px;
  background-color: #f9f9f9;
}

.form-group {
  margin-bottom: 15px;
}

.form-group label {
  display: block;
  margin-bottom: 5px;
}

.form-group input {
  width: 100%;
  padding: 8px;
  box-sizing: border-box;
}

.button-group {
  display: flex;
  justify-content: space-between;
}

.button-group button {
  padding: 10px 20px;
  border: none;
  background-color: #007bff;
  color: white;
  cursor: pointer;
}

.button-group button:last-child {
  background-color: #dc3545;
}
</style>
