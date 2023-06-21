---
title: "Parallel Gpu"
date: 2023-06-21T13:41:13-07:00
draft: false
tags: []
ShowToc: true
cover:
    image: placeholder.png
    alt: ""
    caption: ""
ShowCodeCopyButtons: true
---

# Context

I am training GPT2 on document classification. I'm doing this by following the two script examples below:

// Example of GPT2 Fine-tuning **WITH** classification head
 
https://gmihaila.github.io/tutorial_notebooks/gpt2_finetune_classification/

Example of GPT2 Fine-tuning **WITHOUT** classification head (generative fine-tuning)
 
https://towardsdatascience.com/guide-to-fine-tuning-text-generation-models-gpt-2-gpt-neo-and-t5-dc5de6b3bc5e

# Command Line

CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 python -m torch.distributed.launch --nproc_per_node=8 script.py