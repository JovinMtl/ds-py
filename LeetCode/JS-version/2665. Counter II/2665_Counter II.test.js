
let createCounter = require('./2665_Counter II')


const counter = createCounter(5)

test("See increment", ()=>{
    expect(counter.increment()).toBe(6);
    expect(counter.decrement()).toBe(5);
    expect(counter.decrement()).toBe(4);
    expect(counter.reset()).toBe(5);
});