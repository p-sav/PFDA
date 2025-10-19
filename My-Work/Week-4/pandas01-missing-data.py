# code snippets for lectures
# Author: Andrew Beatty

import os
import pandas as pd

filepath = os.path.join(os.path.dirname(__file__), "people-100-dirty.csv") # file path

df = pd.read_csv(filepath) # Load the csv file


print(df.head()) # Show info
print(df.info())


# Detect missing values
print(df.isnull().sum())

# Drop rows with missing values
#df.dropna(inplace=True)

# Fill missing values
df.fillna(value='default_value', inplace=True)

# drop duplicate rows
df.drop_duplicates(inplace=True)
df.to_csv( "temp_file.csv")

