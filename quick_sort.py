import random

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    lesser, greater, equal = [], [], []
    pivot = arr[random.randint(0, len(arr) - 1)]
    for item in arr:
        if item < pivot:
            lesser.append(item)
        elif item == pivot:
            equal.append(item)
        elif item > pivot:
            greater.append(item)
    return quick_sort(lesser) + equal + quick_sort(greater)


print(quick_sort([2, 8, 1, 7, 2, 8, 10, 3]))
