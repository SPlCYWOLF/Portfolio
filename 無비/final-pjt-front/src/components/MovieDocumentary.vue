<template>
  <div class="please">
    <div class="wrapper">
      <div class="card"><img :src="`https://image.tmdb.org/t/p/w500${documentaryMovie.poster_path}`" alt="movie image">
        <div class="info">
          <h3>{{ this.documentaryMovie.original_title }}</h3>
          <br>
          <button @click="showMovieDetail">More</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'MovieDocumentary',
  props: {
    documentaryMovie: Object
  },
  methods: {
    showMovieDetail: function () {
      const movieInfo = {
        title: this.documentaryMovie.title,
        overview: this.documentaryMovie.overview,
        poster_path: this.documentaryMovie.poster_path,
        release_date: this.documentaryMovie.release_date,
        vote_average: this.documentaryMovie.vote_average,
        adult: this.documentaryMovie.adult,
        movie_id: this.documentaryMovie.id,
        original_title: this.documentaryMovie.original_title,
        runtime: this.documentaryMovie.runtime
      }
      this.$emit('show-movie-detail', movieInfo)
      },
  },
}
</script>

<style scoped>

.please {
  display: inline-block;
}
.wrapper {
  display: inline-block;
}
.card {
  width: 300px;
  height: 450px;

  padding: 1.5rem;
  background: #D9E4EC;  /* 11/24 테두리 색 설정 */
  position: relative;
  display: flex;
  align-items: flex-end;
  transition: 0.4s ease-out;
  box-shadow: 0px 7px 10px rgba(0, 0, 0, 0.5);
  margin: 1em;
}
.card:hover {
  transform: translateY(20px);
}
.card:hover:before {
  opacity: 1;
  
}
.card:hover .info {
  opacity: 1;
  transform: translateY(0px);
}
.info {
  margin: 1em;
  left: -5%;
  top: 30%;
  width: 100%;
  place-items:center;
}
.card:before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  display: block;
  width: 100%;
  height: 100%;
  /* border-radius: 15px; */
  background: rgba(0, 0, 0, 0.6);
  z-index: 2;
  transition: 0.5s;
  opacity: 0;
}
.card img {
  width: 100%;
  height: 100%;
  -o-object-fit: cover;
     object-fit: cover;
  position: absolute;
  top: 0;    /* 11/24 */
  left: 0;
  /* border-radius: 15px; */
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2); /* this adds the "card" effect */
      /* 11/24 테두리 설정 */
}
.card .info {
  position: absolute;

  z-index: 3;
  color: white;
  opacity: 0;
  transform: translateY(30px);
  transition: 0.5s;
}
.card .info h3 {
  margin: 0px;
}
.card .info p {
  letter-spacing: 1px;
  font-size: 15px;
  margin-top: 8px;
}
.card .info button {
  padding: 0.6rem;
  outline: none;
  border: none;
  border-radius: 3px;
  background: #D9E4EC;
  color: black;
  font-weight: bold;
  cursor: pointer;
  transition: 0.4s ease;
}
.card .info button:hover {
  background: #385E72;    /* 11/24 detail 버튼 색 설정 */
  color: #D9E4EC;
}
</style>