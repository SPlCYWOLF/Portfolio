<template>
  <div>
    
    <div> <!-- 코멘트 작성 란 -->
      <label for="content" class="fs-2">Write a comment</label>
      <br>
      <input type="floatingTextarea" id="content" name="content" v-model.trim="commentContent" @keypress.enter="saveComment">
      <button type="button" class="btn btn-outline-dark m-2" @click="saveComment">OK</button>

      <hr>

      <h2 class="mb-4">[Comments List]</h2> <!-- 코멘트 표시 란-->
      <div id="comments" v-for="(comment, idx) in comments.slice().reverse()" :key="idx">
        <div v-if="comment.review === reviewPk"> <!-- 해당 리뷰에 속한 코멘트만 표시 -->
          <b-row cols="3"><!-- 영화 포스터 -->
            <b-col></b-col>
            <b-col>
              <div class="mt-4">
                <span>Written By : {{ comment.username }}</span>
                <button v-if="comment.username === currentUser" type="button" class="btn btn-outline-danger m-2" @click="deleteComment(comment)">X</button> <!-- 댓글 삭제 버튼 --><!--본인일때만 수정 가능-->
                <b-card img-src="https://placekitten.com/300/300" img-alt="Card image" img-left class="my-2">
                  <b-card-text>{{ comment.content }}</b-card-text>
                </b-card>  
              </div>
            </b-col>
          </b-row>  
        </div>
      </div>
    </div>

  </div>
</template>

<script>

import axios from 'axios'
import jwt_decode from "jwt-decode"

export default {
  name: 'CommunityDetailComment',
  props: {
    isAuthor: Boolean,
    reviewPk: Number,
  },
  data: function () {
    return {
      currentUser: '',
      commentContent: '',
      comments: [],
    }
  },

  methods: {

    getComments: function () {

      const token = localStorage.getItem('jwt')
      const decoded = jwt_decode(token)
      this.currentUser = decoded.username

      const SERVER_URL = process.env.VUE_APP_SERVER_URL
      
      this.comments = []    // 중복 내용 방지위해 매번 불러올때마다 comments 초기화
      
      axios({
          method: 'get',
          url: `${SERVER_URL}/community/reviews/${this.reviewPk}/comments/`,
          headers: this.setToken(),
        })
        .then((res) => {
          // comments 리스트에 새로운 댓글 있으면 append
          for (var temp of res.data) {
            this.comments.push(temp)
          }
        })
        .catch((err) => {
          console.log(err)
        })
    },
    saveComment: function () {
      const SERVER_URL = process.env.VUE_APP_SERVER_URL
      const token = localStorage.getItem('jwt')
      const decoded = jwt_decode(token)

      axios({                   // 1. 입력된 댓글 DB에 저장
          method: 'post',
          url: `${SERVER_URL}/community/reviews/${this.reviewPk}/comments/`,
          headers: this.setToken(),
          data: {
            review: this.reviewPk,
            user: decoded.id,
            content: this.commentContent,
          },
        })
        .then((res) => {        // 2. DB에서 댓글들 불러옴
          console.log(res)
          this.getComments()
        })
        .catch((err) => {
          console.log(err)
        })
      this.commentContent = ''  
    },
    deleteComment: function (comment) {
      
      const SERVER_URL = process.env.VUE_APP_SERVER_URL

      axios({
          method: 'delete',
          url: `${SERVER_URL}/community/reviews/${this.reviewPk}/comments/${comment.id}/`,
          headers: this.setToken(),
        })
        .then((res) => {
          console.log(res)
          this.getComments()
        })
        .catch((err) => {
          console.log(err)
        })
    },

    setToken: function () {     // 유저의 토큰 가져옴
        const token = localStorage.getItem('jwt')
        const config = {
          Authorization: `JWT ${token}`
        }
        return config
      },
  },
  created: function () {    // 컴포넌트 생성 시 리뷰 정보들 가져오기
    this.getComments()
  }

}
</script>

<style>

</style>