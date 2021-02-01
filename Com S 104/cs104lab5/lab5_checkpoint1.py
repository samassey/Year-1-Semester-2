#Checkpoint one: a python script that displays all the occurances of letter a and their indexes.
s = raw_input("Enter a phrase/sentence: ")
index = 0

for c in s:
    if(c == 'a' or c == 'A'):
        print str(c) + " at index " + str(index)
    index = index + 1
