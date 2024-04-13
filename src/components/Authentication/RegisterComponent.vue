<template>
  <div>
    <div v-if="showErrorMessage" class="error-message">
      {{ errorMessage }}
    </div>
    <h2>Register</h2>
    <form @submit.prevent="register">
      <label>
        Username:
        <input v-model="username" type="text" required />
      </label>
      <br />
      <label>
        Email:
        <input v-model="email" type="email" required />
      </label>
      <br />
      <label>
        First Name:
        <input v-model="first_name" type="text" required />
      </label>
      <br />
      <label>
        Last Name:
        <input v-model="last_name" type="text" required />
      </label>
      <br />
      <label>
        Date de Naissance:
        <input v-model="date_de_naissance" type="date" required />
      </label>
      <br />
      <label>
        Password:
        <input v-model="password" type="password" required />
      </label>
      <br />
      <button type="submit">Register</button>
    </form>
  </div>
</template>

<script>
import api from '../../axiosInstances';

export default {
  data() {
    return {
      username: '',
      email: '',
      first_name: '',
      last_name: '',
      date_de_naissance: '',
      password: '',
      showErrorMessage: false,
      errorMessage: '',
    };
  },
  methods: {
    async register() {
      let isEmailUnique = await this.checkUnique('email', this.email);
      let isUsernameUnique = await this.checkUnique('username', this.username);

      if (!isEmailUnique) {
        // Display an error message for email
        this.showErrorMessage = true;
        this.errorMessage = 'This email is already in use.';
        return;
      }

      if (!isUsernameUnique) {
        // Display an error message for username
        this.showErrorMessage = true;
        this.errorMessage = 'This username is already in use.';
        return;
      }

      try {
        const response = await api.post('/auth/register/', {
          username: this.username,
          email: this.email,
          first_name: this.first_name,
          last_name: this.last_name,
          date_de_naissance: this.date_de_naissance,
          password: this.password
        });
        // Handle the successful registration, redirect the user to the login page and show a success message
        console.log(response.data);
        this.$router.push('/login?registered=true');
      } catch (error) {
        console.error(error);
      }
    },
    async checkUnique(field, value) {
      try {
        const response = await api.get(`/auth/check-unique/${field}/${value}/`);
        return response.data.is_unique;
      } catch (error) {
        console.error(error);
        return false;
      }
    },
  },
};
</script>

<style scoped>
.error-message {
  background-color: red;
  color: white;
  padding: 10px;
  text-align: center;
  margin-bottom: 10px;
}
</style>