<template>
  <div>
    <div
      v-for="community in paginatedData"
      :key="community.id"
      @click="moveToDetail(community)" class="pointer d-flex justify-content-between">
      <div class="container mx-3">
        <div class="row">  
          <div class="col-1"></div>
          <div class="col-8 d-flex flex-column justify-content-between">
            <div class="fs-2">{{ community.title }}</div>
            <div class="fs-3 mb-5">{{ community.content }}</div>
            <div class="fs-6 mt-5">{{ community.created_at | dateFormat }}</div> 
          </div>
          <div class="col-2">
           <img :src="imageUrl + community.poster_path" alt="movie_poster" class="community-img img-thumbnail image-width">
          </div>
          <div class="col-1"></div>
        </div>
        <hr>
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

export default {
  name: 'CommunityList',
  data: function (){
    return {
      imageUrl: 'https://image.tmdb.org/t/p/w200/',
      movie: null,
      pageNum: 0      
    }
  },  
  props: {
    communities: {
      type: Array,
    },
    pageSize: {
      type: Number,
      required: false,
      default: 4
    }    
  },
  methods: {
    nextPage () {
      this.pageNum += 1;
    },
    prevPage () {
      this.pageNum -= 1;
    },
    moveToDetail: function (community){
      this.$router.push({ name: 'CommunityDetail', params: {community_pk: `${community.id}` }})
    }
  },
  computed: {
    pageCount () {
      let listLeng = this.communities.length,
          listSize = this.pageSize,
          page = Math.floor(listLeng / listSize);
      if (listLeng % listSize > 0) page += 1;
      
      /*
      아니면 page = Math.floor((listLeng - 1) / listSize) + 1;
      이런식으로 if 문 없이 고칠 수도 있다!
      */
      return page;
    },
    paginatedData () {
      const start = this.pageNum * this.pageSize,
            end = start + this.pageSize;
      return this.communities.slice(start, end);
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
  .community-list-content{
    height: 20vh
  }
  .community-img{
    height: 15vh;
  }
  .btn-cover {
    margin-top: 1.5rem;
    text-align: center;
  }
  .btn-cover .page-btn {
    width: 5rem;
    height: 2rem;
    letter-spacing: 0.5px;
  }
  .btn-cover .page-count {
    padding: 0 1rem;
  }  

  .total_width {
    width: 70%;
  }

  .image-width {
    width: 100%;
    height: 100%;
  }
</style>