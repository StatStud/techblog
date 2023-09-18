---
title: "Huggingface Classification"
date: 2023-09-10T13:50:29-07:00
draft: false
tags: []
ShowToc: true
cover:
    image: placeholder.png
    alt: ""
    caption: ""
ShowCodeCopyButtons: true
---

First make all your imports and define your model and tokenizer:

```py
from transformers import AutoModelForSequenceClassification, AutoTokenizer
from transformers import RobertaTokenizer
import torch
import pandas as pd

model = AutoModelForSequenceClassification.from_pretrained("bert-base-uncased").to('cuda')
tokenizer = RobertaTokenizer.from_pretrained('bert-base-uncased')
```
**NOTE**: Adding ".to('cuda')" to the model instance is *vital* if you wish to speed up inference time (trust me, you want to do this)

Next, create the actual function to run inference:

```py
def classify_text(text):

    # Tokenize the input text
    inputs = tokenizer(text, return_tensors='pt').to('cuda')

    # Pass the input through the model to get logits
    logits = model(**inputs).logits

    # Use the logits to get the predicted label
    predicted_class_idx = torch.argmax(logits, dim=1).item()

    # Map the predicted index to the corresponding label
    predicted_label = list(labels)[predicted_class_idx]

    return predicted_label

text = "This is an example sentence for classification"
classify_text(text)
```
**NOTE**: Again, add the tokenizer to the GPU via ".to('cuda')". This is important for speed.

And that's it! Now if you wish to apply it to your pandas dataset, 
all you need to run is something like this:

```py
def classify_text_on_dataframe(row):
    text = row['text']
    predicted_label = classify_text(text)
    return predicted_label

# Apply the function to the DataFrame using the apply method
df['predicted_label'] = df.apply(classify_text_on_dataframe, axis=1)
```