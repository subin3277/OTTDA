import Vue from "vue"
import App from "./App.vue"
import store from "./store"
import router from "./router"

// import VueCarousel from 'vue-carousel' // npm install vue-carousel
// Vue.use(VueCarousel)

import BootstrapVue from "bootstrap-vue"
import "bootstrap/dist/css/bootstrap.min.css"
import "bootstrap-vue/dist/bootstrap-vue.css"

Vue.use(BootstrapVue)

Vue.config.productionTip = false

new Vue({
  store,
  router,
  render: (h) => h(App),
}).$mount("#app")
