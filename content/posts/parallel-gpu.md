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

If you are running a training script that takes no arguments, then you can run the following:
```sh
CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 python -m torch.distributed.launch --nproc_per_node=8 script.py
```

Otherwise, you can also include the argparse for your script, provided that your script is updated to take in arguments.
```sh
CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 python -m torch.distributed.launch --nproc_per_node=8 script.py --model gpt2-medium --epochs 4 --batch_size 32
```

# Code
The main repo for this post can be [found here](https://github.com/StatStud/GPT-classification).

To run parallel GPU training without any parameters, use [this script](https://github.com/StatStud/GPT-classification/blob/main/distributed.py) (we'll call this scriptA).

Otherwise, to train WITH parameters, use [this script](https://github.com/StatStud/GPT-classification/blob/main/distributed-with-params.py) (we'll call this scriptB).

Let's explore what this code does.

## Explaining ScriptB 

### torch.distributed.launch
The script uses the **torch.distributed.launch** utility to enable distributed training with multiple GPUs. By setting **--nproc_per_node=4**, you specify that you want to use 4 GPUs for training.


### GPU Initialization
In the main function, the script *initializes* the distributed training environment using **dist.init_process_group(backend='nccl')**. 

It also retrieves the **local rank** for the current process and sets the GPU device accordingly using **torch.device("cuda", local_rank)**.

The script then loads the model, tokenizer, and other necessary components for training.

### Distributed Batch Samplers
The data loading part of the script creates **distributed samplers** (train_sampler, valid_sampler, and test_sampler) to ensure that each GPU processes a different subset of the data during training, validation, and testing.

During training, validation, and testing, the script goes through each batch of training data in the train function. **Each GPU processes a different batch of data simultaneously, resulting in parallel training**. The gradients from each GPU are **averaged** and used to update the model parameters. 

The script prints the training and validation loss, as well as the training and validation accuracy, for each epoch.

After training, the script evaluates the model on the test dataset using the test function. Again, each GPU processes a different batch of test data in parallel.

Finally, the script generates an evaluation report, including classification metrics such as precision, recall, and F1-score.

In summary, the script trains one model with the help of multiple GPUs, where each GPU processes a different batch of data in parallel. The training process and the model parameters are synchronized across all GPUs to ensure consistent updates.
