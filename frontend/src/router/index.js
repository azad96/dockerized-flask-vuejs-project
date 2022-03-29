import Vue from 'vue';
import VueRouter from 'vue-router';
import Home from '../components/Home.vue';
import Plate from '../components/Plate.vue';

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
  },
  {
    path: '/plate',
    name: 'Plate',
    component: Plate,
  },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

export default router;
