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
              <v-icon>{{ item.icon }}</v-icon>
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
          <router-view></router-view>
        </v-layout>
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
import firebase from 'firebase'
export default {
  name: 'navbar',
  data () {
    return {
      dialog: false,
      drawer: null,
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
</style>
