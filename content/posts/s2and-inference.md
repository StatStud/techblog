---
title: "S2AND Inference on Custom Data"
date: 2023-05-02T11:25:49-04:00
draft: false
tags: []
ShowToc: true
cover:
    image: s2and2.png
    alt: ""
    caption: ""
---

# Introduction

In this post, we actually run the saved model we have on file on the our own custom dataset.

# The Code 

```python
import pickle

# reload model
with open("saved_model.pkl", "rb") as _pkl_file:
  clusterer = pickle.load(_pkl_file)

dataset_name = 'fake' #this points to folder with generated data
DATA_DIR = os.path.join(PROJECT_ROOT_PATH, 'data', dataset_name)
signatures=os.path.join(DATA_DIR, dataset_name + "_signatures.json")
papers=os.path.join(DATA_DIR, dataset_name + "_papers.json")
paper_embeddings=os.path.join(DATA_DIR, dataset_name + "_specter.pickle")
name=dataset_name

anddata = ANDData(
  signatures=signatures,
  papers=papers,
  specter_embeddings=paper_embeddings,
  name=name,
  mode="inference",
  block_type="s2",
)
   
pred_clusters, pred_distance_matrices = clusterer.predict(anddata.get_blocks(), anddata)

```
# Analyzing the results

After running the model on our generated data, where's what the output for the variable pred_clusters looks like:

```sh
{'c raffel_0': ['0'],
 'n shazeer_0': ['1'],
 'a roberts_1': ['2'],
 'a roberts_3': ['12'],
 'a roberts_2': ['21'],
 'k lee_1': ['3'],
 'k lee_2': ['18'],
 's narang_0': ['4'],
 'm matena_0': ['5'],
 'y zhou_0': ['6'],
 'w li_1': ['7'],
 'w li_2': ['16'],
 'z zhou_0': ['8'],
 'm zhou_0': ['9'],
 'y chen_0': ['10'],
 'y xu_0': ['11'],
 't huang_0': ['13'],
 's goyal_0': ['14'],
 'n kumar_0': ['15'],
 'j hartman_0': ['17'],
 'a green_0': ['19'],
 'n lee_0': ['20'],
 'd brown_0': ['22'],
 'j chen_0': ['23'],
 'c reynolds_0': ['24'],
 's lee_0': ['25'],
 'l martinez_0': ['26']}
 ```

 As you can see, S2AND returns a dictionary element where the key is the unique block and the value is a list of all of signatures that belong to that block.

 What does this practically mean? Recall that our signatures.json has 27 total records, but only 23 unique names--specifically, the names ['Katherine Lee', 'Wei Li', 'Adam Roberts'] are the ones with duplicates.

 So our question becomes: 
 
 Is 'Adam Roberts' from the paper titled "Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer" (paper_id 0) the *same* 'Adam Roberts' from the paper titled "Robust Multi-Agent Reinforcement Learning with Incomplete Information" (paper_id 4)?

 According to the above results, the model predicts that the answer is *no*.

 Why? 
 
 First because there there are no more than one listed signatures for any given block (this means all 27 names are represent unique people).

 Second, when you look specifically at the "a roberts_#" section, you see that the signature_id 21 (which corresponds to paper_id 4, when looking at both signatures.json and papers.json) is in it's own bucket ('a roberts_2'), whereas the signature_id 2 (which corresponds to paper_id 0) is also in a separate bucket ( 'a roberts_1').

 ```sh
 'a roberts_1': ['2'],
 'a roberts_3': ['12'],
 'a roberts_2': ['21']
 ```

 # How can we tell if a group of people are the same?

Now, here's how the results would look if all three mentions of Adam Roberts referred to the *same* person:

 ```sh
 'a roberts_1': ['2, 12, 21']
 ```

 As you see in this case, all three signatures_ids that refer to Adam Roberts are grouped in the same bucket ('a roberts_1'); this would indicate that the paper_ids that correspond to these signature_ids all refer to the same person.

 # Great, so how can we practically use this output?

 The unique bucket (e.g. 'a roberts_1') servers as a ORCID that you can merge with the signatures.json file; this puts you in a position to compare two identical or similar names, and determine whether or not they are the same person, depending on if their "ORCID"s match.