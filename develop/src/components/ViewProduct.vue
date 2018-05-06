<template>
  <v-container grid-list-md text-xs-left>
    <v-card class="product" width="400px">
      <v-card-media :src="product.image" height="400px">
      </v-card-media>
      <v-card-title primary-title>
        <div>
          <div class="headline">{{ product.name }}</div>
          <span>R {{ product.price }}</span>
        </div>
      </v-card-title>
      <v-card-actions>
        <v-btn flat color="blue">Add product to cart</v-btn>
      </v-card-actions>
    </v-card>
  </v-container>
</template>

<script>
import firebase from 'firebase'

import products from '../assets/products.json'

export default {
  name: 'viewproducts',
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
      product: null
    }
  },
  created () {
    if (firebase.auth().currentUser) {
      this.isLoggedIn = true
      this.currentUser = firebase.auth().currentUser.email
    }
    this.search = ''
    this.product = products.find(x => x.id === this.$route.params.id)
  }
}
</script>