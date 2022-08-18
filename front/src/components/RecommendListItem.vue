<template>
  <div class="mt-3 mx-3 pointer text-center" @click="moveToRecommendDetail">
    <div class="img-box">
      <div class="overlay-heart offset-10 mt-2">
        <i id="heart" v-if="isLiking" class="fas fa-heart pointer" style="color: crimson"></i>
        <i id="heart" v-else class="far fa-heart pointer"></i> 
      </div>
      <div class="overlay-text col-12 text-center fw-bol">
        <div class="d-flex flex-column">
          <p>제목: {{ movie.title }}</p>
        </div>
        <p>평점: {{ movie.vote_average }}</p>
        <p>개봉일: {{ movie.release_date }}</p>
      </div>
      <img :src="imageUrl + movie.poster_path" class="recommend-img" alt="movie_poster">
    </div>
    <hr>    
  </div>
  
</template>

<script>
import axios from 'axios'

export default {
  name: "RecommendListItem",
  data: function (){
    return{    
      movieOverview: null,
      imageUrl: 'https://image.tmdb.org/t/p/original/',
      isLiking: false,  
    }
  },
  props: {
    movie: {
      type: Object
    },
  },
  methods: {
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },    
    moveToRecommendDetail: function (){
      this.$router.push({ name: 'RecommendDetail', params: {movie_pk: `${this.movie.id}` }})
    },
    getLikeStatus: function (){
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/movies/is_movie_like/${this.movie.id}`,
        headers: this.setToken(),
      })
      .then( res => {
        this.isLiking = res.data
      })
      .catch( err => {
        console.log(err)
      })         
    }
  },
  created: function (){
    this.getLikeStatus()
  }
}
</script>
<style>
  .recommend-img{
    height: 30vh;
    border-radius: 3%;  
  }
  .img-box {
    position: relative;
    overflow: hidden;
    border-radius: 3%;
  }
  .overlay-text{
    position: absolute;
    opacity: 0;
    color: white;
    transition: opacity 0.35s;
    transform: translate(0, 50%);
    font-size: 12px;
  }
  .overlay-heart{
    position: absolute;
    opacity: 0;
  }
  .img-box:hover .overlay-text{
    opacity: 1;
  }
  .img-box:hover .overlay-heart{
    opacity: 1;
  }

  .img-box:hover > img{
    transform: scale(1.1);
    opacity: 0.3;
    background-color: gray;
    transition: all 0.4s;
  }
</style>