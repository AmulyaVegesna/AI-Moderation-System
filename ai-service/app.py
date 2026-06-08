from flask import Flask, request, jsonify
from flask_cors import CORS
import random
import os
from pymongo import MongoClient
import os
import torch

from transformers import (
    DistilBertTokenizer,
    DistilBertForSequenceClassification
)

MONGO_URI = os.getenv("MONGO_URI")

if not MONGO_URI:
    print("❌ MONGO_URI NOT FOUND")
    exit(1)

print("✅ USING MONGO:", MONGO_URI)
client = MongoClient(MONGO_URI)
db = client["moderation_db"]
collection = db["posts"]
app = Flask(__name__)
CORS(app)
# Load model once

print("Loading DistilBERT model...")

tokenizer = DistilBertTokenizer.from_pretrained(
    "bert_model"
)

model = DistilBertForSequenceClassification.from_pretrained(
    "bert_model"
)

model.eval()

print("DistilBERT loaded successfully")

def analyze_text(text):

    inputs = tokenizer(
        text,
        return_tensors="pt",
        truncation=True,
        padding=True,
        max_length=128
    )

    with torch.no_grad():
        outputs = model(**inputs)

    logits = outputs.logits

    prediction = torch.argmax(
        logits,
        dim=1
    ).item()

    probabilities = torch.softmax(
        logits,
        dim=1
    )

    score = int(
        probabilities.max().item() * 100
    )

    if prediction == 1:
        category = "toxic"
        action = "Block"
    else:
        category = "Safe"
        action = "Allow"

    return score, category, action


@app.route("/analyze", methods=["POST"])
def analyze():
    try:
        data = request.json
        text = data.get("text")

        score, category, action = analyze_text(text)

        post = {
            "text": text,
            "score": score,
            "category": category,
            "action": action
        }

        # 🔥 SAVE TO DB
        try:
            collection.insert_one(post)
            print("✅ Saved to MongoDB:", post)
        except Exception as db_error:
            print("❌ DB Insert Error:", db_error)

        return jsonify({
            "score": score,
            "category": category,
            "action": action
        })

    except Exception as e:
        print("❌ ANALYZE ERROR:", e)
        return jsonify({"error": str(e)}), 500
    
    
@app.route("/posts", methods=["GET"])
def get_posts():
    try:
        posts = list(collection.find({}, {"_id": 0}))
        return jsonify(posts)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/delete/<string:text>", methods=["DELETE"])
def delete_post(text):
    collection.delete_one({"text": text})
    return jsonify({"message": "Deleted"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5001)))
