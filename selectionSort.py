def selectionSort(items):
    print(items)
    for i in range(len(items)-1):
        smallest = min(items[i:])
        indexSmallest = items[i:].index(smallest)+i
        items[i], items[indexSmallest] = items[indexSmallest], items[i]
    print(items)
    #roughly n^2 time


def insertionSort(items): #works welll on sorted list
    for i in range(1, len(items)):

        j=i
        while(j>0) and items[j-1] > items[j]:
            print(items)
            items[j-1], items[j] = items[j], items[j-1]
            j=j-1
    print(items)
    #n*(n-1)/2
#insertionSort([-1,20,5,0,5])

y = [1,2,3,4,5]

x = [2*a for a in y]