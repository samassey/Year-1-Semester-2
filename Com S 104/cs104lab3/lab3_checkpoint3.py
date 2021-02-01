from lab3_checkpoint2 import xFactorial

def permutation_and_combinations (n , r):
    if(r > n):
        print "Sorry you cannot select", r, "elements from a collection of", n, "elements!"
    else:
        per = xFactorial(n) / (xFactorial(n - r))
        com = xFactorial(n) / (xFactorial(r)*xFactorial(n - r))
        print "You have", per, "permutations and", com, "combinations to select!"



x = input("Enter total number of elements in the collection:" )
y = input("Enter number of elements to be selected:" )

permutation_and_combinations(x,y)


