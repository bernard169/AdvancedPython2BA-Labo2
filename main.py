import re

#Exercice 1
def compare (myPattern, patternNature):
    p = re.compile (myPattern)
    ask = input ("Please enter your {} : \n".format (patternNature))
    if p.match (ask) is not None : 
        print ("Your {} is :".format (patternNature), ask)
    else :
        while p.match (ask) is None :
             print ("Please enter your {} correctly".format (patternNature))
             ask = input ("Please enter your {}: ".format (patternNature))
        print ("Your {} is :".format (patternNature), ask) 
#a
pattern1 = "^\+\d{2} \d{3} \d{2} \d{2} \d{2}$"
compare (pattern1, "phone number")

#b
pattern2 = "^\+?\-?\d+$"
compare (pattern2, "integer" )

#c
pattern3 = "^[1-9]?[A-Z]{3}\d{3}$"
pattern3b = "^[1-9]?\d{3}[A-Z]{3}$"
compare (pattern3, "plate number")

#d
pattern4 = r"^[A-Z]{1}:\\"
compare (pattern4, "nameSpace")

#Exercice 2 
