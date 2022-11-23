import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    user : {},
  },
  getters: {
  },
  mutations: {
    LOGIN(state, data){
      state.user = data
    }
  },
  actions: {
    login(context, data){
      context.commit('LOGIN',data)
    }
  },
  modules: {
  }
})
