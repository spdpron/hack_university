<template lang='pug'>
b-navbar( toggleable='md' type='dark' variant='dark' ) 
  b-navbar-toggle( target='nav_collapse' )
  b-navbar-brand( to='/dashboard' )
    | Blood Bit {{ time }} GMT
  b-collapse#nav_collapse( is-nav )
    b-navbar-nav
      b-nav-item( to='/dashboard' ) 
        i.fa.fa-fw.fa-dashboard
        | Dashboard
    b-navbar-nav
      b-nav-item( to='/settings' ) 
        i.fa.fa-fw.fa-cog
        | Settings
    b-navbar-nav.ml-auto
      b-nav-item( to='/logout') 
        i.fa.fa-fw.fa-sign-out
        | Logout
</template>

<script>
export default {
  data () {
    return {
      time: new Date()
    }
  },

  created: function () {
    setInterval(() => {
      this.time = formatTime(new Date())
    }, 1000)
  }
}

function formatTime (date) {
  return date.toISOString().replace(/T/, ' ').replace(/\..+/, '')
}
</script>
