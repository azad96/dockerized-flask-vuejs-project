import Vue from 'vue';
import VueRouter from 'vue-router';
import Home from '../components/Home.vue';
import Plates from '../components/Plates.vue';

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
  },
  {
    path: '/plate',
    name: 'Plates',
    component: Plates,
  },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

export default router;
