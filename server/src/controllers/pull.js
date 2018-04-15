const PullRequest = require(__basedir + 'models/pullRequest')

exports.savePullRequest = (req, res) => {
  const pullRequest = new PullRequest({
    url: req.body.url,
    crawledObject: req.body.crawledObject
  })
  pullRequest.save((err, data) => {
    if (err) {
      console.log(err)
      res.sendStatus(500)
    } else {
      res.json(data)
    }
  })
}

exports.getPullRequest = (req, res) => {
  PullRequest.find({}, (err, data) => {
    if (err) {
      console.log(err)
      res.sendStatus(500)
    } else {
      res.json(data)
    }
  })
}

exports.pullRequestCount = (req, res) => {
  PullRequest.count({}, (err, count) => {
    if (err) {
      console.log(err)
      res.sendStatus(500)
    } else {
      res.json(count)
    }
  })
}
