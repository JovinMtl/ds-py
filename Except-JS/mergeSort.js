

function merge(leftArr, rightArr){
    let result = []
    let leftIndex = 0
    let rightIndex = 0

    while(leftIndex < leftArr.length && rightIndex < rightArr.length){
        console.log(leftArr[leftIndex], ":", rightArr[rightIndex],rightIndex,leftArr[leftIndex] < rightArr[rightIndex])
        if (leftArr[leftIndex] < rightArr[rightIndex]){
            result.push(leftArr[leftIndex])
            leftIndex += 1
        }else{
            result.push(rightArr[rightIndex])
            rightIndex += 1
        }
        console.log("R:", result)
    }
    return result.concat(leftArr[leftIndex]).concat(rightArr[rightIndex])
}

function mergeSort(arr){
    if (arr.length < 2){
        return arr
    }

    const middleIndex = Math.floor(arr.length / 2)
    const leftArr = arr.slice(0, middleIndex)
    const rightArr = arr.slice(middleIndex, arr.length)

    return merge(mergeSort(leftArr), mergeSort(rightArr))
}

let arr = [ 1 , 8, 2, 0, 20, 3]
let resultArr = mergeSort(arr)
console.log("THe arr:", arr, "gave:", resultArr)