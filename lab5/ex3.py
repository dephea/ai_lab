import pandas as pd


data = pd.read_csv("StudentsPerformance.csv")

print("/////////////")
print("ex3: ")

print(data.isna().sum())

numerical_cols = data.select_dtypes(include=["number"]).columns
data[numerical_cols] = data[numerical_cols].fillna(data[numerical_cols].median())

categorical_cols = data.select_dtypes(include=["object", "str"]).columns
data[categorical_cols] = data[categorical_cols].fillna("Unknown")

print(data.isna().sum())