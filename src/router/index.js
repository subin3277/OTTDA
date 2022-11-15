import Vue from "vue"
import VueRouter from "vue-router"
import MainView from "../views/MainView.vue"
import SearchView from "../views/SearchView.vue"
import DetailView from "../views/DetailView.vue"
import RecoView from "../views/RecoView.vue"

Vue.use(VueRouter)

const routes = [
  {
    path: "/",
    name: "main",
    component: MainView,
  },
  {
    path: "/search",
    name: "search",
    component: SearchView,
  },
  {
    path: "/detail",
    name: "detail",
    component: DetailView,
  },
  {
    path: "/recom",
    name: "recom",
    component: RecoView,
  },
]

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
})

export default router
