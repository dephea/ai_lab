import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("data.csv")

#ex9
ex9 = data.groupby("Nationality")[["SprintSpeed", "Acceleration"]].mean()


print("/////////////////////////")
print("ex9 Calculați media atributelor \"SprintSpeed\" și \"Acceleration\" pentru fiecare naționalitate. (groupby(\"Nationality\")):")
print(ex9)