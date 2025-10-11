
# Simple program that plots Ireland's population by age (latest census year)
# Author: P-Sav

import pandas as pd                                  # handle CSV data
import matplotlib.pyplot as plt                       # create plots
import re                                             # regex for text cleanup

csv_path = r"C:\Users\CAD-PC\Desktop\GitHub - Cloned Repository\PFDA\My-Work\Week-1\cso-populationbyage.csv"  # file path
data = pd.read_csv(csv_path)                          # load CSV

# Filter for Ireland only and latest census year
data = data[data['Administrative Counties'] == 'Ireland']  # only Ireland
latest_year = data['CensusYear'].max()                     # latest year
data = data[data['CensusYear'] == latest_year]              # filter latest year

# Convert 'Single Year of Age' text (like '1 year', '2 years') to numbers
def to_age(a):                                              # small helper
    if 'Under' in a: return 0                               # handle 'Under 1 year'
    return int(re.findall(r'\d+', a)[0]) if re.findall(r'\d+', a) else None

data['Age'] = data['Single Year of Age'].apply(to_age)      # convert to numbers
data = data.dropna(subset=['Age'])                          # remove missing
data = data.sort_values('Age')                              # sort by age

# Plot
plt.plot(data['Age'], data['VALUE'])                        # simple line plot
plt.title(f"Population by Age in Ireland ({latest_year})")  # title
plt.xlabel("Age (years)")                                   # x-axis label
plt.ylabel("Population")                                    # y-axis label
plt.show()                                                  # display plot
