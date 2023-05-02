---
title: "Specter"
date: 2023-05-02T10:55:01-04:00
draft: false
tags: ['author-disambiguation','specter-embeddings']
ShowToc: true
cover:
    image: specter.png
    alt: ""
    caption: ""
---

# Introduction 
The purpose of this post will be to show you how to generate Specter Embeddings specifically for the S2AND author-disambiguation algorithm. Specter embeddings are one of the most important features used in S2AND. 

The developers of the specter embedding models have shared their model [here](https://github.com/allenai/specter), freely available for anyone to use.

My implementation of the code can be found in [this repo](https://github.com/StatStud/s2and-demo).

# The code

Without too much to waste, here's the fully code that will generate specter embeddings for a give papers.json file.

```python
import json
import pickle
import numpy as np
from transformers import AutoTokenizer, AutoModel
import os
from s2and.consts import PROJECT_ROOT_PATH
import argparse

def process_papers(input_file, output_file, data_dir):
  
  # define data dir
  dataset_name = data_dir
  DATA_DIR = os.path.join(PROJECT_ROOT_PATH, 'data', dataset_name)
  papers_path =os.path.join(DATA_DIR, dataset_name + "_papers.json")
  
  # load model and tokenizer
  tokenizer = AutoTokenizer.from_pretrained('allenai/specter')
  model = AutoModel.from_pretrained('allenai/specter')

  # read papers from input file
  with open(input_file, 'r') as f:
    data = json.load(f)

  # extract title and abstract fields from the data
  papers = []
  paper_ids = []
  for key, paper_data in data.items():
    title = paper_data['title']
    abstract = paper_data.get('abstract', '')
    paper_ids.append(paper_data['paper_id'])
    papers.append({'title': title, 'abstract': abstract})
     
  title_abs = [d['title'] + tokenizer.sep_token + (d.get('abstract') or '') for d in papers]

  # preprocess the input
  inputs = tokenizer(title_abs, padding=True, truncation=True, return_tensors="pt", max_length=512)
  result = model(**inputs)

  # take the first token in the batch as the embedding
  embeddings = result.last_hidden_state[:, 0, :].detach().numpy()
   
  # create tuple with embeddings and paper ids
  #embeddings_with_ids = (embeddings,paper_ids)
  embeddings_with_ids = tuple((embeddings, paper_ids))

  # save tuple as pickle file
  with open(output_file, 'wb') as f:
    pickle.dump(embeddings_with_ids, f)

if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='Process papers')
  parser.add_argument('input_file', help='Path to input JSON file')
  parser.add_argument('output_file', help='Path to output pickle file')
  parser.add_argument('data_dir', help='Path to data')
  args = parser.parse_args()

  process_papers(args.input_file, args.output_file, args.data_dir)
```

To run this script, all you need to type in the command line is:

```sh
python specter.py **papers.json** **embeddings.pkl** **data_dir** 
```

Where:
1. **papers.json** is the data file containing all the research papers, following the format of S2AND data checkout [this post](https://luminous-daifuku-142c42.netlify.app/posts/s2and-data/) on how to format the data
2. **embeddings.pkl** is the name we wish to give to the generated pickle file
3. **data_dir** is the folder containing all the data (i.e. the location to input paper.json file)