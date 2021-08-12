import random

print("number guessing game" )


number=int(input("enter a number between 1 and 9"))
if(number<12):
    print("No admission")
elif(number==12):
    print("adimssion granted")
else:
    print("advance level")