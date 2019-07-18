# Jacob Laframboise
# Student Number  --------
# Sept. 17th, 2018
# this program contains a function to approximate a square root using the Babylonian Method


'''A function to return the floating point square root of an input 'square' float or integer,
using the Babylonian method. '''
def getSquareRoot(square):
    # initialize variable to hold the square root approximation, and a placeholder variable
    root = square
    placeholder = None

    # A loop to run the algorithm until the root is unchanging, and the correct root
    while placeholder!=root:
        placeholder = root
        root = (root + square / root)/2.0
        
    # return the float root when the loop terminates
    return root


