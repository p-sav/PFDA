# A program to read from a URL

import requests

url = "https://www.gov.uk/bank-holidays.json"
response = requests.get(url)
data = response.json()

print (data)

if "Northern Ireland" in data and "events" in data["Northern Ireland"]:
    for event in data["Northern Ireland"]["events"]:
        print (f"{event['title']}")
        print (f" {event['title']} on {event['date']}")

           