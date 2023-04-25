---
title: "Huggingface Caching"
date: 2023-04-25T06:48:28-04:00
draft: false
tags: ['NLP','transformers','huggingface']
ShowToc: true
cover:
    image: placeholder.png
    alt: ""
    caption: ""
---

# Introduction

Huggingface models can be quite large and require a lot of computational resources to train and run, which can be challenging for users who want to run these models on their local machines or in cloud-based environments.

One solution to this problem is to use *caching*, which involves storing *precomputed values* so that they can be reused later without having to be recalculated. 

In the context of Hugging Face and transformer models, caching involves storing intermediate values that are generated during the processing of text data using a transformer model. These values can include things like 
    - the output of attention mechanisms
    - embeddings
    - other intermediate representations of the input text

By caching these values, subsequent computations on the same text data can be much faster because the intermediate values can be reused instead of having to be recalculated from scratch. 

This can greatly speed up the processing of large amounts of text data and make it possible to use transformer models in a wider range of applications.

More information can be found [here](https://huggingface.co/docs/datasets/cache) and [here](https://huggingface.co/docs/huggingface_hub/guides/manage-cache)

# Managing Cache Directory

Practically speaking, there are three important cache environment variables that play a big role in training transformer models.

- **HUGGINGFACE_HUB_CACHE**: Sets the path where Hugging Face will store **models** (the model weights and parameters) that have been downloaded from the Hugging Face Model Hub. By default, models are stored in the user's home directory. If using a cloud computing environment, this can instead point to a larger folder location.
- **TRANSFORMERS_CACHE**: Sets the path where Hugging Face will store cached **data** for the transformer models (e.g. tokenizer vocabulary files and precomputed representations of input text).
- **PIP_CACHE_DIR**: Sets the path where pip (the Python package installer) will store downloaded packages.



