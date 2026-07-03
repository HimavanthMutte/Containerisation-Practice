const express = require('express');
const app = express();
const port = process.env.PORT || 3000;

app.get('/', (req, res) => {
  res.send('Hello from Node.js Practice 1!');
});

app.listen(port, () => {
  console.log(`Node app listening on port ${port}`);
});
