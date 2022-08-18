<template>
  <div>
    <div v-for="review in paginatedData" :key="review.id">
      <p class="mt-5">유저이름: {{ review.userName}}</p>
      <p>MBTI: {{ review.mbti }}</p>
      <p>만족도: {{ review.rank }}</p>
      <p>한줄리뷰: {{ review.content }}</p>
      <p>생성시간: {{ review.created_at | dateFormat }}</p>
      <p>수정시간: {{ review.updated_at | dateFormat }}</p>
      <div class="d-flex align-items-center">
        <button @click="deleteReview(review)" class="mt-0 btn btn-outline-light">삭제</button>
      </div>
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
  name: 'ReviewList',
  props: {
    reviews: {
      type: Array,
    },
    pageSize: {
      type: Number,
      required: false,
      default: 3
    }       
  },
  data: function (){
    return {
      pageNum: 0,
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
    nextPage: function () {
      this.pageNum += 1;
    },
    prevPage: function () {
      this.pageNum -= 1;
    },
    deleteReview: function (review) {
      const movie_pk = this.$route.params.movie_pk

      axios({
        method: 'delete',
        url: `http://127.0.0.1:8000/movies/${movie_pk}/review/${review.id}/`,
        headers: this.setToken(),
      })
      .then( (res) =>{
          if (res.data.message){
            this.$swal({icon: 'error',
            title: 'Oops..',
            text: '본인 글만 삭제 가능합니다.',
            });
          } else {
            this.$emit('delete-review')
          }     
      })
      .catch( err => {
        console.log(err)
      })
    }    
  },    
  computed: {
    pageCount: function () {
      let listLeng = this.reviews.length,
          listSize = this.pageSize,
          page = Math.floor(listLeng / listSize);
      if (listLeng % listSize > 0) page += 1;
      
      /*
      아니면 page = Math.floor((listLeng - 1) / listSize) + 1;
      이런식으로 if 문 없이 고칠 수도 있다!
      */
      return page;
    },
    paginatedData: function () {
      const start = this.pageNum * this.pageSize,
            end = start + this.pageSize;
      return this.reviews.slice(start, end);
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