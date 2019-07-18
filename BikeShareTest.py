# Jacob Laframboise
# Python Course
# A program to check all of the functions in the bike share program.
# Student #: --------
# Last Edited: Nov. 26th, 2018

# import the functions to test as a shorter name.
import BikeShareCompleteProgram_JLaframboise as bike
import random


# Note: functions that do not take any parameters and do not run differently
# each time are not given test functions as if they work once, they will
# continue to work.

# Also, there are a series of CLI functions that get the proper
# input from the user to call the implementation functions.
# These are named callOption1, callOption2, etc.
# Prof. Powley said these are related to the CLI and
# do not need test functions.


def checkReadData():
    '''A function with no parameters that will return True if the
    readData function is working properly in all cases, and False if
    not. If there is a return False, a short description of the
    problem is outputted. '''

    # read in fresh data
    site = "http://research.cs.queensu.ca/home/cords2/bikes.txt"
    result = bike.readData(site)
    # if the readData function does not return a list greater than 0
    if len(result) == 0:
        print('Failed to read data')
        return False

    for station in result:
        # if a station is missing a data point or has extra
        if len(station) != 7:
            print('A station has irregular list')
            return False
        # If there is no data in an item
        for item in station:
            if item == None or item == [] or item == '':
                print('Bad item in station')
                return False

    return True


def checkCastCleanData():
    '''A function to return a boolean value indicating if the
    function is working correctly in all cases. If there is an
    error, there is a message outputted that indicates where
    the error might be. '''

    # read in fresh data
    site = "http://research.cs.queensu.ca/home/cords2/bikes.txt"
    raw = bike.readData(site)
    # apply the function that is being tested.
    cleaned = bike.castCleanData(raw)

    # if it did not return a list of items
    if len(cleaned) == 0:
        print('Failed to read data')
        return False

    for station in cleaned:
        # if a station has an irregular amount of data
        if len(station) != 7:
            print('A station has irregular list')
            return False

        for item in station:
            # if a datum is empty
            if item == None or item == [] or item == '':
                print('Bad item in station')
                return False
            # if a data point contains special chars
            if type(item) == str and (
                    '\t' in item or '\r' in item or '\n' in item):
                print('Item has special chars')
                return False

    return True


def checkGetIdList():
    '''A function that returns a boolean value indicating if the
    getIdList function is working as expected. It will print
    a short description of the error if it catches one. '''

    # load in fresh data
    dataSource = "http://research.cs.queensu.ca/home/cords2/bikes.txt"
    bikeData = bike.castCleanData(bike.readData(dataSource))

    # generate the id list to check
    idList = bike.getIdList(bikeData)

    # check every id
    for id in idList:

        # check for correct data types
        if type(id) != str:
            print('Id is the wrong type')
            return False
        # check that each id is indeed a number but in string form
        try:
            int(id)
        except:
            print('There is an id that cannot be converted to int')
            return False
    # if some ids were missed or extras were introduced.
    if len(idList) != len(bikeData) - 1:
        print('There is an incorrect number of ids')
        return False

    return True


def checkRentBike():
    '''A function that ensures the rentBike function is working
    in all cases, and returns False if it is not along with
    printing a short error message. '''

    # load in fresh data
    dataSource = "http://research.cs.queensu.ca/home/cords2/bikes.txt"
    bikeData = bike.castCleanData(bike.readData(dataSource))
    idList = bike.getIdList(bikeData)

    # call the rentbike function on every station
    output = [bike.rentBike(id, bikeData) for id in idList]
    for x in output:
        # if the function did not return True for Success or False for fail
        if x[0] != True and x[0] != False:
            print('Error in renting bikes.')
            return False

    # call the rentbike function on fictitious data it should be able to handle
    output2 = [bike.rentBike(id, bikeData) for id in ['fakeId', '',
                                                      '1234', 'alsonotid']]
    for x in output2:
        # if the function does not return the appropriate error code
        if x[0] != 'ErrorNotFound':
            print('Error in handling bad ids.')
            return False
    return True


def checkReturnBike():
    '''A function that tests to ensure the returnBike function is
    working as expected in all cases, returning False while printing
    an error message if this is not the case. '''

    # load fresh data
    dataSource = "http://research.cs.queensu.ca/home/cords2/bikes.txt"
    bikeData = bike.castCleanData(bike.readData(dataSource))
    idList = bike.getIdList(bikeData)

    # check the function on legitimate inputs
    output = [bike.returnBike(id, bikeData) for id in idList]
    for x in output:
        # if there is no success/fail boolean returned
        if x[0] != True and x[0] != False:
            print('Error in renting bikes.')
            return False

    # check the function on bad inputs
    output2 = [bike.returnBike(id, bikeData) for id in ['fakeId', '',
                                                        '1234', 'alsonotid']]
    for x in output2:
        # if the proper error code is not returned
        if x[0] != 'ErrorNotFound':
            print('Error in handling bad ids.')
            return False

    return True


def checkLookupStation():
    '''A function that checks whether the lookup station function
    is working in all cases, returning a boolean value indicating
    True or False. It also prints a short message hinting at the
    possible error. '''

    # load fresh data
    dataSource = "http://research.cs.queensu.ca/home/cords2/bikes.txt"
    bikeData = bike.castCleanData(bike.readData(dataSource))
    idList = bike.getIdList(bikeData)

    # lookup every station
    outputList = [bike.lookupStation(id, bikeData) for id in idList]
    for output in outputList:

        # check if a value in idList cannot be looked up
        if output == 'ErrorNotFound':
            print('bad id in idlist')
            return False

        # check if an output does not meet the description of a station
        elif len(output) != 7:
            print('An output does not have the right number of items.')
            return False

    return True


def checkCheckBikeAvailability():
    '''A function that tests to ensure the checkBikeAvailability function is
    working as expected in all cases, returning False while printing
    an error message if this is not the case. '''

    # load in fresh data
    dataSource = "http://research.cs.queensu.ca/home/cords2/bikes.txt"
    bikeData = bike.castCleanData(bike.readData(dataSource))
    idList = bike.getIdList(bikeData)

    # check the availability of every station
    outputs = [bike.checkBikeAvailability(id, bikeData) for id in idList]
    for output in outputs:
        # if the output is not an integer
        if type(output) != int:
            print('bike availability is not an int.')
            return False

    return True


def checkGet5thElem():
    '''A function that tests to ensure the get5thElem function is
        working as expected in all cases, returning False while printing
        an error message if this is not the case. '''

    # load in fresh data
    dataSource = "http://research.cs.queensu.ca/home/cords2/bikes.txt"
    bikeData = bike.castCleanData(bike.readData(dataSource))

    # for every station
    for station in bikeData:
        # ensure the 5th item is returned by get5thElem
        if station[5] != bike.get5thElem(station):
            print('Returning incorrect 5th element. ')
            return False

    return True


def checkListAvailable():
    '''A function that tests to ensure the listAvailable function is
        working as expected in all cases, returning False while printing
        an error message if this is not the case. '''

    # load in fresh data
    dataSource = "http://research.cs.queensu.ca/home/cords2/bikes.txt"
    bikeData = bike.castCleanData(bike.readData(dataSource))

    # create a list of stations with bikes available
    stationsWithBikes = bike.listAvailable(bikeData)
    for i in range(len(stationsWithBikes)):
        # make sure no stations have less than 1 bike
        if stationsWithBikes[i][5] < 1:
            print('A station has less than 1 bike. ')
            return False
        # make sure that every station
        # does not have more bikes than the previous station
        if i > 0 and stationsWithBikes[i][5] > stationsWithBikes[i - 1][5]:
            print('The stations are not sorted properly. ')
            return False

    return True


def checkListFull():
    '''A function that tests to ensure the listFull function is
        working as expected in all cases, returning False while printing
        an error message if this is not the case. '''

    # load in fresh data
    dataSource = "http://research.cs.queensu.ca/home/cords2/bikes.txt"
    bikeData = bike.castCleanData(bike.readData(dataSource))

    # get a list of full stations
    fullStations = bike.listFull(bikeData)
    for station in fullStations:
        # if the number of bikes available is not zero
        if station[6] != 0:
            print("There is a bike available at a 'full' station. ")
            return False

    return True


def checkNiceLine():
    '''A function that tests to ensure the niceLine function is
        working as expected in all cases, returning False while printing
        an error message if this is not the case. '''

    # load in fresh data
    dataSource = "http://research.cs.queensu.ca/home/cords2/bikes.txt"
    bikeData = bike.castCleanData(bike.readData(dataSource))

    # try applying niceLine to every station
    for station in bikeData:
        try:
            bike.niceLine(station)
        except:
            print('A station could not be converted to a nice line. ')
            return False

    return True


def checkDirectionFromTo():
    '''A function that tests to ensure the directionFromTo function is
        working as expected in all cases, returning False while printing
        an error message if this is not the case. '''

    # load in fresh data
    dataSource = "http://research.cs.queensu.ca/home/cords2/bikes.txt"
    bikeData = bike.castCleanData(bike.readData(dataSource))
    idList = bike.getIdList(bikeData)

    # for every possible permutation of two stations:
    for firstStation in idList:
        for secondStation in idList:
            try:
                # get the direction
                direc = bike.directionFromTo(firstStation, secondStation,
                                             bikeData)
                # make sure it is in the list of possible outputs
                if direc not in ['NORTHEAST', 'NORTHWEST', 'SOUTHEAST',
                                 'NORTH', 'SOUTH', 'WEST', 'EAST',
                                 'Same location.', 'SOUTHWEST']:
                    print('invalid direction')
                    return False
            except:
                print('could not get a direction. ')
                return False

    return True


def simulateUse(turns):
    """A function that will import the data, and then
    randomly do an operation for turns number of times
    where turns is large enough that there is a high
    probability that every sequence if use is explored.
    This will find any cases where the logic will cause
    a runtime error. """

    # load and cast the data
    dataSource = "http://research.cs.queensu.ca/home/cords2/bikes.txt"
    bData = bike.castCleanData(bike.readData(dataSource))
    # get the id lisr
    idList = bike.getIdList(bData)
    bike.intro()

    # the following code will run turns number of times
    for x in range(turns):
        # select a random operation
        choice = random.choice(['1', '2', '3', '4', '5', '6', '7'])

        # try renting a bike
        if choice == '1':
            id = random.choice(idList)
            success, bData = bike.rentBike(id, bData)

        # try returning a bike
        elif choice == '2':
            id = random.choice(idList)
            success, bData = bike.returnBike(id, bData)

        # try checking bike availability
        elif choice == '3':
            id = random.choice(idList)
            numAvailable = bike.checkBikeAvailability(id, bData)

        # try listing bike availability
        elif choice == '4':
            sortedList = bike.listAvailable(bData)

        # try getting a direc
        elif choice == '5':
            idOne = random.choice(idList)
            idTwo = random.choice(idList)
            direction = bike.directionFromTo(idOne, idTwo, bData)

        elif choice == '6':
            id = random.choice(idList)
            output = bike.niceLine(bike.lookupStation(id, bData))

        elif choice == '7':
            fullStations = bike.listFull(bData)

        # lets the user quit the program.
        elif choice == 'q' or choice == 'Q':
            print('Thank-you for using the Toronto Bike Share Program!')
            running = False
            return
        else:
            print('Sorry, your selection is not an option. ')

        # print a status.
        if x % 10000 == 0:
            print("Testing: {}%".format(round(x * 100 / turns, 1)))

    print('Done testing, no runtime errors. ')
    return True


def runAllTests(turns=1000000):
    '''A function to run all of the tests in the functions above.
    It takes no parameters and returns no values. Outputs to screen.'''
    if checkRentBike() and \
            checkReadData() and \
            checkCastCleanData() and \
            checkCheckBikeAvailability() and \
            checkDirectionFromTo() and \
            checkGet5thElem() and \
            checkGetIdList() and \
            checkListAvailable() and \
            checkListFull() and \
            checkLookupStation() and \
            checkNiceLine() and \
            checkReturnBike() and \
            simulateUse(turns):
        print('Passed all tests!')


# runAllTests()
