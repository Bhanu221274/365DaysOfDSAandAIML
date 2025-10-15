from sklearn.datasets import make_blobs
from sklearn.cluster import DBSCAN

X, _ = make_blobs(n_samples=200, centers=3, cluster_std=0.6, random_state=42)

dbscan = DBSCAN(eps=0.7, min_samples=5)
labels = dbscan.fit_predict(X)


print("Cluster labels for each point:")
print(labels)
