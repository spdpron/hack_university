const mongoose = require('mongoose');
const Schema = mongoose.Schema
 
const SettingsSchema = new Schema({
    parentLinks: [],
    childLinks: [],
    crawlFields: [],
    name: {
    	type: String,
    	required: true,
    	unique: true
    }
})

const SettingsModel = mongoose.model('settings', SettingsSchema)
module.exports = SettingsModel