from transformers import (
    DistilBertTokenizer,
    DistilBertForSequenceClassification
)

import torch

print("Loading saved model...")

tokenizer = DistilBertTokenizer.from_pretrained("bert_model")

model = DistilBertForSequenceClassification.from_pretrained(
    "bert_model"
)

tests = [
    "You are amazing",
    "You are an idiot",
    "Have a wonderful day",
    "Nobody wants you here",
    "Get lost",
    "I hope you succeed in life"
]

for text in tests:

    inputs = tokenizer(
        text,
        return_tensors="pt",
        truncation=True,
        padding=True,
        max_length=128
    )

    with torch.no_grad():
        outputs = model(**inputs)

    prediction = torch.argmax(
        outputs.logits,
        dim=1
    ).item()

    print(
        f"{text} -> {'Toxic' if prediction == 1 else 'Safe'}"
    )