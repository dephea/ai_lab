import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("data.csv")

print("/////////////////////////")
print("ex6 Afisati cate randuri si coloane are setul de date. Cati jucatori unici avem?:")
print(data["Name"].nunique())