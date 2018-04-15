<template lang='pug'>
b-modal(:title='"Remove " + itemName' v-model='visible' @ok='_ok')
  b-container
    b-form-group
      | Are you sure to remove "
      b
        | {{ name }}
      | " {{ itemName.toLowerCase() }}?
</template>

<script>
export default {
  data () {
    return {
      visible: false,
      name: ''
    }
  },

  methods: {
    show: function (name) {
      this.name = name
      this.visible = true
    },

    _ok: function (e) {
      this.$emit('ok')
    }
  },

  props: ['itemName']
}
</script>
