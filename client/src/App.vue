<template lang='pug'>
  #app
    Navbar
    main
      router-view
</template>

<script>
import Navbar from '@/components/Navbar.vue'

export default {
  components: {
    'Navbar': Navbar
  }
}
</script>