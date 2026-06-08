import pandas as pd
import torch

from sklearn.model_selection import train_test_split

from transformers import (
    DistilBertTokenizer,
    DistilBertForSequenceClassification,
    Trainer,
    TrainingArguments
)

print("Loading dataset...")

df = pd.read_csv("data/labeled_data.csv")

df = df[["tweet", "class"]]

df["label"] = df["class"].apply(
    lambda x: 0 if x == 2 else 1
)

train_texts, test_texts, train_labels, test_labels = train_test_split(
    df["tweet"],
    df["label"],
    test_size=0.2,
    random_state=42,
    stratify=df["label"]
)

print("Loading tokenizer...")

tokenizer = DistilBertTokenizer.from_pretrained(
    "distilbert-base-uncased"
)

class ToxicDataset(torch.utils.data.Dataset):

    def __init__(self, texts, labels):

        self.encodings = tokenizer(
            list(texts),
            truncation=True,
            padding=True,
            max_length=128
        )

        self.labels = list(labels)

    def __getitem__(self, idx):

        item = {
            key: torch.tensor(val[idx])
            for key, val in self.encodings.items()
        }

        item["labels"] = torch.tensor(
            self.labels[idx]
        )

        return item

    def __len__(self):

        return len(self.labels)

train_dataset = ToxicDataset(
    train_texts,
    train_labels
)

test_dataset = ToxicDataset(
    test_texts,
    test_labels
)

print("Loading model...")

model = DistilBertForSequenceClassification.from_pretrained(
    "distilbert-base-uncased",
    num_labels=2
)

training_args = TrainingArguments(
    output_dir="./results",
    num_train_epochs=1,
    per_device_train_batch_size=8,
    per_device_eval_batch_size=8,
    save_strategy="no",
    report_to="none"
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset
)

print("Starting training...")

trainer.train()

print("\nEvaluating...")

predictions = trainer.predict(test_dataset)

preds = predictions.predictions.argmax(axis=1)

from sklearn.metrics import classification_report

print(
    classification_report(
        test_labels,
        preds
    )
)

model.save_pretrained("bert_model")
tokenizer.save_pretrained("bert_model")

print("Model saved successfully!")