import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("data.csv")

res = data[data["Age"] > 40]


print("/////////////////////////")
print("ex1 Importati si afisati intregul set de date (toate coloanele, toate randurile) ‘data.csv’.(dataframes, pandas):")
print(res.head(10))