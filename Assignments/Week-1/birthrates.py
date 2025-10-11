# Program that imports a csv file with the CSO dataset for projected birth rates in Ireland
# The program prints out a line plot showing how birth rates are expected to change over time


import pandas as pd
import matplotlib.pyplot as plt

csv_path = r"C:\Users\CAD-PC\Desktop\GitHub - Cloned Repository\PFDA\My-Work\Week-1\projectedbirths-cso.csv"
births = pd.read_csv(csv_path)

print(births.info())        # check data columns

year_col = 'Year'           # correct year column
value_col = 'VALUE'         # correct value column

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
plt.show()
