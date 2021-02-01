#This is a script that, given the input from the user, will calculate the value for the
#quadratic formula of -b +(or -) sprt(b^2 - 4ac)/ 2a. a, b, and c are all given from the
#input and can be placed into the formula ax^2+bx+c = 0.


from math import sqrt

print "Quadratic Equation: ax^2+bx+c = 0"
a = input("Enter a: ")
b = input("Enter b: ")
c = input("Enter c: ")

#Gets the value of the discriminant and stores it as a value.
dis = b**2 - 4*a*c

#If the value of the discriminant is less than zero it will have no solutions.
if(dis < 0):
    print str(a) + "x^2+" + str(b) + "x+" +  str(c) + " = 0 has no solutions."

#If the value of the discriminanat is zero, it will have one solution.
elif(dis == 0):
    #Finds the solution using the Quadratic Formula with the given input values.
    sol = (-1*b + sqrt(dis))/(2*a)

    print str(a) + "x^2+" + str(b) + "x+" + str(c) + " = 0 has one solution."
    print "Solution: " + str(sol)

#If the value of the discriminant is greater than zero, there will be two solutions.
else:
    #Find the solutions for both of the values.
    sol1 = (-1*b + sqrt(dis))/(2*a)
    sol2 = (-1*b - sqrt(dis))/(2*a)

    print str(a) + "x^2+" + str(b) + "x+" + str(c) + " = 0 has two solutions."
    print "Solution1: " + str(sol1)
    print "Solution2: " + str(sol2)
