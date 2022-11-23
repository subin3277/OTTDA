import Vue from 'vue'
import Vuex from 'vuex'
//npm install vuex-persistedstate
import createPersistedState from 'vuex-persistedstate'
Vue.use(Vuex)

export default new Vuex.Store({
  plugins: [
    createPersistedState(),
  ],
  state: {
    user : {},
  },
  getters: {
  },
  mutations: {
    LOGIN(state, data){
      state.user = data
    },
    LOGOUT(state){
      state.user = {}
    }
  },
  actions: {
    login(context, data){
      context.commit('LOGIN',data)
    },
    logout(context) {
      context.commit('LOGOUT')
    }
  },
  modules: {
  }
})
