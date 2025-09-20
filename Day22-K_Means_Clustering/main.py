import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

X = np.array([
    [2, 10],
    [2, 5],
    [8, 4],
    [5, 8],
    [7, 5],
    [6, 4],
    [1, 2],
    [4, 9]
])

kmeans = KMeans(n_clusters=2, random_state=0)
kmeans.fit(X)
labels = kmeans.labels_
centroids = kmeans.cluster_centers_

plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='rainbow', s=100)
plt.scatter(centroids[:, 0], centroids[:, 1], c='black', marker='X', s=200)
plt.xlabel("Hours")
plt.ylabel("Marks")
plt.title("K-Means Clustering")
plt.show()
