<template>
  <div class="community-bg">
    <div class="container make_font">
      <div class="text-center">
      <br>
      <h3>Community</h3>
      <h5 class="mb-5">영화에 대한 자유로운 대화의 공간입니다.</h5>
      <hr>
      <button @click="moveToCreate" class="m-3 btn btn-outline-light">게시글 작성</button>
      </div>
      <div class="mx-3 mt-5">
      <community-list :communities="communities"> 
      </community-list> 
      </div>    
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import CommunityList from '../../components/CommunityList.vue'

export default {
  name: 'Community',
  data: function (){
    return {
      communities: [], 
    }
  },
  components: {
    CommunityList,
  },
  methods: {
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },        
    moveToCreate: function (){
      this.$router.push({ name: 'CreateCommunity' })
    },
    moveToDetail: function (){
      this.$router.push({ name: 'CommunityDetail', params: {community_pk: `${this.community.id}` }})
    },
    getCommunities: function (){
      axios({
      method: 'get',
      url: 'http://127.0.0.1:8000/movies/community_list_create/',
      headers: this.setToken(),
      })
      .then( res => {
        this.communities = res.data
      })
      .catch( err => {
        console.log(err)
      })
    },
  },
  created: function (){
    this.getCommunities()
  }
}
</script>

<style>
.community-bg{
    border: 0;
    padding: 0; 
    width: auto;
    background-position: center;
    background-size: cover;
    background-position: bottom; 
    background-image: linear-gradient( rgba(0, 0, 0, 0.75), rgba(0, 0, 0, 0.75) ),url("../../assets/signup_back.jpg");
}

</style>