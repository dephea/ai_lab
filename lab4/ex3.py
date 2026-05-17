import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("data.csv")

ex3 = data.sort_values(by="Skill Moves", ascending=False)
print("/////////////////////////")
print("ex3 Afișați toți jucătorii cu Overall ≥ 85 și Age < 25:")
print(ex3)