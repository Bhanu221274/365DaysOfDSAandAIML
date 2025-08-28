import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score, confusion_matrix

X = np.array([
    [2, 1],
    [4, 1],
    [6, 2],
    [7, 3],
    [3, 2],
    [8, 3]
])
y = np.array([0, 0, 1, 1, 0, 1])

model = DecisionTreeClassifier(criterion="entropy", max_depth=3, random_state=0)
model.fit(X, y)

new_student = np.array([[5, 2]])
prediction = model.predict(new_student)
print("Prediction for student:", "Pass ✅" if prediction[0] == 1 else "Fail ❌")

y_pred = model.predict(X)

acc = accuracy_score(y, y_pred)
cm = confusion_matrix(y, y_pred)

print("\nModel Accuracy on Training Data:", acc)
print("Confusion Matrix:\n", cm)

plt.figure(figsize=(8,6))
plot_tree(
    model,
    feature_names=["Hours_Studied", "Assignments"],
    class_names=["Fail", "Pass"],
    filled=True,
    rounded=True
)
plt.title("Decision Tree Classifier")
plt.show()
