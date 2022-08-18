<template>
  <div>
  <div class="backgroundplay d-flex align-items-center">
    <video width="100%" height="auto" autoplay playsinline loop muted>  
      <source src="@/assets/Space2.mp4" type="video/mp4">
    </video>    
  <div class="display-absolute d-flex flex-column justify-content-between">
    <div class="intro-text offset-2 d-flex flex-column justify-content-start align-items-start">
      <p>사람의 과거를 통해서 이해 될 수 있습니다.</p>
      <p class="mt-1">그러나 우리는 앞으로 나아가야 합니다. </p>
    </div>
    <div class="offset-2 d-flex flex-column justify-content-start intro-box">
      <label for="intro" class="intro d-flex align-items-center">What do you think who you are?</label>
      <input 
        type="text" id="intro" 
        class="intro" style="border-color: white; font-size: 30px" 
        @keyup.enter="moveToIntroduce">
    </div>          
  </div>
  </div>
    <footer class="footer">
      <p class="text-center make_font">created by 이상우 임지환</p>
    </footer>    
  </div>
</template>


<script>
export default {
  name: 'Intro',
  methods: {
    moveToIntroduce: function(){
      this.$router.push({ name: 'Introduce' })
    }
  }
}
</script>

<style>
  .backgroundplay {
    padding:0px, 0px, 0px, 0px; 
    margin:0px, 0px, 0px, 0px; 
    overflow:hidden; 
    background-color:#000;
    position: relative;
  }
  .display-absolute {
    position: absolute;
    display: inline;
    height: 70vh;
  }
  .display-relative {
    position: relative;
  }
  .intro{
    font-size: 22px;
    font-family: 'Nanum Myeongjo', serif;
    padding-left: 2%;
    width: 50vh;
    height: 10vh;
    color:white;
    border-left-width: 0px;
    border-right-width: 0px;
    border-top-width: 0px;
    border-bottom-width: 3px;
    background-color: transparent;
  }
  .intro-box{
    height: 40vh;
  }
  .intro-text{
    width: 80vh;
    font-size: 30px;
    font-family: 'Nanum Myeongjo', serif;
    color: white;
    border-color: transparent;
    background-color: transparent;
  }
  .vmax{
    height: 100vmax;
    width: 100vmax;
  }
</style>