import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC

df = pd.read_csv("data/labeled_data.csv")

df = df[["tweet", "class"]]
df["class"] = df["class"].apply(lambda x: 1 if x != 0 else 0)

X_train, X_test, y_train, y_test = train_test_split(
    df["tweet"],
    df["class"],
    test_size=0.2,
    random_state=42
)

vectorizer = TfidfVectorizer(
    max_features=20000,
    ngram_range=(1,3),
    min_df=2,
    stop_words="english"
)

X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

model = LinearSVC(class_weight="balanced")

model.fit(X_train_vec, y_train)

pred = model.predict(X_test_vec)

print(classification_report(y_test, pred))