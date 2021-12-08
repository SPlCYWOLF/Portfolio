<template>
  <div>
    <div v-if="detailOn">
      <div class="mt-5">

        <b-container class="bv-example-row mb-5">
          <b-row cols="2">
              <b-card no-body class="overflow-hidden" style="width: auto;">
                <b-row no-gutters>
                  <b-card-img :src="`https://image.tmdb.org/t/p/w500${movieInfo.poster_path}`" alt="movie image" class="rounded-0"></b-card-img>
                </b-row>
              </b-card>

              <b-card title="" header-tag="header" footer-tag="footer" style="width: auto;">
                <template #header>
                  <h6 class="mb-0">{{ movieInfo.original_title }}</h6>
                </template>
                <b-card-text>개봉일 : {{ movieInfo.release_date }}</b-card-text>
                <hr>
                <b-card-text>평점 : {{ movieInfo.vote_average }}</b-card-text>
                <hr>
                <b-card-text v-if="movieInfo.adult">청소년관람불가</b-card-text>
                <b-card-text v-else>전체관람가능</b-card-text>
                <hr>
                <b-card-text>{{ movieInfo.overview }}</b-card-text>
                <hr>
                <!-- <b-button href="#" @click="createReview" class="m-2" variant="outline-success">Create Review</b-button> -->
                <b-button href="#" @click="detailOn=false" class="m-2" variant="outline-success">close</b-button>
                <template #footer>
                  <em>상영시간 : {{ movieInfo.runtime }}분</em>
                </template>
              </b-card>
          </b-row>
        </b-container>

      </div>
    </div>

    <div v-else class="clean-img">
      <img @click="toDetail" :src="`https://image.tmdb.org/t/p/w300${movie.poster_path}`" alt="movie image">
    </div>

  </div>

</template>

<script>

import axios from 'axios'

export default {
  name: 'CleanMovieList',
  props: {
    movie: Object,
  },
  data: function () {
    return {
      movieInfo: [],
      detailOn: false,
    }
  },
  methods: {

    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },

    toDetail: function () {
      const SERVER_URL = process.env.VUE_APP_SERVER_URL

      axios({
        method: 'get',
        url: `${SERVER_URL}/movies/movies/${this.movie.id}`,
        headers: this.setToken()
        // params,
      })
      .then((res) => {
        this.detailOn = true
        this.movieInfo = res.data

      })
      .catch((err) => {
        console.log(err)
      })
    },
  },
}
</script>

<style>
.clean-img {
  width: 100%;
  height: 100%;
  object-fit:cover;
  
  -webkit-box-reflect:below 2px linear-gradient(transparent, transparent, #0004);
  
  transform-origin:center;
  transform:perspective(800px) rotateY(25deg);
  transition:0.5s;
}

.container .clean-img:hover {
  transform:perspective(800px)       
  rotateY(0deg);
  opacity:1;
}

</style>