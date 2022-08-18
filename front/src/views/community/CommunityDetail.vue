<template>
  <div class="community-detail-bg">
    <div class="container make_font">
      <header>
        <div class="logo mb-4">
          <div class="outer">
            <img class="logo_image" src="@/assets/logo_transparent.png">
            <!-- <p class="signup_title">회원가입</p> -->
          </div>
        </div>
      </header>
    <div v-if="community">
      <p class="my-4 fs-2">제목: {{ community.title }}</p>
      <hr>
      <div class="d-flex flex-row">
        <span class="fs-5">작성자: {{ community.userName }}</span>
        <span class="offset-1 fs-5">MBTI 정보: {{ community.mbti }}</span>
        <span class="offset-1 fs-5">만족도: {{ community.rank }}</span>
      </div>
      <hr>
      <div class="d-flex flex-column justify-content-between community-content">
        <span class="fs-5">내용: 
          <br>
          {{ community.content }}
        </span>
      </div>
      <div class="d-flex flex-row-reverse justify-content-between align-items-center">
        <div>
          <button @click="moveToCommunity" class="btn btn-outline-light ml-5">되돌아가기</button>
          <button @click="deleteCommunity(community)" class="btn btn-outline-light mx-2">삭제</button>
          <button @click="updateCommunity(community)" class="btn btn-outline-light">수정</button>
        </div>
        <div>
          <span>즐겨찾기: {{ count }}</span>
          <span class="mx-2">
            <i class="fas fa-bookmark pointer" v-if="finding" @click="createFinding" style="color: yellow"></i>
            <i class="fas fa-bookmark pointer" v-else @click="createFinding"></i>   
          </span>
        </div>
      </div>
      <hr>
      <div class="mx-3">
        <label for="createcomment"></label>
        <input type="text" id="createcomment" 
          @keyup.enter="createComment" 
          v-model="commentValue"
          class="comment-form ml-2">
        <button @click="createComment" class="mx-3 btn btn-outline-light">댓글 작성</button>
        <hr>
      </div>

      <comment-list
        :comments="comments"> 
      </comment-list>
    </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import CommentList from '../../components/CommentList.vue'

export default {
  name: 'CommunityDetail',
  data: function (){
    return {
      community: null,
      user: [],
      comments: [],
      commentValue: null,
      finding: false,
      count: null,
    }
  },
  components: {
    CommentList
  },
  methods: {
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    getCommunity: function (){
      const community_pk = this.$route.params.community_pk
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/movies/detail/${community_pk}`,
        headers: this.setToken(),
      })
      .then( res => {
        this.community = res.data[0]
        this.count = res.data[1]
        this.finding = res.data[2]

      })
      .catch( err => {
        console.log(err)
      })      
    },
    moveToCommunity: function (){
      this.$router.push({ name: 'Community' })
    },
    updateCommunity: function (community){
      if (this.user.username === community.userName) {
        this.$router.push({ name: 'CommunityDetailUpdate', params: { community_pk: `${community.id}`}})
      } else {
            this.$swal({icon: 'error',
            title: 'Oops..',
            text: '본인 글만 수정 가능합니다.',
            });
      }
    },
    deleteCommunity: function (){
      const community_pk = this.$route.params.community_pk 
      axios({
        method: 'delete',
        url: `http://127.0.0.1:8000/movies/community/${community_pk}/`,
        headers: this.setToken(),
      })
      .then( (res) =>{
          if (res.data.message){
            this.$swal({icon: 'error',
            title: 'Oops..',
            text: '본인 글만 삭제 가능합니다.',
            });
          } else {
            this.$router.push({ name: 'Community' })
          }     
      })
      .catch( err => {
        console.log(err)
      })
    },
    getComment: function (){
      const community_pk = this.$route.params.community_pk
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/movies/comments/${community_pk}`,
        headers: this.setToken(),
      })
      .then( res => {
        this.comments = res.data
      })
      .catch( err => {
        console.log(err)
      })      
    },
    getUser: function (){
        axios({
        method: 'get',
        url: `http://127.0.0.1:8000/accounts/getuser/`,
        headers: this.setToken(),
      })
      .then( res => {
        this.user = res.data
      })
      .catch( err => {
        console.log(err)
      })          
    },
    createFinding: function () {
      const community_pk = this.$route.params.community_pk

      axios({
        method: 'post',
        url: `http://127.0.0.1:8000/movies/${community_pk}/finds/`,
        headers: this.setToken(),
      })
      .then( (res) =>{
        this.finding = res.data[0]
        this.count = res.data[1]
      })
      .catch( err => {
        console.log(err)
      })
    },    
    createComment: function (){
      const community_pk = this.$route.params.community_pk

      axios({
        method: 'post',
        url: `http://127.0.0.1:8000/movies/${community_pk}/comment/`,
        headers: this.setToken(),
        data: {
          content: this.commentValue,
        }
      })
      .then( () =>{
        this.getCommunity()
        this.getComment()
        this.commentValue = null
      })
      .catch( err => {
        console.log(err)
      })
    },
    
  },
  created: function (){
    this.getCommunity()
    this.getComment()
    this.getUser()
  }
} 
</script>

<style>
  .comment-form{
    width: 40vh;
    height: 4vh;
    color:white;
    background: transparent;
    border: white solid 2px;
  }
  .community-content{
    height: 45vh;
  }
  .community-detail-bg{
    border: 0;
    padding: 0; 
    width: auto;
    background-position: center;
    background-size: cover;
    background-position: bottom; 
    background-image: linear-gradient( rgba(0, 0, 0, 0.75), rgba(0, 0, 0, 0.75)),url("../../assets/login_back.jpg");
}
</style>