import Vue from 'vue'
import vuetify from'./plugins/vuetify'
import App from './App.vue'
import router from './router'
// import 'material-design-icons-iconfont/dist/material-design-icons.css'
// import '@mdi/font/css/materialdesignicons.css' // Ensure you are using css-loader


import store from './store/store'
// Vue.use(Vuetify)

new Vue({
  render: h => h(App),
  router,
  store,
  vuetify,
}).$mount('#app')