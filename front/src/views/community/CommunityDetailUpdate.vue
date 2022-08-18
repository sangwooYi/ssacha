<template>
  <div>
  <header>
        <div class="logo mb-4">
          <div class="outer">
            <img class="logo_image" src="@/assets/logo_transparent.png">
            <!-- <p class="signup_title">회원가입</p> -->
          </div>
        </div>
      </header>
      <section >
        <div class="mb-4 titles_width inner">
          <label for="title" class="form-label" id="bg_text_color">제목 </label>
          <input type="text" id="bg_text_color" v-model="title" class="form-control border border-white">
        </div>
        <div class="mb-4 titles_width inner">
          <label for="movie" id="bg_text_color">관련 영화 </label>
          <input id="movie" v-model="movieTitleInput" @input="submitAutoComplete" type="text"  class="bg_text_color form-control border border-white" :placeholder="movie_title" >
          <div class="autocomplete disabled">
            <span v-if="!movie_title">
              <div
                  @click="addMovie(res.title)"
                  class="pointer"
                  v-for="(res,idx) in result"
                  :key="idx"
                  >{{ res.title }}</div>
            </span>
          </div>
        </div>
        <div class="mb-4 content_width inner">
          <label for="content" id="bg_text_color">내용 </label>
          <textarea name="content" id="bg_text_color" cols="30" rows="10" v-model="content" class="form-control border border-white">
          </textarea>
        </div>
        <div class="d-flex align-items-center mb-0 col-1 inner">
          <label for="rate" class="me-3">만족도(0~10)</label>
          <input type="number" id="rate" min="0" max="10" step="0.5"
            v-model="rank" class="bg_text_color form-control border border-white mb-0">
        </div>        
        <div class=outer>
        <div>
          <button type="button" class="btn btn-outline-light mt-4" @click="addCommnuity">게시글 수정</button>
        </div>
        <div>
          <button type="button" class="btn btn-outline-light mt-4" @click="moveToCommunityDetail">돌아가기</button>
        </div>    
        </div>
      </section>    
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'CommunityDetailUpdate',
  data: function (){
    return {
      title: null,
      content: null,
      movie_title: null,
      movie_titles: [],
      movieTitleInput: null,
      result: null,
      rank: null,
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
    submitAutoComplete() {
      const autocomplete = document.querySelector(".autocomplete");
      if (this.movieTitleInput) {
        autocomplete.classList.remove("disabled");
        this.result = this.movie_titles.filter((movie_title) => {
          return movie_title.title.match(new RegExp("^" + this.movieTitleInput, "i"));
        });
      } else {
        autocomplete.classList.add("disabled");
      }
    },  
    selectMovie: function (movie){
      this.movie_title = movie
      this.movieTitleInput = movie
    },
    getCommunity: function (){
      const community_pk = this.$route.params.community_pk
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/movies/detail/${community_pk}`,
        headers: this.setToken(),
      })
      .then( res => {
        const community = res.data[0]
        this.title = community.title
        this.content = community.content
        this.movieTitleInput = community.movie_title
        this.movie_title = community.movie_title
        this.rank = community.rank
      })
      .catch( err => {
        console.log(err)
      })           
    },
    addCommnuity: function (){
      const community_pk = this.$route.params.community_pk  
      axios({
        method: 'put',
        url: `http://127.0.0.1:8000/movies/community/${community_pk}/`,
        headers: this.setToken(),
        data: {
          title: this.title,
          content: this.content,
          movie_title: this.movie_title,
          rank: this.rank,
        }
      })
      .then( (res) =>{
          if (res.data.message){
            this.$swal({icon: 'error',
            title: 'Oops..',
            text: '본인 글만 삭제 가능합니다.',
            });
          } else {
            this.$router.push({ name: 'CommunityDetail', params:{ community_pk: `${community_pk}`}})
          }     
      })
      .catch( err => {
        console.log(err)
      })
    },
    getMovies: function (){
          axios({
      method: 'get',
      url: 'http://127.0.0.1:8000/movies/community_list_create/',
      headers: this.setToken(),
    })
    .then( () => {
      
    })
    .catch( err => {
      console.log(err)
    })
    // 영화 제목 가져오기
    axios({
      method: 'get',
      url: 'http://127.0.0.1:8000/movies/take_movie/',
      headers: this.setToken(),       
     })
     .then( res => {
       this.movie_titles = res.data
     })
     .catch( err => {
       console.log(err)
     })
    },
    addMovie: function (movie){
      this.movie_title = movie
      this.movieTitleInput = movie
    }, 
    moveToCommunityDetail: function (){
      const community_pk = this.$route.params.community_pk   
      this.$router.push({ name: 'CommunityDetail', params: { community_pk: `${community_pk}`}})
    }   
  },
  created: function (){
    this.getCommunity()
    this.getMovies()
  }
}
</script>

<style>

</style>