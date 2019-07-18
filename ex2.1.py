# Jacob Laframboise
# Student Number  --------
# Sept. 17th, 2018
# this program contains a function to get a machine epsilon value


'''A function with no parameters to determine the approximate float machine epsilon
value for a machine. It uses a variable called machineEpsilon and halfMachineEpsilon
and if halfMachineEpsilon is not too small to be detected, then it sets machineEpsilon
as equal to halfMachineEpsilon, and divides halfMachineEpsilon in half again, and repeats
until halfMachineEpsilon is too small to be detected, so machineEpsilon is accurate. '''
def getMachineEpsilon():
    # initialize the variables to store machine epsilon values
    halfMachineEpsilon = 1.0
    machineEpsilon = 2 * halfMachineEpsilon
    
    # A loop that runs until halfMachine Epsilon is too small for detection
    while 1.0 + halfMachineEpsilon != 1.0:
        machineEpsilon=halfMachineEpsilon
        halfMachineEpsilon = halfMachineEpsilon/2
        
    # return machineEpsilon + 1.0 when halfMachineEpsilon is too small
    return machineEpsilon + 1.0




