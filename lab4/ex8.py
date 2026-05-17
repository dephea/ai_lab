import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("data.csv")

top5 = data["Nationality"].value_counts().head(5)

#ex 8
# Reprezentați într-un pie chart proporția jucătorilor pe naționalități (top 5)
plt.pie(top5, labels=top5.index, autopct='%1.1f%%')

plt.title("Top 5 Nationalities (ex8)")

plt.show()