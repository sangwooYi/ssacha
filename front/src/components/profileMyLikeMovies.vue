<template>
  <div>
    <div 
      v-for="likeMovie in paginatedData"
      :key="likeMovie.id"
      class="pointer"
      @click="moveToMovieDetail(likeMovie)"
    >
    <div class="offset-1">
      <span>{{ likeMovie.title }}</span>
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
  name: 'profileMyLikeMovies',
  data: function (){
    return {
      pageNum: 0,
    }
  },
  props: {
    likeMovies: {
      type: Array,
    },
    pageSize: {
      type: Number,
      required: false,
      default: 10
    }        
  },
  methods: {
    moveToMovieDetail: function (movie){
      this.$router.push({ name: 'RecommendDetail', params: { movie_pk: `${movie.id}`}})
    },
    nextPage: function () {
      this.pageNum += 1;
    },
    prevPage: function () {
      this.pageNum -= 1;
    },       
  },
  computed: {
    pageCount: function () {
      let listLeng = this.likeMovies.length,
          listSize = this.pageSize,
          page = Math.floor(listLeng / listSize);
      if (listLeng % listSize > 0) page += 1;
      
      return page;
    },
    paginatedData: function () {
      const start = this.pageNum * this.pageSize,
            end = start + this.pageSize;
      return this.likeMovies.slice(start, end);
    }
  },           
}
</script>

<style>

</style>