<template lang='pug'>
div
  b-input-group( prepend='Name' )
    b-form-input( v-model='name' placeholder='Type field name here' @input='(val) => $emit("nameChanged", val)')
    b-input-group-append
      b-btn(
        v-b-toggle='id + "Collapse"'
        variant='primary'
      )
        | Toggle settings
      b-btn(
        @click='$emit("close")'
        variant='outline-primary'
      )
        | x
  b-collapse( :id='id + "Collapse"' )
    b-card
      b-form-group(
        id='id + "SearchEntitiesInputGroup"'
        :label='searchEntities.length ? "Search entities:" : "There are no search entities."')
        b-row.m-1
         b-col
            search-entity.m-2( v-for='entity, entityIndex in searchEntities'
              :name='searchEntities[entityIndex].name'
              :xPath='searchEntities[entityIndex].xPath'
              :cssClass='searchEntities[entityIndex].cssClass'
              :id='searchEntities[entityIndex].id'
              @nameChanged='(val) => searchEntities[entityIndex].name = val'
              @xPathChanged='(val) => searchEntities[entityIndex].xPath = val'
              @cssClassChanged='(val) => searchEntities[entityIndex].cssClass = val'
              @idChanged='(val) => searchEntities[entityIndex].id = val'
              @close='removeSearchEntity(entityIndex)'
              :ref='id + "FieldSearchEntity" + searchEntities[entityIndex]._id'
            )
        b-row.m-1.mt-2
          b-col
            b-button.float-right(
              size='sm'
              @click='addSearchEntity'
              variant='primary'
            )
              | Add search entity

      b-row.m-1
        b-col
          b-input-group( prepend='Search query' )
            b-form-input( v-model='searchQuery' placeholder='Type search query here' @input='(val) => $emit("searchQueryChanged", val)')

      b-form-group.mt-3( v-if='addFields'
        id='id + "FieldsInputGroup"'
        :label='fields.length ? "Fields:" : "There are no fields."')
        b-row.m-1
         b-col
            field.m-1( v-for='field, fieldIndex in fields'
              :name='fields[fieldIndex].name'
              @nameChanged='(val) => fields[fieldIndex].name = val'
              :searchEntities='fields[fieldIndex].searchEntities'
              :searchQuery='fields[fieldIndex].searchQuery'
              @searchEntitiesChanged='(val) => fields[fieldIndex].searchEntities = val'
              @searchQueryChanged='(val) => fields[fieldIndex].searchQuery = val'
              @close='fields.splice(fieldIndex, 1)'
              addFields='true'
            )
        b-row.m-1.mt-2
          b-col
            b-button.float-right(
              size='sm'
              @click='addField'
              variant='primary'
            )
              | Add field

</template>

<script>
import SearchEntity from '@/components/SearchEntity.vue'
// import SettingsService from '@/services/SettingsService'

export default {
  name: 'field',

  data () {
    return {
      name: '',
      id: Date.now(),
      searchEntities: [],
      fields: [],
      searchQuery: ''
    }
  },

  props: ['addFields'],

  methods: {
    addSearchEntity () {
      this.searchEntities.push({
        name: '',
        xPath: '',
        cssClass: '',
        id: '',
        _id: Date.now()
      })
      this.$emit('searchEntitiesChanged', this.searchEntities)
    },
    removeSearchEntity (entityIndex) {
      this.searchEntities.splice(entityIndex, 1)
    },
    addField () {
      this.fields.push({
        name: '',
        id: Date.now(),
        searchEntities: [],
        fields: []
      })
      this.$emit('fieldsChanged', this.fields)
    }
  },

  components: {
    'search-entity': SearchEntity
  }
}
</script>