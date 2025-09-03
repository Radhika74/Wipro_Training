import pandas as pd

cars = pd.read_csv(r"09_Numpy_Pandas\Assignments\cars.csv")
print(cars.head(10))
print(cars)
print(cars.tail())
print(cars.info())
print(cars.describe())
