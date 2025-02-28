
let createCounter = require('./2665_Counter II')


const counter = createCounter(5)
test("See increment", ()=>{
    expect(counter.increment()).toBe(6)
});