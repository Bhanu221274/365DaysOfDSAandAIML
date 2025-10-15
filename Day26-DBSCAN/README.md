Day 26 – DBSCAN Clustering 🌌

🔹 What I Learned

DBSCAN (Density-Based Spatial Clustering of Applications with Noise) is an unsupervised learning algorithm used for clustering data points.

It groups points based on density, making it excellent for discovering clusters of arbitrary shapes.

Points in low-density areas are labeled as noise and assigned a label of -1.

Unlike K-Means, DBSCAN does not require the number of clusters to be specified in advance.

Key parameters:

eps → defines the radius to look for neighboring points

min_samples → minimum number of points required to form a dense region (cluster)

Advantages:

Can identify clusters of any shape, not just spherical.

Robust to outliers.

Automatically identifies noise points.

Limitations:

Performance depends on appropriate selection of eps and min_samples.

Not suitable for datasets with varying density clusters.

🔹 Implementation

Generated a synthetic dataset with 3 clusters using make_blobs from scikit-learn.

Applied DBSCAN with eps=0.7 and min_samples=5.

Retrieved cluster labels for all data points, where -1 indicates noise.

Evaluated how well the clusters matched the underlying structure of the dataset.

🔹 Key Learnings from Implementation

Understanding how density-based clustering works in practice.

Seeing how noise points are automatically identified without manual labeling.

Learning to tune DBSCAN parameters (eps and min_samples) for better clustering results.

Comparing DBSCAN with other clustering algorithms like K-Means and understanding when to use each.
