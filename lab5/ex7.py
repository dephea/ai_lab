import pandas as pd
from sklearn.preprocessing import StandardScaler


data = pd.read_csv("StudentsPerformance.csv")

print("/////////////")
print("ex7: ")

numerical_cols = data.select_dtypes(include=["number"]).columns

scaler = StandardScaler()

data_scaled = data.copy()

data_scaled[numerical_cols] = scaler.fit_transform(data[numerical_cols])

print(data[numerical_cols].head())

print(data_scaled[numerical_cols].head())