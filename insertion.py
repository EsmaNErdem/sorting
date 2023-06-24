def insertion(lst):
    """
    this function sorts a list with insertion sorting method
    when encounter a small number take to its appropriate spot. 
    """
    for i in range(1,len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and key < lst[j]:
            # shift biggger number to the left
            lst[j+1] = lst[j]
            j -= 1

        lst[j+1] = key

    return lst


print(insertion([4, 20, 12, 10, 7, 9]))

