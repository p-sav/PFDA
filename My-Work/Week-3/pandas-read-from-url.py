# Program to read from a URL using pandas

import pandas as pd

url = "https://api.open-meteo.com/v1/forecast?latitude=53.997491&longitude=-6.198404&hourly=temperature_2m,wind_speed_10m&timezone=GMT&format=csv"

df = pd.read_csv(url)
print(df.head())

