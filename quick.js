/*
pivot accepts an array, starting index, and ending index
You can assume the pivot is always the first element
*/

function pivot(arr, start = 0, end = arr.length - 1){
    let pivot = arr[start]
    let pivotIndex = start
    for (let i = start + 1; i <= end; i++) {
        if (arr[i] < pivot && pivotIndex != i) {
            pivotIndex++
            [arr[i], arr[pivotIndex]] = [arr[pivotIndex], arr[i]]
        }
    }
    [arr[start], arr[pivotIndex]] = [arr[pivotIndex], arr[start]]
    return pivotIndex
}
/*
quickSort accepts an array, left index, and right index
*/

function quickSort(arr, left = 0, right = arr.length-1) {
    if(left < right) {
        let pivotIndex = pivot(arr, left, right)
        quickSort(arr, left, pivotIndex - 1)
        quickSort(arr, pivotIndex + 1, right)
    }
    return arr
}

quickSort([4, 20, 12, 10, 7, 9])

module.exports = {quickSort, pivot};