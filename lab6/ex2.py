from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import pandas as pd

iris = load_iris()


# ex2:
X_train, X_test, y_train, y_test = train_test_split(
    iris.data,
    iris.target,
    test_size=0.2,
    random_state=42
)

print("////////////////")
print("ex2: ")

print("X_train:", X_train.shape)
print("y_train:", y_train.shape)

print("X_test:", X_test.shape)
print("y_test:", y_test.shape)


# ex3:

print("////////////////")
print("ex3: ")

df = pd.DataFrame(iris.data, columns=iris.feature_names)

print("before:")
print(df.head(3))

scaler = StandardScaler()

data_scaled = scaler.fit_transform(iris.data)

df_scaled = pd.DataFrame(data_scaled, columns=iris.feature_names)

print("after:")
print(df_scaled.head(3))




# ex4: 
print("////////////////")
print("ex4: ")

model = KNeighborsClassifier(3)

model.fit(X_train, y_train)

predictions = model.predict(X_test)

print("original:\n")

print("predictions:\n", predictions)
print("y_test:\n", y_test)

print("accuracy score: ",accuracy_score(y_test, predictions))

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model.fit(X_train_scaled, y_train)

predictions = model.predict(X_test_scaled)

print("scaled:\n")

print("predictions:\n", predictions)
print("y_test:\n", y_test)

print("accuracy score: ",accuracy_score(y_test, predictions))


################

#ex5:

k_values = range(1, 16)
accuracies = []

for k in k_values:
    model = KNeighborsClassifier(n_neighbors=k)
    model.fit(X_train_scaled, y_train)

    predictions = model.predict(X_test_scaled)
    acc = accuracy_score(y_test, predictions)

    accuracies.append(acc)

plt.plot(k_values, accuracies)
plt.xlabel("k (neighbours)")
plt.ylabel("Accuracy")
plt.title("ex 5")
plt.show()

#ex6:

print("////////////////")
print("ex6: ")

cm = confusion_matrix(y_test, predictions)
print(cm)


print(classification_report(y_test, predictions))