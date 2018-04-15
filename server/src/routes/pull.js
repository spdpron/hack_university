const express = require('express')
const router = express.Router()
const PullController = require(__basedir + 'controllers/pull')

router.post('/pull', PullController.savePullRequest)
router.get('/pull', PullController.getPullRequest)
router.get('/pull/count', PullController.pullRequestCount)

module.exports = router