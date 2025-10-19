# This code will find some text in an access file
# Author: Andrew Beatty

import re

regex = "\[.*\]"
filename = r"C:\Users\CAD-PC\Desktop\GitHub - Cloned Repository\PFDA\My-Work\Week-4\smallerAccess.log.txt"

with open(filename, encoding="utf-8") as inputFile:
    for line in inputFile:
        foundTextList = re.findall(regex, line)
        if (len(foundTextList) != 0):
            # print(foundTextList)
            foundText = foundTextList[0]
            print(foundText)
            # if I did not want the [] at the beginning and end
            print(foundText[1:-1])
