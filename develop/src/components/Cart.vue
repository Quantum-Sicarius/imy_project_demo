<template>
  <v-layout justify-center align-center>
    <v-card class="white--text">
        <v-card-title primary-title>
        <div>
        <h1>Shopping cart</h1>
        <v-data-table
            :headers="headers"
            :items="cartProducts"
            :search="search"
            v-model="selected"
            item-key="name"
            select-all
            class="elevation-1"
        >
            <template slot="headerCell" slot-scope="props">
            <v-tooltip bottom>
                <span slot="activator">
                {{ props.header.text }}
                </span>
                <span>
                {{ props.header.text }}
                </span>
            </v-tooltip>
            </template>
            <template slot="items" slot-scope="props">
            <td>
                <v-checkbox
                primary
                hide-details
                v-model="props.selected"
                ></v-checkbox>
            </td>
            <td>{{ props.item.name }}</td>
            <td class="text-xs-right">{{ props.item.price }}</td>
            </template>
        </v-data-table>
        </div>
        </v-card-title>
        <v-card-actions>
        <v-btn flat dark>Checkout</v-btn>
        </v-card-actions>
    </v-card>
  </v-layout>
</template>

<script>
import db from './firebaseInit'
import firebase from 'firebase'
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'cart',
  computed: mapGetters({
      cartProducts: 'cartProducts'
  }),
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
      search: '',
      selected: [],
      headers: [
        {
          text: 'Name',
          align: 'left',
          sortable: false,
          value: 'name'
        },
        { text: 'Price', value: 'price' }
      ]
      }
    },
    created () {
    }
  }
</script>
