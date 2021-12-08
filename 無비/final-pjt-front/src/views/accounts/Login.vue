<template>
  <div class="wow">
    <div class="container">
      <p class=h1><b-icon-person-check animation="fade"></b-icon-person-check></p>
      <div>
        <label for="username"></label>
        <input class="mb-2 bg-danger border-danger text-white" placeholder="ID" type="text" id="username" v-model.trim="credentials.username">
      </div>
      <div>
        <label for="password"></label>
        <input
          class="mb-2 bg-primary border-primary text-white"
          type="password" 
          placeholder="PASSWORD"
          id="password" 
          v-model.trim="credentials.password"
          @keypress.enter="login(credentials)"
        >
      </div>
      <b-button pill @click="login(credentials)" variant="outline-success" class="m-2 btn-sm btn-block">Sign in</b-button>
      <b-button pill @click="$emit('to-signup')" variant="outline-success" class="m-2 btn-sm btn-block">Sign up</b-button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'Login',
  data: function () {
    return {
      credentials: {
        username: '',
        password: '',
      },
    }
  },
  methods: {
    login: function (credentials) {
      axios({
        url: `${SERVER_URL}/accounts/api-token-auth/`,
        method: 'post',
        data: credentials,
      })
      .then((res) => {
        // Token 저장 (로그인)
        localStorage.setItem('jwt', res.data.token)
        // 로그인 됬다 부모 컴포넌트에게 알림
        this.$emit('user-login')
        // 화면 홈으로 전환해주기
        this.$router.push({ name: 'Home' })
      })
      .catch((err) => {
        console.log(err)
      })
    }
  }
}
</script>

<style scoped>
input::placeholder {
  color: white;
  font-style: italic;
}

.container {
    max-width: 250px;
    /* 넓이 좀 이상함 */
    background-color: white;
    border: thick double black;
}

.wow {
  width: 100%;
  height: 80vh;
  
  display:grid;
  place-items:center;
}
</style>