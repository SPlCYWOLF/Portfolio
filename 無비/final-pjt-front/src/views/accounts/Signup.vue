<template>
  <div class="wow">
    <div class="container">
      <p class=h1><b-icon-person-plus animation="fade"></b-icon-person-plus></p>
      <div>
        <label for="username"></label>
        <input class="mb-2 bg-danger border-danger text-white" placeholder="ID" type="text" id="username" v-model.trim="credentials.username">
      </div>
      <div>
        <label for="password"></label>
        <input class="mb-2 bg-primary border-primary text-white" placeholder="PASSWORD" type="password" id="password" v-model.trim="credentials.password">
      </div>
      <div>
        <label for="passwordConfirmation"></label>
        <input
          class="mb-2 bg-primary border-primary text-white"
          type="password"
          placeholder="PASSWORD CONFIRMATION" 
          id="passwordConfirmation" 
          v-model.trim="credentials.passwordConfirmation"
          @keypress.enter="signup(credentials)"
        >
      </div>
      <!-- 11/21 수정 내용 시작 -->
      <div>
        <label for="first_name"></label>
        <input class="mb-2 bg-success border-success text-white" placeholder="FIRST NAME" type="text" id="first_name" v-model.trim="credentials.first_name">
      </div>

      <div>
        <label for="last_name"></label>
        <input class="mb-2 bg-success border-success text-white" placeholder="LAST NAME" type="text" id="last_name" v-model.trim="credentials.last_name">
      </div>

      <div>
        <label for="email"></label>
        <input class="mb-2 bg-warning border-warning text-white" placeholder="EMAIL" type="text" id="email" v-model.trim="credentials.email">
      </div>

      <div>
        <label for="age"></label>
        <input class="mb-2 bg-secondary border-secondary text-white" placeholder="AGE" type="text" id="age" v-model.trim="credentials.age">
      </div>

      <div>
        <form action="/action_page.php">
          <label for="genres">[Genre]</label>
          <select v-model="credentials.preference" name="genres" id="genres">
            <option value="28">Action</option>
            <option value="12">Adventure</option>
            <option value="16">Animation</option>
            <option value="35">Comedy</option>
            <option value="80">Crime</option>
            <option value="99">Documentary</option>
            <option value="18">Drama</option>
            <option value="10751">Family</option>
            <option value="14">Fantasy</option>
            <option value="36">History</option>
            <option value="27">Opel</option>
            <option value="10402">Music</option>
            <option value="9648">Mystery</option>
            <option value="10749">Romance</option>
            <option value="878">Science Fiction</option>
            <option value="53">Thriller</option>
            <option value="10770">TV</option>   
            <option value="10752">War</option>
            <option value="37">Western</option>   
          </select>
        </form>
      </div>
      <!-- 11/21 수정 내용 끝 -->
        <b-button pill @click="signup(credentials)" variant="outline-success" class="m-2 btn-sm btn-block">OK</b-button>
        <b-button pill @click="$emit('to-login')" variant="outline-success" class="m-2 btn-sm btn-block">Cancel</b-button>
    </div>
  </div>  
</template>

<script>
import axios from 'axios'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'Singup',
  data: function () {
    return {
      credentials: {
        username: '',
        password: '',
        passwordConfirmation: '',
        first_name: '',
        last_name: '',
        email: '',
        age: '',
        preference: '',
      },
    }
  },
  methods: {
    signup: function (credentials) {
      axios({
        url: `${SERVER_URL}/accounts/signup/`,
        method: 'post',
        data: credentials,
      })
      .then(() => {
        // 로그인 화면으로 이동
        this.$router.push({ name: 'Login' })
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