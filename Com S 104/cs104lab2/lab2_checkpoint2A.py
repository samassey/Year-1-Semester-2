print "What is the customer's full name?"
name = raw_input()
print "How many nights?"
nights = input()
print "What is the total charge for room service?"
room_service = input()
print "What is the total charge for using the telephone?"
phone = input()

total_charge = 55 * nights

tax = total_charge * 0.1

total = total_charge + room_service + phone + tax

print "Customer's full name:", name
print "Number of nights:", nights
print "Total room service charge($):", room_service
print "Total telephone charge($):", phone
print "River Bend Hotel Bill (Customer : " + str(name) + ")"
print "Total room charge($):", total_charge
print "Entertainment tax($):", tax
print "Total bill($):", total
