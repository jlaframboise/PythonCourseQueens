# Jacob Laframboise
# Student Number  --------
# Sept. 17th, 2018
# this program contains a function to count string items with a minimum length in a list

'''A function that will take a list of strings, and a threshold value which is an integer.
It will return the number of elements in the list which have a length longer than
the threshold value'''
def thresholdStringCount(stringList, threshold):
    count = 0
    
    # for loop to iterate through every element
    for item in stringList:
        # if the item is longer than the threshold
        if len(item) > threshold:
            # count it
            count += 1
            
    # return the final count of strings with length > threshold
    return count

