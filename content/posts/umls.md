---
title: "Unified Medical Language System (UMLS)"
date: 2023-03-28T10:53:06-04:00
draft: false
tags: ['datasets','healthcare']
ShowToc: true
cover:
    image: umls1.png
    alt: "UMLS"
    caption: ""
---

# The UMLS Explained

## What is the UMLS used for?

Let's talk about the Unified Medical Language System, or UMLS for short. 

The UMLS is a tool that helps people in the medical field understand and communicate with each other better.

Imagine you and your friend both speak different languages. It would be pretty hard to have a conversation, right? Well, in the medical field, there are lots of different words and terms that mean the same thing, depending on who you're talking to. That can be confusing and make it hard to work together.

That's where the UMLS comes in! It's like a big dictionary that takes all those different words and terms and puts them together in one place. That way, everyone can look up what they need to know and use the same language to communicate.

The UMLS helps people in the medical field work together and understand each other better. Just like how we use dictionaries to understand words in different languages, the UMLS helps doctors and scientists understand all the different medical words they need to know.

The UMLS is considered a knowledge graph because it represents biomedical knowledge as a graph of interconnected concepts and relationships.

The official site can be found [here](https://www.nlm.nih.gov/research/umls/index.html)

## What does the UMLS consist of?

![](/umls.png)

The UMLS consists of 3 components:
1. The Metathesaurus
2. Semantic Network
3. SPECIALIST Lexicon

### The Metathesaurus

The Metathesaurus is a big list of all the medical words and what they mean; it is a collection of biomedical vocabularies and codes that have been mapped and integrated into a single, unified database.

Each concept in the Metathesaurus has a unique identifier (CUI) and is linked to other concepts in the database through relationships, such as "is a" (hyponymy) and "has ingredient" (part-whole). These relationships are represented as edges in the knowledge graph.

### The Semantic Network

The Semantic Network groups all those words together based on their meanings; a hierarchy of semantic types that categorize concepts in the Metathesaurus based on their meaning and attributes.

### The SPECIALIST Lexicon

The SPECIALIST Lexicon has lexical tools to help people understand how the words are spelled and how they're used.

The SPECIALIST Lexicon includes components like 
- morphological analyzers
- spelling correction algorithms
- natural language processing tools 

The lexical information in the SPECIALIST Lexicon is organized into a hierarchy of related concepts, similar to the Semantic Network. However, the relationships between concepts in the SPECIALIST Lexicon are not represented as edges in a graph, but rather as a set of related concepts and lexical information.

# Similar Datasets

The NIH has a page of similar datasets [here](https://uts.nlm.nih.gov/uts/). These are some of the alternatives listed.
- SNOMED CT
- RxNorm
- Value Set Authority Center (VSAC)

