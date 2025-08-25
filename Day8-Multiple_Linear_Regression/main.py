import numpy as np
from sklearn.linear_model import LinearRegression

X = np.array([
    [1000, 2],
    [1500, 3],
    [1200, 2],
    [1700, 3],
    [2000, 4]
])

y = np.array([300, 450, 330, 500, 600])
model = LinearRegression()

model.fit(X, y)

new_house = np.array([[1600, 3]])
predicted_price = model.predict(new_house)

print(f"\nPredicted price for house {new_house[0]}: {predicted_price[0]:.2f}k")
print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)
