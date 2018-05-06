// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import firebase from 'firebase'
import './components/firebaseInit'

import Vuetify from 'vuetify'
import VueFuse from 'vue-fuse'
import Vuex from 'vuex'

import store from './store'

Vue.use(Vuetify)
Vue.use(VueFuse)
Vue.use(Vuex)

Vue.config.productionTip = false

let app
firebase.auth().onAuthStateChanged(function (user) {
  if (!app) {
    /* eslint-disable no-new */
    app = new Vue({
      el: '#app',
      router,
      store,
      template: '<App/>',
      components: { App }
    })
  }
})

