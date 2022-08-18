<template>
  <div id="app">
    <!-- <img src="@/assets/background.png" alt="background" class="background-img"> -->
    <!-- <font-awesome-icon icon="user-secret" /> -->
    <nav class="navbar navbar-expand-lg navbar-dark bg-transparent fw-bold fs-6 make_font" style="border-bottom: solid white 0.5px;">
      <div class="container-fluid">  
        <span v-if="isLogin">
          <router-link :to="{ name: 'Recommend' }" class="navbar-brand">
            <img src="@/assets/logo_transparent.png" alt="" width="100" height="80">
          </router-link>
        </span>
        <span v-else>
          <router-link :to="{ name: 'Intro' }" class="navbar-brand">
            <img src="@/assets/logo_transparent.png" alt="" width="100" height="80">
          </router-link>
        </span>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse d-flex justify-content-between mt-1" id="navbarSupportedContent">
          <div class="d-flex justify-content-between">
            <ul class="navbar-nav me-auto mb-2 mb-lg-0 fs-5">
              <div v-if="isLogin" class="d-flex">
                <div class="d-flex align-items-center">
                  <li class="nav-item me-3">
                    <router-link :to="{ name: 'Recommend' }" class="nav-link active" style="color: beige">Recommend</router-link>
                  </li>
                  <li class="nav-item me-3">
                    <router-link :to="{ name: 'Community' }" class="nav-link active" style="color: beige">Community</router-link>
                  </li> 
                </div>
              </div>
              <div v-if="isLogin" class="d-flex">
                <div class="d-flex align-items-center">
                  <li class="nav-item me-3">
                    <router-link :to="{ name: 'Mbti' }" class="nav-link active" style="color: beige">MBTI</router-link>
                  </li>                     
                  <li class="nav-item me-3">
                    <router-link :to="{ name: 'Profile' }" class="nav-link active" style="color: beige">Profile</router-link>
                  </li>
                  <li class="nav-item">
                    <router-link @click.native="logout" to="#" class="nav-link active" style="color: beige">Logout</router-link>
                  </li>                       
                </div>
              </div>
              <div v-else class="d-flex">
              <li class="nav-item me-3">
                <router-link :to="{ name: 'Signup' }" class="nav-link active" style="color: beige">Signup</router-link>
              </li>
              <li class="nav-item me-3">
                <router-link :to="{ name: 'Login' }" class="nav-link active" style="color: beige">Login</router-link>
              </li>            
              <li class="nav-item me-3">
                <router-link :to="{ name: 'Mbti' }" class="nav-link active" style="color: beige">MBTI</router-link>
              </li>                 
              </div>
            </ul>
          </div>
          <form class="d-flex make_font">
            <input class="form-control me-2" type="search" placeholder="Search movie" aria-label="Search"  @keyup.enter="moveToSearch"  v-model="movieTitleInput">
            <button class="btn btn-outline-light" type="submit"  @click="moveToSearch">Search</button>
          </form>
        </div>
      </div>
    </nav>

    <router-view @login="isLogin=true"/>
  </div>

</template>

<script>
export default {
  name: 'App',
  data: function () {
    return {
      isLogin: false,
      movieTitleInput: null,      
      user: null,
    }
  },
  components: {
  },
  methods: {
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },    
    logout: function () {
      this.isLogin = false
      localStorage.removeItem('jwt')
      this.$router.push({ name: 'Login' })
      
    },
    moveToSearch: function (){
      if (!this.isLogin) {
        alert('로그인을 해주세요')
      } else {
        this.$router.push({ name: 'RecommendSearch', params: {keyword: `${this.movieTitleInput}`}})
      }

    },     
  },
  created: function () {
    const token = localStorage.getItem('jwt')

    if (token) {
      this.isLogin = true
    }
  }
}

</script>


<style>
@import url('https://fonts.googleapis.com/css2?family=Nanum+Myeongjo&display=swap');
#app {
  font-family: 'Nanum Myeongjo', serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: white;
  background-color: black;
  width: auto;
  height: auto;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
li{
  list-style-type: none;
}
.backnav{
  position: absolute;
  display: block;
  width: 100%;
  z-index: 1;
}
button{
  margin: 5px;
}
.footer{
  position: fixed;
  bottom: 0px;
  width: 100%;
}
</style>