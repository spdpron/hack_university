const mongoose = require('mongoose');
const Schema = mongoose.Schema
 
const PullRequestSchema = new Schema({
    url: {
    	type: String,
    	unique: true
    },
    crawledObject: {}
})

const PullRequestModel = mongoose.model('pullRequests', PullRequestSchema)
module.exports = PullRequestModel