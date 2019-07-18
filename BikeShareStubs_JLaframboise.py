# Jacob Laframboise
# Python Course
# A file to contain the back end code stubs for the
# Toronto bike share program
# Student #: --------
# Last Edited: Nov. 10th, 2018

# for accessing the data.
import urllib.request


'''Note:
        As these are just stubs, the output does not necessarily make sense,
        but it is the correct data types. '''

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

    return [['station_id', 'name', 'lat', 'lon', 'capacity', 'num_bikes_available', 'num_docks_available'],
            ['7000', 'Ft. York / Capreol Crt.', 43.639832, -79.395954, 31, 20, 11],
            ['7001', 'Lower Jarvis St / The Esplanade', 43.647992, -79.370907, 15, 5, 10],
            ['7002', 'St George St / Bloor St W', 43.667333, -79.399429, 19, 1, 18],
            ['7003', 'Madison Ave / Bloor St W', 43.667158, -79.402761, 15, 2, 13],
            ['7004', 'University Ave / Elm St', 43.656518, -79.389099, 11, 0, 11],
            ['7005', 'University Ave / King St W', 43.648093, -79.384749, 19, 0, 18],
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


    return ['7000', 'Ft. York / Capreol Crt.', 43.639832, -79.395954, 31, 20, 11]


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

    sortList = [['7000', 'Ft. York / Capreol Crt.', 43.639832, -79.395954, 31, 20, 11],
                ['7007', 'College St / Huron St', 43.658148, -79.398167, 11, 11, 0],
    ['7001', 'Lower Jarvis St / The Esplanade', 43.647992, -79.370907, 15, 5, 10],
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