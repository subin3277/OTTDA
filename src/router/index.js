import Vue from "vue"
import VueRouter from "vue-router"
import MainView from "../views/MainView.vue"
import SearchView from "../views/SearchView.vue"
import DetailView from "../views/DetailView.vue"
import RecoView from "../views/RecoView.vue"
import SigninView from "../views/SigninView.vue"
import SignupView from "../views/SignupView.vue"
import CreateArticleView from "../views/CreateArticleView.vue"
import ArticleView from "../views/ArticleView.vue"
import ArticleDetailView from "../views/ArticleDetailView.vue"

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
  {
    path: "/signin",
    name: "signin",
    component: SigninView,
  },
  {
    path: "/signup",
    name: "signup",
    component: SignupView,
  },
  {
    path: "/article/create",
    name: "createarticle",
    component: CreateArticleView,
  },
  {
    path: "/article",
    name: "article",
    component: ArticleView,
  },
  {
    path: "/article/detail",
    name: "articledetail",
    component: ArticleDetailView,
  },
]
  
const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
})

export default router
