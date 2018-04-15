const express = require('express')
const cookieParser = require('cookie-parser');
const bodyParser = require('body-parser')
const cors = require('cors')
const morgan = require('morgan')
const mongoose = require('mongoose')
const config = require('./config/config')

global.__basedir = __dirname + '/';
global.loginEfforts = 0;
global.maxLoginEfforts = function() { return 5; }

const app = express()
mongoose.Promise = global.Promise

app.use(morgan('combined'))
app.use(bodyParser.json())
app.use(bodyParser.urlencoded())
app.use(cookieParser())
app.use(cors())

// IS THIS FRONT-END ?
/*
// Configuring Passport
const passport = require('passport');
const expressSession = require('express-session');
// TODO - Why Do we need this key ?
app.use(expressSession({secret: 'ERdscvS#3d@VFD(#sD)3Dvc;;!@l;D#lvds3E##Fds'}));
app.use(passport.initialize());
app.use(passport.session());

const initPassport = require('./passport/init');
initPassport(passport);
*/

app.use(require('./routes/pull'))
app.use(require('./routes/settings'))

app.get('/server/time', function(req, res) {
	res.json(
		+Date.now()
	);
})

mongoose.connect(config.dbURL, config.dbOptions)
mongoose.connection
  .once('open', () => {
    console.log(`Mongoose - successful connection ...`)
    app.listen(process.env.PORT || config.port,
      () => console.log(`Server start on port ${config.port} ...`))
  })
  .on('error', error => console.warn(error))