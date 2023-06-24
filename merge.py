def merge(lst1, lst2):
    a, b = 0, 0
    output = []
    while a < len(lst1) and b < len(lst2):
        if lst1[a] <= lst2[b]:
            output.append(lst1[a])
            a += 1
        else:
            output.append(lst2[b])
            b += 1

    while a < len(lst1):
        output.append(lst1[a])
        a += 1
    while b < len(lst2):
        output.append(lst2[b])
        b += 1

    return output

# print(merge([1,2,3,4,5], [6,7,8,9]))
# print(merge([1,2,3,4,5], [1,2,6,7,8,9]))

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2 
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


print(merge_sort([4, 20, 12, 10, 7, 9]))
