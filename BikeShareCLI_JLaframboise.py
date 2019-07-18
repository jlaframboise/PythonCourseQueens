# Jacob Laframboise
# Python Course
# A file to contain the command line interface code for a
# Toronto bike share program
# Student #: --------
# Last Edited: Nov. 10th, 2018

# import the functions with a short name
import BikeShareFunctions_JLaframboise as logic


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
 functions in the logic file. As their function is 
 clear from looking at the logic function they call, 
 their documentation is short.'''


def callOption1(bData, idList):
    '''A function to get inputs and call the logic.rentBike function'''

    id = input('What station ID (ex. 7000) will you be renting from: ')
    if id in idList:
        success, bData = logic.rentBike(id, bData)
        if success:
            print("A bike was rented.")
        else:
            print(
                "Sorry, there are no bikes available at station {}.".format(id))
    else:
        print("Sorry, {} is not a valid ID.".format(id))


def callOption2(bData, idList):
    '''A function to get inputs and call the logic.returnBike function'''

    id = input('What station ID (ex. 7000) will you be returning to: ')
    if id in idList:
        success, bData = logic.returnBike(id, bData)
        if success:
            print("The bike was returned.")
        else:
            print("Sorry, there are no spaces available at station {}.".format(
                id))
    else:
        print("Sorry, {} is not a valid ID.".format(id))


def callOption3(bData, idList):
    '''A function to get inputs and call the
    logic.checkBikeAvailability function'''

    id = input('What station ID (ex. 7000) will you check: ')
    if id in idList:
        numAvailable = logic.checkBikeAvailability(id, bData)
        print('There are {} bikes available here.'.format(numAvailable))
    else:
        print("Sorry, {} is not a valid ID.".format(id))


def callOption4(bData):
    '''A function to get inputs and call the
    logic.listAvailable function'''

    print('Listing stations filtered by bikes available: ')
    sortedList = logic.listAvailable(bData)
    for station in sortedList:
        print(logic.niceLine(station))


def callOption5(bData, idList):
    '''A function to get inputs and call the
        logic.directionFromTo function'''

    idOne = input("What station will you be departing from: ")
    idTwo = input("What station will you be heading to: ")

    # get the direction from one valid id to another
    if idOne in idList and idTwo in idList:
        direction = logic.directionFromTo(idOne, idTwo, bData)
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
    logic.lookupStation function'''

    id = input("What station ID (ex. 7000) will you look up: ")
    if id in idList:
        print(logic.niceLine(logic.lookupStation(id, bData)))
    else:
        print("Sorry, {} is not a valid ID.".format(id))


def callOption7(bData):
    '''A function to get inputs and call the
        logic.listFull function'''

    print('Listing all stations with full capacity: ')
    fullStations = logic.listFull(bData)
    for station in fullStations:
        print(logic.niceLine(station))


def main():
    '''A main function that allows the user to use all the
    functionality contained in all the functions. This function
    takes no parameters and returns None. It consists of a
    couple lines to load the data, then enters the main loop.
    In the main loop the menu is repeatedly printed and the
    user gets to select an options which calls the corresponding code. '''

    # load and cast the data
    dataSource = "http://research.cs.queensu.ca/home/cords2/bikes.txt"
    bData = logic.castData(logic.readData(dataSource))
    idList = logic.getIdList(bData)
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
