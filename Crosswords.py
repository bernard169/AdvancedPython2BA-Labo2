#Mots croisés
#Bernard Tourneur
import re

def checkRegexCrossword (linesRegex, columnsRegex, answer):
    isCorrect = True
    for line in linesRegex: #If one single line doesn't match the answer, function is interrupted 
        l = re.compile (line)
        if l.match (answer [linesRegex.index (line)]) is None:
            return False
    for column in columnsRegex : #Same as for the lines
        c = re.compile (column)
        ansCol = "" #Contains the answer's columns, to be compared to columnsRegex
        for line in answer :
            ansCol += line [columnsRegex.index (column)]
        if c.match (ansCol) is None :
            return False
    return isCorrect

print (checkRegexCrossword (["EC|CD[ABS]",".[GROS]+","C?[KS]+"],
                            ["[^CBF]MC|XD","[CRI]*[ACK]","[AEIOU]*S"], 
                            ["ECA", "MRO", "CKS"])) #given by the teacher 

print (checkRegexCrossword (["(BO|DF)[MNO]", "[IXZ]+(RA|MN)", "^[CSO]+$"], 
                            ["[^DXZ](IS|MV)", "[OPQR]*", "(NA|ST)[JKS]+"],
                            ["BON", "IRA", "SOS"])) #new crossword
