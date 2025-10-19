# this is code for the quiz


import re                                            # import the regular expressions module

regex = "Hello World"                                         # regex pattern to match any line
filename = r"C:\Users\CAD-PC\Desktop\GitHub - Cloned Repository\PFDA\My-Work\Week-4\quiz.txt"     # path to the quiz text file

with open(filename, encoding="utf-8") as quizFile:                     # open the file safely
    for line in quizFile:                            # iterate through each line in the file
        searchResult = re.search(regex, line)        # search the line for the regex pattern
        if searchResult:                             # if a match is found
            matchingLine = line                      # store the matched line
            print(matchingLine, end="")              # print the line (avoid adding extra newline)
