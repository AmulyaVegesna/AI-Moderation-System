from flask import Flask, request, jsonify
import random
from transformers import pipeline
import os

app = Flask(__name__)
# Load model once
classifier = pipeline("sentiment-analysis")

def analyze_text(text):
    result = classifier(text)[0]

    score = int(result['score'] * 100)

    if result['label'] == "NEGATIVE":
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

    return jsonify({
    "score": score,
    "category": category,
    "action": action
})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5001)))
