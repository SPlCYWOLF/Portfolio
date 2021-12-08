<template>
  <div class="wow" v-if="!detailOn">
    <div class="container">
      <clean-movie-list v-for="(movie, idx) in randomlyPickedMovies" :key="idx" :movie="movie"></clean-movie-list>
    </div>
  </div>
</template>
  
<script>
import CleanMovieList from '@/components/CleanMovieList'
import _ from "lodash"

import axios from 'axios'
import jwt_decode from "jwt-decode"

export default {
  name: 'Clean',
  components: {
    CleanMovieList,
  },
  data: function () {
    return {
      currentUserId: '',
      currentUserName: '',
      preference: '',
      userInfo: [],
      userMovies: [],
      randomlyPickedMovies: [],
      detailOn: false,
    }
  },
  methods: {
    
    randomPick: function () {
      this.randomlyPickedMovies = _.sampleSize(this.userMovies, 3)
    },
    
    // 먼저 영화 리스트 다 받아오고,
    getPreference: function () {
      const SERVER_URL = process.env.VUE_APP_SERVER_URL

      axios({
        method: 'get',
        url: `${SERVER_URL}/movies/`,
        headers: this.setToken()
        // params,
      })
      .then((res) => {
        let movies = res.data
        this.userMovies = movies.filter(movie => {
          // 범죄, 호러, 미스터리, 스릴러 장르 삽입
          if (movie.genres.includes(this.preference)) {
            return true
          }
        })
        this.randomPick()
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
  created: function () {
    // 유저 정보 가져오고
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
        this.preference = res.data.preference
        this.getPreference()
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

<style scoped>
.wow {
  width: 100%;
  height: 80vh;
  
  display:grid;
  place-items:center;
}

.container {
  display:flex;
  justify-content:center;
  align-items:center;
  gap:40px;

}

</style>