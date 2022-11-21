<template>
  <div>
    <h4 style="margin-top: 50px">아이디</h4>
    <input type="text" style="width: 250px" />
    <h4 style="margin-top: 20px">비밀번호</h4>
    <input type="text" style="width: 250px; margin-bottom: 30px" />

    <br />
    <button style="margin: 10px">로그인</button>
    <br />
    <button style="margin: 5px" @click="gosignup">회원가입</button>
  </div>
</template>

<script>
export default {
  name: "SigninView",
  methods: {
    gosignup() {
      this.$router.push({ name: "signup" })
    },
  },
}
</script>

<style></style>
