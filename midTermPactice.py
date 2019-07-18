def main():
    aVal = 6
    i=0
    j=0

    while i<= aVal:
        print(i, end=': ')
        j=i
        while j<= aVal:
            print(j*i,end=' ')
            j=j+1
        i=i+1
        print()
#main()

def mainC():
    listOne = [2,3]*4
    print(listOne)

    listTwo = list(range(4,33,4))
    print(listTwo)

    i=0
    while i< len(listOne):
        if listTwo[i] % listOne[i] ==0:
            print(i, end=' | ')
        i=i+1
#mainC()


def aFunction(valOne, valTwo=5, valThree=2):
    aList = []
    for i in range(valOne):
        aList.append(i*valTwo+valThree)
    return aList

def mainD():
    print(aFunction(5))
    print(aFunction(4,3))
    print(aFunction(6, valThree=1))
    print(aFunction(4,4,4))

#mainD()

def aFunction(anInt, aString, aList1, aList2, aList3):
    anInt = 1000
    aString = 'Exam'
    aList1.sort()
    for i in range(len(aList2)):
        aList2[i] = 10 * aList2[i]
    aList3 = [2,4,6,8]

def mainE():
    intOne = 20
    aStr = "PythonCourse"
    listOne = [10,2,3,5,7]
    listTwo = [1,4,5,2]
    listThree = [3,5,7,9]
    aFunction(intOne, aStr, listOne, listTwo, listThree)
    print(intOne, aStr)
    print(listOne)
    print(listTwo)
    print(listThree)

mainE()