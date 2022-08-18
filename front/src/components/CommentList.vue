<template>
  <div class="container">
    <div
      v-for="comment in paginatedData"
      :key="comment.id"
      class="row g-2 align-middle"
    >
      <div class="col-7">
        <span class="fs-5">{{ comment.userName }}: {{ comment.content }}</span>
      </div>
      <div class="col-4 ">
        <span class="offset-2 fs-6 align-middle">작성시간: {{ comment.created_at | dateFormat }}</span>
      </div>
      <div class="col-1">
        <button @click="deleteComment(comment)" class="btn btn-outline-light btn-sm mt-1">삭제</button> 
      </div>
      <hr>
    </div>
    <div class="btn-cover">
      <button :disabled="pageNum === 0" @click="prevPage" class="page-btn">
        이전
      </button>
      <span class="page-count">{{ pageNum + 1 }} / {{ pageCount }} 페이지</span>
      <button :disabled="pageNum >= pageCount - 1" @click="nextPage" class="page-btn">
        다음
      </button>
    </div>       
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'CommentList',
  props: {
    comments: {
      type: Array,
    },
    pageSize: {
      type: Number,
      required: false,
      default: 8
    }    
  },
  data: function () {
    return {
      pageNum: 0,
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
    deleteComment: function (comment) {
      const community_pk = this.$route.params.community_pk
      axios({
        method: 'delete',
        url: `http://127.0.0.1:8000/movies/comment/${community_pk}/${comment.id}/`,
        headers: this.setToken(),
      })
      .then( (res) =>{
        // console.log(community_pk)
        if (res.data.message){
          this.$swal({icon: 'error',
          title: 'Oops..',
          text: '본인 글만 삭제 가능합니다.',
          });
        } else {
          this.$router.go({ name: 'CommunityDetail' ,params: { community_pk: `${community_pk}` }})
        }        
      })
      .catch( err => {
        console.log(err)
      })
    },
    nextPage () {
      this.pageNum += 1;
    },
    prevPage () {
      this.pageNum -= 1;
    },
  },
  computed: {
    pageCount () {
      let listLeng = this.comments.length,
          listSize = this.pageSize,
          page = Math.floor(listLeng / listSize);
      if (listLeng % listSize > 0) page += 1;
      return page;
    },
    paginatedData () {
      const start = this.pageNum * this.pageSize,
            end = start + this.pageSize;
      return this.comments.slice(start, end);
    }
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

</style>