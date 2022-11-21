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
    <router-view id="routerview" style="margin: 0px 30px" />

    <footer
      class="footer"
      style="background: #fdf5c7; margin-top: 50px; padding: 5px"
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
  text-decoration: none;
}

nav a.router-link-exact-active {
  color: #a3e1f4;
}

#button {
  margin: 7px;
  border-radius: 10px;
}

#button a {
  text-decoration: none;
  color: black;
}

#routerview {
  height: auto;
  min-height: 100%;
  padding-bottom: 100px;
}

footer {
  width: 100%;
  height: 100px;
  position: relative;
  transform: translate(-100%);
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
