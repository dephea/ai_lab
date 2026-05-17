import pandas as pd
from sklearn.preprocessing import LabelEncoder


data = pd.read_csv("StudentsPerformance.csv")

print("/////////////")
print("ex4: ")


le = LabelEncoder()
data["gender"] = le.fit_transform(data["gender"])

print(data["gender"])

remaining_cols = [
    'race/ethnicity',
    'parental level of education',
    'lunch',
    'test preparation course'
]

data = pd.get_dummies(data, columns=remaining_cols, drop_first=True)

print(data)