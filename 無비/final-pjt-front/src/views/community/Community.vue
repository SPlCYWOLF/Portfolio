<template>
  <div>
    <h2 class="text-light">[Community]</h2>
    <br>
    
    <vue-glide v-if="reviews.length"
      class="glide__track m-4"
      data-glide-el="track"
      ref="slider"
      type="carousel"
      :breakpoints="{3000: {perView: 4}, 1100: {perView: 4}, 600: {perView: 4}}"
    >
      <vue-glide-slide
        v-for = "(review, idx) in reviews"
        :key="idx"
      >
        <CommunityDetail
          :review="review"
          @show-detail="showDetail"
        />
        
      </vue-glide-slide>
    </vue-glide>

  </div>
</template>

<script>

import CommunityDetail from '@/components/CommunityDetail'

import axios from 'axios'

export default {
  name: 'Community',
  components: {
    CommunityDetail,
  },

  data: function () {
    return {
      reviews: [],
      movie_pk: '',
      review_pk: '',
      username: '',
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

    getReviews: function () {
      const SERVER_URL = process.env.VUE_APP_SERVER_URL

      axios({
        method: 'get',
        url: `${SERVER_URL}/community/reviews/`,
        headers: this.setToken()
        // params,
      })
      .then((res) => {
        this.reviews = res.data
      })
      .catch((err) => {
        console.log(err)
      })

    },

    showDetail: function (info) {
      this.movie_pk = info.movie_pk
      this.review_pk = info.review_pk
      const info2 = {
        movie_pk: this.movie_pk,
        review_pk: this.review_pk
      }
      this.$emit('show-detail', info2)
    },

    toHome: function () {
      this.$emit('to-home')
    },
  },

  created: function () {
    // 로그인이 됐다면
    if (localStorage.getItem('jwt')) {
      // todo 리뷰 정보 가져오자
      this.getReviews()
    // 로그인이 안됐다면
    } else {
      this.$router.push({ name: 'Login' })
    }
  }
  
}
</script>

<style>

</style>