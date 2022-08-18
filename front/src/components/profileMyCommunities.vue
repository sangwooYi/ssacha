<template>
  <div>
    <div
      v-for="community in paginatedData"
      :key="community.id"
      class="pointer"
      @click="moveToCommunity(community)"
    >
    <div class="d-flex justify-content-between">
      <p class="offset-1">{{ community.title }}</p>
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
  name: 'profileMyCommunities',
  props: {
    communities: {
      type: Array,
    },
    pageSize: {
      type: Number,
      required: false,
      default: 10
    }        
  },
  data: function (){
    return {
      pageNum: 0,
    }
  },
  methods: {
    moveToCommunity: function (community){
      this.$router.push({ name: 'CommunityDetail', params: { community_pk: `${community.id}` }})
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
      let listLeng = this.communities.length,
          listSize = this.pageSize,
          page = Math.floor(listLeng / listSize);
      if (listLeng % listSize > 0) page += 1;
      
      return page;
    },
    paginatedData: function () {
      const start = this.pageNum * this.pageSize,
            end = start + this.pageSize;
      return this.communities.slice(start, end);
    }
  },     
}
</script>

<style>

</style>