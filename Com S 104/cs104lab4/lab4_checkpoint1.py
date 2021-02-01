#Checkpoint 1 Phone Number Format
def  phoneNumberFormat(phoneNum):
    l = len(phoneNum)
    if(l != 10):
        print "Error: Wrong Phone Numbere Format"
    else:
        areaCode = phoneNum[:3]
        next3Digits  = phoneNum[3:6]
        last4Digits = phoneNum[6:]
        number = "(" + areaCode + ")" + next3Digits + "-" + last4Digits
        print number


phoneNum = raw_input("What is the phone number? ")
phoneNumberFormat(phoneNum)
