<template lang='pug'>
div
  b-container
    b-breadcrumb( :items='breadcrump' )
    b-jumbotron
      template( slot='lead' )
        b-row.align-items-end
          b-col
            | Control crawling dataflow
            i.fa.fa-fw.fa-spinner.fa-spin( v-if='running' )
          b-col
          b-col
            small
              b-link.float-right( @click='$refs.hotToGetModal.show()' )
                | How to get crawled data?
      hr
      b-row.m-1
        b-col( cols='3' )
          | Object to crawl:
        b-col
          b-input( type='number' :min='crawledCount' max='100000' v-model='objectsToCrawl' :disabled='running' )
      b-row.m-1
        b-col( cols='3' )
          | Hours to crawl:
        b-col
          b-input( type='number' min='0' v-model='hoursToCrawl' :disabled='running' )
      b-row.m-1
        b-col( cols='3' )
          | Minutes to crawl:
        b-col
          b-input( type='number' min='0' max='60' v-model='minutesToCrawl' :disabled='running' )
      b-row.m-1
        b-col
          | Personal 
      b-row.m-3.mt-5
        b-col
          b-progress( :max='objectsToCrawl' height='20px' )
            b-progress-bar( animated :value='crawledCount' variant='primary' )
            b-progress-bar( :value='objectsToCrawl - crawledCount' variant='secondary' )
      b-row.mt-2
        b-col
        b-col( cols='3' )
          b-btn.form-control( variant='primary' :disabled='running' @click='changeCrawlerState' v-model='minutesToCrawl' )
            | {{ running ? 'Stop' : 'Run' }}
        b-col
  b-modal( title='Convenience API to get your crawled data' ref='hotToGetModal' )
    p
      | Simply use GET request to fetch crawled objects.
    p
      | http://10.0.1.71:8081/pull
</template>

<script>
import SettingsService from '@/services/SettingsService'

export default {
  data () {
    return {
      breadcrump: [{
        text: 'Blood Bit',
        to: '/'
      }, {
        text: 'Dashboard',
        to: '/dashboard'
      }],
      parentLinks: [],
      childLinks: [],
      crawlFields: [],

      running: false,
      crawledCount: 0,
      objectsToCrawl: 1000,
      hoursToCrawl: 0,
      minutesToCrawl: 30
    }
  },

  mounted () {
    this.getSettings()

    setInterval(() => {
      this.updatePullRequestCount()
    }, 1000)
  },

  methods: {
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
        crawlFields: this.crawlFields,
        objectsToCrawl: Number.parseInt(this.objectsToCrawl, 10),
        hoursToCrawl: Number.parseInt(this.hoursToCrawl, 10),
        minutesToCrawl: Number.parseInt(this.minutesToCrawl, 10)
      })
    },
    async updatePullRequestCount () {
      const response = await SettingsService.getPullRequestCount()
      this.crawledCount = response.data
      if (this.crawledCount >= this.objectsToCrawl) {
        this.objectsToCrawl = this.crawledCount
        this.running = false
      }
    },
    changeCrawlerState () {
      if (this.running) {

      } else {
        this.sendSettings()
      }
      this.running = !this.running
    }
  }
}
</script>