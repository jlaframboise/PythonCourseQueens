'''time complexity at best case is nlog(n)
at worst when the list is already sorted, the
worst case time complxity is n^2'''


# the implementation from powley's class
def quickSort(lis):
    if len(lis) < 2:
        return lis

    less, equal, greater = [], [], []
    pval = lis[0]

    for i in lis:
        if i < pval:
            less.append(i)
        elif i > pval:
            greater.append(i)
        else:
            equal.append(i)
    return quickSort(less) + equal + quickSort(greater)



# the implementation I wrote
def qs(lis):
    if len(lis) <2:
        return lis
    if len(lis) >= 2:
        pivot = [lis[0]]
        smaller = []
        greater = []
        for x in lis[1:]:
            if x < pivot[0]:
                smaller.append(x)
            elif x > pivot[0]:
                greater.append(x)
            else:
                pivot.append(x)
        return qs(smaller) + pivot + qs(greater)


list1 = [5, 26, 3, 1]

print(qs(list1))
