import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

X = np.array([
    [2, 1],
    [4, 1],
    [6, 2],
    [7, 3],
    [3, 2],
    [8, 3],
])
y = np.array([0, 0, 1, 1, 0, 1])

model = RandomForestClassifier(n_estimators=10, max_depth=3, random_state=0)
model.fit(X, y)

new_student = np.array([[5, 2]])
prediction = model.predict(new_student)
print("Prediction for student:", "Pass ✅" if prediction[0] == 1 else "Fail ❌")

y_pred = model.predict(X)
print("Model Accuracy:", accuracy_score(y, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y, y_pred))
