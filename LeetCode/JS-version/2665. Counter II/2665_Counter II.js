/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {
    let val = init
    let bckUp = init
    function increment(){
        return ++val
    }
    function decrement(){
        return --val
    }
    function reset(){
        val = bckUp
        return val
    }
  
    return {increment, decrement, reset}
    
  };
  
  /**
  * const counter = createCounter(5)
  * counter.increment(); // 6
  * counter.reset(); // 5
  * counter.decrement(); // 4
  */
  const counter = createCounter(5)
  // counter.increment(); // 6
  console.log(counter.increment())
  console.log(counter.reset())
  console.log(counter.decrement())