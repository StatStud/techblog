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





