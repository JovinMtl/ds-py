
// given an array [2, 1, 1, 3, 5]  => 1

function recuringNumber(arr){
    let cumilated = {}
    let result = undefined
    for (let i = 0; i < arr.length; i++){
        if(arr[i] in cumilated){
            result = arr[i]
            break
        }
        cumilated[arr[i]] = 0
    }
    return result
}
console.log("The result is : ", recuringNumber([2, 5, 1, 0, 3, 5, 1, 2, 4]))