#### 1. bankholiday.py Program

When you run this program, it connects to the UK Government’s open data API and retrieves the official list of bank holidays for Northern Ireland.
It then prints out the name and date of each holiday in a simple, readable format.


#### 2. What was learned :cd:
    - How to import and use the requests library to get live data from an online API
    - How to read and parse JSON data into a Python dictionary
    - How to loop through and print structured data clearly
    - How to format text output using f-strings


#### 3. Program Code :floppy_disk:

```python
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
    print(f"{event['title']}: {event['date']}")     # print name and date'
```

#### 4. Program Output :computer:

![Image showing the output of the program](/Assignments/Week-2/bank_holidays.jpg)


#### 5. Summary

The project can can be found here: **github** <https://github.com/p-sav/PFDA/tree/main/Assignments/Week-2>


