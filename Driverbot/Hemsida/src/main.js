import Vue from 'vue'
import vuetify from'./plugins/vuetify'
import App from './App.vue'
import router from './router'
import VueHotkey from 'v-hotkey'
import 'material-design-icons-iconfont/dist/material-design-icons.css'
// import '@mdi/font/css/materialdesignicons.css' // Ensure you are using css-loader
import Vuetify from 'vuetify/lib'


import store from './store/store'
// Vue.use(Vuetify)
Vue.use(VueHotkey, {
  'a': 65 // the key code of character 'a'
})

Vue.use(Vuetify)

new Vue({
  render: h => h(App),
  router,
  store,
  vuetify,
  VueHotkey,
}).$mount('#app')
