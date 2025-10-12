# This program creates a JSON file and prints a JSON string


import json
import os

FILENAME="iris.json"
DATADIR="../Week-3/"
FULLPATH= os.path.join(DATADIR+FILENAME)

print("Reading file from:", os.path.abspath(FULLPATH))


with open(FULLPATH, "r") as fp:
    irisdataset = json.load(fp)
    print (json.dumps(irisdataset, indent=4))
    
    


