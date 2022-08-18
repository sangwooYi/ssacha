<template>
  <div class="signup-bg">
    <header>
      <div class="logo outer mb-4">
        <div>
          <img class="logo_image" src="@/assets/logo_transparent.png">
        </div>
      </div>
    </header>
    <section class="inner" style="width: 20%">
      <div>
        <span>
          <form class="was-validated py-3" >
            <label for="validationTooltip03" class="form-label signup_input outer">아이디</label>
            <div class="input-group has-validation">
              <input type="text" class="form-control is-invalid" id="validationTooltip03" aria-describedby="inputGroupPrepend3 validationServerUsernameFeedback" required v-model="credentials.username" style="background: transparent; color: white;">
            </div>
          </form>
        </span>
      </div> 
      <div class="pt-3">
        <span>
          <form class="was-validated py-3">
            <label for="validationTooltip04" class="form-label signup_input outer">비밀번호</label>
            <div class="input-group has-validation">
              <input type="password" class="form-control is-invalid" 
                id="validationTooltip04" aria-describedby="inputGroupPrepend3 validationServerUsernameFeedback" 
                required v-model="credentials.password" style="background: transparent; color: white;"
                @keyup.enter="login">
            </div>
          </form>
        </span>
      </div>

      <div class="outer mb-4 pt-3">
        <button type="button" class="btn btn-outline-light" @click="login">로그인</button>
      </div>
    </section>
    <br><br><br><br><br><br><br><br>
    <br><br><br><br><br><br><br><br>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Login',
  data: function () {
    return {
      credentials: {
        username: null,
        password: null,
      }
    }
  },
  methods: {
    login: function () {
      axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/accounts/api-token-auth/',
        data: this.credentials,
      })
        .then(res => {
          // console.log(res)
          localStorage.setItem('jwt', res.data.token)
          this.$emit('login')
          this.$router.push({ name: 'Recommend' })
        })
        .catch(err => {
          console.log(err)
          this.$swal({icon: 'error',
          title: 'Oops...',
          text: '아이디 혹은 비밀번호가 틀렸습니다.',
          });
        })
    }
  }
}
</script>

<style>
  .outer{
    display: flex;
    justify-content: center;
  }

  .inner{
    margin: 0 auto;
  }
</style>