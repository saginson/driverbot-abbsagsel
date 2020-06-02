import Vue from "vue";
import Router from "vue-router";
// import home from '@/components/home'
// import Secure from '@/components/secure'

Vue.use(Router);

let router = new Router({
  mode: "history",
  base: process.env.BASE_URL,
  routes: [
    {
      path: "/",
      name: "Home",
      component: () => import("./views/Home.vue")
    },
    {
      path: "/help",
      name: "help",
      component: () => import("./views/Help.vue")
    }
  ]
});

export default router;