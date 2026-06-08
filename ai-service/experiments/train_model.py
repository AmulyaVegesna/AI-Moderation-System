import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import pickle

# Simple dataset
data = {
    "text": [
        "I hate you",
        "You are stupid",
        "You are ugly",
        "I love this",
        "You are amazing",
        "This is wonderful"
    ],
    "label": [1, 1, 1, 0, 0, 0]  # 1 = toxic, 0 = safe
}

df = pd.DataFrame(data)

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df["text"])

model = LogisticRegression()
model.fit(X, df["label"])

# Save files
pickle.dump(model, open("model.pkl", "wb"))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))

print("Model trained and saved!")