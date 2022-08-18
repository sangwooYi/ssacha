<template>
  <div class="mx-4">
    <h3 class="my-5 mx-5 make_font">검색 결과</h3>
    <div class="my-5 mx-5
    ">
      <h4 class="make_font">영화 제목 연관</h4>
      <hr>
      <div class="d-flex col-12 flex-wrap">
        <li
          v-for="(titleResult, idx) in titleResults"
          :key="idx" 
          @click="moveToRecommendDetail(titleResult)"
          class="pointer d-flex flex-column align-items-center me-5 mt-2"
        >
          <img :src="posterBaseUrl + titleResult.poster_path" alt="poster_image" class="search-img">
          <p class="mt-3 make_font">{{ titleResult.title }}</p>
        </li>
      </div>
    </div>
    <div class="my-5 mx-5">
      <h4 class="make_font">줄거리 연관</h4>
      <hr>
      <div class="d-flex col-12 flex-wrap">
        <li
          v-for="(overviewResult, idx) in overviewResults"
          :key="idx" 
          @click="moveToRecommendDetail(overviewResult)"
          class="pointer d-flex flex-column align-items-center me-5 mt-2"
        >
          <img :src="posterBaseUrl + overviewResult.poster_path" alt="pster_image" class="search-img">
          <p class="mt-3 make_font">{{ overviewResult.title }}</p>
        </li>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios' 

export default {
  name: 'RecommendSearch',
  data: function () {
    return {
      titleResults: [],
      overviewResults: [],
      posterBaseUrl: 'https://image.tmdb.org/t/p/w200/',
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
    getResults: function (){
      const keyword = this.$route.params.keyword
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/movies/take_movie_search/${keyword}`,
        headers: this.setToken(),
        data: {
          keyword: keyword
        }
      })
      .then( (res) =>{
        // console.log(res)
        this.titleResults = res.data[0]
        this.overviewResults = res.data[1]
      })
      .catch( err => {
        console.log(err)
      })      
    },
    moveToRecommendDetail: function (movie){
      this.$router.push({ name: 'RecommendDetail', params: { movie_pk: `${movie.id}` }})
    }
  },
  created: function () {
    this.getResults()
  },
}
</script>

<style>
  .search-img{
    height: 25vh;
  }
</style>