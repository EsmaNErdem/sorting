def selection (lst):
    for j in range(len(lst)):
        min_index = j
        for i in range(j+1, len(lst)):
            if lst[i] < lst[min_index]:
                min_index = i

        lst[j], lst[min_index] = lst[min_index], lst[j]
    return lst
  
print(selection([4, 20, 12, 10, 7, 9]))


