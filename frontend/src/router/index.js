import Vue from 'vue';
import VueRouter from 'vue-router';
import HomeComponent from "@/components/HomeComponent";
import AddPlateComponent from "@/components/AddPlateComponent";
import ListPlatesComponent from "@/components/ListPlatesComponent";

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'HomeComponent',
    component: HomeComponent,
  },
  {
    path: '/add-plate',
    name: 'AddPlateComponent',
    component: AddPlateComponent,
  },
  {
    path: '/list-plates',
    name: 'ListPlatesComponent',
    component: ListPlatesComponent,
  },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

export default router;
