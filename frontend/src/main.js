import Vue from 'vue';
import App from './App.vue';
import router from './router';
import SortedTablePlugin from "vue-sorted-table";

Vue.config.productionTip = false;
Vue.use(SortedTablePlugin);

new Vue({
  router,
  render: (h) => h(App),
}).$mount('#app');
