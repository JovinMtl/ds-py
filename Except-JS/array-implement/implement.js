
// I want to implement an array

class JoveArray {
    constructor(){
        this.lenght = 0;
        this.data = {}
        return this
    }
    add(val){
        this.data[this.lenght] = val
        this.lenght++
    }
}

const myArray = new JoveArray()
myArray.add(1)

console.log("Look at this: " + myArray)