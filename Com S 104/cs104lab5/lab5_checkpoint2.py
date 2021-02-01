#Checkpoint two: Factorial function to give the factorial of a given number.

def nFactorial(n):
    factorial = 1
    for i in range(1,n + 1):
        factorial = factorial * i
    print factorial
