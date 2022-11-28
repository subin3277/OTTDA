<template>
  <div>
    <h1>회원 가입</h1>
    <hr>
    <div>아이디</div>
    <input id ="id" type="text" v-model="id" >
    <div id="idstate"></div>

    <div>비밀번호</div>
    <input id ="password" type="password" v-model="password" >
    <div id="pwstate"></div>

    <div>비밀번호 확인</div>
    <input id ="passwordcheck" type="password" v-model="checkpassword" @input="checkpw">
    <div id="checkstate"></div>

    <div>이메일</div>
    <input id ="email" type="text" v-model="email" >
    <div id="emailstate"></div>

    <div>닉네임</div>
    <input id ="nickname" type="text" v-model="nickname" >
    <div id="nicknamestate"></div>

    <button @click="signup">회원가입 하기</button>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name : 'SignupView',
  data() {
    return {
      id : '',
      password : '',
      checkpassword : '',
      email : '',
      nickname : '',
    }
  },
  methods : {
    checkpw(){
      const pwcheckst = document.querySelector('#checkstate')
      if(this.password !== this.checkpassword){
        
        pwcheckst.setAttribute('style', 'color : red')
        pwcheckst.innerText = "위 비밀번호와 동일해야합니다."
      } else {
        pwcheckst.innerText = ""
      }
    },
    signup() {
      if(this.id == '') {
        const idst = document.querySelector('#idstate')
        idst.setAttribute('style', 'color : red')
        idst.innerText = "아이디를 입력해주세요"
      }
      if(this.password == '') {
        const passwordst = document.querySelector('#pwstate')
        passwordst.setAttribute('style', 'color : red')
        passwordst.innerText = "비밀번호를 입력해주세요"
      }
      if(this.checkpassword == '') {
        const pwcheckst = document.querySelector('#checkstate')
        pwcheckst.setAttribute('style', 'color : red')
        pwcheckst.innerText = "비밀번호를 확인해주세요"
      }
      if(this.email == '') {
        const emailst = document.querySelector('#emailstate')
        emailst.setAttribute('style', 'color : red')
        emailst.innerText = "이메일을 입력해주세요"
      }
      if(this.nickname == '') {
        const nicknamest = document.querySelector('#nicknamestate')
        nicknamest.setAttribute('style', 'color : red')
        nicknamest.innerText = "닉네임을 입력해주세요"
      }
      if(this.id != '' && this.password != '' && this.checkpassword != '' && this.email != '' && this.nickname != '' && this.password === this.checkpassword){
        const url = `${this.$store.state.url}`+"accounts/register/"
        // const url = "http://52.196.3.18:8000/accounts/register/"
        axios({
          url : url,
          method : 'post',
          data : {
            login_id : this.id,
            password : this.password,
            email : this.email,
            nickname : this.nickname,
          }
        })
        .then((res) => {
          if (res.data.message === "register successs"){
            alert('회원가입 되었습니다.')
            this.$router.push({name: 'signin'})
          }
        })
        .catch((err) => {
          console.log(err.response.data)
          for (var i in err.response.data) {
            if (i === 'login_id') {
              const idst2 = document.querySelector('#idstate')
              idst2.setAttribute('style', 'color : red')
              idst2.innerText = "아이디를 확인해주세요"
            }
            else if(i === 'password') {
              const pwst2 = document.querySelector('#pwstate')
              pwst2.setAttribute('style', 'color : red')
              pwst2.innerText = "비밀번호를 확인해주세요"
            }
            else if(i === 'email') {
              const emailst2 = document.querySelector('#emailstate')
              emailst2.setAttribute('style', 'color : red')
              emailst2.innerText = "이메일을 확인해주세요"
            }
            else if(i === 'nickname') {
              const nicknamest2 = document.querySelector('#nicknamestate')
              nicknamest2.setAttribute('style', 'color : red')
              nicknamest2.innerText = "닉네임을 확인해주세요"
            }
          } 
        })
      }
    }
  },
  updated(){
    //this.checkpw()
  }
}
</script>

<style scoped>
input {
  margin : 0px 10px
}

input[type=password] {
  font-family: "굴림";
}

div { 
  margin : 20px 10px
}


</style>