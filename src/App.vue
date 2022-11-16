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
      <span class="flex-direction">
        <button id="button">Sign In</button>
        <button id="button">Sign Up</button>
      </span>
    </div>

    <nav class="container">
      <div class="row">
        <router-link to="/search" class="col">무엇으로 웃지</router-link>
        <router-link to="/recom" class="col">어디서 웃지</router-link>
        <router-link to="/article" class="col">누구랑 웃지</router-link>
        <router-link to="/review" class="col">나는 이걸로 웃지</router-link>
      </div>
    </nav>
    <router-view />
  </div>
</template>

<style>
#app {
  /* font-family: Avenir, Helvetica, Arial, sans-serif; */
  font-family: cafe;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: black;
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
}

nav a.router-link-exact-active {
  color: #a3e1f4;
}

#button {
  margin: 7px;
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
