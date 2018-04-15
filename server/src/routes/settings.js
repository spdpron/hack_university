const express = require('express')
const router = express.Router()
const SettingsController = require(__basedir + 'controllers/settings')

router.get('/settings/', SettingsController.getSettings)
router.put('/settings/', SettingsController.putSettings)

router.post('/api/bloodbitapi/?/', SettingsController.testSettings)

module.exports = router