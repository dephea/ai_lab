from sklearn.datasets import load_iris

iris = load_iris()

print("Examples:", iris.data.shape[0])
print("Properties:", iris.data.shape[1])


print("Attributes:", iris.feature_names)

print("Classes:", iris.target_names)

