<template>
  <div>
    <div
      v-for="review in paginatedData"
      :key="review.id"
      class="pointer"
      @click="moveToReviewMovieDetail(review)"
    > 
    <div class="col-12 d-flex justify-content-between">
      <span class="offset-1">{{ review.content }}</span>
      <span>{{ review.updated_at | dateFormat}}</span>
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
export default {
  name: 'profileMyReviews',
  data: function (){
    return {
      pageNum: 0,
    }
  },
  props: {
    reviews: {
      type: Array,
    },
    pageSize: {
      type: Number,
      required: false,
      default: 10
    }        
  },
  methods: {
    moveToReviewMovieDetail: function (review){
      this.$router.push({ name: 'RecommendDetail', params: { movie_pk: `${review.movie}` }})
    },    
    nextPage: function () {
      this.pageNum += 1;
    },
    prevPage: function () {
      this.pageNum -= 1;
    },            
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
  },
  computed: {
    pageCount: function () {
      let listLeng = this.reviews.length,
          listSize = this.pageSize,
          page = Math.floor(listLeng / listSize);
      if (listLeng % listSize > 0) page += 1;
      
      return page;
    },
    paginatedData: function () {
      const start = this.pageNum * this.pageSize,
            end = start + this.pageSize;
      return this.reviews.slice(start, end);
    }
  },          

}
</script>

<style>

</style>