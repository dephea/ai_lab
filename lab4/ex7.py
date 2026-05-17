import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("data.csv")

top5 = data["Nationality"].value_counts().head(5)

print("/////////////////////////")
print("ex7 Care este cea mai frecventa nationalitate a jucatorilor? Afisati top 5 nationalitati.:")
print(top5)