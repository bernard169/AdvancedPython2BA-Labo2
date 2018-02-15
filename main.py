import re
import string

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
    digits = "\d+"
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
                    for number in digitsInLine: 
                        result += number + ", "
                    result += '\n'
                i+=1
            return result
    except IOError:
        print ("incorrect path")
        newPath = input ("enter a new path : ")
        findDigits (newPath)

myPath = input ("enter a path : ")
print (findDigits (myPath))


#Exercice 3 
def cutURL (myURL):
    result = myURL
    URLtypo = "(?P<Protocol>[a-z]+)://(?P<Domain>www\.[a-z]+\.[a-z]+)(?P<Path>/.+){0,1}"
    p = re.compile (URLtypo)
    m = p.match (myURL)
    if m is not None : 
        m.groups ()
        if m.group ('Path') is not None :
            result += '\n' + "Protocol : " + m.group ('Protocol') + '\n' + "Domain : " + m.group ('Domain') + "Path : " + m.group ('Path')
        else : 
            result += '\n' + "Protocol : " + m.group ('Protocol') + '\n' + "Domain : " + m.group ('Domain')
    return result
print (cutURL ("https://www.google.com"))

def cutWithStr (myURL):
    s1 = myURL.split ("://")
    protocol = s1 [0]
    s2 = s1[1].split ("/")
    domain = s2 [0]
    path =""
    if len (s2) >1 :
        i = 1
        while i < len (s2):
            path += s2 [i] +"/"
    return (protocol, domain, path)

cut = cutWithStr ("https://www.hello.com/hello/world") 
print ("Protocol : ", cut [0], "Domain : ", cut [1], "Path", cut [2])


