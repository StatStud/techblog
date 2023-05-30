---
title: "S2AND: Allen AI Paper Summary"
date: 2023-03-24T16:52:30-04:00
draft: false
tags: ['author-disambiguation']
ShowToc: true
cover:
    image: s2and1.png
    alt: "S2AND Algorithm"
    caption: ""
ShowCodeCopyButtons: true
---

# Introduction
The purpose of this post is to provide readers a quick recap on the [S2AND paper by Allen AI](https://arxiv.org/pdf/2103.07534.pdf). Readers are encouraged to review the original paper for technical details they wish to further investigate. Additionally, Daniel King and Sergey Feldman have done a great job documenting S2AND development in a [separate Medium post](https://blog.allenai.org/s2and-an-improved-author-disambiguation-system-for-semantic-scholar-d09380da30e6) by Sergey Feldman.

For a post demonstrating the implementation of S2AND, feel free to read [the second part](https://google.com) of this post.

# Introduction
## What problem does this algorithm solve?

![](/s2and1.png)

S2AND is an algorithm to resolve author disambiguation in publication papers when an ORCID (or some unique identifier) is not present. These scenarios include:

- Authors with similar names
- Authors with multiple aliases
- Changes in author properties (e.g. institution, name, etc.)

## What is the output from the S2AND algorithm?

![](/s2and2.png)

The final output from S2AND is a unique author key for each record (author-paper combination). This is essentially adding a column to the records that serves as an ORCID.

## What does this paper offer?

For the community of ML practitioners, there are two main contributions from this paper:

1. S2AND, a new, unified training dataset and evaluation benchmark for author name disambiguation (AND)
2. A new, state-of-the-art open-sourced AND algorithm

Additionally, the paper itself provides additional insight, such as

1. Experiments showing that training on S2AND improves generalization
2. A comparison against the existing Semantic Scholar production system

# About the Data

## Why the need for a new AND dataset?
A common issue with many pre-existing AND datasets is that they tend to cover idiosyncratic and biased slices of the literature. For instance, the AMiner dataset consists of only Chinese names, while SCAD-zbMATH contains only mathematics papers.

Matters are further complicated when each dataset contains unique features not present in other datasets.

Such niche datasets may impair generalization performance; algorithms trained to perform well on one on dataset may generalize poorly to others.

## What makes the S2AND dataset different?

S2AND attempts to ameliorate the previously mentioned issues by harmonizing eight disparate AND datasets into a uniform format with a consistent, rich feature set drawn from the Semantic Scholar (S2) database.

## What datasets does S2AND consist of?

- Aminer
- ArnetMiner
- INSPIRE
- KISTI
- Medline
- PubMed
- QIAN
- SCAD-zbMATH

# About the Model

## How does the S2AND algorithm work?

Broadly speaking, there are three steps in the algorithm:

1. Group candidate records into disjoint, potentially-coreferent blocks
2. Score the similarity of each pair of records within a block based on available features
3. Cluster the records based on the pairwise scores

## How are records grouped into blocks?

This is often performed heuristically, based on author names; the goal is to group together records such that each pair of records within a block potentially refers to the same author (potentially-coreferent).

A record (AKA, a *signature*) is simply any author-paper combination.

![](/s2and3.png "Simple representation of signatures (Note: all other features are excluded in this illustration)")

![](/s2and4.png "An author name can have multiple signature IDs for each unique paper")

The blocks are **disjoint**, meaning that no two blocks can contain the same record (author-paper combination).

![](/s2and5.png)

Although different datasets use different blocking functions, a typical choice is to put all records with the same last name and first initial into the same block.

## How are records scored for similarity?

![](/s2and6.png "Pairwise Similarity Evaluation")

Within each block, similarity of each record pair is estimated using Gradient Boosted Trees (LightGBM); if the score is high enough, we assume that the two records were written by the same author.

It is important to note that S2AND uses an ensemble of two classifiers:

- A classifier trained on the full feature set
- An identical classifier trained on “nameless” feature set

This “nameless” feature set is identical in every respect to the full feature set, but does not contain any features related to the author names (co-author names are still included).

## What clustering method does S2AND use?

After having scored each pair within a block, S2AND implements Hierarchical Agglomerative Clustering (HAC).

Specifically, the classifier from the previous step is used to construct a distance matrix D where Dᵢⱼ is the probability that two records i and j are not by the same author. Each block is then partitioned into clusters with HAC over the matrix D.

![](/s2and7.png "Construction of Distance Matrix D")

The paper mentions how the clustering will depend on a linkage function that estimates the dissimilarity between two clusters (in terms of the pairwise distances between the individual elements of each cluster); experiments suggest that a straightforward average of all the pairwise distances performs best.

![](/s2and8.png)

Note: The use of HAC was considered after comparing only two methods: DBSCAN and HAC. The paper highlights the use of other clustering methods for future studies.

# About the Features

## What features are the models trained on?

The paper uses a total of 15 features to estimate similarity between documents. A list of these features with a brief description is shown below.

![](/s2and9.png "List of features with descriptions (credit to original paper)")

While many of these features are self-explanatory, a few warrant further explanation.

“Name counts” reflects name popularity, which is estimated as number of distinct referents of author names across S2.


“SPECTER embeddings” are the vectorized representations of the paper title and abstract (concatenated as one text). SPECTER refers to a specific document-embedding algorithm trained on the citation graph to produce paper embeddings applicable across multiple tasks.

## What are the most important features?

Feature importance is estimated using SHapley Additive exPlanations (SHAP).

The results indicate that three features appear to consistently rank as most important across all datasets (no order):

- SPECTER embedding
- Affiliations
- Name counts (last names)

Although these features appear vital in AND, this does not imply these three features alone would led to adequate model training. This is because the authors also compared feature variations (i.e. excluding certain features to evaluate performance) and found that most design alternatives hurt performance.

![](/s2and10.png "Table illustrating performance change after excluding certain features (credit to original paper)")

In other words, it is best practice to train with the full set of features.

## What additional features are helpful?
In addition to the original feature list, the authors found that imposing a feature-wise monotonicity constraints led to substantial qualitative improvements in B³.

The monotonicity constraints influence the features in order to:

- Regularize the model
- Constrain the model to behave sensibly when faced with data from outside the training distribution

This is often best explained through example:

Holding all other features constant, the model decreases the output probability if the year difference between two records increases.

Note: the output probability is the probability that any two records from the same block are by the same author.

# About Using S2AND

## What is the main takeaway when training with S2AND?

Training on the union of all datasets, rather than any single data source, is an effective way to transfer to out-of-domain data and produces models that are more robust across all the existing datasets.

## What are the limitations of S2AND?
1. S2AND features, particularly SPECTER embeddings, are only intended for English-language records
2. If certain metadata is missing, its absence could inadvertently encourage the model to learn spurious interactions and make counterintuitive predictions
3. Although the model is resistant to obvious errors (e.g. blocking “John” and “James” together because they share the same initial), this is not to suggest that all errors are accounted for, as authors can change their names, and names can be mis-extracted from papers
4. At the time of this post, there is no successful solution for recovering from name blocking errors
5. Lossy transliteration of names may occur (e.g. Chinese names to English)
6. The HAC pipeline does not allow for the similarity of one pair of records to influence the similarity of another pair of records

