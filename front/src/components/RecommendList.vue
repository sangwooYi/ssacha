<template>
  <div class="col-12">
    <carousel :perPage="8"
      :paginationPadding="4"
      :paginationSize="12"
      paginationColor="#a0a0a0"
      paginationActiveColor="#FFCD28"
    >
      <slide
        v-for="movie in movies"
        :key="movie.id"
      >
      <recommend-list-item :movie="movie"></recommend-list-item>
      </slide>
    </carousel> 
  </div>
</template>

<script>
import { Carousel, Slide } from 'vue-carousel';
import RecommendListItem from './RecommendListItem.vue'

export default {
  name: 'RecommendList',
  props: {
    movies: {
      type: Array,
    }
  },
  data: function (){
    return {
    }
  },
  components: {
    RecommendListItem,
    Carousel,
    Slide
  },
}
</script>

<style>

</style>