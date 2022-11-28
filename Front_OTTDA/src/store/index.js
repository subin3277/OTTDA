import Vue from "vue"
import Vuex from "vuex"
//npm install vuex-persistedstate
import createPersistedState from "vuex-persistedstate"
Vue.use(Vuex)

export default new Vuex.Store({
  plugins: [createPersistedState()],
  state: {
    user: {},
    url: "",
  },
  getters: {},
  mutations: {
    LOGIN(state, data) {
      state.user = data
    },
    LOGOUT(state) {
      state.user = {}
    },
    URL(state) {
      // state.url = "http://52.196.3.18:8000/"
      state.url = "http://127.0.0.1:8000/" //로컬
      // state.url = "http://13.125.74.7:8000/" //서버
    },
  },
  actions: {
    login(context, data) {
      context.commit("LOGIN", data)
    },
    logout(context) {
      context.commit("LOGOUT")
    },
    change(context) {
      context.commit("URL")
    },
  },
  modules: {},
})
