import pandas as pd


data = pd.read_csv("StudentsPerformance.csv")

print("/////////////")
print("ex1: ")

print("\n\nHEAD:")
print(data.head())

print("\n\nINFO:")
print(data.info())

print("\n\nDESCRIBE:")
print(data.describe())

print("\n\nISNA:")
print(data.isna().sum())