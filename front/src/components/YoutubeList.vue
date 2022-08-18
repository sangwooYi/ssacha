<template>
  <li @click="selectVideo" class="pointer col-12">
    <div class="d-flex justify-content-start">
      <img 
        :src="video.snippet.thumbnails.default.url" 
        alt="youtube thumbnail"
        class="youtube-img"
      >
      <span class="offset-1 mt-2">
        {{ video.snippet.title | stringUnescape }}
      </span>
    </div>
    <hr>
  </li>
</template>

<script>
import _ from 'lodash'

export default {
  name: 'YoutubeList',
  props: {
    video: {
      type: Object,
      required: true,
    }
  },
  methods: {
    selectVideo: function () {
      this.$emit('select-video', this.video)
    }
  },
  filters: {
    stringUnescape: function (text) {
      return _.unescape(text)
    }
  }

}
</script>

<style>
  .youtube-img{
    height: 15vh;
  }
</style>