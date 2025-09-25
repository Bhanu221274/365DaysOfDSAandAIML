📘 Day 24 Principal Component Analysis (PCA)

Today, I explored Principal Component Analysis (PCA), a powerful dimensionality reduction technique in Machine Learning. PCA is widely used to simplify datasets, remove noise, and speed up model training while retaining maximum information.

🔑 What is PCA?

PCA is a statistical technique that transforms high-dimensional data into a smaller set of uncorrelated variables called principal components.

These components capture the maximum variance in the data.

The first component captures the highest variance, the second captures the next highest, and so on.

🛠 Steps of PCA

Standardization

Normalize the dataset so that all features contribute equally.

Example:

from sklearn.preprocessing import StandardScaler
X_scaled = StandardScaler().fit_transform(X)


Covariance Matrix Computation

Compute the covariance matrix to understand relationships between features.

Eigen Decomposition

Find eigenvalues and eigenvectors from the covariance matrix.

Eigenvectors = directions of maximum variance (principal components).

Eigenvalues = amount of variance captured by each eigenvector.

Sort & Select Principal Components

Sort eigenvalues in descending order.

Select the top k components based on variance explained.

Transform Data

Project original data onto the new feature space.

Syntax:

from sklearn.decomposition import PCA
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)


This plots the dataset in 2D space after PCA, showing how well the reduced dimensions separate classes.

✅ Key Takeaways

PCA is unsupervised (doesn’t use labels).

Helps reduce dimensionality and visualize high-dimensional data.

Useful in image compression, noise filtering, and speeding up ML algorithms.
