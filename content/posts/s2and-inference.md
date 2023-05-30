---
title: "S2AND Inference on Custom Data"
date: 2023-05-02T11:25:49-04:00
draft: false
tags: ['author-disambiguation']
ShowToc: true
cover:
    image: s2and2.png
    alt: ""
    caption: ""
ShowCodeCopyButtons: true
---

# Introduction

In this post, we actually run the saved model we have on file on the our own custom dataset.

# The Code 

S2AND comes with a production model that has already been pretrained on their own collection of data.

To run the production model on your unique datasets, simply run the code below:


```python
import pickle

# reload model
with open("data/production_model.pkl", "rb") as _pkl_file:
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
 'a roberts_1': ['2', '21'],
 'a roberts_2': ['12'],
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

## Similar names, different people

 Let's start with 'Katherine Lee'; her name is mentioned twice in two different papers--are these the same person?

 ```sh
    "3": {
        "author_id": 8130398,
        "paper_id": 0,
        "signature_id": "3",
        "author_info": {
            "given_block": "k lee",
            "block": "k lee",
            "position": 3,
            "first": "Katherine",
            "middle": null,
            "last": "lee",
            "suffix": null,
            "affiliations": [],
            "email": null
        },
    "18": {
        "author_id": 1659573,
        "paper_id": 3,
        "signature_id": "18",
        "author_info": {
            "given_block": "k lee",
            "block": "k lee",
            "position": 1,
            "first": "Katherine",
            "middle": null,
            "last": "lee",
            "suffix": null,
            "affiliations": [],
            "email": null
        }
 ```

If we look for 'Katherine Lee' in the signatures.json, we find that the signatures_ids that correspond to 'Katherine Lee' are 3 and 18.

 ```sh
 'k lee_1': ['3'],
 'k lee_2': ['18'],
 ```

Looking at the output from the model, we see that signature_ids 3 and 18 are placed in two distinct buckets ('k lee_1', and 'k lee_2', respectively).

This means the model predicts the two mentions of 'Katherine Lee' are two *separate* people.

## Similar names, same person

Now let's look at another example

```sh
    "2": {
        "author_id": 1992890,
        "paper_id": 0,
        "signature_id": "2",
        "author_info": {
            "given_block": "a roberts",
            "block": "a roberts",
            "position": 2,
            "first": "Adam",
            "middle": null,
            "last": "roberts",
            "suffix": null,
            "affiliations": [],
            "email": null
        }, 
    "21": {
        "author_id": 4297540,
        "paper_id": 4,
        "signature_id": "21",
        "author_info": {
            "given_block": "a roberts",
            "block": "a roberts",
            "position": 1,
            "first": "Adam",
            "middle": null,
            "last": "roberts",
            "suffix": null,
            "affiliations": [],
            "email": null
        }
```

 Is 'Adam Roberts' from the paper titled "Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer" (paper_id 0) the *same* 'Adam Roberts' from the paper titled "Robust Multi-Agent Reinforcement Learning with Incomplete Information" (paper_id 4)?


```sh
 'a roberts_1': ['2', '21'],
 'a roberts_2': ['12'],
```
 According to the above results, the model predicts that the answer is **yes**.

 Why? 

 Because we see that signature_ids 2 and 21 are grouped in the same bucket, and hence considered to be the same person.

## Same Names, but different people

 But what about Adam Roberts from the paper "Toward Personalized Conversational Agents: A Longitudinal Field Study of a Knowledge-Grounded Chatbot"? Is this Adam Roberts the same person from the other two papers?

 ```sh
 'a roberts_1': ['2', '21'],
 'a roberts_2': ['12'],
```

According to the model output, the predicted answer is **no**, because the signature_id that corresponds with this author is in a *separate* bucket from the other mentions of Adam Roberts.

So, out of three mentions of the name "Adam Roberts", two of them are predicted to refer to the same author, while the other one is likely to be a different person with the same name (Just like the same with Katherine Lee).

 # Great, so how can we practically use this output?

 The unique bucket (e.g. 'a roberts_1') servers as a ORCID that you can merge with the signatures.json file; this puts you in a position to compare two identical or similar names, and determine whether or not they are the same person, depending on if their "ORCID"s match.