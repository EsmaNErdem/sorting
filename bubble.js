function bubbleSort(arr) {
    let swapped, temp
    for(let i=0; i<arr.length; i++) {
        swapped = false
        for(let j=0; j<arr.length-i-1; j++){
            if (arr[j] > arr[j+1]) {
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
                swapped = true
            }
        }
        if (swapped == false) break
    }
    console.log(arr)
    return arr
}

module.exports = bubbleSort;