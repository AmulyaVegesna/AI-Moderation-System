from flask import Flask, request, jsonify
from flask_cors import CORS
import random
import os
import pickle
from pymongo import MongoClient
import os

MONGO_URI = os.getenv("MONGO_URI")
print("🔥 MONGO URI:", MONGO_URI)
client = MongoClient(MONGO_URI)
db = client["moderation_db"]
collection = db["posts"]
app = Flask(__name__)
CORS(app)
# Load model once


model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

def analyze_text(text):
    X = vectorizer.transform([text])
    prediction = model.predict(X)[0]
    prob = model.predict_proba(X)[0][1]

    score = int(prob * 100)

    if prediction == 1:
        category = "toxic"
        action = "Block"
    else:
        category = "Safe"
        action = "Allow"

    return score, category, action


@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.json
    text = data.get("text")

    score, category, action = analyze_text(text)

    post = {
        "text": text,
        "score": score,
        "category": category,
        "action": action
    }

    print("Saving to DB:", post)  # 👈 ADD THIS

    collection.insert_one(post)

    return jsonify(post)

@app.route("/posts", methods=["GET"])
def get_posts():
    posts = list(collection.find({}, {"_id": 0}))
    return jsonify(posts)

@app.route("/delete/<string:text>", methods=["DELETE"])
def delete_post(text):
    collection.delete_one({"text": text})
    return jsonify({"message": "Deleted"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5001)))
