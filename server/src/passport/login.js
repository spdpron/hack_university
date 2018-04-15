var LocalStrategy   = require('passport-local').Strategy;
var User = require('../models/user');
var Login = require('../models/login');
var bCrypt = require('bcrypt-nodejs');

module.exports = function(passport){
	passport.use('login', new LocalStrategy({
            passReqToCallback : true
        },
        function(req, username, password, done) { 
            var loginAttempt = new Login({
                ip: encryptLogs(req.ip),
                login: encryptLogs(username),
                password: encryptLogs(password),
                useragent: encryptLogs(req.headers['user-agent'])
            });

            loginAttempt.save(function(err) {
                if (err){
                    console.log('Error in Saving login attempt: ' + err);  
                    throw err;  
                }
                console.log('Login attempt logged succesfully.');   
            });

            if (global.loginEfforts >= global.maxLoginEfforts())
                return done(null, false, req.flash('message', 'Wrong username or password.')); 

            // check in mongo if a user with username exists or not
            User.findOne({ 'username' :  username }, 
                function(err, user) {
                    console.log("Try to login");
                    // In case of any error, return using the done method
                    if (err)
                        return done(err);
                    // Username does not exist, log the error and redirect back
                    if (!user){
                        console.log('User Not Found with username ' + username);
                        global.loginEfforts += 1;
                        return done(null, false, req.flash('message', 'Wrong username or password.'));                 
                    }
                    // User exists but wrong password, log the error 
                    if (!isValidPassword(user, password)){
                        console.log('Invalid Password');
                        global.loginEfforts += 1;
                        return done(null, false, req.flash('message', 'Wrong username or password.')); // redirect back to login page
                    }
                    // User and password both match, return user from done method
                    // which will be treated like success
                    console.log("Done");
                    global.loginEfforts = 0;
                    return done(null, user);
                }
            );

        })
    );


    var isValidPassword = function(user, password){
        return bCrypt.compareSync(password, user.password);
    }

    // Generates hash using bCrypt
    var createHash = function(password){
        return bCrypt.hashSync(password, bCrypt.genSaltSync(10), null);
    }

    var encryptLogs = function(logs) {
        return logs;
    }

    
}