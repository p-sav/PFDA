# Basic overview of statistics concepts using pandas

import pandas as pd

# a series with an even number of data points

eve_example_values = pd.Series([1, 2, 2, 3, 3, 4, 5, 6, 10000])

print(f'series values:\n{eve_example_values.to_list()}\n')
print(f'mean: {eve_example_values.mean()}')
print(f'median: {eve_example_values.median()}')
print(f'standard deviation: {eve_example_values.std()}\n')
print(f'series mode: {eve_example_values.mode().to_list()}\n')
print (f'series min: {eve_example_values.min()}')
print (f'series max: {eve_example_values.max()}')
print(f'series length: {len(eve_example_values)}\n')

