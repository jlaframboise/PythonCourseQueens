# Jacob Laframboise
# Python Course
# A file to contain the command line interface code
# and implementation function stubs for a
# Toronto bike share program
# Student #: --------
# Last Edited: Nov. 10th, 2018


'''--------Implementation Functions--------'''

'''Note:
        As these are just stubs, the output does not necessarily make sense,
        but it is the correct data type. '''


def readData(url):
    '''a function which loads the data about the bike share network,
    removes special characters and splits each stations data to a
    list the parameter is the string url of the site with the data
    the function returns a list of lists, where each list holds
    data for one station, having the following
    string elements in order:
    o	station ID
    o	name of station
    o	latitude
    o	longitude
    o	capacity (total number of bike positions, filled or not)
    o	bikes available: number of bikes at station
    o	docks available: number of empty bike docks at station
    '''

    return [
        ['station_id', 'name', 'lat', 'lon', 'capacity', 'num_bikes_available',
         'num_docks_available'],
        ['7000', 'Ft. York / Capreol Crt.', 43.639832, -79.395954, 31, 20, 11],
        ['7001', 'Lower Jarvis St / The Esplanade', 43.647992, -79.370907, 15,
         5, 10],
        ['7002', 'St George St / Bloor St W', 43.667333, -79.399429, 19, 1, 18],
        ['7003', 'Madison Ave / Bloor St W', 43.667158, -79.402761, 15, 2, 13],
        ['7004', 'University Ave / Elm St', 43.656518, -79.389099, 11, 0, 11],
        ['7005', 'University Ave / King St W', 43.648093, -79.384749, 19, 0,
         18],
        ['7006', 'Bay St / College St', 43.66009, -79.385653, 11, 0, 11],
        ['7007', 'College St / Huron St', 43.658148, -79.398167, 11, 11, 0]]


def castData(bikeData):
    '''A function which casts the data for each station as the correct
     data types. The parameter is the list of lists which is the data
     for all the stations Will return the list of lists, with each sub
     list’s elements casted to the correct type.
    '''

    return [
        ['station_id', 'name', 'lat', 'lon', 'capacity', 'num_bikes_available',
         'num_docks_available'],
        ['7000', 'Ft. York / Capreol Crt.', 43.639832, -79.395954, 31, 20, 11],
        ['7001', 'Lower Jarvis St / The Esplanade', 43.647992, -79.370907, 15,
         5, 10],
        ['7002', 'St George St / Bloor St W', 43.667333, -79.399429, 19, 1, 18],
        ['7003', 'Madison Ave / Bloor St W', 43.667158, -79.402761, 15, 2, 13],
        ['7004', 'University Ave / Elm St', 43.656518, -79.389099, 11, 0, 11],
        ['7005', 'University Ave / King St W', 43.648093, -79.384749, 19, 0,
         18],
        ['7006', 'Bay St / College St', 43.66009, -79.385653, 11, 0, 11],
        ['7007', 'College St / Huron St', 43.658148, -79.398167, 11, 11, 0]]


def getIdList(bikeData):
    '''A function which takes a list of lists,
    and returns a list of the first element in
    each list. '''

    idList = ['7000', '7001', '7002', '7003', '7004', '7005', '7006', '7007']
    return idList


def rentBike(stationId, bikeData):
    '''a function to remove a bike from a station if there is a bike available
    takes the string station id and the list of lists with the data,
    and looks up the station.
    returns True if a bike is rented, and False if none are available
    returns modified bikeData
    '''

    return True, bikeData


def returnBike(stationId, bikeData):
    '''a function to add a bike to a station if a bike dock is available,
    modifies takes the string station id for lookup in the list of lists,
    modifies the list
    returns True if a bike is returned, False if the station is full
    returns modified bikedata
    '''

    return True, bikeData


def checkBikeAvailability(stationId, bikeData):
    '''A function to return the number of bikes available at a given station
    Parameters are the string station id, and the lists of lists holding
    the bike share data
    Returns the integer number of bikes available.
    '''

    return 5


def lookupStation(stationId, bikeData):
    '''A function which searches for a station with given id
    in the list of lists
    Parameters are the string station id to search for, and the list of lists
    Returns the list of data points for the specific station.
    '''

    return ['7000', 'Ft. York / Capreol Crt.', 43.639832, -79.395954, 31, 20,
            11]


def get5thElem(item):
    '''A function to return the 5th indexed item of a list, for use in sorting.
    Parameter is the list
    Returns the item, in this project’s use case it will be the
    number of bikes available.
    '''

    return 5


def listAvailable(bikeData):
    '''A function to sort the list of lists by the number of bikes
    available in each sub list, and truncate the list when number of
    bikes is zero
    Parameter is the list of list holding data for our bike network
    Returns a list of lists sorted by element 5 in each sub list
    '''

    sortList = [
        ['7000', 'Ft. York / Capreol Crt.', 43.639832, -79.395954, 31, 20, 11],
        ['7007', 'College St / Huron St', 43.658148, -79.398167, 11, 11, 0],
        ['7001', 'Lower Jarvis St / The Esplanade', 43.647992, -79.370907, 15,
         5, 10],
        ['7003', 'Madison Ave / Bloor St W', 43.667158, -79.402761, 15, 2, 13],
        ['7002', 'St George St / Bloor St W', 43.667333, -79.399429, 19, 1, 18]]

    return sortList


def listFull(bikeData):
    '''A function to list all of the sub lists for stations with no more
    bike space left.
    Parameter is the list of lists containing the data for the bike network
    Returns a list of lists where each sub list is a station at max capacity
    '''

    return [['7007', 'College St / Huron St', 43.658148, -79.398167, 11, 11, 0]]


def niceLine(station):
    '''A function to convert a list for a station to a nice one line string
    to print.
    Parameter is a list corresponding to a station
    Returns a string containing data from the station.
    '''

    return "Station 7007 at College St / Huron St(43.658148, -79.398167) has " \
           "11 bike(s) and 0 empty dock(s)" \
           " out of 11 total spot(s)."


def directionFromTo(stationIdA, stationIdB, bikeData):
    '''A function to compare the latitude and longitude between two stations
    to determine what direction someone at stationA
    should walk to reach station B
    Parameters are the string id of the first station, the string id of
    the second station, and the list of lists which holds the
    data for the bike network
    Returns the direction to travel as a string.
    '''

    return 'NORTHEAST'


'''--------Command Line Interface Functions--------'''


def intro():
    '''A function to introduce the user to the program
    with a series of print statements that will be printed
    at run time. It takes no parameters and returns None'''

    print('Welcome to the Toronto Bike Share Program.')
    print()
    print('This is a service which allows users to rent bikes')
    print('from locations all over the city. You may return the')
    print('bike at any location which has docks left. ')
    print('This program is a system to rent, return, and ')
    print('provide information about the status of the bike')
    print('share system.')
    print()


def menu():
    '''A series of print statements that list of the various
    options that the user can choose from. It takes no
    parameters and returns their string input as to what
    operation they want to do. '''

    print('Please select from the list of operations:')
    print('\t1. Rent a bike.')
    print('\t2. Return a bike.')
    print('\t3. Check bikes available at location by ID.')
    print('\t4. List locations by # bikes available. ')
    print('\t5. Direction from a station to another. ')
    print('\t6. Lookup detailed station data by ID.')
    print('\t7. List all full stations.')
    print('\tq. Quit the program. ')
    print()
    return input("Enter the character for an option: ")


'''The next series of functions are designed to reduce
 the size of the main function by running the code to 
 get necessary inputs from the user to call the 
 functions in the logic file. They handle letting 
 the user know when an error is caught. As their function is 
 clear from looking at the logic function they call, 
 their documentation is short.'''


def callOption1(bData, idList):
    '''A function to get inputs and call the rentBike function'''

    id = input('What station ID (ex. 7000) will you be renting from: ')
    if id in idList:
        success, bData = rentBike(id, bData)
        if success:
            print("A bike was rented.")
        else:
            print(
                "Sorry, there are no bikes available at station {}.".format(id))
    else:
        print("Sorry, {} is not a valid ID.".format(id))


def callOption2(bData, idList):
    '''A function to get inputs and call the returnBike function'''

    id = input('What station ID (ex. 7000) will you be returning to: ')
    if id in idList:
        success, bData = returnBike(id, bData)
        if success:
            print("The bike was returned.")
        else:
            print("Sorry, there are no spaces available at station {}.".format(
                id))
    else:
        print("Sorry, {} is not a valid ID.".format(id))


def callOption3(bData, idList):
    '''A function to get inputs and call the
    checkBikeAvailability function'''

    id = input('What station ID (ex. 7000) will you check: ')
    if id in idList:
        numAvailable = checkBikeAvailability(id, bData)
        print('There are {} bikes available here.'.format(numAvailable))
    else:
        print("Sorry, {} is not a valid ID.".format(id))


def callOption4(bData):
    '''A function to get inputs and call the
    listAvailable function'''

    print('Listing stations filtered by bikes available: ')
    sortedList = listAvailable(bData)
    for station in sortedList:
        print(niceLine(station))


def callOption5(bData, idList):
    '''A function to get inputs and call the
        directionFromTo function'''

    idOne = input("What station will you be departing from: ")
    idTwo = input("What station will you be heading to: ")

    # get the direction from one valid id to another
    if idOne in idList and idTwo in idList:
        direction = directionFromTo(idOne, idTwo, bData)
        if direction != 'Same location.':
            print("Travel {}.".format(direction))
        else:
            print(direction)

    # tell the user if either or both ids are not valid.
    elif idOne not in idList and idTwo not in idList:
        print("Sorry, {} and {} are not valid stations ID's.".format(idOne,
                                                                     idTwo))

    elif idOne not in idList:
        print("Sorry, {} is not a valid ID.".format(idOne))

    else:
        print("Sorry, {} is not a valid ID.".format(idTwo))


def callOption6(bData, idList):
    '''A function to get inputs and call the
    lookupStation function'''

    id = input("What station ID (ex. 7000) will you look up: ")
    if id in idList:
        print(niceLine(lookupStation(id, bData)))
    else:
        print("Sorry, {} is not a valid ID.".format(id))


def callOption7(bData):
    '''A function to get inputs and call the
        listFull function'''

    print('Listing all stations with full capacity: ')
    fullStations = listFull(bData)
    for station in fullStations:
        print(niceLine(station))


def main():
    '''A main function that allows the user to use all the
    functionality contained in all the functions. This function
    takes no parameters and returns None. It consists of a
    couple lines to load the data, then enters the main loop.
    In the main loop the menu is repeatedly printed and the
    user gets to select an options which calls the corresponding code. '''

    # load and cast the data
    dataSource = "http://research.cs.queensu.ca/home/cords2/bikes.txt"
    bData = castData(readData(dataSource))
    idList = getIdList(bData)
    intro()

    # main loop of the program
    running = True
    while running:
        # let the user make a choice
        choice = menu()
        print()

        # This if statement executes a function call
        #  to a function which implements the
        # operation corresponding to the user's choice
        if choice == '1':
            callOption1(bData, idList)

        elif choice == '2':
            callOption2(bData, idList)

        elif choice == '3':
            callOption3(bData, idList)

        elif choice == '4':
            callOption4(bData)

        elif choice == '5':
            callOption5(bData, idList)

        elif choice == '6':
            callOption6(bData, idList)

        elif choice == '7':
            callOption7(bData)

        # lets the user quit the program.
        elif choice == 'q' or choice == 'Q':
            print('Thank-you for using the Toronto Bike Share Program!')
            running = False
            return
        else:
            print('Sorry, your selection is not an option. ')
        print()


main()
