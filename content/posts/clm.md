---
title: "Transformers: Causal Language Modeling Versus Mask Language Modeling"
date: 2023-05-10T02:16:06-04:00
draft: false
tags: ['language-models']
ShowToc: true
cover:
    image: clm.png
    alt: ""
    caption: ""
---

# Introduction

In this post, we will investigate the differences between Causal Language Modeling (CLM) and Masked Language Modeling (MLM)

# What is Causal Language Modeling?

Causal Language Modeling (CLM) is a type of language modeling task where the model is trained to predict the next word in a sequence, given the previous words in the sequence; the model is trained to generate a sequence of words that makes sense in a given context.

CLM is a common pre-training objective used in transformer models, including the popular GPT (Generative Pre-training Transformer) models. 

By training a transformer model to perform CLM, it can learn to generate high-quality natural language text, which can be fine-tuned for a wide range of downstream tasks, such as language translation, text classification, and question answering.

# How is CLM different from MLM?
The key difference between CLM and MLM is in the way they process input data. 

In CLM, the model processes a sequence of words *from left to right*, predicting each word based on the preceding words. 

In contrast, MLM processes the *entire* input sequence at once, and the model is trained to predict masked words based on the *surrounding* context.

![](/clm.png)

CLM is strictly "looking" from left to right, and predicting the text that comes directly after, whereas MLM "looks" both ways (before the generated and after). CLM is *unidirectional*, while MLM is *bidirectional*.


Both training techniques also serve different purposes.

CLM is useful for *generating text*, while MLM is useful for learning *contextual representations* of words that can be fine-tuned for a wide range of downstream tasks, such as language translation and sentiment analysis.