<template>
  <v-container grid-list-md text-xs-left>
    <v-layout row wrap> 
      <v-flex xs4 v-for="product in products" :key="product.id">
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
            <v-btn flat color="blue" :to="{ name: 'viewproducts', params: { id: product.id }}">View Product</v-btn>
          </v-card-actions>
        </v-card>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import firebase from 'firebase'

import gpus from '../assets/gpus.json'
import cpus from '../assets/cpus.json'
import harddrives from '../assets/harddrives.json'
import motherboards from '../assets/motherboards.json'
import powersupplies from '../assets/powersupplies.json'

export default {
  name: 'home',
  data () {
    return {
      loading: true,
      menu_items: [
        {icon: 'exit_to_app', text: 'Logout', url: '/logout/'},
        {icon: 'home', text: 'Home', url: '/'},
        {icon: 'shopping_cart', text: 'Shopping Cart', url: '/cart'},
        {icon: 'history', text: 'Purchase history', url: '/history'},
        {icon: 'settings', text: 'Settings', url: '/settings'},
        {icon: 'chat_bubble', text: 'Send feedback', url: '/feedback'},
        {icon: 'help', text: 'Help', url: '/help'}
      ],
      isLoggedIn: false,
      currentUser: false,
      products: []
    }
  },
  created () {
    if (firebase.auth().currentUser) {
      this.isLoggedIn = true
      this.currentUser = firebase.auth().currentUser.email
    }
    if (this.$route.params.name == 'gpu') {
        this.products = gpus
    }
    else if (this.$route.params.name == 'cpu') {
        this.products = cpus
    }
    else if (this.$route.params.name == 'harddrives') {
        this.products = harddrives
    }
    else if (this.$route.params.name == 'motherboard') {
        this.products = motherboards
    }
    else if (this.$route.params.name == 'powersupply') {
        this.products = powersupplies
    }
  }
}
</script>

<style scoped>
  .category {
    margin: 10px;
  }
</style>
