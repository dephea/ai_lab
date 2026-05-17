import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier

iris = load_iris()

X = iris.data[:, 2:4]  # petal length, petal width
y = iris.target

plt.scatter(X[:, 0], X[:, 1], c=y)
plt.xlabel("petal length")
plt.ylabel("petal width")
plt.title("Iris classes (2 features)")
plt.show()


model = KNeighborsClassifier(n_neighbors=3)
model.fit(X, y)

sl = float(input("petal length: "))
sw = float(input("petal width: "))

new_flower = [[sl, sw]]


prediction = model.predict(new_flower)

print("class:", iris.target_names[prediction[0]])