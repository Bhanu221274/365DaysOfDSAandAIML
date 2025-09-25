from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

iris = load_iris()
X = iris.data
y = iris.target

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

print("original shape:", X.shape)
print("scaled shape:  ", X_scaled.shape)
print("pca shape:     ", X_pca.shape)
print("explained variance ratio:", pca.explained_variance_ratio_)
print("components shape:", pca.components_.shape)


