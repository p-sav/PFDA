# Preparing population data for data analysis

import pandas as pd

FULLPATH= r"C:\Users\CAD-PC\Desktop\GitHub - Cloned Repository\PFDA\My-Work\Week-5\cso-populationbyage.csv" # Path to the folder

# Or use FULLPATH = os.path.join(FILENAME)

df = pd.read_csv(FULLPATH) # Load csv file into dataframe

print(df.head(3)) # Show the first three rows

drop_col_list = ["Statistic Label","CensusYear","Sex","UNIT"] # Remove unrequired columns
df.drop(columns=drop_col_list, inplace=True)

# Remove rows that indicate all ages (case-insensitive) and any missing values
df = df[~df["Single Year of Age"].astype(str).str.contains("All age", case=False, na=False)]

# Replace 'Under 1 year' with '0' (use regex=False to avoid deprecation) and coerce to numeric
df["Single Year of Age"] = df["Single Year of Age"].astype(str).str.replace('Under 1 year', '0', regex=False)
df['Single Year of Age'] = pd.to_numeric(df['Single Year of Age'], errors='coerce')

# Drop rows that could not be converted and cast to integer
df = df.dropna(subset=['Single Year of Age'])
df['Single Year of Age'] = df['Single Year of Age'].astype('int64') # Convert "Single Year of Age" column to integer type

df_anal =pd.crosstab(df.loc[:, "Administrative Counties"], df.loc[:, "Single Year of Age"]) # Create a crosstab dataframe for analysis


df_anal = pd.pivot_table(df, values='VALUE', index='Administrative Counties', columns='Single Year of Age', aggfunc='sum', fill_value=0) # type: ignore # Alternative pivot table method


print(df.head(10)) # Show the first three rows after dropping columns
 
print(df.info()) # Show dataframe information

df.to_csv("population_for_analysis.csv", index=False) # Save the cleaned dataframe to a new csv file






