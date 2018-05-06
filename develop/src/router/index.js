import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import Cart from '@/components/Cart'
import ViewProduct from '@/components/ViewProduct'
import Login from '@/components/Login'
import Logout from '@/components/Logout'
import Register from '@/components/Register'
import Navbar from '@/components/Navbar'
import ListProducts from '@/components/ListProducts'
import firebase from 'firebase'

Vue.use(Router)

let router = new Router({
  routes: [
    {
      path: '/login',
      component: Login,
      meta: {
        requiresGuest: true
      }
    },
    {
      path: '/logout',
      component: Logout
    },    
    {
      path: '/',
      component: Navbar,
      meta: {
        requiresAuth: true
      },
      children: [
        {
          path: '',
          name: 'home',
          component: Home
        },
        {
          path: 'cart',
          name: 'cart',
          component: Cart
        },
        {
          path: 'tag/:name',
          name: 'tag',
          component: ListProducts
        },
        { path: 'product/:id',
          name: 'viewproducts',
          component: ViewProduct
        },
        { path: 'settings',
          name: 'settings',
          component: Home
        },
        { path: 'help',
          name: 'help',
          component: Home
        },
        { path: 'feedback',
          name: 'feedback',
          component: Home
        }
      ]
    }
  ]
})

// Nav Guard
router.beforeEach((to, from, next) => {
  // Check for requiresAuth guard
  if (to.matched.some(record => record.meta.requiresAuth)) {
    // Check if NO logged user
    if (!firebase.auth().currentUser) {
      // Go to login
      next({
        path: '/login',
        query: {
          redirect: to.fullPath
        }
      })
    } else {
      // Proceed to route
      next()
    }
  } else if (to.matched.some(record => record.meta.requiresGuest)) {
    // 
    if (firebase.auth().currentUser) {
      // Go to login
      next({
        path: '/',
        query: {
          redirect: to.fullPath
        }
      })
    } else {
      // Proceed to route
      next()
    }
  } else {
    // Proceed to route
    next()
  }
})

export default router
