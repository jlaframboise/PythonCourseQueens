def checkCallOption1():
    '''A function that takes the function from the program file
    and redefines the input function in the other file to
    return the input that should be run in the test case in
    this function, and redefines that input function back
    to normal when done. '''
    dataSource = "http://research.cs.queensu.ca/home/cords2/bikes.txt"
    bikeData = bike.castCleanData(bike.readData(dataSource))
    idList = bike.getIdList(bikeData)
    for id in idList:
        bike.input = lambda x: id
        output = bike.callOption1(bikeData, idList)
    bike.input = input


def checkCallOption2():
    '''A function that takes the function from the program file
    and redefines the input function in the other file to
    return the input that should be run in the test case in
    this function, and redefines that input function back
    to normal when done. '''
    dataSource = "http://research.cs.queensu.ca/home/cords2/bikes.txt"
    bikeData = bike.castCleanData(bike.readData(dataSource))
    idList = bike.getIdList(bikeData)
    for id in idList:
        bike.input = lambda x: id
        output = bike.callOption2(bikeData, idList)
    bike.input = input


def checkCallOption3():
    '''A function that takes the function from the program file
    and redefines the input function in the other file to
    return the input that should be run in the test case in
    this function, and redefines that input function back
    to normal when done. '''
    dataSource = "http://research.cs.queensu.ca/home/cords2/bikes.txt"
    bikeData = bike.castCleanData(bike.readData(dataSource))
    idList = bike.getIdList(bikeData)
    for id in idList:
        bike.input = lambda x: id
        output = bike.callOption3(bikeData, idList)
    bike.input = input


def checkCallOption4():
    '''A function that takes the function from the program file
    and redefines the input function in the other file to
    return the input that should be run in the test case in
    this function, and redefines that input function back
    to normal when done. '''
    dataSource = "http://research.cs.queensu.ca/home/cords2/bikes.txt"
    bikeData = bike.castCleanData(bike.readData(dataSource))
    output = bike.callOption4(bikeData)


def checkCallOption5():
    '''A function that takes the function from the program file
    and redefines the input function in the other file to
    return the input that should be run in the test case in
    this function, and redefines that input function back
    to normal when done. '''
    dataSource = "http://research.cs.queensu.ca/home/cords2/bikes.txt"
    bikeData = bike.castCleanData(bike.readData(dataSource))
    idList = bike.getIdList(bikeData)
    for id in idList:
        for id2 in idList:
            bike.input = lambda x: id
            output = bike.callOption1(bikeData, idList)
    bike.input = input


def checkCallOption6():
    '''A function that takes the function from the program file
    and redefines the input function in the other file to
    return the input that should be run in the test case in
    this function, and redefines that input function back
    to normal when done. '''
    dataSource = "http://research.cs.queensu.ca/home/cords2/bikes.txt"
    bikeData = bike.castCleanData(bike.readData(dataSource))
    idList = bike.getIdList(bikeData)
    for id in idList:
        bike.input = lambda x: id
        output = bike.callOption1(bikeData, idList)
    bike.input = input


def checkCallOption7():
    '''A function that takes the function from the program file
    and redefines the input function in the other file to
    return the input that should be run in the test case in
    this function, and redefines that input function back
    to normal when done. '''
    dataSource = "http://research.cs.queensu.ca/home/cords2/bikes.txt"
    bikeData = bike.castCleanData(bike.readData(dataSource))
    idList = bike.getIdList(bikeData)
    for id in idList:
        bike.input = lambda x: id
        output = bike.callOption1(bikeData, idList)
    bike.input = input
