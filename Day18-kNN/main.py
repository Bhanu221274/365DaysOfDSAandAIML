import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

X = np.array([
    [2, 1],
    [4, 1],
    [6, 2],
    [7, 3],
    [3, 2],
    [8, 3],
])
y = np.array([0, 0, 1, 1, 0, 1])

model = KNeighborsClassifier(n_neighbors=3)
model.fit(X, y)

new_student = np.array([[5, 2]])
prediction = model.predict(new_student)
print("Prediction for student:", "Pass ✅" if prediction[0] == 1 else "Fail ❌")


y_pred = model.predict(X)
print("\nAccuracy:", accuracy_score(y, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y, y_pred))
print("\nClassification Report:\n", classification_report(y, y_pred))
