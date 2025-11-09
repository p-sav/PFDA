# Preparing population data for data analysis


import pandas as pd

FULLPATH= r"C:\Users\CAD-PC\Desktop\GitHub - Cloned Repository\PFDA\My-Work\Week-5\cso-populationbyage.csv" # Path to the folder

# Or use FULLPATH = os.path.join(FILENAME)

df = pd.read_csv(FULLPATH) # Load csv file into dataframe

print (df.head(3)) # Show the first three rows

drop_col_list = ["Statistic Label","CensusYear","Sex","UNIT"] # Remove unrequired columns
df.drop(columns=drop_col_list, inplace=True)

print (df.head(3)) # Show the first three rows after dropping columns






