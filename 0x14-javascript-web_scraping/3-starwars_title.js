#!/usr/bin/node
const request = require('request').default;
const ID = process.argv[2];
const endPoint = `https://swapi-api.hbtn.io/api/films/${ID}`;

request.get(endPoint)
  .then(res => console.log(res.data.title))
  .catch(err => console.log(err.message));