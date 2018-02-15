import re

#Exercice 1
#a
pattern1 = "\+\d{2} \d{3} \d{2} \d{2} \d{2}"
p1 = re.compile (pattern1)

ask = input ("Please enter your phone number :")
if p1.match (ask) is not None : 
    print ("Your phone number is :", ask)
else :
    while p1.match (ask) is None :
        print ("Please enter your phone number correctly")
        ask = input ("Please enter your phone number: ")
    print ("Your phone number is :", ask)
    
#b
pattern2 = "\+?\-?\d+"
p2 = re.compile (pattern2)

ask2 = input ("Please enter an integer :")
if p2.match (ask2) is not None : 
    print ("Your number is :", ask2)
else :
    while p2.match (ask2) is None :
        print ("Please enter an integer")
        ask2 = input ("Your integer : ")
    print ("Your integer is :", ask2)
    