def binarySearch(aList, start, end, target):
    if end<start:
        return False
    mid = (start+end)//2
    if aList[mid]==target:
        return True
    elif aList[mid]>target:
        return binarySearch(aList,start, mid-1, target)
    else:
        return binarySearch(aList, mid+1, end, target)

theList = [1,2,4,5,7,9,12,13,16,18,19,34,45,56,67,78,89]
print(binarySearch(theList, 0, len(theList)-1, 6))
