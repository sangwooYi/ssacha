<template>
  <div class="profile-bg">
    <div v-if="user" class="container make_font">
      <div class="d-flex flex-column align-items-start offset-1">
        <h5 style="color: khaki" class="my-5">내 프로필  <i class="fas fa-address-card"></i></h5>
        <p class="mt-2">아이디: {{ user.username }}</p>
        <p>MBTI: {{ user.mbti }}</p>
      </div>
      <hr>
      <div class="d-flex justify-content-between flex-wrap form">
        <div class="col-5 my-5">
          <h5 class="text-center" style="color: khaki">내가 좋아요 한 영화 <i class="fas fa-thumbs-up"></i></h5>
          <hr>
          <div class="d-flex flex-column">
            <profile-my-like-movies :like-movies="likeMovies"></profile-my-like-movies>
          </div>
        </div>
        <div class="col-5 my-5">
          <h5 class="text-center" style="color: khaki">내가 작성한 리뷰 <i class="fas fa-feather-alt"></i></h5>
          <hr>
          <profile-my-reviews :reviews="reviews"></profile-my-reviews>
        </div>
        <div class="col-5 my-5">
          <h5 class="text-center" style="color: khaki">내가 작성한 글 <i class="fas fa-pen-fancy"></i></h5>
          <hr>
          <profile-my-communities :communities="communities"></profile-my-communities>
        </div>
        <div class="col-5 my-5 offset-1">
          <h5 class="text-center" style="color: khaki">내가 즐겨찾기한 글 <i class="fas fa-star"></i></h5>
          <hr>
          <profile-my-finds :find-communities="findCommunities"></profile-my-finds>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import profileMyCommunities from "@/components/profileMyCommunities"
import profileMyFinds from "@/components/profileMyFinds"
import profileMyLikeMovies from "@/components/profileMyLikeMovies"
import profileMyReviews from '@/components/profileMyReviews'

export default {
  name: 'Profile',
  data: function() {
    return {
      likeMovies: [],
      reviews: [],
      communities: [],
      findCommunities: [], 
      user: null,     
    }
  },
  components: {
    profileMyCommunities,
    profileMyFinds,
    profileMyLikeMovies,
    profileMyReviews,
  },
  methods: {
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },  
    getUser: function (){
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
    getProfile: function (){
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/movies/profile/`,
        headers: this.setToken()
      })
        .then(res => {
          this.likeMovies = res.data[0]
          this.reviews = res.data[1]
          this.communities = res.data[2]
          this.findCommunities = res.data[3]
        })
        .catch(err => {
          console.log(err)
        })
    },
  },
  created: function (){
    this.getProfile()
    this.getUser()
  }, 
}
</script>

<style>
.profile-bg{
    border: 0;
    padding: 0; 
    width: auto;
    background-position: center;
    background-size: cover;
    background-position: bottom; 
    background-image: linear-gradient( rgba(0, 0, 0, 0.75), rgba(0, 0, 0, 0.75) ),url("../../assets/community_back.jpg");
}

</style>