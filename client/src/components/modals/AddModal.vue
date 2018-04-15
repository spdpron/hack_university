<template lang='pug'>
b-modal(:title='"Add " + itemName' v-model='visible' @ok='_validate')
  b-container
    b-form-group
      input.form-control(type='text' placeholder='Name' v-model='name')
    b-form-group
      b-textarea.form-control(placeholder='Content' v-model='content' rows='10')
    b-form-group
      b-alert(v-if='alert' variant='danger' show)
        | {{ alert }}
</template>

<script>
export default {
  data () {
    return {
      visible: false,
      itemsToValidate: [],
      name: '',
      content: '',
      alert: ''
    }
  },

  methods: {
    show: function (itemsToValidate) {
      this.itemsToValidate = itemsToValidate
      this.alert = ''
      this.name = ''
      this.content = ''
      this.visible = true
    },

    _validate: function (e) {
      this.alert = ''

      if (this.name === '') {
        this.alert += 'Name should not be empty. '
      }

      var unic = true
      for (var i = 0; i < this.itemsToValidate.length; i++) {
        if (this.name === this.itemsToValidate[i].name) {
          unic = false
        }
      }
      if (!unic) {
        this.alert += 'Name should be unic. '
      }

      if (this.content === '') {
        this.alert += 'Content should not be empty. '
      }

      (this.alert === '') ? this.$emit('ok', { name: this.name, content: this.content }) : e.preventDefault()
    }
  },

  props: ['itemName']
}
</script>
