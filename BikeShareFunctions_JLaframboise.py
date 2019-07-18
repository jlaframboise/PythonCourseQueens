# Jacob Laframboise
# Python Course
# A file to contain the back end code for a
# Toronto bike share program
# Student #: --------
# Last Edited: Nov. 10th, 2018

# for accessing the data.
import urllib.request


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

    response = urllib.request.urlopen(url)
    html = response.readlines()
    # for every line in html, the next line decodes the data,
    # removes special characters,
    # and splits in into a sub list by the tab character.
    data = [line.decode('utf-8').strip().split('\t') for line in
            html]
    return data


def castData(bikeData):
    '''A function which casts the data for each station as the correct
     data types. The parameter is the list of lists which is the data
     for all the stations Will return the list of lists, with each sub
     list’s elements casted to the correct type.
    '''

    # use list comprehension to create a new list identical to the first,
    # but with different data types.
    newBikeData = [[station[0], station[1],
                    float(station[2]), float(station[3]),
                    int(station[4]), int(station[5]), int(station[6])]
                   for station in bikeData[1::]]

    # add the 'titles' list to the front.
    newBikeData = [bikeData[0]] + newBikeData
    return newBikeData


def getIdList(bikeData):
    '''A function which takes a list of lists,
    and returns a list of the first element in
    each list. '''

    idList = [station[0] for station in bikeData]
    return idList


def rentBike(stationId, bikeData):
    '''a function to remove a bike from a station if there is a bike available
    takes the string station id and the list of lists with the data,
    and looks up the station.
    returns True if a bike is rented, and False if none are available
    '''
    # lookup the station
    station = lookupStation(stationId, bikeData)

    # return if the station doesn't exist.
    if station == "ErrorNotFound":
        return station, bikeData

    # if there are bikes available
    if station[5] > 0:
        station[5] -= 1
        station[6] += 1
        return True, bikeData
    else:
        return False, bikeData


def returnBike(stationId, bikeData):
    '''a function to add a bike to a station if a bike dock is available,
    modifies takes the string station id for lookup in the list of lists,
    modifies the list
    returns True if a bike is returned, False if the station is full
    '''

    # lookup the station
    station = lookupStation(stationId, bikeData)

    # return if the station doesn't exist.
    if station == "ErrorNotFound":
        return station, bikeData

    # if there are spots available
    if station[6] > 0:
        station[6] -= 1
        station[5] += 1
        return True, bikeData
    else:
        return False, bikeData


def checkBikeAvailability(stationId, bikeData):
    '''A function to return the number of bikes available at a given station
    Parameters are the string station id, and the lists of lists holding
    the bike share data
    Returns the integer number of bikes available.
    '''

    station = lookupStation(stationId, bikeData)
    return station[5]


def lookupStation(stationId, bikeData):
    '''A function which searches for a station with given id
    in the list of lists
    Parameters are the string station id to search for, and the list of lists
    Returns the list of data points for the specific station.
    '''

    for station in bikeData:
        if station[0] == str(stationId):
            return station
    return "ErrorNotFound"


def get5thElem(item):
    '''A function to return the 5th indexed item of a list, for use in sorting.
    Parameter is the list
    Returns the item, in this project’s use case it will be the
    number of bikes available.
    '''
    return item[5]


def listAvailable(bikeData):
    '''A function to sort the list of lists by the number of bikes
    available in each sub list, and truncate the list when number of
    bikes is zero
    Parameter is the list of list holding data for our bike network
    Returns a list of lists sorted by element 5 in each sub list
    '''

    # create a new bikeData list that is sorted by bike available
    stationsWithBikes = sorted(bikeData[1:], key=get5thElem, reverse=True)

    # iterate through the sorted list till one has no bikes
    for stationNum in range(len(stationsWithBikes)):
        if stationsWithBikes[stationNum][5] == 0:
            # truncate the list before the station with no bikes
            stationsWithBikes = stationsWithBikes[:stationNum]
            break
    return stationsWithBikes


def listFull(bikeData):
    '''A function to list all of the sub lists for stations with no more
    bike space left.
    Parameter is the list of lists containing the data for the bike network
    Returns a list of lists where each sub list is a station at max capacity
    '''

    fullStations = []
    for station in bikeData[1:]:
        if station[6] == 0:
            fullStations.append(station)
    return fullStations


def niceLine(station):
    '''A function to convert a list for a station to a nice one line string
    to print.
    Parameter is a list corresponding to a station
    Returns a string containing data from the station.
    '''

    # string formatting to make a nice sentence
    niceLine = "Station {} at {}({}, {}) has {} bike(s) and {} empty dock(s)" \
               " out of {} total spot(s).".format(
        station[0], station[1], station[2], station[3], station[5], station[6],
        station[4])
    return niceLine


def directionFromTo(stationIdA, stationIdB, bikeData):
    '''A function to compare the latitude and longitude between two stations
    to determine what direction someone at stationA
    should walk to reach station B
    Parameters are the string id of the first station, the string id of
    the second station, and the list of lists which holds the
    data for the bike network
    Returns the direction to travel as a string.
    '''

    # lookup stations
    stationA = lookupStation(stationIdA, bikeData)
    stationB = lookupStation(stationIdB, bikeData)

    # find the lat and lon differences
    latA, lonA = stationA[2], stationA[3]
    latB, lonB = stationB[2], stationB[3]
    latDiff = latB - latA
    lonDiff = lonB - lonA

    # determine latitudinal direction
    if latDiff > 0:
        latDirec = 'NORTH'
    elif latDiff < 0:
        latDirec = 'SOUTH'
    else:
        latDirec = ''

    # determine longitudinal direction
    if lonDiff < 0:
        lonDirec = 'WEST'
    elif lonDiff > 0:
        lonDirec = 'EAST'
    else:
        lonDirec = ''

    # concatenate
    direction = latDirec + lonDirec

    # if the user entered the same station twice
    if direction == '' + '':
        direction = 'Same location.'
    return direction
