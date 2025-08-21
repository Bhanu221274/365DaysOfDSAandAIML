import matplotlib.pyplot as plt
import numpy as np
import sklearn as sk

hours=np.array([1,2,3,4,5]).reshape(-1,1)
scores=np.array([10,20,30,40,50])

model=sk.linear_model.LinearRegression()
model.fit(hours,scores)

hours_pred=model.predict(hours)

print(hours_pred)

plt.scatter(hours, scores, color='blue', label="Actual Data")
plt.plot(hours, scores, color='red', label="Best Fit Line")
plt.xlabel("Hours Studied")
plt.ylabel("Marks Scored")
plt.legend()
plt.show()