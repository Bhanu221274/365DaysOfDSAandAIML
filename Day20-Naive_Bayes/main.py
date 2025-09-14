import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

data = {
    "label": ["spam", "ham", "ham", "spam", "ham"],
    "text": [
        "Win money now!!!",
        "Hey, are we still meeting today?",
        "I will call you later",
        "Congratulations! You won a free ticket",
        "Let's have lunch tomorrow"
    ]
}

df = pd.DataFrame(data)
df["label_num"] = df["label"].map({"ham": 0, "spam": 1})

X = df["text"]
y = df["label_num"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

cv = CountVectorizer()
X_train_cv = cv.fit_transform(X_train)
X_test_cv = cv.transform(X_test)

nb = MultinomialNB()
nb.fit(X_train_cv, y_train)

y_pred = nb.predict(X_test_cv)

print("Accuracy:", accuracy_score(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred, zero_division=0))


sample = ["You won a free iPhone! Claim now"]
sample_vec = cv.transform(sample)
print("Prediction:", "Spam 🚨" if nb.predict(sample_vec)[0] == 1 else "Ham ✅")
