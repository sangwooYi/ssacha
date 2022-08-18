<template>
  <div class="mt-5 m-3 make_font">
    <div>
      <h4 class="mx-3">나의 MBTI에 어울리는 영화 <i class="fas fa-video"></i></h4>
      <div class="d-flex recommend-list-box">
        <recommend-list :movies="my_movies"></recommend-list>
      </div>
    </div>
    <div>
      <h4 class="mx-3 mt-4">파트너가 좋아 할 영화 <i class="fas fa-smile-wink"></i></h4>
      <div class="d-flex recommend-list-box">
        <recommend-list :movies="partner_movies"></recommend-list>
      </div>
    </div>
    <div>
      <h4 class="mx-3 mt-4">당신의 파트너와 같이 보면 좋을 영화 <i class="fas fa-child"></i></h4>
      <div class="d-flex recommend-list-box">
        <recommend-list :movies="our_movies"></recommend-list>
      </div>
    </div>
    <div>
      <h4 class="mx-3 mt-4">내가 평소에는 볼 일 없을테지만 한번 도전할 만한 영화 <i class="fas fa-eye"></i></h4>
      <div class="d-flex recommend-list-box">
        <recommend-list :movies="dislike_movies"></recommend-list>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import RecommendList from '../../components/RecommendList.vue'

export default {
  name: 'Recommend',
  components: {
    RecommendList,
  },
  data: function () {
    return {
        my_movies: [],
        partner_movies: [],
        our_movies: [],
        dislike_movies: [],
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
  },
  created: function () {
    axios({
      method: 'get',
      url: 'http://127.0.0.1:8000/movies/recommend_movies/',
      headers: this.setToken()
    })
    .then( res => {
      this.my_movies = res.data[0]
      this.partner_movies = res.data[1]
      this.our_movies = res.data[2]
      this.dislike_movies = res.data[3]
    })
    .catch( err => {
      console.log(err)
    })
  }
  }

</script>

<style>
  .recommend-list-box{
    height: 35vh;
  }

</style>