<template>
  <div>
    <div class="card" style="width: 25rem;">
      <img class="card-img-top" :src="`https://image.tmdb.org/t/p/w400${this.poster_path}`" alt="Card image" style="cursor:pointer" @click="showDetail">
      <div class="card-body">
        <br>
        <h3 class="card-title">{{ review.title }}</h3>
      </div>
    </div>
  </div>
</template>

<script>

import axios from 'axios'

export default {
  name:'CommunityDetail',
  props: {
    review: Object,
  },
  data: function () {
    return {
      poster_path: '',
    }
  },
  methods: {
    showDetail: function () {
      const info = {
        movie_pk: this.review.movie,
        review_pk: this.review.id,
      }
      this.$emit('show-detail', info)
    },
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
  },
  created: function () {      // 영화 포스터 가져오기위한 낫떔질..

    const SERVER_URL = process.env.VUE_APP_SERVER_URL

    axios({      
      method: 'get',
      url: `${SERVER_URL}/movies/movies/${this.review.movie}/`,
      headers: this.setToken()
    })
    .then((res) => {
      this.poster_path = res.data.poster_path
    })
    .catch((err) => {
      console.log(err)
    })
  }

}
</script>

<style scoped>
.card {
  transition: 0.1s ease-out;
  box-shadow: 0px 7px 10px rgba(0, 0, 0, 0.5);
  position: relative;
  display: flex;
}

.card:hover {
  transform: translateY(20px);
}
</style>