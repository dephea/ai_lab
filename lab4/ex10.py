import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("data.csv")

#ex10

print("/////////////////////////")
print("ex10 Completați valorile lipsă din coloana 'Position' cu stringul \"Unknown\":")

print(data["Position"].isna().sum())

ex10 = data["Position"].fillna("Unknown")

print(ex10.isna().sum())