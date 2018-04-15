const Settings = require(__basedir + 'models/settings')

exports.putSettings = (req, res) => {
  Settings.findOne({ name: 'main' }, (err, settings) => {
    if (err || settings === null) {
      console.log(err)
      res.sendStatus(500)
    } else {
      if (req.body.parentLinks) {
        settings.parentLinks = req.body.parentLinks
      }
      if (req.body.childLinks) {
        settings.childLinks = req.body.childLinks
      }
      if (req.body.crawlFields) {
        settings.crawlFields = req.body.crawlFields
      }
      settings.save( err => {
        if (err) {
          console.log(err)
          res.sendStatus(500)
        } else {
          res.sendStatus(200)
        }
      })
    }
  })
}

exports.getSettings = (req, res) => {
  Settings.findOne({ name: 'main' }, (err, settings) => {
    if (err || settings === null) {
      console.log(err)
      res.sendStatus(500)
    } else {
      res.send(settings)
    }
  })
}

exports.testSettings = (req, res) => {
  console.log(req.body)
}