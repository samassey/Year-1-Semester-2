# Loop examples

# Returns the average of the values in list
def average(list):
    total = 0.0
    for number in list:
        total = total + number
    return total / len(list)

# Counts the number of p's in a word
def count_p(word):
    count = 0
    for c in word:
        if c == "p":
            count = count + 1
    return count

# Prints a specified number of cheers
def many_cheers(num_cheers):
    for i in range(num_cheers):
        print "Hip hip, hooray!"

# Returns the sum of the values
# entered one at a time from the keyboard.

def find_sum():
          total = 0.0
          entry = raw_input("Enter a value, or q to quit: ")
          while entry != "q":
                    total = total + int(entry)
                    entry = raw_input("Enter a value, or q to quit: ")
          return total

# Returns the average of the values
# entered one at a time from the keyboard.

def find_average():
          total = 0.0
          count = 0
          entry = raw_input("Enter a value, or q to quit: ")
          while entry != "q":
                    total = total + int(entry)
                    count += 1
                    entry = raw_input("Enter a value, or q to quit: ")
          return total/count



          
          
