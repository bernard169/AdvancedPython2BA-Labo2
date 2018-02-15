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
pattern3 = "^[1-9]?[A-Z]{3}\d{3}|[1-9]?\d{3}[A-Z]{3}$"
compare (pattern3, "plate number")

#d
pattern4 = r"^[A-Z]{1}:\\"
compare (pattern4, "nameSpace")

#Exercice 2 
def findDigits (path):
    result =""
    digits = "\d +"
    d = re.compile (digits)
    try :
        with open (path) as file :
            tabledFile = file.readlines ()
            i=0
            while i < len (tabledFile):
                line = tabledFile [i]
                if d.match (line) is not None:
                    result += "line {} : ".format (str (i))
                    digitsInLine = d.findall (line)
                    for number in digitsInLine : 
                        result += number + ", "
                i+=1
            return result
    except IOError:
        print ("incorrect path")
        newPath = input ("enter a new path : ")
        findDigits (newPath)

myPath = input ("enter a path : ")
print (findDigits (myPath))


