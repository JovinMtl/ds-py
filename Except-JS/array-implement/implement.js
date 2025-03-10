
// I want to implement an array

class JoveArray {
    constructor(){
        this.length = 0;
        this.data = {}
        // return this.data
    }
    see(index=-1){
        if (index < 0){
            console.log(this.data)
        } else {
            console.log(this.data[index])
        }
        
    }
    add(val){
        this.data[this.length] = val
        this.length++
    }
}

const myArray = new JoveArray()
myArray.add(5)
// myArray.see()
myArray.add('jove')
myArray.see()
// console.log("Look at this: " + myArray)