<template>
  <div>    
    <div class="backgroundplay d-flex align-items-center">
      <video width="100%" height="auto" autoplay playsinline loop muted>
        <source src="@/assets/Space2.mp4" type="video/mp4">
      </video>    
      <div class="introduce-page offset-2">
        <marquee behavior="slide" direction="up" loop="1" scrollamount="40">
          <p>왜 넷플릭스 영화 고를 때 오래 걸릴까..?</p>
          <p>왜 나의 여자친구와 영화 취향이 안 맞을까...</p>
          <p>직장상사랑 어떤 영화를 봐야할까요?</p>
          <p>나를 위한 영화추천이 왜 마음에 안 맞을까...</p>
          <p>그 영화 이름이 무엇이더라...</p>
          <p>지구과학에 대한 영화는 없을까?</p>
          <p>짝사랑하는 사람과 볼 영화 추천 좀요!</p>
          <p>제일 멋있는 풍경이 나오는 영화는 무엇일까?</p>
          <p>복선이 제일 많은 영화는 무엇일까?</p>
          <p>내 친구는 무슨영화를 좋아할까?</p>
          <p>거북이는 토끼영화를 좋아할까?</p>
          <p>내 성격과 정반대인 사람은 무슨 영화를 좋아할까? </p>
          <p>우리 엄마는 무슨 영화를 좋아할까? </p>
          <p>비오는 무슨 영화를 좋아할까? 카운팅 스타~</p>
          <p>나는 무슨 기준으로 영화를 좋아하는 걸까?</p>
          <p>그 영화를 보고 싶게 만드려면 어떤 포인트가 중요할 까?</p>
          <p>특정 기분에 어울리는 영화 장르가 혹시 있을까?</p>
          <p>불같은 사람들은 무슨 영화를 좋아할까?</p>
          <p>내 나이에 맞는 영화는 무엇일까?</p>
          <br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>
          <img class="logo_image" src="@/assets/logo_transparent.png">
          <p>이런 고민들을 했을 당신을 위해..</p>
          <div class="d-flex" style="padding-bottom: 40%">
            <button class="btn btn-link text-light text-decoration-none btn-lg"
              @click="moveToSignup">Signup</button>
            <button class="btn btn-link text-light text-decoration-none btn-lg"
              @click="moveToLogin">Login</button>
          </div>
        </marquee>
      </div>
    </div>
  </div>
</template> 

<script>
export default {
  name: 'Introduce',
  methods: {
    moveToSignup: function (){
      this.$router.push({ name: 'Signup' })
    },
    moveToLogin: function (){
      this.$router.push({ name: 'Login' })
    }
  }
}
</script>

<style scoped>
  .introduce-page{
    position: absolute;
    width: 100vh;
    color: white;
    font-weight: bold;
    font-size: 30px;
  }
  p{
    margin-bottom: 50px;
  }
  a {
    display: inline-block;
    width: 50px;
    text-decoration: none;
  }
  nav, .scroll-container {
    display: block;
    margin: 0 auto;
    text-align: center;
  }
  nav {
    width: 339px;
    padding: 5px;
    border: 1px solid black;
  }
  .scroll-container {
    width: 350px;
    height: 200px;
    overflow-y: scroll;
    scroll-behavior: smooth;
  }
  .scroll-page {
    display: flex;
    align-items: center;
    justify-content: center;
    height: 100%;
    font-size: 5em;
  }
  
  .logo_image {
  height: 150px;
  }

  marquee {
    padding-bottom: 2500px;
  }

</style>