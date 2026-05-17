import pandas as pd


data = pd.read_csv("StudentsPerformance.csv")

print("/////////////")
print("ex2: ")


categorical_cols = data.select_dtypes(include=["object", "str"]).columns
numerical_cols = data.select_dtypes(include=["number"]).columns

print("Categorical variables:")
print(list(categorical_cols))

print("\nNumerical variables:")
print(list(numerical_cols))