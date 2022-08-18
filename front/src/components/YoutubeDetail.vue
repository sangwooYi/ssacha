<template>
  <div v-if="video" class="youtube d-flex align-items-start">
    <iframe :src="videoUrl" frameborder="0" style="width:60vh; height:35vh;"></iframe>
    <button type="button" class="btn-close bg-light opacity-100 btn-lg" aria-label="Close" @click="closeYoutube"></button>
  </div>
</template>

<script>
export default {
  name: 'VideoDetail',
  props: {
    video: {
      type: Object,
    }
  },
  methods: {
    closeYoutube: function (){
      this.$emit('close-youtube')
    }
  },
  computed: {
    videoUrl: function () {
      const videoId = this.video.id.videoId
      return `https://www.youtube.com/embed/${videoId}`
    }
  }
}
</script>

<style>
  .youtube{
    position: absolute;
    z-index: 5;
  }
</style>