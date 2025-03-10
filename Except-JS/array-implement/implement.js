
// I want to implement an array

class JoveArray {
    constructor(){
        this.length = 0;
        this.data = {}
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
    reverse(){
        let secondArray = new JoveArray()
        for (let i = this.length - 1; i >= 0; i--){
            secondArray.add(this.data[i])
        }
        this.data = secondArray.data
        // return secondArray
    }
}

const myArray = new JoveArray()
myArray.add(5)
myArray.add('jove')
myArray.see(-1)
myArray.reverse()
myArray.see()

function reverseStr(str){
    const oldArray = str.split('')
    const newArray = new JoveArray()
    const nArray = []
    for (let i = oldArray.length - 1; i >= 0; i--){
        // newArray.add(oldArray[i])
        nArray.push(oldArray[i])
    }
    console.log(nArray)
}

const myStr = "Hello"
reverseStr(myStr)