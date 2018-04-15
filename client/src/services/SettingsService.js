import api from '@/services/api'
import axios from 'axios'

export default {
  saveSettings (settings) {
    return api().put('/settings/', settings)
  },
  getSettings () {
    return api().get('/settings/')
  },
  sendSettings (settings) {
    return axios.create({
      baseURL: 'http://10.0.1.130:8888'
      // baseURL: 'http://localhost:8081'
      // baseURL: 'https://webhook.site/b1432e70-21b0-4a55-985a-d60a0600e790'
    }).post('/api/bloodbitapi/?', settings, {
      headers: {
        'Content-Type': 'application/json'
      }
    })
  },
  getPullRequestCount () {
    return api().get('/pull/count')
  }
}
