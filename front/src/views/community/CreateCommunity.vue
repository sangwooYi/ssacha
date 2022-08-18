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
        <input type="text" id="bg_text_color" v-model="title" class="form-control border border-white" placeholder="게시글 제목을 입력해주세요">
      </div>
      <div class="mb-4 titles_width inner">
        <label for="movie" id="bg_text_color">관련 영화 </label>
        <input id="movie" v-model="movieTitleInput" @input="submitAutoComplete" type="text"  class="bg_text_color form-control border border-white" placeholder="영화 제목을 입력해주세요" >
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
        <textarea name="content" id="bg_text_color" cols="30" rows="10" v-model="content" class="form-control border border-white" placeholder="게시글 내용을 입력해주세요"></textarea>
      </div>
      <div class="d-flex align-items-center mb-0 col-1 inner">
        <label for="rate" class="me-3">만족도(0~10)</label>
        <input type="number" id="rate" min="0" max="10" step="0.5"
          v-model="rank" class="bg_text_color form-control border border-white mb-0">
      </div>
      <div class="outer">
        <div>
          <button type="button" class="btn btn-outline-light mt-4" @click="addCommnuity">게시글 작성</button>
        </div>    
        <div>
          <button type="button" class="btn btn-outline-light mt-4" @click="moveToCommunity">돌아가기</button>
        </div>  
      </div>
    </section>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'CreateCommunity',
  data: function (){
    return {
      title: null,
      content: null,
      movie_title: null,
      movie_titles: [],
      movieTitleInput: null,
      rank: null,
      result: null,
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
    addMovie: function (movie){
      this.movie_title = movie
      this.movieTitleInput = movie
    },
    addCommnuity: function (){
      axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/movies/community_list_create/',
        headers: this.setToken(),
        data: {
          title: this.title,
          content: this.content,
          movie_title: this.movie_title,
          rank: this.rank
        }
      })
      .then( () =>{
        this.$router.push({ name: 'Community' })
      })
      .catch( err => {
        console.log(err)
      })
    },
    moveToCommunity: function (){
      this.$router.push({ name: 'Community' })
    }
  },
  created: function (){
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
   
}
</script>

<style>
  .pointer{
    cursor: pointer;
  }

  #bg_text_color{
    color: white;
    background: black;
  }

  .bg_text_color{
    color: white;
    background: black;
  }

  .content_width{
    width: 50%;
  }

  .titles_width{
    width: 50%;
  }

  .outer{
    display: flex;
    justify-content: center;
  }

  .inner{
    margin: 0 auto;
  }

  .search-bar {
  color:white;
  background: transparent;
  }

</style>