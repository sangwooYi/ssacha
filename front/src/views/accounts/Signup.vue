<template>
  <div class="signup-bg make_font">
    <header>
      <div class="logo outer mb-4">
        <img class="logo_image" src="@/assets/logo_transparent.png">
        <hr>
        
          <!-- <p class="signup_title">회원가입</p> -->
      </div>
      <p class="outer fs-6">아래 링크에서 무료 MBTI 검사를 해보세요.</p>
      <a href="https://www.16personalities.com/ko/%EB%AC%B4%EB%A3%8C-%EC%84%B1%EA%B2%A9-%EC%9C%A0%ED%98%95-%EA%B2%80%EC%82%AC" class="outer text-decoration-none link-warning">
      | MBTI |
      </a>
    </header>
    <section class="inner" style="width: 25%">
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
      <div>
        <span>
          <form class="was-validated py-3">
            <label for="mbti-my" class="form-label signup_input outer">나의 MBTI</label>
            <select name="mbti" id="mbti-my" v-model="credentials.mbti" class="form-select select-bg" required style="background: transparent; color: white;">
                <option selected disabled value="" style="background:black;">--MBTI를 골라주세요--</option>
                <option value="INTJ" style="background:black;">INTJ</option>
                <option value="INFJ" style="background:black;">INFJ</option>
                <option value="ISTJ" style="background:black;">ISTJ</option>
                <option value="ISFJ" style="background:black;">ISFJ</option>
                <option value="INTP" style="background:black;">INTP</option>
                <option value="INFP" style="background:black;">INFP</option>
                <option value="ISTP" style="background:black;">ISTP</option>
                <option value="ISFP" style="background:black;">ISFP</option>
                <option value="ENTJ" style="background:black;">ENTJ</option>
                <option value="ENFJ" style="background:black;">ENFJ</option>
                <option value="ESTJ" style="background:black;">ESTJ</option>
                <option value="ESFJ" style="background:black;">ESFJ</option>
                <option value="ENTP" style="background:black;">ENTP</option>
                <option value="ENFP" style="background:black;">ENFP</option>
                <option value="ESTP" style="background:black;">ESTP</option>
                <option value="ESFP" style="background:black;">ESFP</option>
            </select>
          </form>
        </span>
      </div>
      <div v-if="mbtiDict">
        <span v-if="credentials.mbti">
          <div>
            <h5 class="text-center mt-3">끌리는 단어를 4개 선택해 주세요</h5>
            <div class="d-flex col-12">
              <form action="was-validated py-3">
                <div v-for="(keyword, idx) in mbtiDict[credentials.mbti]['keyword']"
                  :key="idx" class="form-check ms-3" style="display: inline-block"
                  >
                  <input type="checkbox" :id="keyword" 
                  :value="idx" class="pointer form-check-input" v-model="checkedValues"
                  >
                  <label :for="keyword" class="pointer form-check-label">{{ keyword }}</label>
                </div>
              </form>
            </div>
          </div>
        </span>
      </div>
      <div>
        <span class="py-3">
            <label for="mbti-my" class="form-label signup_input outer pt-3">나의 파트너 MBTI(선택)</label>
            <select name="mbti" id="mbti-my" v-model="credentials.mbti_partner" class="form-select select-bg" required style="background: transparent;  color: white;">
                <option selected disabled value="" style="background:black;">--MBTI를 골라주세요--</option>
                <option value="INTJ" style="background:black;">INTJ</option>
                <option value="INFJ" style="background:black;">INFJ</option>
                <option value="ISTJ" style="background:black;">ISTJ</option>
                <option value="ISFJ" style="background:black;">ISFJ</option>
                <option value="INTP" style="background:black;">INTP</option>
                <option value="INFP" style="background:black;">INFP</option>
                <option value="ISTP" style="background:black;">ISTP</option>
                <option value="ISFP" style="background:black;">ISFP</option>
                <option value="ENTJ" style="background:black;">ENTJ</option>
                <option value="ENFJ" style="background:black;">ENFJ</option>
                <option value="ESTJ" style="background:black;">ESTJ</option>
                <option value="ESFJ" style="background:black;">ESFJ</option>
                <option value="ENTP" style="background:black;">ENTP</option>
                <option value="ENFP" style="background:black;">ENFP</option>
                <option value="ESTP" style="background:black;">ESTP</option>
                <option value="ESFP" style="background:black;">ESFP</option>
            </select>
        </span>
      </div>
      
      <div class="pt-3">
        <span>
          <form class="was-validated py-3">
            <label for="validationTooltip04" class="form-label signup_input outer">비밀번호</label>
            <div class="input-group has-validation">
              <input type="password" class="form-control is-invalid" id="validationTooltip04" aria-describedby="inputGroupPrepend3 validationServerUsernameFeedback" required v-model="credentials.password" style="background: transparent; color: white;">
            </div>
          </form>
        </span>
      </div>
         
      <div>
        <span>
          <form class="was-validated py-3">
            <label for="validationTooltip05" class="form-label signup_input outer">비밀번호 확인</label>
            <div class="input-group has-validation">
              <input type="password" class="form-control is-invalid" id="validationTooltip05" aria-describedby="inputGroupPrepend3 validationServerUsernameFeedback" required v-model="credentials.passwordConfirmation" style="background: transparent; color: white;">
            </div>
          </form>
        </span>
      </div>
      <div class="outer mb-4 pt-3">
        <button type="button" class="btn btn-outline-light " @click="signup">
          회원가입
        </button>
      </div>
    </section>
    <footer>
    </footer>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Signup',
  data: function () {
    return {
      mbtiDict: null,
      checkedValues: [],
      credentials: {
        username: null,
        mbti: null,
        mbti_partner: null,
        password: null,
        passwordConfirmation: null,
        mbti_keywords: null,
      }
    }
  },
  methods: {
    signup: function () {
      if (this.credentials.password !== this.credentials.passwordConfirmation) {
          this.$swal({icon: 'error',
          title: '비밀번호 불일치',
          text: '비밀번호 일치 여부를 확인해 주세요.',
          });
      }
      else if (this.checkedValues.length != 4) {
            this.$swal({icon: 'error',
            title: '선택 갯수 오류',
            text: '키워드는 4개 선택해 주세요',
            });
      }
      else {
        axios({
          method: 'post',
          url: 'http://127.0.0.1:8000/accounts/signup/',
          data: this.credentials
        })
          .then(() => {
            // console.log(res)
            this.$router.push({ name: 'Login'})
            this.$swal('회원가입 완료', '회원가입을 축하합니다.', '확인');
            })
          .catch(err => {
            console.log(err)
            this.$swal({icon: 'error',
            title: '제출 양식 오류',
            text: '아이디가 중복 되었습니다..',
            });
          })  
      }
    },
    getKeywords: function (){
        axios({
          method: 'get',
          url: `http://127.0.0.1:8000/movies/mbti/`,
        })
          .then((res) => {
            this.mbtiDict = res.data
            })
          .catch(err => {
            console.log(err)
          })        
    },
  },
  created: function (){
    this.getKeywords()
  },
  watch: {
    checkedValues: function (){
      let temp = ""
      for (let i = 0; i < this.checkedValues.length; i++){
        temp += this.checkedValues[i]
      }
      this.credentials.mbti_keywords = temp
    }
  }
}
</script>

<style>
.logo {
  height: 120px;
}

.logo_image {
  height: 150px;
 }



.signup_input{
  /* padding: 10px; */
  cursor: pointer;
  font-size: 18px;
}

.signup-id{
    height: 29px;
    border: solid 3px white;
    outline:none;
    background: transparent;
    width: 15%;
    color: white;
}

.select-bg{
  background: black;
}

 option {
  color:white;
  background: transparent;
}

.signup_wrap{
  padding: 5px;
  margin: 20px;

}

.modal-text{
  color: black;
}

.outer{
    display: flex;
    justify-content: center;
}

.inner{
    margin: 0 auto;
}

.tail-text{
  font-size: 15px;
  padding-top: 4px;
}
.signup-bg{
    border: 0;
    padding: 0; 
    width: auto;
    background-position: center;
    background-size: cover;
    background-position: bottom; 
    background-image: linear-gradient( rgba(0, 0, 0, 0.75), rgba(0, 0, 0, 0.75) ),url("../../assets/cre_up_back.jpg");
}

</style>