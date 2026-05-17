import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("data.csv")

res2= data[(data["Overall"] >= 85) & (data["Age"] < 25)]

print("/////////////////////////")
print("ex2 Afisati primii 10 jucatorii cu varsta > 40.:")
print (res2)
