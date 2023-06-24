def bubble (arr):
    """
    Bubble function sort an list with bubble sort method.
    Bubble sort method bring the biggest value of element to the end of the list
    """
    n = len(arr)
    for i in range(n):
        swapped = False
        # end of list is already sorted
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        # rest of the array is sorted
        if swapped is False:
            break
    return arr



print(bubble([4, 20, 12, 10, 7, 9]))