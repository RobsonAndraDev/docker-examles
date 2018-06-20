var express = require('express');
var app = express();

app.get('/node', function (req, res) {
  res.send('Hello World From Nodejs!');
});

app.listen(3000, function () {
  console.log('Example app listening on port 3000!');
});