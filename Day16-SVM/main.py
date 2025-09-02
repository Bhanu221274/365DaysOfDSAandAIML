import pandas as pd
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

data = {
    'Hours': [1,2,3,4,5,6,7,8,9,10],
    'Assignments': [1,2,1,3,4,3,6,7,8,9],
    'Pass': [0,0,0,0,1,1,1,1,1,1]
}
df = pd.DataFrame(data)
x_train, x_test, y_train, y_test = train_test_split(df[['Hours','Assignments']],df['Pass'] , test_size=0.2, random_state=42)

X = df[['Hours','Assignments']]
y = df['Pass']

model = SVC(kernel='linear')
model.fit(x_train, y_train)

y_pred = model.predict(x_test)
print("Accuracy:", accuracy_score(y_test, y_pred))

