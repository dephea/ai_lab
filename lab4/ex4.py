import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("data.csv")

data["Contract Valid Until"] = pd.to_datetime(data["Contract Valid Until"], format='mixed')
ex4 = data[data["Contract Valid Until"].dt.year <= 2021]

print("/////////////////////////")
print("ex4 Sortează jucătorii după Skill Moves descrescător.:")
print(ex4)