def linear_search(arr, target):
    for i in range(0, len(arr)):
        if arr[i] == target:
            index = i
            return index
    
    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    first = 0
    last = (len(arr) - 1)

    found = False
    while first <= last and found == False:
        middle = (first + last) // 2
        if arr[middle] == target:
            found = True
            return middle
        else:
            if target < arr[middle]:
                last = middle - 1

            if target > arr[middle]:
                first = middle + 1  

    return -1  # not found
