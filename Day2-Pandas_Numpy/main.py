import pandas as pd
import numpy as np

students=np.array(["Bhanu","Mohan","Ashrith","Rajesh","Shiva"])
scores=np.array([20,18,15,10,16])

data = pd.DataFrame({
    "Student": students,
    "Score": scores
})

print("\nMean Score (Pandas):", data["Score"].mean())


print("Mean Score (NumPy):", np.mean(scores))


above_avg_mask = scores > np.mean(scores)

print("\nAbove Average (NumPy):", students[above_avg_mask])


data["Above_Avg"] = above_avg_mask
print("\n📊 Data with Above Average Column:")
print(data)