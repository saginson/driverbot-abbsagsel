import Vue from 'vue'
import Vuex from 'vuex'
// import axios from "axios";
Vue.use(Vuex)
const state = {
  loadingStatus:"not loading"
}
const mutations = {
    Loading_Status (state,Status) {
        state.loadingStatus = Status;
      },

}
const actions = {
      LoadingStatus: ({ commit },Status) => {

        commit('Loading_Status',Status);
      },

}
const getters = {
  loadingStatus: state => state.loadingStatus,
}
export default new Vuex.Store({
  state,
  getters,
  actions,
  mutations
})