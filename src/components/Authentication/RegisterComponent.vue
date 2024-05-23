<template>
  <div class="register">
    <div class="content">
      <div v-if="showErrorMessage" class="error-message">
        {{ errorMessage }}
      </div>
      <h2>Register</h2>
      <form class="form-register" @submit.prevent="register">
        <div class="inputBox">
          <input v-model="username" type="text" required /> <i>Username</i>
        </div>
        <div class="inputBox"><input v-model="email" type="email" required /> <i>Email</i></div>

        <div class="inputBox">
          <input v-model="first_name" type="text" required /> <i>First Name</i>
        </div>
        <div class="inputBox">
          <input v-model="last_name" type="text" required /> <i>Last Name</i>
        </div>
        <div class="inputBox date">
          <input v-model="date_de_naissance" type="date" required /> <i>Date of birth</i>
        </div>

        <div class="inputBox">
          <input v-model="password" type="password" required /> <i>Password</i>
        </div>
        <div class="links">
          <p>You have an account ?</p>
          <a @click="goToLogin" href="#">Login</a>
        </div>
        <div class="inputBox">
          <input type="submit" value="Register" />
        </div>
      </form>
    </div>
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
      errorMessage: ''
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
    goToLogin() {
      this.$router.push('/login');
    }
  }
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

.register {
  position: absolute;
  top: 55%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 400px;
  height: 640px; /* Réduire la hauteur */
  background: #222;
  z-index: 1000;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 40px;
  border-radius: 4px;
  box-shadow: 0 15px 35px rgba(0, 0, 0, 9);
}

.register .content {
  position: relative;
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  gap: 20px;
}

.register .content h2 {
  font-size: 2em;
  color: #02bd9c;
  text-transform: uppercase;
}

.register .content .form-register {
  width: 100%;
  display: flex;
  flex-direction: column;
  gap: 25px;
}

.register .content .form-register .inputBox {
  position: relative;
  width: 100%;
}

.register .content .form-register .inputBox input {
  position: relative;
  width: 100%;
  background: #333;
  border: none;
  outline: none;
  padding: 25px 10px 7.5px;
  border-radius: 4px;
  color: #fff;
  font-weight: 500;
  font-size: 1em;
}

.register .content .form-register .inputBox i {
  position: absolute;
  left: 0;
  padding: 15px 10px;
  font-style: normal;
  color: #aaa;
  transition: 0.5s;
  pointer-events: none;
}

.register .content .form-register .inputBox.date i {
  transform: translateY(-7.5px);
  font-size: 0.8em;
}

.register .content .form-register .inputBox input:focus ~ i,
.register .content .form-register .inputBox input:valid ~ i {
  transform: translateY(-7.5px);
  font-size: 0.8em;
  color: #fff;
}

.register .content .form-register .links {
  position: relative;
  width: 100%;
  display: flex;
  justify-content: space-between;
}

.register .content .form-register .links p {
  color: #fff;
}

.register .content .form-register .links a {
  color: #02bd9c;
  font-weight: 600;
  text-decoration: none;
}

.register .content .form-register .inputBox input[type='submit'] {
  padding: 10px;
  background: #02bd9c;
  color: #000;
  font-weight: 600;
  font-size: 1.35em;
  letter-spacing: 0.05em;
  cursor: pointer;
}

input[type='submit']:active {
  opacity: 0.6;
}

@media (max-width: 900px) {
  span {
    width: calc(10vw - 2px);
    height: calc(10vw - 2px);
  }
}

@media (max-width: 600px) {
  span {
    width: calc(20vw - 2px);
    height: calc(20vw - 2px);
  }
}
</style>
