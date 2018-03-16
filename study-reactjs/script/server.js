const express = require('express')
const app = express()

app.get('/', (req, res) => res.send('Hello World!'))

app.get('/app/jobs', (req, res) => {
    console.log("/app/jobs")
    res.send('{"id":1}')
})

app.listen(8080, () => console.log('Example app listening on port 8080!'))