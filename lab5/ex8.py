import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler


data = pd.read_csv("StudentsPerformance.csv")

# print("/////////////")
# print("ex4: ")


le = LabelEncoder()
data["gender"] = le.fit_transform(data["gender"])

# print(data["gender"])

remaining_cols = [
    'race/ethnicity',
    'parental level of education',
    'lunch',
    'test preparation course'
]


# print("/////////////")
# print("ex5: ")

data["average_score"] = (
    data["math score"] 
    + data["reading score"]
    + data["writing score"]
) / 3

def performance(score): 
    if score < 50:
        return "low"
    elif score <= 70:
        return "mid"
    else:
        return "high"
    

data["performance_level"] = data["average_score"].apply(performance)

data["is_prepared"] = (
    data["test preparation course"] == "completed"
)

data = pd.get_dummies(data, columns=remaining_cols, drop_first=True)


# print("/////////////")
# print("ex7: ")

numerical_cols = [
    "math score",
    "reading score",
    "writing score",
    "average_score"
]

scaler = StandardScaler()

data_scaled = data.copy()

data_scaled[numerical_cols] = scaler.fit_transform(data[numerical_cols])

# print(data[numerical_cols].head())

# print(data_scaled[numerical_cols].head())

# ex8:

print("/////////////")
print("ex8: ")

X = data.drop(columns=["performance_level"])
y = data["performance_level"]

print("X shape:", X.shape)
print("y shape:", y.shape)