---
title: "Entity Linking"
date: 2023-03-30T13:39:03-04:00
draft: false
tags: ['NLP','SRL','NER','FAISS']
ShowToc: true
cover:
    image: entity-linking1.jpeg
    alt: "Entity Linking"
    caption: ""
---

# Introduction

Entity linking is a critical task in natural language processing that  involves linking entities mentioned in text to their corresponding entries in a knowledge base. 

In this project, we implement a creative approach to entity linking that leverages the complementary capabilities of Semantic Role Labeling (SRL), Named Entity Recognition (NER), and BERT-based FAISS   indexing. 

We use SRL and NER to extract relevant queries from the input   text, which are then used to perform a search in our FAISS index. 

The index is built using a BERT-based synonym model that generates embedding vectors for each entity in the knowledge base. The candidate entities are then ranked using nearest neighbors of embedding space.   

Our proposed approach to entity linking has significant implications in the medical space for patient care and biomedical use cases by improving the accuracy and efficiency of clinical decision support systems, as well as facilitating the extraction of valuable insights from biomedical literature.
