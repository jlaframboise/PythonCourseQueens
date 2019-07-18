

def rangeSum(n,m):
    if n>m:
        return 0
    if n==m:
        return m
    else:
        return n+rangeSum(n+1,m)

print(rangeSum(1,5))

def equalSums(A):
    B = [sum(numList) for numList in A]
    for total in B:
        if B.count(total)>1:
            return True
    return False

myList = [[1,2,3,4],
          [34,4,5,4,6],
          [4,1,1,1,1,1]]

print(equalSums(myList))

def permutation(A,B):
    if len(A)!=len(B):
        return False
    for item in A:
        if item not in B or B.count(item)!=A.count(item):
            return False
    for item in B:
        if item not in A or B.count(item)!=A.count(item):
            return False
    return True

print(permutation([1,4,2,3], [4,2,1,3]))