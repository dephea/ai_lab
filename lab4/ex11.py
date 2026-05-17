import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("data.csv")

ex11 = data.groupby("Club")["Overall"].mean()


print("/////////////////////////")
print("ex11 Aflați care club are cea mai mare medie de Overall:")
print(ex11.idxmax())