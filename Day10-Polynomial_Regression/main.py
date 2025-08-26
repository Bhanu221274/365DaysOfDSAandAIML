import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures


X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
y = np.array([1.5, 3.7, 7.2, 12.1, 18.0])

poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)


model = LinearRegression()
model.fit(X_poly, y)


y_pred = model.predict(X_poly)

new_hours = np.array([6]).reshape(-1, 1)
new_hours_poly = poly.transform(new_hours)
predicted_marks = model.predict(new_hours_poly)


print(f"Predicted marks for {new_hours[0][0]} hours: {predicted_marks[0]:.2f}")
print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)


plt.scatter(X, y, color="red", label="Original Data")   # Scatter plot of data
plt.plot(X, y_pred, color="blue", label="Polynomial Regression")  # Curve fit
plt.xlabel("Hours Studied")
plt.ylabel("Marks")
plt.title("Polynomial Regression Example")
plt.legend()
plt.show()







