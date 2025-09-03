'''
Download the dataset: 50_Startups Dataset
Create DataFrame using Pandas.
Read the data from 50_Startups.csv file and load into DataFrame.
Check the statistical summary.
Check correlation coefficient between dependent and independent variables.
'''

import pandas as pd

startups = pd.read_csv(r"09_Numpy_Pandas\Assignments\50_Startups.csv")
print(startups.head())
print(startups.describe())
print(startups.select_dtypes(include=['number']).corr())
