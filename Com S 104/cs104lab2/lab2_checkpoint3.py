# This script computes the total amount for an order of mousetraps
# costing 2.00 each for the first 50, and 1.50 each thereafter

num = input("How many mousetraps? ")
iowa = raw_input("Are you an Iowa resident (y/n)?")

if num <= 50:
    total = num * 2.00
else:
    first = 50 * 2.00
    extra = (num - 50) * 1.50
    total = first + extra

if iowa == "y":
    tax = total * .05
    total = total + tax
else:
    tax = total * .1
    total = taotal + tax

print "Tax:", tax
print "Total:", total


    
