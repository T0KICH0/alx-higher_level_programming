#!/usr/bin/node
let myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
myObject.incr = function () {
  Object.value++;
};
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
