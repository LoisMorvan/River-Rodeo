<template>
  <div class="login">
    <div class="content">
      <div v-if="showSuccessMessage && !loginAttempted" class="success-message">
        You have registered successfully! Please log in.
      </div>
      <div v-if="showErrorMessage" class="error-message">
        {{ errorMessage }}
      </div>
      <h2>Login</h2>
      <form class="form-login" @submit.prevent="login">
        <div class="inputBox">
          <input v-model="username" type="text" required /> <i>Username</i>
        </div>
        <div class="inputBox">
          <input v-model="password" type="password" required /> <i>Password</i>
        </div>
        <div class="links">
          <a href="#">Forgot Password</a>
          <a @click="goToRegister" href="#">Register</a>
        </div>
        <div class="inputBox">
          <input type="submit" value="Login">
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
    goToRegister() {
      this.$router.push('/register');
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

.login {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 400px;
  background: #222;
  z-index: 1000;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 40px;
  border-radius: 4px;
  box-shadow: 0 15px 35px rgba(0, 0, 0, 9);
}

.login .content {
  position: relative;
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  gap: 40px;
}

.login .content h2 {
  font-size: 2em;
  color: #02BD9C;
  text-transform: uppercase;
}

.login .content .form-login {
  width: 100%;
  display: flex;
  flex-direction: column;
  gap: 25px;
}

.login .content .form-login .inputBox {
  position: relative;
  width: 100%;
}

.login .content .form-login .inputBox input {
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

.login .content .form-login .inputBox i {
  position: absolute;
  left: 0;
  padding: 15px 10px;
  font-style: normal;
  color: #aaa;
  transition: 0.5s;
  pointer-events: none;
}

.login .content .form-login .inputBox input:focus~i,
.login .content .form-login .inputBox input:valid~i {
  transform: translateY(-7.5px);
  font-size: 0.8em;
  color: #fff;
}

.login .content .form-login .links {
  position: relative;
  width: 100%;
  display: flex;
  justify-content: space-between;
}

.login .content .form-login .links a {
  color: #fff;
  text-decoration: none;
}

.login .content .form-login .links a:nth-child(2) {
  color: #02BD9C;
  font-weight: 600;
}

.login .content .form-login .inputBox input[type="submit"] {
  padding: 10px;
  background: #02BD9C;
  color: #000;
  font-weight: 600;
  font-size: 1.35em;
  letter-spacing: 0.05em;
  cursor: pointer;
}

input[type="submit"]:active {
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