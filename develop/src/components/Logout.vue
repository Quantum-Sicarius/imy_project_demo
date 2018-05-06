<template>
<p>Logging out...</p>
</template>

<script>
import firebase from 'firebase'
export default {
  name: 'logout',
  methods: {
    logout: function () {
        firebase
            .auth()
            .signOut()
            .then(() => {
                this.$router.push({ path: '/login' })
                this.$router.go(1)
        })
    }
  },
  created () {
      this.logout()
  }
}
</script>
