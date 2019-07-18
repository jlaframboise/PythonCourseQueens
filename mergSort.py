a = [14, 9, 60, 7, 30, 2, 17, 12, 1, 55]


def mergeSort(lis):
    if len(lis) < 2:
        return lis
    else:
        mid = len(lis) // 2
        left = mergeSort(lis[:mid])
        right = mergeSort(lis[mid:])
        return merge(left, right)


def merge(left, right):
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result


b=[3,7,4,1,9]
print(mergeSort(a))
