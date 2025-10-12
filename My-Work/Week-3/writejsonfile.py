# Program to write JSON data to a file

import json

data = {
    "name": "joe",
    "age": 21,
    "student": True
}

with open ("silly.json", "w") as fp:
    json.dump(data, fp)
jsonString = json.dumps(data)
print (data)
print (jsonString)

