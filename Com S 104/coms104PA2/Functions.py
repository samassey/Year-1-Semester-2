#Holds all the functions needed to play the game of Bulls and Cows with a user.
#The user will guess a secret randomly generated number buy the generateSecretNumber function.
#To win the game the user must correctly guess all of the digits and all of their placements to perfectly match the secret number. 


#Used to generate the random number.
from random import randint


#Generates the random number that the user will need to try and guess.
#The numbers are generated between 0 and 9999.
#Returns the generated number as a string. 
def generateSecretNumber():
    randomInt = randint(0,9999)
    stringRandomInt = str(randomInt)
    length = len(stringRandomInt)
    finalInt = ((4-length)*"0" + stringRandomInt)
    return finalInt

#Takes a string value as a parameter, s, and returns a list of unique digits in s.
def findUniqueDigits(s):
    uniqueDigits = []
    for i in s:
        if(i == "0"):
            uniqueDigits.add(i)
    return uniqueDigits

#Takes two string values as parameters, secret and guess, and returns the number of digits in guess that match the secret exactly.
#To match it needs the same position and value.
#Assume there are exactly 4 digits in both values. 
def findBulls(secret, guess):
    bulls = 0
    indexList = [0, 1, 2, 3]
    for i in indexList:
        if(guess[i] == secret[i]:
           bulls += 1
    return bulls

#Takes two strings as the parameters, secret and guess, and returns the number of digits in guess that match the sectret.
#They must match in only value not position.
#Assume there are exactly 4 digits in both values.
def findCows(secret, guess):
    bothBC = 0
    secretUniDigits = findUniqueDigits(secret)
    for i in secretUniDigits:
        secretCount = secret[i]
        guessCount = guess[i]
        if(secretCount < guessCount):
           bothBC += secretCount
        else:
           bothBC += guessCount
    bulls = findBulls(secret, guess)
    return bothBC - bulls
