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
import ScrollView from "../views/ScrollView.vue"
import ReviewView from "../views/ReviewView.vue"
import ReviewDetailView from "../views/ReviewDetailView.vue"
import CreateReviewView from "../views/CreateReview.vue"

Vue.use(VueRouter)

const routes = [
  {
    path: "/scroll",
    name: "scroll",
    component: ScrollView,
  },
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
    path: "/article/detail",
    name: "articledetail",
    component: ArticleDetailView,
  },
  {
    path: "/article",
    name: "article",
    component: ArticleView,
  },
  {
    path: "/reviews/create",
    name: "createreview",
    component: CreateReviewView,
  },
  {
    path: "/reviews/detail",
    name: "reviewdetail",
    component: ReviewDetailView,
  },
  {
    path: "/review",
    name: "review",
    component: ReviewView,
  },

]

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
})

export default router
