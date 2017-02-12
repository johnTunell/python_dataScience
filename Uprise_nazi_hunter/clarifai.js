// Require the client
var Clarifai = require('clarifai');

// instantiate a new Clarifai app passing in your clientId and clientSecret
var app = new Clarifai.App(
    'M0ytZ-ulTpWGpY9zCtZHea-VPJQRe4I4onV_5tAe',
    'WVDAYcncI5DozDkEJUiMFgNRoFgaWjQyJqrCS1wm'
);

// You can also use the client directly in your browser:

// predict the contents of an image by passing in a url
app.models.predict(Clarifai.GENERAL_MODEL, 'http://www.crystalinks.com/swastikaflaghitler.jpg').then(
    function(response) {
        console.log(response);
        console.log(response.input);

        app.models.predict(Clarifai.NSFW_MODEL, 'http://www.crystalinks.com/swastikaflaghitler.jpg').then(
            function(response2) {
                console.log(response2);
                console.log(response2.input);
            },
            function(err) {
                console.error(err);
            }
        );

    },
    function(err) {
        console.error(err);
    }
);