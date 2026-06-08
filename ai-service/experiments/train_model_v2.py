import pandas as pd
import pickle

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC

print("Loading dataset...")

df = pd.read_csv("data/labeled_data.csv")

# Keep only required columns
df = df[["tweet", "class"]]

# Convert to binary classification
# 0 = toxic, 1 = toxic, 2 = safe
df["label"] = df["class"].apply(lambda x: 0 if x == 2 else 1)

X = df["tweet"]
y = df["label"]

print("Training samples:", len(df))

vectorizer = TfidfVectorizer(
    max_features=20000,
    ngram_range=(1,3),
    min_df=2,
    stop_words="english"
)

X_vec = vectorizer.fit_transform(X)

print("Training LinearSVC model...")

model = LinearSVC(class_weight="balanced")

model.fit(X_vec, y)

pickle.dump(model, open("model_v2.pkl", "wb"))
pickle.dump(vectorizer, open("vectorizer_v2.pkl", "wb"))

print("✅ Training complete")