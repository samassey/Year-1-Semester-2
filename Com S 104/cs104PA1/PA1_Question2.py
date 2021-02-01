#Takes the input from a user asking what value they want to be converted, then what they want it to be converted too.
#this must be a value that can actually be converted. Ex: gal to l or kg to lb.
#Values that cannot be converted will be rejected.
#This will take the given value and convert it to what the desired unit is.

print "Unit Conversion"
#Get the initial unit.
initial = raw_input("Convert from (only gal, lb and mi)? ")
#Get the final unit.
final = raw_input("Convert to (only l, kg and km)? ")

if(initial == "gal" and final == "l"):
    value = input("Value? ")
    print 3.78541 * value, "l"

elif(initial == "lb" and final == "kg"):
    value = input("Value? ")
    print 0.45359 * value, "kg"

elif(initial == "mi" and final == "km"):
    value = input("Value? ")
    print 1.60934 * value, "km"

#Statement to return if conversion is incompatible.
else:
    print "Error: Incompatible conversion."
