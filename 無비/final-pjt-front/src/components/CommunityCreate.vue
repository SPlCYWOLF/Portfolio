<template>
  <div class="wow">
    <form action="#">
      <div class="card container" style="width: 18rem;">
        <div class="card-body">
          <h5 class="card-title"><label for="title">[Title]</label></h5>
          <h5><input type="text" id="title" name="title" v-model.trim="params.title"></h5>
          <hr>
          <h5 class="card-subtitle mb-2">[Content]</h5>
          <h5><input type="floatingTextarea" id="content" name="content" v-model.trim="params.content"></h5>
          <hr>
          <h6>[Rating]</h6>
          <h6><input type="number" id="rating" name="rating" v-model.trim="params.rating"></h6>
          <hr>
          <button type="button" class="btn btn-outline-success m-2" @click="saveReview">OK</button>
          <button type="button" class="btn btn-outline-success m-2" @click="backToHome">Cancel</button>
        </div>
      </div>
    </form> 
  </div>
</template>

<script>

import axios from 'axios'

export default {
  name: 'CommunityCreate',
  props: {
    infoForCreateReview: Object,
  },
  
  data: function () {
    return {
        params: {
          title: '',
          rating: '',
          content: '',
        }
    }
  },
  methods: {

    backToHome: function () {
      this.$emit('back-to-home')
    },

    setToken: function () {
        const token = localStorage.getItem('jwt')
        const config = {
          Authorization: `JWT ${token}`
        }
        return config
      },

    saveReview: function () {
      const SERVER_URL = process.env.VUE_APP_SERVER_URL
      const movie_pk = this.infoForCreateReview.movie_id

      axios({
          method: 'post',
          url: `${SERVER_URL}/community/movies/${movie_pk}/reviews/`,
          headers: this.setToken(),
          data: {
            title: this.params.title,
            content: this.params.content,
            rating: this.params.rating,
          },
        })
        .then((res) => {
          console.log(res.data)
          this.title = ''
          this.content = ''
          this.rating = ''
          this.$emit('close-review-create')
        })
        .catch((err) => {
          console.log(err)
        })
      
    },
  },
}
</script>

<style scoped>
.wow {
  width: 100%;
  height: 80vh;
  
  display:grid;
  place-items:center;
}
</style>