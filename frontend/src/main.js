// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import '../static/css/custom.css'
import 'bootstrap/dist/css/bootstrap.css'
import BootStrapVue from 'bootstrap-vue'
// 引入element-UI框架
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import VCharts from 'v-charts'
import echarts from 'echarts'
import Vue from 'vue'
import App from './App'
import router from './router'

Vue.config.productionTip = false

Vue.use(BootStrapVue)
Vue.use(ElementUI)
Vue.use(VCharts)
Vue.use(echarts)

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
