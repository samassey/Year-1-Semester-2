#Checkpoint 2 find user name
def findUserName(s):
    randomNum = int(s[0])
    t = s[2:]
    i = 0
    while(t[i] != " "):
        i = i + 1
    firstNameInitial = t[0]
    lastName = t[i + 1:]
    l = len(lastName)
    randomNumFinal = randomNum * int(l)
    print firstNameInitial.upper() + lastName.lower() + str(randomNumFinal)

s = raw_input("Please enter a random number 1-5, your first name, and your last name: ")
findUserName(s)
