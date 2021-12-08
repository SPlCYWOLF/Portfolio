<template>
  <div>

    <div v-if="showReviewCreate">   <!-- 리뷰글 생성 컴포넌트 -->
      <community-create 
      :infoForCreateReview="infoForCreateReview" 
      @close-review-create="closeReviewCreate"
      @back-to-home="backToHome"
      ></community-create>
    </div>

    <div v-else>
      <div v-if="showMovieDetail">  <!-- 디테일 페이지 컴포넌트 -->
        <movie-modal
        @close="showMovieDetail = false" 
        @create-review="createReview"  
        :movieInfo="movieInfo"></movie-modal>
      </div>

      <div v-else> <!-- 디테일 페이지 표시 안될때 -->
        <div class="dropdown mb-4"> <!-- 장르 선택 dropdown menu -->
          <div>
            <b-dropdown size="lg" variant="link" toggle-class="text-decoration-none" no-caret>
              <template #button-content><span class="text-white fw-bold ms-1 fs-1">[無 비] ▼</span></template>
                <a @click="toPopular" href="#" class="text-decoration-none"><b-dropdown-item href="#">&#x1F929; [卑 : 낮을 비]</b-dropdown-item></a>
                <a @click="toBright" href="#" class="text-decoration-none"><b-dropdown-item href="#">&#x1F628; [毘 : 밝을 비]</b-dropdown-item></a>
                <a @click="toDocumentary" href="#" class="text-decoration-none"><b-dropdown-item href="#">&#x1F634; [非 : 아닐 비]</b-dropdown-item></a>
                <a @click="toWar" href="#" class="text-decoration-none"><b-dropdown-item href="#">&#x1F607; [斐 : 아름다울 비]</b-dropdown-item></a>
                <a @click="toDark" href="#" class="text-decoration-none"><b-dropdown-item href="#">&#x1F604; [悲 : 슬플 비]</b-dropdown-item></a>
                <a @click="toRomance" href="#" class="text-decoration-none"><b-dropdown-item href="#">&#x1F618; [秘 : 숨길 비]</b-dropdown-item></a>
            </b-dropdown>
          </div>
        </div>
        <div> <!-- 장르별 영화 리스트 출력 컴포넌트 -->
          <movie-popular v-show="popular" @show-movie-detail="movieDetailOn" v-for="(movie, idx) in movies" :key="idx" :movie="movie"></movie-popular>
          <movie-bright v-show="bright" @show-movie-detail="movieDetailOn" v-for="(brightMovie, idx) in brightMovies" :key="'B' + idx" :brightMovie="brightMovie"></movie-bright>
          <movie-documentary v-show="documentary" @show-movie-detail="movieDetailOn" v-for="(documentaryMovie, idx) in documentaryMovies" :key="'Do' + idx" :documentaryMovie="documentaryMovie"></movie-documentary>
          <movie-war v-show="war" @show-movie-detail="movieDetailOn" v-for="(warMovie, idx) in warMovies" :key="'W' + idx" :warMovie="warMovie"></movie-war>
          <movie-dark v-show="dark" @show-movie-detail="movieDetailOn" v-for="(darkMovie, idx) in darkMovies" :key="'Da' + idx" :darkMovie="darkMovie"></movie-dark>
          <movie-romance v-show="romance" @show-movie-detail="movieDetailOn" v-for="(romanceMovie, idx) in romanceMovies" :key="'R' + idx" :romanceMovie="romanceMovie"></movie-romance>
        </div>
      </div>
    </div>
  </div>
</template>

<script>

import axios from 'axios'

import MovieBright from '@/components/MovieBright'
import MovieDark from '@/components/MovieDark'
import MovieDocumentary from '@/components/MovieDocumentary'
import MoviePopular from '@/components/MoviePopular'
import MovieRomance from '@/components/MovieRomance'
import MovieWar from '@/components/MovieWar'
import MovieModal from '@/components/MovieModal'
import CommunityCreate from '@/components/CommunityCreate'

export default {
  name: 'Home',
  components: {
    MovieBright,
    MovieDark,
    MovieDocumentary,
    MoviePopular,
    MovieRomance,
    MovieWar,
    MovieModal,
    CommunityCreate
  },
  data: function () {
    return {
      movies: [],
      brightMovies: [],
      documentaryMovies: [],
      warMovies: [],
      darkMovies: [],
      romanceMovies: [],
      movieInfo: [],
      bright: false,
      dark: false,
      documentary: false,
      popular: true,
      romance: false,
      war: false,
      showMovieDetail: false,
      showReviewCreate: false,
      infoForCreateReview: [],
    }
  },
  
  methods: {
    toBright: function () {
      this.bright = true
      this.documentary = false
      this.war = false
      this.popular = false
      this.dark = false
      this.romance = false
    },
    toDocumentary: function () {
      this.bright = false
      this.documentary = true
      this.war = false
      this.popular = false
      this.dark = false
      this.romance = false
    },
    toWar: function () {
      this.bright = false
      this.documentary = false
      this.war = true
      this.popular = false
      this.dark = false
      this.romance = false
    },
    toPopular: function () {
      this.bright = false
      this.documentary = false
      this.war = false
      this.popular = true
      this.dark = false
      this.romance = false
    },
    toDark: function () {
      this.bright = false
      this.documentary = false
      this.war = false
      this.popular = false
      this.dark = true
      this.romance = false
    },
    toRomance: function () {
      this.bright = false
      this.documentary = false
      this.war = false
      this.popular = false
      this.dark = false
      this.romance = true
    },

    movieDetailOn: function (movieInfo) {
      this.movieInfo = movieInfo
      this.showMovieDetail = true
    },

    createReview: function (infoForReview) {
      this.infoForCreateReview = infoForReview
      this.showReviewCreate = true
    },
    closeReviewCreate: function () {
      this.showReviewCreate = false
      this.showMovieDetail = true
    },
    backToHome: function () {
      this.showReviewCreate = false
      this.showMovieDetail = true      
    },

    setToken: function () {
        const token = localStorage.getItem('jwt')
        const config = {
          Authorization: `JWT ${token}`
        }
        return config
      },
    getMovies: function () {
      
      const SERVER_URL = process.env.VUE_APP_SERVER_URL

      axios({
        method: 'get',
        url: `${SERVER_URL}/movies/`,
        headers: this.setToken()
        // params,
      })
      .then((res) => {
        let movies = res.data
        this.movies = movies
        this.brightMovies = movies.filter(movie => {
          // 범죄, 호러, 미스터리, 스릴러 장르 삽입
          if (movie.genres.includes(80) || movie.genres.includes(27) || movie.genres.includes(9648) || movie.genres.includes(53)) {
            return true
          }
        })
        this.documentaryMovies = movies.filter(movie => {
          // 다큐멘터리 장르 삽입
          if (movie.genres.includes(99)) {
            return true
          }
        })
        this.warMovies = movies.filter(movie => {
          // 전쟁 장르 삽입
          if (movie.genres.includes(10752)) {
            return true
          }
        })
        this.darkMovies = movies.filter(movie => {
          // 다큐멘터리 장르 삽입
          if (movie.genres.includes(12) || movie.genres.includes(16) || movie.genres.includes(35)) {
            return true
          }
        })
        this.romanceMovies = movies.filter(movie => {
          // 다큐멘터리 장르 삽입
          if (movie.genres.includes(10749) || movie.genres.includes(10766))  {
            return true
          }
        })

      })
      .catch((err) => {
        console.log(err)
      })

    },
    
  },

  created: function () {
    // 로그인이 됐다면
    if (localStorage.getItem('jwt')) {
      // todo 리뷰 정보 가져오자
      this.getMovies()
    // 로그인이 안됐다면
    } else {
      this.$router.push({ name: 'Login' })
    }
  }

}
</script>

<style scoped>
/* Dropdown Button */
.dropbtn {
  background-color: green;
  color: white;
  padding: 16px;
  font-size: 16px;
  border: none;
}

/* The container <div> - needed to position the dropdown content */
.dropdown {
  position: relative;
  display: inline-block;
}

/* Dropdown Content (Hidden by Default) */
.dropdown-content {
  display: none;
  position: absolute;
  background-color: green;
  min-width: 160px;
  box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
  z-index: 5;
}

/* Links inside the dropdown */
.dropdown-content a {
  color: white;
  padding: 12px 16px;
  text-decoration: none;
  display: block;
}

/* Change color of dropdown links on hover */
.dropdown-content a:hover {background-color: #ddd;}

/* Show the dropdown menu on hover */
.dropdown:hover .dropdown-content {display: block;}

/* Change the background color of the dropdown button when the dropdown content is shown */
.dropdown:hover .dropbtn {background-color: #3e8e41;}

</style>