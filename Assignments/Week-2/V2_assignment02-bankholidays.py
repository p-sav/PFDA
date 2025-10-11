# Program Name: assignment02-bankholidays.py
# Description: Prints out only the bank holidays that are unique to Northern Ireland.
# Author: P-Sav



import requests                                     # to fetch data from the web

url = "https://www.gov.uk/bank-holidays.json"       # official UK Gov API for bank holidays
response = requests.get(url)                        # send HTTP request
data = response.json()                              # convert JSON response to Python dictionary

# Extract all regions
ni_holidays = data["northern-ireland"]["events"]    # Northern Ireland holidays
eng_holidays = data["england-and-wales"]["events"]  # England & Wales holidays
scot_holidays = data["scotland"]["events"]          # Scotland holidays

# Collect all non NI holiday names for comparison
other_holiday_names = {h["title"] for h in eng_holidays + scot_holidays}  # set of titles

# Filter Northern Ireland holidays that are NOT in other regions
unique_ni_holidays = [h for h in ni_holidays if h["title"] not in other_holiday_names]

# Output
print("\nUnique Bank Holidays in Northern Ireland:\n")  # header text
if unique_ni_holidays:                                  # check if any unique holidays exist
    for event in unique_ni_holidays:                    # loop through and print
        print(f"{event['title']}: {event['date']}")     # print name and date
else:
    print("No unique bank holidays found.")             # fallback if none exist


