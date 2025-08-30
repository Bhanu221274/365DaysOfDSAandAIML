# Day 14 – Random Forest Classifier 🌲

## 🔹 What I Learned

- Random Forest is an ensemble method that uses multiple decision trees.
- Instead of trusting one tree, it combines many and takes a majority vote (classification) or average (regression).
- Reduces overfitting and improves accuracy compared to a single decision tree.
- Uses bootstrapping (sampling with replacement) and random feature selection.
- Key parameters:
  - n_estimators → number of trees
  - max_depth → depth of trees
  - random_state → reproducibility

## 🔹 Implementation

- Dataset: Student Pass/Fail (based on Hours Studied & Assignments).
- Trained RandomForestClassifier using scikit-learn.
- Evaluated with accuracy score and confusion matrix.
- Made predictions for new students.

