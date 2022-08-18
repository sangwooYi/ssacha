<template>
  <div class="recommend-bg">
    <div v-if="movie" class="relative d-flex justify-content-between make_font app">
      <!-- <img :src="base_url + movie.poster_path" alt="poster" class="absolute back-img offset-5"> -->
      <div class="offset-1 col-10">
        <div class="mt-5 d-flex">
          <div class="col-4">
            <div>
            <img :src="base_url + movie.poster_path" alt="movie_photo" class="mb-3">
            <br>
            </div>
          </div>
          <div v-if="movie" class="d-flex flex-column col-6 offset-1 form">
            <h5>제목: {{ movie.title }}</h5>
            <div>
            <span>좋아요: {{ count }}</span>
            <span class="mx-2">
              <i id="heart" v-if="liking" @click="createLiking" class="fas fa-heart pointer" style="color: crimson"></i>
              <i id="heart" v-else @click="createLiking" class="far fa-heart pointer"></i>        
            </span>
            </div>
            <div v-for="genre in genres"
              :key="genre.id">
              <p>장르: {{ genre.name }}</p>
            </div>
            <p>줄거리: {{ movie.overview }}</p>
            <p>평점: {{ movie.vote_average }}</p>
            <p>개봉일: {{ movie.release_date }}</p>
            <br><br>
            <button class="col-4 btn btn-outline-light form" @click="moveToRecommend">뒤로</button>
          </div>
        </div>
        <hr>
        <div class="d-flex">
        <div class="col-6 d-flex flex-column justify-content-between align-items-start">
          <h5>관련 영상</h5>
          <youtube-list v-for="video in videos"
          :key="video.id.videoId"
          :video="video"
          @select-video="onSelectVideo"
          >
          </youtube-list>
          <youtube-detail
          :video="selectVideo"
          @close-youtube="closeYoutube">
          </youtube-detail>
        </div>
        <div class="offset-1 col-5 form">
          <h5 class="mb-3"> 영화 리뷰</h5>
          <div class="d-flex align-items-end">
            <div class="d-flex flex-column col-8 me-3">
              <label for="input">리뷰 작성</label>
              <input type="text" id="input" v-model="reviewValueText" 
                class="bg_text_color form-control border border-white">
            </div>
            <div class="d-flex flex-column">
              <label for="rate">만족도(0~10)</label>
              <input type="number" id="rate" min="0" max="10" step="0.5"
                v-model="reviewValueRank" class="bg_text_color form-control border border-white">
            </div>
            <button @click="createReview" class="mb-0 ms-3 btn btn-outline-light">작성</button>
          </div>
          <hr>
          <div>
              <review-list :reviews="reviews" @delete-review="deleteReview"></review-list>                  
            </div>        
        </div>
        <hr>
        </div>
      </div>
    </div>
  </div>
</template>


<script>
import axios from 'axios'
import YoutubeList from '@/components/YoutubeList'
import YoutubeDetail from '@/components/YoutubeDetail'
import ReviewList from '@/components/ReviewList'


const API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY
const API_URL = 'https://www.googleapis.com/youtube/v3/search'

export default {
  name: 'RecommendDetail',
  components: {
    YoutubeList,
    YoutubeDetail,
    ReviewList
  },
  data: function () {
    return { 
      movie: null,
      genres: null,
      base_url: 'https://image.tmdb.org/t/p/w400/',
      reviewValueText: null,
      reviewValueRank: null,
      reviews: [],
      communities: [],
      liking: null,
      user: null,
      count: null,
      videos: [],
      selectVideo: null,
   }
  },
  methods : {
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    getMovieDetail: function () {
      const movie_pk = this.$route.params.movie_pk
      // console.log(movie_pk)

      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/movies/take_movie_detail/${movie_pk}`,
        headers: this.setToken(),
      })
      .then( (res) =>{
        // console.log(res.data[1])
        this.movie = res.data[0]
        this.genres = res.data[1]
        // console.log(res.data[2])
        this.count = res.data[2]
        this.liking = res.data[3]
        this.getYouTube(this.movie.title)
      })
      .catch( err => {
        console.log(err)
      })
    },
    getReviewDetail: function () {
      const movie_pk = this.$route.params.movie_pk
      // console.log(movie_pk)
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/movies/${movie_pk}/review_list_create/`,
        headers: this.setToken(),
      })
      .then( (res) =>{
        // console.log(res.data[1])
        this.reviews = res.data
      })
      .catch( err => {
        console.log(err)
      })
    },
    getCommunity: function () {
      const movie_pk = this.$route.params.movie_pk

      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/movies/${movie_pk}/community/`,
        headers: this.setToken(),
      })
      .then( (res) =>{
        // console.log(res.data[1])
        this.communities = res.data
        
      })
      .catch( err => {
        console.log(err)
      })
    },
    getUser: function () {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/accounts/getuser/`,
        headers: this.setToken(),
      })
      .then( (res) => {
        // console.log(res)
        // console.log(res.data)
        this.user = res.data
      })
    },
    getYouTube: function (inputValue) {
      const params = {
        key: API_KEY,
        part: 'snippet',
        q: inputValue,
        type: 'video'
      }
      axios({
        method: 'get',
        url: API_URL,
        params,
      })
      .then( (res) => {
        console.log(res)
        this.videos = res.data.items
      })
      .catch(err => {
          console.log(err)
        })
    },
    createLiking: function () {
      const movie_pk = this.$route.params.movie_pk

      axios({
        method: 'post',
        url: `http://127.0.0.1:8000/movies/${movie_pk}/like/`,
        headers: this.setToken(),
      })
      .then( (res) =>{
        this.liking = res.data[0]
        this.count = res.data[1]
      })
      .catch( err => {
        console.log(err)
      })
    },
    createReview: function () {
      const movie_pk = this.$route.params.movie_pk

      if (this.reviewValueRank > 10) {
        alert('점수는 0~10점까지 작성해주세요')
      } else {
        axios({
        method: 'post',
        url: `http://127.0.0.1:8000/movies/${movie_pk}/review_list_create/`,
        headers: this.setToken(),
        data: {
          rank: this.reviewValueRank,
          content: this.reviewValueText,
        }
      })
      .then ( (res) => {
        this.reviews.push(res.data)
        // console.log(this.reviews)
        this.reviewValueText = null,
        this.reviewValueRank = null,
        this.getMovieDetail()
      })
      }
    },
    deleteReview: function (){
      this.getMovieDetail()
      this.getReviewDetail()
    },
    MoveToCommunityDetail: function(community) {
      this.$router.push({ name: 'CommunityDetail', params: {community_pk: `${community.id}` } })
    },
    moveToRecommend: function (){
      this.$router.push({ name: 'Recommend' })
    },
    onSelectVideo: function (video) {
      this.selectVideo = video
    },
    setScrollTop: function() {
      window.scrollTo(0, 0)
    },
    closeYoutube: function (){
      this.selectVideo = null
    }    
  },
  created : function () {
    this.getMovieDetail()
    this.getReviewDetail()
    this.getCommunity()
    this.getUser()
    this.setScrollTop()
  },
  filters: {
    dateFormat: function (value){
      if (!value){
        return " "
      }
      const js_date = new Date(value)
      let year = js_date.getFullYear()
      let month = js_date.getMonth() + 1
      let day = js_date.getDate()
      let hour = js_date.getHours()
      let minute = js_date.getMinutes()

      if (month < 10){
        month = "0" + month
      }
      if (day < 10){
        day = "0" + day
      }
      if (hour < 10){
        hour = "0" + hour
      }
      if (minute < 10){
        minute = "0" + minute
      }
      return `${year}-${month}-${day} ${hour}:${minute}`
    }
  }  
}
</script>

<style>
  .app{
    height: auto;
    width: auto;
  }
  .relative{
    position: relative;
  }
  .absolute{
    position: absolute;
  }
  .back-img{
    height: 150vh;
    opacity: 0.2;
    background-color: gray;
    z-index: 1;
    transform: translate( 0%, 6%);
    border-radius: 5%;
    border-style: none inset inset none;
    border-color: grey;
    border-width: 8px;
    box-shadow: 0 0 8px 8px white inset;
  }
  .form{
    z-index: 3;
  }
  .recommend-bg{
      border: 0;
      padding: 0; 
      width: auto;
      background-position: center;
      background-size: cover;
      background-position: bottom; 
      background-image: linear-gradient( rgba(0, 0, 0, 0.75), rgba(0, 0, 0, 0.75) ),url("../../assets/login_back.jpg");
  }

</style>