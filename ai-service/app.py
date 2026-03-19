from flask import Flask, request, jsonify
import random
from transformers import pipeline

app = Flask(__name__)
# Load model once
classifier = pipeline("text-classification", model="unitary/toxic-bert")

def analyze_text(text):
    result = classifier(text)[0]

    score = result["score"]
    label = result["label"]

    # Convert to percentage
    score_percent = int(score * 100)

    # 🔥 FIX: apply threshold
    if score < 0.5:
        return score_percent, "Safe"
    else:
        return score_percent, label


@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.json
    text = data.get("text")

    score, category = analyze_text(text)

    return jsonify({
        "score": score,
        "category": category
    })


if __name__ == "__main__":
    app.run(port=5001, debug=True)
