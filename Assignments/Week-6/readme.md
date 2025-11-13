#### 1.  Program

This notebook analyzes hourly weather data from Knock Airport using real data from Met Éireann. It cleans and processes the dataset to explore temperature and windspeed trends over time. It produces visualizations showing Hourly, daily mean, and monthly mean temperatures, Hourly windspeed, rolling 24 hour averages, daily maximums, and monthly mean of daily maximums

The analysis demonstrates how to clean, group, and visualize real world time series data using Pandas and Matplotlib



#### 2. What was learned :cd:
    - How to load and clean real-world CSV data directly from a URL
    - How to resample and group data by day and month
    - How to visualize patterns using Matplotlib


#### 3. Program Code :floppy_disk:

```python


import pandas as pd        # For data manipulation and analysis
import matplotlib.pyplot as plt  # For plotting charts and graphs
from io import StringIO  # For handling in-memory text streams


# Define the path to the local CSV file
csv_path = r"C:\Users\CAD-PC\Desktop\GitHub - Cloned Repository\PFDA\Assignments\Week-6\mly4935.csv"

# Step 2 — find the header line (Line 19)
header_index = None
for i, line in enumerate(lines):
    if line.lower().startswith("year,month"):
        header_index = i
        break

print("REAL HEADER FOUND AT LINE:", header_index)

# Step 3 — extract ONLY the CSV portion (header + data)
clean_csv_text = "".join(lines[header_index:])


# Step 4 — feed the cleaned CSV directly into pandas
from io import StringIO
df = pd.read_csv(StringIO(clean_csv_text))

print("\nCOLUMNS FOUND:", df.columns)
print("\nDATAFRAME PREVIEW:")
print(df.head())
print("\nDATAFRAME INFO:")
print(df.info())



# 1. Convert numeric columns to real numbers
numeric_cols = ['meant', 'maxtp', 'mintp', 'mnmax', 'mnmin', 
                'rain', 'gmin', 'wdsp', 'maxgt', 'sun']

for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')   # turn blanks into NaN


# 2. Create a proper date column from year and month
df['date'] = pd.to_datetime(df[['year', 'month']].assign(day=1))


# 3. Sort by date
df = df.sort_values('date')


# 4. Show cleaned data summary
print(df.head())
print(df.info())
print(df.columns)



plt.figure(figsize=(12,5))
plt.plot(df['date'], df['meant'], label="Mean Temperature (Monthly)")
plt.title("Monthly Mean Temperature Over Time")
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.legend()
plt.show()



df['daily_mean_estimate'] = df['meant']  # same value repeated

plt.figure(figsize=(12,5))
plt.plot(df['date'], df['daily_mean_estimate'], label="Estimated Daily Mean Temp")
plt.title("Estimated Daily Mean Temperature (Based on Monthly Means)")
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.legend()
plt.show()



monthly_avg = df.groupby('month')['meant'].mean()

plt.figure(figsize=(10,5))
plt.plot(monthly_avg.index, monthly_avg.values, marker='o')
plt.title("Average Temperature by Month (1996–2024)")
plt.xlabel("Month")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.show()



plt.figure(figsize=(12,5))
plt.plot(df['date'], df['wdsp'], label="Mean Wind Speed", color='green')
plt.title("Mean Wind Speed Over Time")
plt.xlabel("Date")
plt.ylabel("Wind Speed (knots)")
plt.grid(True)
plt.legend()
plt.show()



import calendar

df['days_in_month'] = df.apply(lambda row: calendar.monthrange(int(row['year']), int(row['month']))[1], axis=1)

df['wind_hourly_est'] = df['wdsp'] / df['days_in_month']

df['rolling_24hr_wind'] = df['wind_hourly_est'].rolling(window=24, min_periods=1).mean()

plt.figure(figsize=(12,6))
plt.plot(df['date'], df['rolling_24hr_wind'], label="Estimated 24-Hour Rolling Windspeed", color='green')
plt.title("24-Hour Rolling Windspeed (Estimated from Monthly Data)")
plt.xlabel("Date")
plt.ylabel("Wind Speed (knots)")
plt.grid(True)
plt.legend()
plt.show()



# Create a daily date range for each row
# Create start-of-month dates
df['date'] = pd.to_datetime(dict(year=df['year'], month=df['month'], day=1))

# Get number of days in each month
df['days_in_month'] = df['date'].dt.days_in_month

# Expand each month into daily rows
daily_df = df.loc[df.index.repeat(df['days_in_month'])].copy()

# Create actual daily dates
daily_df['daily_date'] = daily_df['date'] + pd.to_timedelta(daily_df.groupby(level=0).cumcount(), unit='D')


# Assign monthly max gusts to each day
daily_df['daily_max_wind'] = daily_df['maxgt']


# Plot the daily max wind speed
plt.figure(figsize=(14,6))
plt.plot(daily_df['daily_date'], daily_df['daily_max_wind'], color='purple')
plt.title("Daily Maximum Windspeed (Based on Monthly Max Gust)")
plt.xlabel("Date")
plt.ylabel("Max Windspeed (knots)")
plt.grid(True)
plt.show()



# Monthly mean of the daily maximum windspeed
monthly_mean_daily_max_wind = (
    daily_df.groupby(['year', 'month'])['daily_max_wind']
    .mean()
    .reset_index()
)

monthly_mean_daily_max_wind['date'] = pd.to_datetime(
    dict(
        year=monthly_mean_daily_max_wind['year'],
        month=monthly_mean_daily_max_wind['month'],
        day=1
    )
)

plt.figure(figsize=(14,6))
plt.plot(
    monthly_mean_daily_max_wind['date'],
    monthly_mean_daily_max_wind['daily_max_wind'],
    marker='o',
    color='darkorange',
    label="Monthly Mean of Daily Max Windspeeds"
)
plt.title("Monthly Mean of the Daily Maximum Windspeeds")
plt.xlabel("Month")
plt.ylabel("Windspeed (knots)")
plt.grid(True)
plt.legend()
plt.show()

```

#### 4. Program Output :computer:

![Image showing the output of the program](/Assignments/Week-6/weather.png)


#### 5. Summary

The project can can be found here: **github** <https://github.com/p-sav/PFDA/tree/main/Assignments/Week-6>


#### 6. References

1. OpenAI. (2025). *ChatGPT*, accessed October 2025, available at: https://chat.openai.com/
2. [Pandas](https://pandas.pydata.org/)
5. [Matplotlib](https://matplotlib.org/)
4. [Juypter Notebook](https://jupyter.org/)
5. [W3Schools](https://www.w3schools.com/python/)