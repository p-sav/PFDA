# Population analysis of CSO data using pandas

import pandas as pd

FULLPATH= r"C:\Users\CAD-PC\Desktop\GitHub - Cloned Repository\PFDA\My-Work\Week-5\cso-populationbyage.csv" # Path to the folder

df = pd.read_csv(FULLPATH) # Load csv file into dataframe

print(df.head(3)) # Show the first three rows

