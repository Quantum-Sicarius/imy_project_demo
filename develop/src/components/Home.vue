<template>
  <v-container grid-list-md text-xs-center>
    <v-layout row wrap>    
      <v-flex xs4>
        <v-card class="category" width="300">
          <v-card-media src="/static/NV-vs-AMD-640x353.jpg" height="200px">
          </v-card-media>
          <v-card-title primary-title>
            <div>
              <h3 class="headline mb-0">Graphics cards</h3>
              <div>View Graphics cards sold by us.</div>
            </div>
          </v-card-title>
          <v-card-actions>
            <v-btn flat color="blue" :to="{ name: 'tag', params: { name: 'gpu' }}">View All</v-btn>
          </v-card-actions>
        </v-card>
      </v-flex>
      <v-flex xs4>
        <v-card class="category" width="300">
          <v-card-media src="/static/AMD_vs_Intel_Challenge.jpg" height="200px">
          </v-card-media>
          <v-card-title primary-title>
            <div>
              <h3 class="headline mb-0">CPUs</h3>
              <div> CPU (Processors) </div>
            </div>
          </v-card-title>
          <v-card-actions>
            <v-btn flat color="blue" :to="{ name: 'tag', params: { name: 'cpu' }}">View All</v-btn>
          </v-card-actions>
        </v-card>
      </v-flex>
      <v-flex xs4>
        <v-card class="category" width="300">
          <v-card-media src="/static/motherboard.jpg" height="200px">
          </v-card-media>
          <v-card-title primary-title>
            <div>
              <h3 class="headline mb-0">Motherboards</h3>
              <div>Our collection of motherboards.</div>
            </div>
          </v-card-title>
          <v-card-actions>
            <v-btn flat color="blue" :to="{ name: 'tag', params: { name: 'motherboard' }}">View All</v-btn>
          </v-card-actions>
        </v-card>
      </v-flex>
      <v-flex xs4>
        <v-card class="category" width="300">
          <v-card-media src="/static/harddrive.jpg" height="200px">
          </v-card-media>
          <v-card-title primary-title>
            <div>
              <h3 class="headline mb-0">Hard drives</h3>
              <div>Our collection of hard drives and solid state drives.</div>
            </div>
          </v-card-title>
          <v-card-actions>
            <v-btn flat color="blue" :to="{ name: 'tag', params: { name: 'harddrives' }}">View All</v-btn>
          </v-card-actions>
        </v-card>
      </v-flex>
      <v-flex xs4>
        <v-card class="category" width="300">
          <v-card-media src="/static/powersupplies.png" height="200px">
          </v-card-media>
          <v-card-title primary-title>
            <div>
              <h3 class="headline mb-0">Power supplies</h3>
              <div>Our collection of power supplies.</div>
            </div>
          </v-card-title>
          <v-card-actions>
            <v-btn flat color="blue" :to="{ name: 'tag', params: { name: 'powersupply' }}">View All</v-btn>
          </v-card-actions>
        </v-card>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import db from './firebaseInit'
import firebase from 'firebase'

export default {
  name: 'home',
  data () {
    return {
      products: [],
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
      currentUser: false
    }
  },
  created () {
    if (firebase.auth().currentUser) {
      this.isLoggedIn = true
      this.currentUser = firebase.auth().currentUser.email
    }
  }
}
</script>

<style scoped>
  .category {
    margin: 10px;
  }
</style>
