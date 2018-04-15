<template lang='pug'>
b-card
  b-input-group.m-1( prepend='Name' )
    b-form-input( v-model='name' placeholder='Type name here' @input='(val) => $emit("nameChanged", val)' )
  b-input-group.m-1( prepend='XPath' )
    b-form-input( v-model='xPath' placeholder='Type xPath here' @input='(val) => $emit("xPathChanged", val)' )
  b-input-group.m-1( prepend='Class' )
    b-form-input( v-model='cssClass' placeholder='Type CSS classes here' @input='(val) => $emit("cssClassChanged", val)' )
  b-input-group.m-1( prepend='ID' )
    b-form-input( v-model='id' placeholder='Type element ID here' @input='(val) => $emit("idChanged", val)' )
  b-button.float-right(
    size='sm'
    @click='$emit("close")'
    variant='primary'
  )
    | Remove entity
</template>

<script>

export default {
  data () {
    return {
      name: '',
      xPath: '',
      cssClass: '',
      id: ''
    }
  }
}
</script>