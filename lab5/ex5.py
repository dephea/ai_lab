import pandas as pd


data = pd.read_csv("StudentsPerformance.csv")

print("/////////////")
print("ex5: ")


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

print(data)