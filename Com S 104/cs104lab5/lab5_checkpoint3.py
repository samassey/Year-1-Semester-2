#Checkpoint three: a script to play the game Guess and Win

print "Try to guess a number between 1 to 10"

x = input("What's your first guess? ")

from random import randint

r = randint(1,10)

while(x != r):
    if(x > r):
        print "Too high!"
        x = input("What's your next guess? ")
    if(x < r):
        print"Too low!"
        x = input("What's your next guess? ")
print "That's it!"
