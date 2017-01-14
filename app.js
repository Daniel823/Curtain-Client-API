var express = require('express')
var app = express()

app.route('/state')
  .get(function (req, res) {
    res.send('get the item state')
  })
  .post(function (req, res) {
    res.send('tell the client what to do ie. close/open the blind')
  })

app.listen(3000, function () {
  console.log('Client API listening on port 3000: ')
})
