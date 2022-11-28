<template>
  <div>
    <h4 style="margin-top: 50px">아이디</h4>
    <input type="text" style="width: 250px" v-model="id"/>
    <h4 style="margin-top: 20px">비밀번호</h4>
    <input type="password" style="width: 250px; margin-bottom: 30px; color:black" v-model="password"/>

    <br />
    <button style="margin: 10px" @click="login" @keyup.enter="login">로그인</button>
    <br />
    <button style="margin: 5px" @click="gosignup">회원가입</button>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: "SigninView",
  data() {
    return {
      id : '',
      password : ''
    }
  },
  methods: {
    gosignup() {
      this.$router.push({ name: "signup" })
    },
    login(){
      const url = `${this.$store.state.url}`+"accounts/auth/"
      // const url = "http://52.196.3.18:8000/accounts/auth/"
      if(this.id == ""){
        alert('아이디를 입력해주세요')
      }
      else if(this.password == "") {
        alert('비밀번호를 입력해주세요')
      }
      else {
        const data = {
            login_id : this.id,
            password : this.password
          }
        axios({
          url : url,
          method : 'POST',
          data : data
        })
        .then((res) =>{
          console.log(res.data)
          if (res.data.message === "login success"){
            alert('로그인 되었습니다.')
            const store = {
              id : res.data.user.id,
              nickname : res.data.user.nickname,
              token : res.data.token.access
            }
            this.$store.dispatch('login', store)
            this.$router.push({name : 'main'})
          }
          
        })
        .catch((err)=> {
          alert('아이디와 비밀번호를 확인해주세요.')
          console.log(err)
        })
      }
    }
  },
}
</script>

<style>
input[type=password] {
  font-family: "굴림";
}
</style>
