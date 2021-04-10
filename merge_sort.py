def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    a = merge_sort(arr[mid:])
    b = merge_sort(arr[:mid])
    return merge(a, b)


def merge(a, b):
    ai, bi = 0, 0
    ans = []
    while ai < len(a) and bi < len(b):
        if a[ai] <= b[bi]:
            ans.append(a[ai])
            ai += 1
        else:
            ans.append(b[bi])
            bi += 1
    if ai < len(a):
        ans += a[ai:]
    elif bi < len(b):
        ans += b[bi:]
    return ans


print(merge_sort([2, 8, 1, 7, 2, 8, 10, 3]))
