# correlation_iris.py
# This script loads the Iris dataset from a given URL
# and computes the correlation matrix for its numerical features
# using the pandas library



import pandas as pd

dataurl="https://gist.githubusercontent.com/Thanatoz-1/9e7fdfb8189f0cdf5d73a494e4a6392a/raw/aaecbd14aeaa468cd749528f291aa8a30c2ea09e/iris_dataset.csv"

irisdf = pd.read_csv(dataurl)

print(irisdf.select_dtypes(include='number').corr())

