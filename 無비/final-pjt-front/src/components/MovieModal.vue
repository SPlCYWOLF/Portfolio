<template>
  <div class="wow mt-2">

    <b-container class="bv-example-row mb-3">
      <b-row cols="2">
          <b-card no-body class="overflow-hidden" style="max-width: 540px;">
            <b-row no-gutters>
                <b-card-img :src="`https://image.tmdb.org/t/p/w500${movieInfo.poster_path}`" alt="movie image" class="rounded-0"></b-card-img>
            </b-row>
          </b-card>
          
          <div class="rightequal">
            <b-card title="" header-tag="header" footer-tag="footer">
              <template #header>
                <h6 class="mb-0">{{ movieInfo.original_title }}</h6>
              </template>
              <b-card-text>개봉일 : {{ movieInfo.release_date }}</b-card-text>
              <hr>
              <b-card-text>평점 : {{ movieInfo.vote_average }}</b-card-text>
              <hr>
              <b-card-text v-if="movieInfo.adult" class="text-danger">청소년관람불가</b-card-text>
              <b-card-text v-else>전체관람가능</b-card-text>
              <hr>
              <b-card-text>{{ movieInfo.overview }}</b-card-text>
              <hr>
              <b-button href="#" @click="createReview" class="m-2" variant="outline-success">Create Review</b-button>
              <b-button href="#" @click="$emit('close')" class="m-2" variant="outline-success">close</b-button>
              <template #footer>
                <em>상영시간 : {{ movieInfo.runtime }}분</em>
              </template>
            </b-card>
          </div>
      </b-row>
    </b-container>

  </div>

</template>

<script>


export default {
  name: 'MovieModal',
  props: {
    movieInfo: Object,
  },
  methods: {
    createReview: function () {
      this.$emit('close')
      const infoForReview = this.movieInfo
      this.$emit('create-review', infoForReview)
    }
  }

}
</script>

<style scoped>
.rightequal {
  display: flex;
  flex-wrap: nowrap;
  flex-direction: column;
  justify-content: space-evenly;
}

.wow {
  width: 100%;
  height: 80vh;
  
  display:grid;
  place-items:center;
}
</style>