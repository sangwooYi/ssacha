import '@babel/polyfill'
import 'mutationobserver-shim'
import Vue from 'vue'
import './plugins/bootstrap-vue'
import App from './App.vue'
import router from './router'
// VueCarousel
import VueCarousel from 'vue-carousel';
// vuesweetalert2
import VueSweetalert2 from 'vue-sweetalert2';

// import VideoBg from 'vue-videobg'
// Optionally install the BootstrapVue icon components plugin
Vue.config.productionTip = false

Vue.use(VueCarousel);

Vue.use(VueSweetalert2);

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
