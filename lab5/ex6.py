import pandas as pd


data = pd.read_csv("StudentsPerformance.csv")

print("/////////////")
print("ex6: ")


print(list(data.columns))
print(data.info())

const_cols = [col for col in data.columns if data[col].nunique() == 1]

print(const_cols)

corr = data.select_dtypes(include=["number"]).corr()

print(corr)