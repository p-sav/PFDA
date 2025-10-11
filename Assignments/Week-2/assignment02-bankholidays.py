# Program Name: assignment02-bankholidays.py
# Description: Prints out the bank holidays that happen in Northern Ireland.
# Author: P-Sav


import requests                                     # fetch data from the web

# URL for UK Government bank holidays API
url = "https://www.gov.uk/bank-holidays.json"       # public data source

# Fetch and parse JSON data
response = requests.get(url)                        # send GET request
data = response.json()                              # convert JSON to dictionary

# Extract Northern Ireland bank holidays
ni_holidays = data["northern-ireland"]["events"]    # access Northern Ireland list

print("\nBank Holidays in Northern Ireland:\n")     # header text
for event in ni_holidays:                           # loop through each holiday
    print(f"{event['title']}: {event['date']}")     # print name and date


