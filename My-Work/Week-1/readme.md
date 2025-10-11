#### 1. Birth Rates Program

When you run this notebook, it will load the CSO dataset for projected birth rates in Ireland, clean the data, and display a line plot showing how birth rates are expected to change over time


#### 2. What was learned :cd:
    - How to load a CSV file into a pandas DataFrame
    - How to inspect column names and data types
    - How to detect the correct columns for analysis automatically
    - How to clean and sort data for accurate plotting
    - How to create a line plot using matplotlib
    - How to save a short text summary of dataset statistics


#### 3. Program Code :floppy_disk:

'import pandas as pd                              # data handling
import matplotlib.pyplot as plt                   # plotting

csv_path = r"C:\Users\CAD-PC\Desktop\GitHub - Cloned Repository\PFDA\My-Work\Week-1\projectedbirths-cso.csv"
births = pd.read_csv(csv_path)                    # load the dataset
births.info()                                     # check structure

year_col = 'Year'                                 # detected year column
value_col = 'Births'                              # detected value column

births[year_col] = pd.to_numeric(births[year_col], errors='coerce')
births[value_col] = pd.to_numeric(births[value_col], errors='coerce')

df = births.dropna(subset=[year_col, value_col]).copy()
df = df.sort_values(year_col)
df = df.groupby(year_col, as_index=False)[value_col].mean()

plt.figure(figsize=(10, 6))
plt.plot(df[year_col], df[value_col], marker='o')
plt.title("Projected Birth-rates in Ireland")
plt.xlabel(year_col)
plt.ylabel(value_col)
plt.grid(True)
plt.tight_layout()
plt.show()' 


#### 4. Program Output :computer:

![Image showing the output of the program](C:\Users\CAD-PC\Desktop\GitHub - Cloned Repository\PFDA\My-Work\Week-1)


#### 5. Summary

The project can can be found here: **github** <My-Work/Week-1>


