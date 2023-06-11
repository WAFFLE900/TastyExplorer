import Vue from "vue";
import VueRouter from "vue-router";
import Bricks from "../components/BricksTest.vue";
import Login from "../components/Login.vue";
import Register from "../components/Register.vue";
import HomePage from "../components/Homepage.vue";
import Login_2 from "../components/Login_2.vue";
import Register_2 from "../components/Register_2.vue";
import Homepage_2 from "../components/Homepage_2.vue";
import following from "../components/following.vue";

Vue.use(VueRouter);


const routes = [
  //測試連線
  {
    path: "/bricks",
    name: "BricksTest",
    component: Bricks,
  },
  {
    path: "/register",
    name: "Register",
    component: Register,
  },
  {
    path: "/login",
    name: "Login",
    component: Login,
  },
  {
    path: "/homepage",
    name: "Homepage",
    component: HomePage,
  },
  {
    path: "/login_2",
    name: "Login_2",
    component: Login_2,
  },
  {
    path: "/register_2",
    name: "Register_2",
    component: Register_2,
  },
  {
    path: "/homepage_2",
    name: "Homapage_2",
    component: Homepage_2,
  },
  {
    path: "/following",
    name: "following",
    component: following,
  },
];


const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});


export default router;

