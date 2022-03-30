import Vue from 'vue';
import VueRouter from 'vue-router';
import HomePage from "@/components/HomePage";
import AddPlate from "@/components/AddPlate";
import ListPlates from "@/components/ListPlates";

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'HomePage',
    component: HomePage,
  },
  {
    path: '/add-plate',
    name: 'AddPlate',
    component: AddPlate,
  },
  {
    path: '/list-plates',
    name: 'ListPlates',
    component: ListPlates,
  },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

export default router;
