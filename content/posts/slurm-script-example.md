---
title: "Slurm Script Example"
date: 2024-01-09T12:41:17-05:00
draft: false
tags: ['slurm','HPC']
ShowToc: true
cover:
    image: placeholder.png
    alt: ""
    caption: ""
ShowCodeCopyButtons: true
---

```sh
#!/bin/bash
#SBATCH -p gpu
#SBATCH -t 24:00:00

cd /main/working/dir

module load modules/anaconda3/4.3.1

conda activate env

export data_path="/some/data/path"

export HUGGINGFACE_HUB_CACHE=$data_path
export PIP_CACH_DIR=$data_path
export TRANSFORMERS_CACHE=$data_path

python script.py

```
