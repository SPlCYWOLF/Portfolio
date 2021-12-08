<template>
  <div id="app">
    <div id="nav" v-if="!landed">
      <b-navbar toggleable="lg" type="dark">
        <b-icon variant="white" icon="camera-reels" animation="fade" font-scale="2" class="mx-3"></b-icon>
        <b-navbar-brand href="#"><router-link :to="{ name: 'Home' }" class="font-weight-bold text-white text-decoration-none ms-2">無</router-link></b-navbar-brand>
        <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
        
        <b-collapse id="nav-collapse" is-nav>

          <!-- Right aligned nav items -->
          <!-- 1. 로그인 했을 경우 -->
          <b-navbar-nav class="ml-auto" v-if="isLoggedIn">
            <b-navbar-nav>
              <b-nav-item href="#"><router-link :to="{ name: 'Community' }" class="text-white text-decoration-none">Community</router-link></b-nav-item>
              <b-nav-item href="#"><router-link :to="{ name: 'Clean' }" class="text-white text-decoration-none">Clean</router-link></b-nav-item>
              <b-nav-item href="#"><router-link :to="{ name: 'Profile' }" class="text-white text-decoration-none">Profile</router-link></b-nav-item>
              <b-nav-item href="#"><router-link @click.native="logout" to="#" class="text-danger text-decoration-none">Logout</router-link></b-nav-item>
              <b-nav-item href="#" style="cursor:pointer;" onclick="window.scrollTo(0,0);">Top</b-nav-item>
            </b-navbar-nav>
          </b-navbar-nav>
          
          <!-- 2. 로그인 하지 않았을 경우 -->
          <b-navbar-nav class="ml-auto" v-else>
            <b-navbar-nav>
              <b-nav-item href="#"><router-link :to="{ name: 'Landing' }" class="text-white text-decoration-none" @click="landed=true">Landing</router-link></b-nav-item>
              <b-nav-item href="#"><router-link :to="{ name: 'Login' }" class="text-white text-decoration-none">Login</router-link></b-nav-item>
              <b-nav-item href="#"><router-link :to="{ name: 'Signup' }" class="text-white text-decoration-none">Signup</router-link></b-nav-item>
            </b-navbar-nav>
          </b-navbar-nav>

        </b-collapse>
      </b-navbar>
    </div>

      <br>
      <br>
      <br>
      <br>
      <router-view
        @landed="isLanding"
        @user-login="userLoggedIn" 
        @show-detail="reviewDetailClicked"
        @back-to-review="backToReview"
        @to-home="toHome"
        @delete-review="deleteReview"
        @to-signup="toSignup"
        @to-login="toLogin"
        @create-review="createReview"/>
  </div>
  
</template>

<script>
export default {
  name: 'App',
  data: function () {
    return {
      isLoggedIn: false,
      showReviewDetail: false,
      landed: true,
    }
  },
  methods: {
    isLanding: function () {
      this.landed = false
      this.$router.push({ name: 'Login' })
    },
    userLoggedIn: function () {
      this.isLoggedIn = true
    },
    logout: function () {
      localStorage.removeItem('jwt')
      this.isLoggedIn = false
      this.$router.push({ name: 'Login' })
    },
    reviewDetailClicked: function (info2) {
      this.showReviewDetail = true
      this.$router.push({ name: 'Modal', params: info2})
    },
    backToReview: function () {
      this.showReviewDetail = false
      this.$router.push({ name: 'Community' })
    },
    toHome: function () {
      this.$router.push({ name: 'Home' })
    },
    toSignup: function () {
      this.$router.push({ name: 'Signup' })
    },
    toLogin: function () {
      this.$router.push({ name: 'Login' })
    },
    toLanding: function () {
      this.$router.push({ name: 'Landing' })
    },
    createReview: function (infoForReview) {
      this.showReviewDetail = false
      this.$router.push({ name: 'Community', params: infoForReview })
    },
    deleteReview: function () {
      this.$router.push({ name: 'Community' })
    },

  },

  created: function () {
    const token = localStorage.getItem('jwt')
    if (token) {
      this.isLoggedIn = true
      this.landed = false
      this.toHome()
    } else {
      this.toLanding()
    }
  }
}
</script>

<style>
#app {
  display: block;
  justify-content: center;
  text-align: center;
}

#nav {
  width: 100%;
  position: fixed;
  z-index: 8;
  background-color: #385E72;
}


</style>