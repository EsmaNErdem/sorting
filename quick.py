def quick(lst):
    if len(lst) <= 1:
        return lst
    pivot = lst[0]
    smaller = [i for i in lst[1:] if i < pivot]
    bigger = [i for i in lst[1:] if i > pivot]

    return quick(smaller) + [pivot] + quick(bigger)

print(quick([4, 20, 12, 10, 7, 9]))