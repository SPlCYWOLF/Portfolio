<template>
  <div>
    <div>
      <b-row cols="3">
        <b-col></b-col>
        <b-col>
          <b-card no-body class="mb-3">
            <b-card-header header-tag="nav">
              <b-nav card-header tabs>
                <b-nav-item active>Profile</b-nav-item>
                <b-nav-item>Like</b-nav-item>
                <b-nav-item>Dislike</b-nav-item>
              </b-nav>
            </b-card-header>

            <b-card-body class="text-center">
              <b-card-title>Welcome!! Our {{ this.userInfo.id }}번째 Guest!!</b-card-title>

              <b-card-text>ID : {{ this.userInfo.username }}</b-card-text>
              <b-card-text>AGE : {{ this.userInfo.age }} years old</b-card-text>
              <b-card-text>EMAIL : {{ this.userInfo.email }}</b-card-text>
              <b-card-text>NAME : {{ this.userInfo.first_name }} {{ this.userInfo.last_name }}</b-card-text>

              <b-card-text v-if="this.userInfo.preference===28">FAVORITE GENRE : Action</b-card-text>
              <b-card-text v-else-if="this.userInfo.preference===12">FAVORITE GENRE : Adventure</b-card-text>
              <b-card-text v-else-if="this.userInfo.preference===16">FAVORITE GENRE : Animation</b-card-text>
              <b-card-text v-else-if="this.userInfo.preference===35">FAVORITE GENRE : Comedy</b-card-text>
              <b-card-text v-else-if="this.userInfo.preference===80">FAVORITE GENRE : Crime</b-card-text>
              <b-card-text v-else-if="this.userInfo.preference===99">FAVORITE GENRE : Documentary</b-card-text>
              <b-card-text v-else-if="this.userInfo.preference===18">FAVORITE GENRE : Drama</b-card-text>
              <b-card-text v-else-if="this.userInfo.preference===10751">FAVORITE GENRE : Family</b-card-text>
              <b-card-text v-else-if="this.userInfo.preference===14">FAVORITE GENRE : Fantasy</b-card-text>
              <b-card-text v-else-if="this.userInfo.preference===36">FAVORITE GENRE : History</b-card-text>
              <b-card-text v-else-if="this.userInfo.preference===27">FAVORITE GENRE : Opel</b-card-text>
              <b-card-text v-else-if="this.userInfo.preference===10402">FAVORITE GENRE : Music</b-card-text>
              <b-card-text v-else-if="this.userInfo.preference===9648">FAVORITE GENRE : Mystery</b-card-text>
              <b-card-text v-else-if="this.userInfo.preference===10749">FAVORITE GENRE : Romance</b-card-text>
              <b-card-text v-else-if="this.userInfo.preference===878">FAVORITE GENRE : Science Fiction</b-card-text>
              <b-card-text v-else-if="this.userInfo.preference===53">FAVORITE GENRE : Thriller</b-card-text>
              <b-card-text v-else-if="this.userInfo.preference===10752">FAVORITE GENRE : War</b-card-text>
              <b-card-text v-else-if="this.userInfo.preference===10770">FAVORITE GENRE : TV</b-card-text>
              <b-card-text v-else>FAVORITE GENRE : Western</b-card-text>

              <b-button class="m-1" variant="outline-primary">EDIT</b-button>
              <b-button class="m-1" variant="outline-danger">WITHDRAWL</b-button>
            </b-card-body>
          </b-card>
        </b-col>
      </b-row>
    </div>
    
    <hr>

    <b-row cols="3">
      <b-col></b-col>
        <b-col>
          <h2>[{{ this.userInfo.username }}'s Review List]</h2>
          <div v-for="(review, idx) in userReviews" :key="idx">
            <b-card no-body class="overflow-hidden mb-3">
              <b-row>
                <b-col md="6">
                  <!-- 11/24 수정-->
                  <b-card-img :src="`https://image.tmdb.org/t/p/w500${posters[idx]}`" alt="Image" class="rounded-0"></b-card-img>
                </b-col>
                <b-col md="6">
                  <b-card-body title="[Review]">
                    <b-card-text class="mt-1">[No.{{ review.id }}] [Title] : {{ review.title }}</b-card-text>
                    <b-card-text>[Content] : {{ review.content }}</b-card-text>
                    <b-card-text>Rating : {{ review.rating }} points</b-card-text>
                  </b-card-body>
                </b-col>
              </b-row>
            </b-card>
          </div>
        </b-col>     
    </b-row>
  </div>
</template>

<script>

import axios from 'axios'
import jwt_decode from "jwt-decode"

export default {
  name: 'Profile',
  data: function () {
    return {
      userInfo: [],
      userReviews: [],
      currentUserName: '',
      currentUserId: '',
      posters: [],  // <!-- 11/24 수정-->
    }
  },
  methods: {
    getMovie: function (movie_pk) {     //<!-- 11/24 수정-->
      const SERVER_URL = process.env.VUE_APP_SERVER_URL

      axios({      
        method: 'get',
        url: `${SERVER_URL}/movies/movies/${movie_pk}/`,
        headers: this.setToken()
      })
      .then((res) => {
        this.posters.push(res.data.poster_path)
      })
      .catch((err) => {
        console.log(err)
      })
    },

    getUserReviews: function () {

      const SERVER_URL = process.env.VUE_APP_SERVER_URL

      axios({      
      method: 'get',
      url: `${SERVER_URL}/community/${this.currentUserId}/reviews/`,
      headers: this.setToken()
      })
      .then((res) => {
        this.userReviews = res.data
        for (var review of this.userReviews) {    //<!-- 11/24 수정-->
          this.getMovie(review.movie)
        }
      })
      .catch((err) => {
        console.log(err)
      })
    },

    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },

  },
  created: function () {    // 유저 프로필 가져오기

    const SERVER_URL = process.env.VUE_APP_SERVER_URL
    const token = localStorage.getItem('jwt')
    const decoded = jwt_decode(token)
    this.currentUserName = decoded.username
    this.currentUserId = decoded.user_id

    axios({      
      method: 'get',
      url: `${SERVER_URL}/accounts/${this.currentUserName}/`,
      headers: this.setToken()
    })
    .then((res) => {
      if (res.data.id === this.currentUserId) {   // 현재 유저가 맞는지 1차 확인
        this.userInfo = res.data
        this.getUserReviews()
      } else {
        console.log('수작 부리지 말거라..')
      }
    })
    .catch((err) => {
      console.log(err)
    })
  }
}
</script>

<style>

</style>