<template>
  <div>
    <div v-if="doUpdate"><!-- 리뷰 글 업데이트 컴포넌트 -->
      <div class="wow">
        <form action="/home">
          <div class="card container" style="width: 18rem;">
            <div class="card-body">
              <h5 class="card-title"><label for="title">[Title]</label></h5>
              <h5><input v-model.trim="newTitle" id="title" type="text" :placeholder="detail.title"/></h5>
              <hr>
              <h5 class="card-subtitle mb-2">[Content]</h5>
              <h5><input v-model.trim="newContent" id="content" type="text" :placeholder="detail.content"/></h5>
              <hr>
              <h6>[Rating]</h6>
              <h6><input v-model.trim="newRating" id="rating" type="number" :placeholder="detail.rating"/></h6>
              <hr>
              <button type="button" class="btn btn-outline-success m-2" @click="updateReview">OK</button>
              <button type="button" class="btn btn-outline-success m-2" @click="backToDetail">Cancel</button>
            </div>
          </div>
        </form> 
      </div>
    </div>

    <div v-else><!-- 리뷰 글 내용 컴포넌트 -->
      <b-row cols="3"><!-- 영화 포스터 -->
      <b-col></b-col>
        <b-col>
          <h2>[{{ original_title }}]</h2>
            <b-card no-body class="overflow-hidden mb-3">
              <b-row>
                <b-col md="6">
                  <b-card-img :src="`https://image.tmdb.org/t/p/w500${this.poster_path}`" alt="movie image" class="rounded-0"></b-card-img>
                </b-col>
                 
                <b-col md="6">
                  
                  <b-card-body title="[Review]">
                    <b-card-text>[Title] : {{ detail.title }}</b-card-text>
                    
                    <b-card-text>[Content] : {{ detail.content }}</b-card-text>
                    
                    <b-card-text>Written By : {{ detail.username }}</b-card-text>
                    
                    <b-card-text>Rating : {{ detail.rating }} points</b-card-text>
                    
                    <span v-if="isAuthor">
                      <b-button class="m-1" @click="updateMode" variant="outline-primary">EDIT</b-button>
                      <b-button class="m-1" @click="deleteReview" variant="outline-danger">DELETE</b-button>
                    </span>
                    <span>  
                      <b-button class="m-1" @click="backToReview" variant="outline-success">BACK</b-button>
                    </span>
                  </b-card-body>
                 
                </b-col>
                 
              </b-row>
            </b-card>
        </b-col>     
      </b-row>
      <hr>
      <community-detail-comment :isAuthor="isAuthor" :reviewPk="this.$route.params.review_pk"></community-detail-comment>
    </div>
  </div>

</template>

<script>

import CommunityDetailComment from '@/components/CommunityDetailComment'

import axios from 'axios'
import jwt_decode from "jwt-decode"

export default {
  name: 'Modal',
  components: {
    CommunityDetailComment,
  },
  data: function () {
    return {
      detail: [],
      doUpdate: false,
      newContent: '',
      newTitle: '',
      newRating: '',
      isAuthor: false,
      poster_path: '',
      original_title: '',
    }
  },
  methods: {

    backToDetail: function() {
      this.doUpdate = false
    },
    
    backToReview: function () {
      this.$emit('back-to-review')
    },

    setToken: function () {     // 유저의 토큰 가져옴
        const token = localStorage.getItem('jwt')
        const config = {
          Authorization: `JWT ${token}`
        }
        return config
      },

    updateMode: function () {   // 수정 창 띄우기 위한 상태정보 전환
      this.doUpdate = true
    },

    updateReview: function () {
      const SERVER_URL = process.env.VUE_APP_SERVER_URL
      const movie_pk = this.$route.params.movie_pk
      const review_pk = this.$route.params.review_pk

      axios({
          method: 'put',
          url: `${SERVER_URL}/community/movies/${movie_pk}/reviews/${review_pk}/`,
          headers: this.setToken(),
          data: {
            title: this.newTitle,
            content: this.newContent,
            rating: this.newRating, 
          },
        })
        .then((res) => {
          this.detail = res.data
          this.doUpdate = false
          this.newTitle = ''
          this.newContent = ''
          this.newRating = ''
        })
        .catch((err) => {
          console.log(err)
        })
    },

    deleteReview: function () {
      const SERVER_URL = process.env.VUE_APP_SERVER_URL
      const movie_pk = this.$route.params.movie_pk
      const review_pk = this.$route.params.review_pk

      axios({
          method: 'delete',
          url: `${SERVER_URL}/community/movies/${movie_pk}/reviews/${review_pk}/`,
          headers: this.setToken(),

        })
        .then((res) => {
          console.log(res.data)
          this.newTitle = ''
          this.newContent = ''
          this.newRating = ''
          this.$emit('delete-review')
        })
        .catch((err) => {
          console.log(err)
        })
      
    }
  },

  created: function () {    // 상세보기 페이지 생성 시 자동으로 영화 상세정보 가져옴

    const SERVER_URL = process.env.VUE_APP_SERVER_URL
    const movie_pk = this.$route.params.movie_pk
    const review_pk = this.$route.params.review_pk

    axios({
        method: 'get',
        url: `${SERVER_URL}/community/movies/${movie_pk}/reviews/${review_pk}/`,
        headers: this.setToken()
        // params,
      })
      .then((res) => {
        // console.log(res.data)
        this.detail = res.data

        const token = localStorage.getItem('jwt')
        const decoded = jwt_decode(token)
        if (decoded.username === this.detail.username) {    // 로그인 유저와 작성 유저 이름 동일해야
          this.isAuthor = true                              // 리뷰 글 수정버튼 보여줌
        }
      })
      .catch((err) => {
        console.log(err)
      })

    axios({       // 영화 포스터 가져오기위한 낫떔질..
        method: 'get',
        url: `${SERVER_URL}/movies/movies/${movie_pk}/`,
        headers: this.setToken()
        // params,
      })
      .then((res) => {
        this.poster_path = res.data.poster_path
        this.original_title = res.data.original_title
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

.rightequal {
  display: flex;
  flex-wrap: nowrap;
  flex-direction: column;
  justify-content: space-between;
}
</style>