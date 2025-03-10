
// given a = [0,3,4, 31]; b = [4, 6, 30]
//  [0, 3, 4, 6, 30, 31]

// Lets assume there are going to be two arrays

function mergeTwoSortedArrays(arr1, arr2){
    let totalElements = Number(arr1.length + arr2.length)

    let a = 0; 
    let b = 0;
    let result = []

    for (let i = 0; i <= totalElements - 2; i++){
        if(arr1[a] < arr2[b]){
            result.push(arr1[a])
            a++
        } else{
            result.push(arr2[b])
            b++
        }
    }
    
    // should be able to print the result
    console.log(result)
}

// let's call the function
arr1 = [0, 3, 4, 31]
arr2 = [4, 6, 30]
mergeTwoSortedArrays(arr1, arr2)