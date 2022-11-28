<template>
  <div id="app">
    <div id="logo">
      <span style="visibility: hidden">
        <button id="button">Sign In</button>
        <button id="button">Sign Up</button>
      </span>
      <router-link to="/">
        <img src="../src/assets/logo_main.png" alt="logo" width="80px" />
      </router-link>
      <span v-if="$store.state.user.token" style="margin-right:10px">
        {{$store.state.user.nickname}}님 안녕하세요
        <button id="button" @click="logout">
          로그아웃
        </button>
      </span>
      <span v-else class="flex-direction">
        <button id="button">
          <router-link to="/signin">Sign In</router-link>
        </button>
        <button id="button" to="/signup">
          <router-link to="/signup">Sign Up</router-link>
        </button>
      </span>
    </div>

    <nav class="container">
      <div class="row">
        <router-link to="/search" class="col">무엇으로 웃지?</router-link>
        <router-link to="/recom" class="col">어디서 웃지?</router-link>
        <router-link to="/article" class="col">누구랑 웃지?</router-link>
        <router-link to="/review" class="col">나는 이걸로 웃지?</router-link>
      </div>
    </nav>
    <div id="router">
      <router-view id="routerview" />
    </div>
    

    <footer
      class="footer"
      style="background: #fdf5c7; margin-top: 50px; padding: 5px; height:100px"
    >
      SSAFY 8th
      <br />
      SEOUL_01
      <br />
      김수빈 subin3277@gmail.com
      <br />
      박세희 seheep1217@gmail.com
    </footer>
  </div>
</template>

<script>
export default {
  name: 'App',
  methods : {
    logout() {
      this.$store.dispatch('logout')
      this.$router.push({name : 'main'})
    }
  }
}
</script>

<style>
#app {
  /* font-family: Avenir, Helvetica, Arial, sans-serif; */
  font-family: cafe;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: black;
  min-height: 100%;
  position: relative;
  padding-bottom : 0px;
}

#logo {
  height: 70px;
  background: #a3e1f4;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

nav {
  padding: 30px;
}

nav a {
  /* font-weight: bold; */
  color: #2c3e50;
  font-size: 20px;
  text-decoration: none;
}

nav a.router-link-exact-active {
  color: #a3e1f4 !important;
}

#button {
  margin: 7px;
  border-radius: 10px;
}

#button a {
  text-decoration: none;
  color: black;
}

#router {
  display: flex;
  justify-content: center;
}
#routerview {
  height: auto;
  min-height: 70vh;
  padding-bottom: 100px;
  width: 70%;
  
}

footer {
  font-family: cafeair;
  width: 100%;
  height: 130px;
  position: relative;
  padding: 5px;
  bottom : 0;
}

@font-face {
  font-family: "cafe";
  src: url("../src/assets/fonts/Cafe24Ssurround.ttf");
}

@font-face {
  font-family: "cafeair";
  src: url("../src/assets/fonts/Cafe24SsurroundAir.ttf");
}
</style>
