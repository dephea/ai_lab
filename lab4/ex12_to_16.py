import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("data.csv")

def convert_money(value):
    value = value.replace('€', '')

    if 'M' in value:
        return float(value.replace('M', '')) * 1_000_000

    if 'K' in value:
        return float(value.replace('K', '')) * 1_000

    return float(value)

data["Value_num"] = data["Value"].apply(convert_money)
data["Wage_num"] = data["Wage"].apply(convert_money)

result = data[data["Value_num"] > data["Wage_num"]]

print("/////////////////////////")
print("ex12 Câți jucători au o valoare de transfer mai mare decât salariul?:")

print (len(result))


#ex13

print("/////////////////////////")
print("ex13 Creați o coloană nouă “is_underpaid” care este True dacă Wage < Value / 100:")

data["is_underpaid"] = data["Wage_num"] < (data["Value_num"] / 100)

print(data[["Value", "Wage", "is_underpaid"]])


#ex14

data["CustomScore"] = (
    0.3 * data["Overall"] +
    0.3 * data["Potential"] +
    0.2 * data["SprintSpeed"]
)

print("/////////////////////////")
print("ex14 Construiți un scor general pentru fiecare jucător pe baza unei formule proprii: ex:Scor = 0.3 * Overall + 0.3 * Potential + 0.2 * SprintSpeed:")

print(data[["Name", "CustomScore"]])


#ex15

print("/////////////////////////")
print("ex15 Care jucatori reprezinta o “afacere buna”:")
print("Afisati doar coloanele Name, Wage, Value intr-un nou df")
print("Adaugati o noua coloana “difference” in care sa calculati diferenta dintre value(current market value) si wage(current wage)")
print("Afisati jucatorii in ordine descrescatoare, de la cea mare diferenta la cea mai mica")

new_df = data[["Name", "Wage", "Value", "Wage_num", "Value_num"]].copy()

new_df["difference"] = new_df["Value_num"] - new_df["Wage_num"]

new_df = new_df.sort_values(by="difference", ascending=False)

print(new_df[["Name", "Wage", "Value", "difference"]])

#ex16
#Creati un grafic pentru a vizualiza mai bine datele.(seaborn scatterplot)
sns.scatterplot(
    data=new_df,
    x="Wage_num",
    y="Value_num"
)

plt.title("Player Value vs Wage (ex16)")

plt.show()