info = [4,5,[10,20],'fox', 'cnn', 'abc', ['cisc', 'bio']]

if 10 in info:
    print('True')

print(print('sup'))

five = ['a', 'b']
for x in five:
    #five.append('x')
    print('hi')

s = 'Holidays'
ns = s[1::2]
ns2 = s[4:7]
print(ns, ns2)

def updateValue(value):
    value = value + 5
    return value

speed = 10
updateValue(speed)

speech = 'to be or not to be'
speechList = speech.split()

dict = {}
for word in speechList:
    if word in dict:
        dict[word] = dict[word]+1
    else:
        dict[word] = 1

print(dict)


def priceCalculator(mealPrice, tipAmt, taxRate = .13):
    print(mealPrice, tipAmt, taxRate)

priceCalculator(tipAmt=5, mealPrice=89)
#priceCalculator(taxRate=.1, mealPrice=79)

myList = []
for i in range(0,6,2):
    for k in range(4):
        myList.append(i+k)
print()
print(i)
print(k)
print(myList)

def removeLetter(s, let):
    places = []
    for x in range(len(s)):
        if s[x] != let:
            places = places + [x]
    newString = ''
    for place in places:
        newString = newString + s[place]
    return newString

print(removeLetter('Hello world', 'e'))

card = [['X', 'X', 'X'],
        ['X', 'X', 'X'],
        ['X', 'X', 'X'],
        ['X', 'X', 'X']]
card2 = [['X', 'p', 'y'],
        ['l', 'X', 'z'],
        ['a', 'b', 'X']]

card3 = [['X', 'p', 'X'],
        ['X', 'X', 'z'],
        ['X', 'b', 'X']]

def fullCardCheck(card):
    bingo = True
    for x in card:
        for y in x:
            if y!='X':
                bingo = False
    return bingo

def diagCardCheck(card):
    if len(card) != len(card[0]):
        return False
    bingo =True
    for rowNum in range(len(card)):
        if card[rowNum][rowNum]!='X':
            bingo = False
    if bingo == False:
        bingo = True
        for rowNum in range(len(card)):
            if card[::-1][rowNum][rowNum] != 'X':
                bingo = False
    return bingo

print(diagCardCheck(card))

print('aaa'>'aaaaa')

t = (500)
t+=5
print(t)


def binSearch(lis, tar):
    high = len(lis)-1
    low = 0
    found = False

    while high>=low and not found:
        mid = (high+low)//2
        guess = lis[mid]
        if guess==tar:
            return True
        elif guess > tar:
            high = mid-1
        else:
            low = mid+1
    return found

print(binSearch([2,5,6,7,8,9,10,11],7))