Day 18 – K-Nearest Neighbors (KNN) 

🔹 What I Learned

- KNN is a simple algorithm that makes predictions based on the nearest data points.

- It uses distance metrics (like Euclidean) to find the closest neighbors.

- Classification → majority vote of neighbors.

- Regression → average of neighbors.

- Key parameters:

  - n_neighbors (K) → number of neighbors considered.

  - metric → distance calculation (default: Euclidean).

- Sensitive to scaling, so normalization/standardization helps.

🔹 Implementation

- Dataset: Student Pass/Fail (based on Hours Studied & Assignments).

- Implemented KNeighborsClassifier from scikit-learn.

- Used K=3 for predictions.

- Evaluated using Accuracy Score and Confusion Matrix.

- Predicted outcome for a new student’s performance.
