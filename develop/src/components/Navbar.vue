<template>
  <v-app id="inspire" dark>
    <v-navigation-drawer
      fixed
      :clipped="$vuetify.breakpoint.lgAndUp"
      app
      v-model="drawer"
    >
    <v-toolbar flat class="transparent">
        <v-list class="pa-0">
          <v-list-tile avatar v-if="isLoggedIn">
              <v-list-tile-avatar>
                <img src="https://randomuser.me/api/portraits/women/15.jpg" >
              </v-list-tile-avatar>
              <v-list-tile-content>
                <v-list-tile-title>{{currentUser}}</v-list-tile-title>
              </v-list-tile-content>
          </v-list-tile>
        </v-list>
      </v-toolbar>
      <v-list dense>
        <template v-for="item in menu_items">
          <v-layout
            row
            v-if="item.heading"
            align-center
            :key="item.heading"
          >
          </v-layout>
          <v-list-tile :to="item.url" :key="item.text">
            <v-list-tile-action :to="item.url">
              <v-badge v-if="item.badge">
                  <span slot="badge">{{item.badge}}</span>
                  <v-icon>{{ item.icon }}</v-icon>
              </v-badge>
              <v-icon v-else>{{ item.icon }}</v-icon>
            </v-list-tile-action>
            <v-list-tile-content>
              <v-list-tile-title>
                  {{ item.text }}
              </v-list-tile-title>
            </v-list-tile-content>
          </v-list-tile>
        </template>
      </v-list>
    </v-navigation-drawer>
    <v-toolbar
      color="blue darken-3"
      dark
      app
      :clipped-left="$vuetify.breakpoint.lgAndUp"
      fixed
    >
      <v-toolbar-title style="width: 300px" class="ml-0 pl-3">
        <v-toolbar-side-icon @click.stop="drawer = !drawer"></v-toolbar-side-icon>
        <span class="hidden-sm-and-down">ComX</span>
      </v-toolbar-title>
      <v-text-field
        v-model="search"
        flat
        solo-inverted
        prepend-icon="search"
        label="Search"
        class="hidden-sm-and-down"
      ></v-text-field>
      <v-spacer></v-spacer>
      <v-btn icon>
        <v-icon>notifications</v-icon>
      </v-btn>
      <v-btn icon large>
        <v-avatar size="32px" tile>
          <img
            src="https://vuetifyjs.com/static/doc-images/logo.svg"
            alt="Vuetify"
          >
        </v-avatar>
      </v-btn>
    </v-toolbar>
    <v-content>
      <v-container fluid>
        <v-layout justify-center align-center>
          <router-view v-if="search === ''"></router-view>
          <v-container grid-list-md text-xs-left v-else>
          <v-progress-circular indeterminate color="primary" :size="70" v-if="loading == true"></v-progress-circular>
          <v-layout row wrap> 
            <v-flex xs4 v-for="product in searchResulsts" :key="product.id">
              <v-card class="product" width="300">
                <v-card-media :src="product.image" height="300px">
                </v-card-media>
                <v-card-title primary-title>
                  <div>
                    <div class="headline">{{ product.name }}</div>
                    <span>R {{ product.price }}</span>
                  </div>
                </v-card-title>
                <v-card-actions>
                  <v-btn flat color="blue"  v-on:click="search = ''" :to="{ name: 'viewproducts', params: { id: product.id }}">View Product</v-btn>
                </v-card-actions>
              </v-card>
            </v-flex>
          </v-layout>
        </v-container>
        </v-layout>
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
import firebase from 'firebase'

import products from '../assets/products.json'
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'navbar',
  computed: mapGetters({
    cart: 'cartProducts'
  }),
  data () {
    return {
      dialog: false,
      drawer: null,
      menu_items: [
        {icon: 'exit_to_app', text: 'Logout', url: '/logout/'},
        {icon: 'home', text: 'Home', url: '/'},
        {icon: 'shopping_cart', text: 'Shopping Cart', url: '/cart', badge: 0},
        {icon: 'history', text: 'Purchase history', url: '/history'},
        {icon: 'settings', text: 'Settings', url: '/settings'},
        {icon: 'chat_bubble', text: 'Send feedback', url: '/feedback'},
        {icon: 'help', text: 'Help', url: '/help'}
      ],
      isLoggedIn: false,
      currentUser: false,
      search: '',
      options: {
        keys: [
          "id",
          "name",
          "price",
          "tag"
        ]
      },
      products: [],
      searchResulsts: [],
      loading: false
    }
  },
  created () {
    if (firebase.auth().currentUser) {
      this.isLoggedIn = true
      this.currentUser = firebase.auth().currentUser.email
    }
    this.products = products
    this.loading = false
    this.debouncedGetAnswer = _.debounce(this.getAnswer, 500)

    menu_items: [
        {icon: 'exit_to_app', text: 'Logout', url: '/logout/'},
        {icon: 'home', text: 'Home', url: '/'},
        {icon: 'shopping_cart', text: 'Shopping Cart', url: '/cart', badge: this.cart},
        {icon: 'history', text: 'Purchase history', url: '/history'},
        {icon: 'settings', text: 'Settings', url: '/settings'},
        {icon: 'chat_bubble', text: 'Send feedback', url: '/feedback'},
        {icon: 'help', text: 'Help', url: '/help'}
      ]
  },
  watch: {
    // whenever question changes, this function will run
    search: function (val) {
      this.loading = true
      this.debouncedGetAnswer()
    }
  },
  methods: {
    getAnswer:  function () {
      this.$search(this.search, this.products, this.options).then(results => {
        this.searchResulsts = results
        this.loading = false
      })
    }
  }
}
</script>

<style scoped>
</style>
