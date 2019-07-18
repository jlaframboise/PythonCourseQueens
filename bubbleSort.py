#JL
#March 2nd
#
import random

myList= []
length = 400
for i in range(length):
    myList.append(random.randrange(0,100))
print(myList)


def bubleSort(myList, ad):
    '''A function to return a list sorted with bubble sort techniques
    where each item is compared to the next item, and swapped if it is
    less than or greater than according to the ad parameter which
     specifies ascending or descending. 'a' for ascending, 'd' for descending
     runs through the list the number of elements times'''
    compars=0
    swaps=0
    for x in range(0,len(myList)-1): #run the number of times equal to the lsit length
        for i in range(0,len(myList)-1): #for every item
            if myList[i]>myList[i+1] and ad == 'a': #if ascending
                myList[i], myList[i+1] = myList [i+1], myList[i] #swap values
                swaps+=1
                print(myList)
            if myList[i]<myList[i+1] and ad =='d': #if descending
                myList[i], myList[i+1] = myList [i+1], myList[i] #swap
                swaps+=1
                print(myList)
            compars+=1
    print("There were {} comparisons, and {} swaps.".format(compars, swaps))
    return(myList) #retunr sorted list

def checkSort(myList, ad):
    '''Function to check is a list is sorted in 'a' ascending,
    or 'd' descending by comparing it to a list sorted by Python's
    default sort funciton. Retunrs true or false'''
    if myList == sorted(myList) and ad == 'a':
        #print("True")
        return True
    elif myList == sorted(myList, reverse =True) and ad == 'd':
        #print("True")
        return True
    else:
        #print("FALSE")
        return False



print(checkSort(myList, 'd'))
bubleSort(myList, 'd')
print(checkSort(myList, 'd'))

