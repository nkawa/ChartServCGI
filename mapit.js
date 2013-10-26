(function(){
    var page = require('webpage').create(),
      system = require('system'),
    fs = require('fs');

    var fname = system.args[1];
    var output = system.args[2];
    var input;
    page.viewportSize = { width: 320, height: 320 };
    

    page.open('file://'+fname, function (status) {
        if (status !== 'success') {
            console.log('Unable to load the file!');
            phantom.exit();
        } else {
            window.setTimeout(function () {
                page.render(output);
                phantom.exit();
            }, 100);
        }
    });
}());

