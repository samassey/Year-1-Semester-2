#The user interface that will take the users guesses and display a hint according to the secret number and the guess.
#This will keep going until the user correctly guesses the secret number.
#A indicates the bulls and B indicates the cows.
#Assume the secret number only has 4 digits.

from PA2_Functions import generateSecretNumber
from PA2_Functions import findBulls
from PA2_Functions import findCows

print "Bulls and Cows Game"

secret = generateSecretNumber()

guess = raw_input("Enter your guess: ")

while(guess != secret):
    bulls = findBulls(secret, guess)
    cows = findCows(secret, guess)
    print str(bulls) + "A" + str(cows) + "B"
    guess = raw_input("Enter your guess: ")

print "That's it!"
