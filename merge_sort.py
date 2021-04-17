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


# print(merge_sort([2, 8, 1, 7, 2, 8, 10, 3]))

def longest_common_prefix(strs):
        ans = ''
        if strs:            
            min_word = strs[0]
            min_len = len(strs[0])
            for word in strs:
                if len(word) < min_len:
                    min_len = len(word)
                    min_word = word
            i = 0
            is_common = True
            while (i < min_len) and is_common:
                for j in range(len(strs)):
                    if strs[j][i] == min_word[i]:
                        continue
                    else:
                        is_common = False
                        break
                if is_common:
                    ans += min_word[i]
                i += 1
        return ans

print(longest_common_prefix(['flyer', 'flyow', 'frooow']))