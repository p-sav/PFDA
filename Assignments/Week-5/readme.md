#### 1.  Program

When this notebook runs, it loads CSO population data for Ireland, compares male and female populations by age, calculates the weighted mean age for each sex, and identifies which region has the largest population difference in a chosen age group.



#### 2. What was learned :cd:
    - How to load and inspect CSV data using the `pandas` library
    - How to clean and prepare demographic data using pandas
    - How to calculate weighted means and population differences
    - How to group and filter data based on age ranges
    - How to visualize comparisons using matplotlib charts


#### 3. Program Code :floppy_disk:

```python


import pandas as pd
import matplotlib.pyplot as plt

# Display options (optional)
pd.set_option('display.max_columns', None)

# Load the CSO dataset
csv_path = r"C:\Users\CAD-PC\Desktop\GitHub - Cloned Repository\PFDA\My-Work\Week-5\cso-populationbyage.csv"
df = pd.read_csv(csv_path)

# Quick peek
print(df.head(3))
print(df.info())


# Keep only Ireland rows
df_Ireland = df[df["Administrative Counties"] == "Ireland"].copy()

# Ensure VALUE is numeric
df_Ireland["VALUE"] = pd.to_numeric(df_Ireland["VALUE"], errors="coerce")

# Keep only rows that are single years of age (strings like 'Under 1 year', '17 years', '100 years and over')
df_Ireland = df_Ireland[df_Ireland["Single Year of Age"].str.contains("Under|year", case=False, na=False)]

# Clean 'Single Year of Age' into numeric Age
df_Ireland["Age"] = (
    df_Ireland["Single Year of Age"]
    .str.replace("Under 1 year", "0", regex=False)
    .str.replace("100 years and over", "100", regex=False)
    .str.replace(" years", "", regex=False)
    .str.replace(" year", "", regex=False)
)

# Keep only numeric ages and convert to int
df_Ireland = df_Ireland[df_Ireland["Age"].str.isnumeric()]
df_Ireland["Age"] = df_Ireland["Age"].astype(int)

df_Ireland[["Age", "Sex", "VALUE"]].head()


# Pivot: rows = Age, columns = Sex, values = summed population
pivot = df_Ireland.pivot_table(index="Age", columns="Sex", values="VALUE", aggfunc="sum").reset_index()

# Plot male vs female population by age
plt.figure(figsize=(10,6))
if "Male" in pivot.columns:
    plt.plot(pivot["Age"], pivot["Male"], label="Male")
if "Female" in pivot.columns:
    plt.plot(pivot["Age"], pivot["Female"], label="Female")
plt.title("Population by Age and Sex (Ireland)", fontweight="bold", fontsize=14)
plt.xlabel("Age (years)")
plt.ylabel("Population")
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()
pivot.head()



wm_results = {}

if "Male" in pivot.columns and pivot["Male"].sum() > 0:
    wm_results["Male"] = float((pivot["Age"] * pivot["Male"]).sum() / pivot["Male"].sum())

if "Female" in pivot.columns and pivot["Female"].sum() > 0:
    wm_results["Female"] = float((pivot["Age"] * pivot["Female"]).sum() / pivot["Female"].sum())

print("Weighted Mean Age (by sex):")
for k, v in wm_results.items():
    print(f"  {k}: {v:.2f}")


    # Compute difference if both columns present
if all(c in pivot.columns for c in ["Male", "Female"]):
    pivot["Difference (M-F)"] = pivot["Male"] - pivot["Female"]
    
    plt.figure(figsize=(10,6))
    plt.bar(pivot["Age"], pivot["Difference (M-F)"])
    plt.axhline(0, color="black", linewidth=0.8)
    plt.title("Population Difference Between Sexes by Age (Males - Females)", fontweight="bold", fontsize=14)
    plt.xlabel("Age (years)")
    plt.ylabel("Population Difference")
    plt.tight_layout()
    plt.show()
else:
    print("Required columns ('Male' and 'Female') not found in the pivot.")
    
pivot.head()



focus_age = 35
low, high = focus_age - 5, focus_age + 5

fg = pivot[(pivot["Age"] >= low) & (pivot["Age"] <= high)].copy()

if all(c in fg.columns for c in ["Male", "Female"]) and not fg.empty:
    total_male = int(fg["Male"].sum())
    total_female = int(fg["Female"].sum())
    diff = total_male - total_female
    print(f"Focus Age Range: {low}–{high}")
    print(f"  Total Male:   {total_male:,}")
    print(f"  Total Female: {total_female:,}")
    print(f"  Difference (M - F): {diff:,}")
else:
    print("Insufficient data to compute focus group difference (missing Male/Female columns or empty range).")

fg[["Age"] + [c for c in ["Male","Female","Difference (M-F)"] if c in fg.columns]].head(20)



# Prepare full DF with numeric Age for the same focus range
df_focus = df.copy()
df_focus["VALUE"] = pd.to_numeric(df_focus["VALUE"], errors="coerce")

# Parse numeric age from 'Single Year of Age'
age_extracted = df_focus["Single Year of Age"].str.extract(r"(\d+)")
df_focus["Age"] = pd.to_numeric(age_extracted[0], errors="coerce")

# Keep only valid age rows in focus range
df_focus = df_focus[df_focus["Age"].between(low, high, inclusive="both")]

# Pivot by region and sex
region_pivot = df_focus.pivot_table(
    index="Administrative Counties",
    columns="Sex",
    values="VALUE",
    aggfunc="sum"
).fillna(0)

# Compute absolute difference
if all(c in region_pivot.columns for c in ["Male", "Female"]):
    region_pivot["Difference (M-F)"] = (region_pivot["Male"] - region_pivot["Female"]).abs()
  

    # Find region with the largest absolute difference
    largest_region = region_pivot["Difference (M-F)"].idxmax()
    largest_value = int(region_pivot.loc[largest_region, "Difference (M-F)"])
    print(f"Largest absolute sex difference (ages {low}–{high}):")
    print(f"  Region: {largest_region}")
    print(f"  |Male - Female|: {largest_value:,}")
else:
    print("Required columns ('Male' and 'Female') not present in regional pivot.")

region_pivot.sort_values("Difference (M-F)", ascending=False).head(10)

```

#### 4. Program Output :computer:

![Image showing the output of the program](/Assignments/Week-5/Population.png)


#### 5. Summary

The project can can be found here: **github** <https://github.com/p-sav/PFDA/tree/main/Assignments/Week-5>


#### 6. References

1. OpenAI. (2025). *ChatGPT*, accessed October 2025, available at: https://chat.openai.com/
2. [Pandas](https://pandas.pydata.org/)
5. [Matplotlib](https://matplotlib.org/)
4. [Juypter Notebook](https://jupyter.org/)
5. [W3Schools](https://www.w3schools.com/python/)