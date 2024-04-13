<template>
  <div>
    <div v-if="showSuccessMessage && !loginAttempted" class="success-message">
      You have registered successfully! Please log in.
    </div>
    <div v-if="showErrorMessage" class="error-message">
      {{ errorMessage }}
    </div>
    <h2>Login</h2>
    <form @submit.prevent="login">
      <label>
        Username:
        <input v-model="username" type="text" required />
      </label>
      <br />
      <label>
        Password:
        <input v-model="password" type="password" required />
      </label>
      <br />
      <button type="submit">Login</button>
    </form>
  </div>
</template>
<script>
import api from '../../axiosInstances';

export default {
  data() {
    return {
      username: '',
      password: '',
      showSuccessMessage: false,
      showErrorMessage: false,
      errorMessage: '',
      loginAttempted: false,
    };
  },
  created() {
    const registered = this.$route.query.registered;
    if (registered === 'true') {
      this.showSuccessMessage = true;
    }
  },
  methods: {
    async login() {
      this.loginAttempted = true;
      try {
        const response = await api.post('/auth/login/', {
          username: this.username,
          password: this.password,
        });
        // Save the token in the local storage
        localStorage.setItem('auth_token', response.data.token);
        // Redirect the user to the home page
        this.$router.push('/');
      } catch (error) {
        console.error(error);
        this.showErrorMessage = true;
        this.errorMessage = 'Invalid username or password.';
      }
    },
  },
};
</script>

<style scoped>
.success-message {
  background-color: green;
  color: white;
  padding: 10px;
  text-align: center;
  margin-bottom: 10px;
}

.error-message {
  background-color: red;
  color: white;
  padding: 10px;
  text-align: center;
  margin-bottom: 10px;
}
</style>