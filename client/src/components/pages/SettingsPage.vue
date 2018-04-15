<template lang='pug'>
div
  b-container
    b-breadcrumb( :items='breadcrump' )
    b-card.m-1( title='Parent links' )
      b-form-group(
        id='startLinksInputGroup'
        :label='parentLinks.length ? "Links to start:" : "There are no links to start."'
        description='These links will be used as start point for crawler engine.')
        b-row.m-1( v-for='link, linkIndex in parentLinks' )
          b-col
            b-input-group
              b-form-input( v-model='parentLinks[linkIndex]' type='url' placeholder='Type url here' )
              b-input-group-append
                b-btn(
                  @click='parentLinks.splice(linkIndex, 1)'
                  variant='outline-primary'
                )
                  | x
        b-row.m-1.mt-2
          b-col
            b-button.float-right(
              size='sm'
              @click='parentLinks.push("")'
              variant='primary'
            )
              | Add link

    b-card.m-1( title='Child links' )
      b-form-group(
        id='startLinksInputGroup'
        :label='childLinks.length ? "Links to move through:" : "There are no links to move through."'
        description='These links will be used to jump from one page to another.')
        b-row.m-1( v-for='link, linkIndex in childLinks' )
          b-col
            field( :name='childLinks[linkIndex].name'
              @nameChanged='(val) => childLinks[linkIndex].name = val'
              :searchEntities='childLinks[linkIndex].searchEntities'
              :searchQuery='childLinks[linkIndex].searchQuery'
              @searchEntitiesChanged='(val) => childLinks[linkIndex].searchEntities = val'
              @searchQueryChanged='(val) => childLinks[linkIndex].searchQuery = val'
              @close='childLinks.splice(linkIndex, 1)'
            )

        b-row.m-1.mt-2
          b-col
            b-button.float-right(
              size='sm'
              @click='addChildLink'
              variant='primary'
            )
              | Add link

    b-card.m-1( title='Object to crawl' )
      b-form-group(
        id='crawlFieldInputGroup'
        :label='crawlFields.length ? "Fields to crawl:" : "There are no fields."'
        description='These fields will compose the prototype of the object to crawl.')
        b-row.m-1( v-for='field, fieldIndex in crawlFields' )
          b-col
            field( :name='crawlFields[fieldIndex].name'
              @nameChanged='(val) => crawlFields[fieldIndex].name = val'
              :searchEntities='crawlFields[fieldIndex].searchEntities'
              :searchQuery='crawlFields[fieldIndex].searchQuery'
              @searchEntitiesChanged='(val) => crawlFields[fieldIndex].searchEntities = val'
              @searchQueryChanged='(val) => crawlFields[fieldIndex].searchQuery = val'
              @close='crawlFields.splice(fieldIndex, 1)'
              addFields='true'
            )

        b-row.m-1.mt-2
          b-col
            b-button.float-right(
              size='sm'
              @click='addCrawlField'
              variant='primary'
            )
              | Add field
    b-row.m-3
      b-col
      b-col( cols='3' )
        b-button.form-control(
          @click='saveSettings'
          variant='primary'
        )
          | Save
      // b-col( cols='3' )
        // b-button.form-control(
          // @click='test'
          // variant='primary'
        // )
          // | Test
      b-col
</template>

<script>
import Field from '@/components/Field.vue'
import SettingsService from '@/services/SettingsService'

export default {
  data () {
    return {
      breadcrump: [{
        text: 'Blood Bit',
        to: '/'
      }, {
        text: 'Settings',
        to: '/settings'
      }],
      parentLinks: [],
      childLinks: [],
      crawlFields: []
    }
  },

  mounted () {
    this.getSettings()
  },

  methods: {
    addChildLink () {
      this.childLinks.push({
        name: '',
        id: Date.now(),
        searchEntities: [],
        searchQuery: ''
      })
    },
    addCrawlField () {
      this.crawlFields.push({
        name: '',
        id: Date.now(),
        searchEntities: [],
        fields: [],
        searchQuery: ''
      })
    },
    async saveSettings () {
      await SettingsService.saveSettings({
        parentLinks: this.parentLinks,
        childLinks: this.childLinks,
        crawlFields: this.crawlFields
      })
    },
    async getSettings () {
      const response = await SettingsService.getSettings()
      this.parentLinks = response.data.parentLinks
      this.childLinks = response.data.childLinks
      this.crawlFields = response.data.crawlFields
    },
    async sendSettings () {
      await SettingsService.sendSettings({
        parentLinks: this.parentLinks,
        childLinks: this.childLinks,
        crawlFields: this.crawlFields
      })
    },
    test () {
      for (let i = 0; i < this.crawlFields.length; i++) {
        console.log('Logging field...')
        logField(this.crawlFields[i])
      }
      for (let i = 0; i < this.childLinks.length; i++) {
        console.log('Logging links...')
        logField(this.childLinks[i])
      }
      this.sendSettings()
    }
  },

  components: {
    'field': Field
  }
}

function logField (field) {
  console.log('name ' + field.name)
  console.log('id ' + field.id)
  console.log('query ' + field.searchQuery)
  for (let i = 0; i < field.searchEntities.length; i++) {
    console.log(i)
    console.log('.name ' + field.searchEntities[i].name)
    console.log('.xPath ' + field.searchEntities[i].xPath)
    console.log('.cssClass ' + field.searchEntities[i].cssClass)
    console.log('.id ' + field.searchEntities[i].id)
  }
  if (field.fields !== undefined) {
    for (let i = 0; i < field.fields.length; i++) {
      logField(field.fields[i])
    }
  }
}
</script>