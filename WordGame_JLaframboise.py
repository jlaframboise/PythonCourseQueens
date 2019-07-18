# Jacob Laframboise
# Oct. 3rd, 2018
# Student No. --------

'''A program to play a word guessing game with the user.
The user is given a start and end letters, and they get to
guess a word which matches the criteria. The word is then
checked against a dictionary modified from the on at:
"http://www.mit.edu/~ecprice/wordlist.10000"
If the word is valid, the user is scored points on the
length of the word and the letters they used. Score is
tracked through multiple rounds and displayed to the user at the end.'''

# for character selection
import random
# this loads a library you will need - put this at top of file.
import urllib.request

'''A function to read in the dictionary data from the internet 
at the url specified in the function below. It uses the urllib 
library, and takes no paramteters and returns the data as a list.'''


def readWordList():
    # get data from internet
    response = urllib.request.urlopen("http://www.mit.edu/~ecprice/wordlist.10000")
    html = response.read()
    data = html.decode('utf-8').split()  # decode and split to a list
    return data


'''A function to check to see if a word needs to be removed. 
A word needs to be removed if it is a repetition of the same 
character more than once with no other characters. it takes the 
word as a string paramtet, and returns a boolean value, 
True for valid, andFalse for needing to be removed. '''


def checkWord(word):
    length = len(word)
    if length == 1:  # it is good if it is a one letter word
        return True
    for letter in word:
        if letter != word[0]:  # if there is more than 1 different letter
            return True
    return False  # if neither clause above is true, it must need to be removed.


'''A function to 'clean' a list of words of the non-words described in
 the docstring for checkWord. It takes the list of words as input, 
 and returns a new list without the bad words as list output. '''


def cleanWordList(words):
    cleanWords = []
    for word in words:
        if checkWord(word):  # only add the valid words to the new list
            cleanWords.append(word)
    return cleanWords  # return the new list without the repeat chars.


'''A function to randomly select a character from a to z for 
the end char and thestart char. it takes no paramters, and 
returns the startChar and the endChar as strings. '''


def pickChars():
    letters = 'abcdefghijklmnopqrstuxwxyz'
    # random library is used to choose a random letter from a list
    startChar = letters[random.randint(0, 25)]
    endChar = letters[random.randint(0, 25)]
    return startChar, endChar


'''A function to run the intro text and see if the user wants to play the game. 
The user is asked to hit enter to play, and if they do anything else the game
will not run. The function returns True if the user hits enter to play, and False
if they do anything else. '''


def intro():
    # tell them how the game will be played
    print('Welcome to the word guessing game!')
    print('In this game, you will be given a starting and an ending character,')
    print('and your goal is to think of a word which fits those characters!')
    print()
    print('Be careful, if the word is not valid I will know... ')
    print('At the end of the game you will have a score of how well you did!')
    print()
    # let them just press enter to play, if the put anything else, don't play
    if input("Press enter to begin: ") == '':
        return True
    else:
        return False


'''A function to calculate and return the score associated with a given string
based on the system outlined in the assignment description. It assigns a value for 
each character as seen in the dictionary, and them gives a bonus for the length,
and if the end char and the start char are the same. '''


def getWordScore(word):
    # the corresponding value for each letter
    letter_values = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 1, 'f': 5, 'g': 2,
                     'h': 3, 'i': 1, 'j': 9, 'k': 5, 'l': 1,
                     'm': 2, 'n': 2, 'o': 1, 'p': 4, 'q': 15, 'r': 1, 's': 1,
                     't': 1, 'u': 1, 'v': 8, 'w': 4, 'x': 15,
                     'y': 4, 'z': 15}
    score = 0  # initialize
    for x in word:  # add the score for every letter
        score += letter_values[x]
    # add the bonus for word length
    if len(word) > 8:
        score += 6
    elif len(word) > 7:
        score += 5
    elif len(word) > 6:
        score += 4
    elif len(word) > 5:
        score += 3

    # ad the bonus for the same start and end char
    if word[0] == word[-1]:
        score += 10

    return score


'''A function to drive the various functions to play a round of the game with the 
user. it takes in the list of possible words as a list input parameter, 
and will output an integer corresponding to the score the user earned 
as output. It interacts with the user with  print and input statements
to drive the round. '''


def playRound(words):
    # pick the characters
    startChar, endChar = pickChars()
    print('Your starting letter is: ' + startChar)
    print('Your ending letter is: ' + endChar)
    print()
    # get the user's attempt
    word = input("What is the complete word with these letters?: ")

    # if the word is in the dictionary, and matches criteria
    if word.lower() in words and word[0].lower() == startChar \
            and word[-1].lower() == endChar:
        scoreEarned = getWordScore(word.lower())
        print('Congratulations! {} is correct for {} points!'.format(word, scoreEarned))
        print()

    # if the word matches the criteria but is not a word
    elif word[0].lower() == startChar and word[-1].lower() == endChar:
        scoreEarned = -10  # negative score
        print('Oh no! {} is not a complete word!'.format(word))
        print('You lost 10 points!')
        print('Remember to try a complete english word.')
        print()
    # if the word does not match criteria and may or may not be a word
    else:
        scoreEarned = -2  # negative score
        print("Oh no! '{}' does not start with '{}' "
              "and end with '{}'.".format(word, startChar, endChar))
        print("You lost 2 points!")
        print("Remember to try a word that begins with "
              "and ends with the given characters!")

    return scoreEarned


'''This is the main function, which will run all the functions above to play the game. 
First it runs the intro, then retrieves and cleans the word list from the internet, 
then it starts a game loop which contains calls to the payRound function to play
 rounds until the user wants to quit, and then the user can type q to quit. 
 Then their score is outputted and the program will finish execution. '''


def main():
    # run the intro, if the user does not press enter to play, end main
    if not intro():
        print('Maybe next time! Just rerun me to play again. ')
        return

    words = cleanWordList(readWordList())  # clean the wordlist
    score = 0

    # play five rounds
    for round in range(5):
        try:  # try and except in case the user hits enter before typing anything.
            score += playRound(words)  # repetitively play rounds
            if round < 4:
                print('Your points: {}'.format(score))

            # let the user quit if they like before round 5
            if round < 4 and \
                    input("Press enter to play again or type 'q' to finish: ") == 'q':
                break
            elif round > 3:  # end after 5 rounds
                break
            else:
                print()
        except:
            print()
            print('Oh no! An error has occurred :(')
            print()

    # tell the user how they did on the way out
    print('Great game! You scored {} points.'.format(score))
    print('Thanks for playing!')


'''A function to test the pickChars function to see if 
a and z will be chosen fairly. Will print success if
it is generating a and z.'''


def testRandomChoice():
    letterList = []
    for x in range(1000):
        a, b = pickChars()
        letterList.append(a)
        letterList.append(b)
    if 'a' in letterList and 'z' in letterList:
        print('Success: a and z are being chosen.')


'''A function to check what words are being cleaned 
by the cleaning function. Prints out all the removed
words for verification.'''


def testCleaner():
    wordList = readWordList()
    print('There are {} words.'.format(len(wordList)))
    cleanWords = cleanWordList(wordList)
    badWords = []
    # make a list of the removed words
    for x in wordList:
        if x not in cleanWords:
            badWords.append(x)
    print('The words removed are:')
    for x in badWords:
        print(x)
    if len(badWords) == len(wordList) - len(cleanWords):
        print('The lengths add up.')


'''A function to test the cleanser on a very small list of 
important cases. prints out the original list and the 
list of remaining words'''


def testCleaner2():
    wordList = ['a', 'ab', 'aab', 'aaa', 'bbbbcq', 'a',
                'zzzzzzzzzzzzzzzzzzzzzzzzzzzzzz', '', 'zzzzzzzzzzzzqz']
    wordList2 = cleanWordList(wordList)
    print(wordList)
    print(wordList2)


main()
