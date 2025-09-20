Day 22 – K-Means Clustering 🌐


🔹 What I Learned

K-Means is an unsupervised machine learning algorithm used to group similar data points into clusters without needing labels.

Clusters are formed based on the distance of points from centroids (the center of each cluster).

The algorithm iteratively updates centroids by calculating the mean of points in each cluster until centroids stop moving significantly (convergence).

Each data point is assigned to the nearest centroid, forming a cluster.

Key points about K-Means:

k (number of clusters): You must decide how many clusters to form.

Centroids: Initial random positions that move during training.

Distance metric: Usually Euclidean distance is used.

Convergence: The algorithm stops when centroids do not change significantly.

Applications:

Customer segmentation in marketing.

Document and text clustering.

Image compression (reducing colors).

Anomaly detection (points far from centroids).

Recommendation systems.

Visualization: Plotting clusters and centroids helps to understand cluster formation and see where new data points belong.

🔹 Implementation

Created a simple dataset of students with features: Hours Studied and Marks Scored.

Applied KMeans clustering with n_clusters=2 to divide students into two groups (e.g., high performers vs low performers).

Visualized the clustered data points, centroids, and new student prediction using matplotlib.

Demonstrated how a new student can be assigned to a cluster based on proximity to centroids.

🔹 Insights from Visualization

Colored points represent cluster assignments.

Black Xs represent final centroids after convergence.

New points can be plotted to see which cluster they belong to.

Helps in understanding the pattern and similarity among data points.

