---
title: "S2AND Data"
date: 2023-04-18T15:04:45-04:00
draft: false
tags: ['author-disambiguation','datasets']
ShowToc: true
cover:
    image: s2and11.png
    alt: "Cover"
    caption: ""
---

Here is what the papers.json looks like for ArnetMiner.

```json
"15718873": {
        "paper_id": 15718873,
        "title": "A predictive empirical model for pricing and resource allocation decisions",
        "abstract": "We present a semi-parametric model that describes pricing behaviors in a market environment, and we show how that model can be used to guide resource allocation and pricing decisions in an autonomous trading agent. We validate our model by presenting experimental results obtained in the Trading Agent Competition for Supply Chain Management.",
        "journal_name": null,
        "venue": "ICEC",
        "year": 2007,
        "references": [
            40571,
            556512,
            670266,
            1058249,
            1937296,
            3086197,
            6190706,
            14544267,
            15490824,
            15607829,
            16041257,
            17261939,
            19006713,
            26314016,
            52819017,
            60981168,
            120049887,
            124992180,
            125648827,
            126099359,
            151245949,
            167908624,
            208846619,
            40571,
            556512,
            670266,
            1058249,
            1937296,
            3086197,
            6190706,
            14544267,
            15490824,
            15607829,
            16041257,
            17261939,
            19006713,
            26314016,
            52819017,
            60981168,
            120049887,
            124992180,
            125648827,
            126099359,
            151245949,
            167908624,
            208846619
        ],
        "authors": [
            {
                "position": 3,
                "author_name": "Paul R. Schrater"
            },
            {
                "position": 2,
                "author_name": "Maria L. Gini"
            },
            {
                "position": 1,
                "author_name": "John Collins"
            },
            {
                "position": 4,
                "author_name": "Alok Gupta"
            },
            {
                "position": 0,
                "author_name": "Wolfgang Ketter"
            }
        ]
    }
```

Here is what the signatures.json file looks like for ArnetMiner:

```json
"34": {
        "author_id": 6879414,
        "paper_id": 15718873,
        "signature_id": "34",
        "author_info": {
            "given_block": "a gupta",
            "block": "a gupta",
            "position": 4,
            "first": "Alok",
            "middle": null,
            "last": "Gupta",
            "suffix": null,
            "affiliations": [
                "University of Minnesota"
            ],
            "email": null
        }
    },
"3059": {
        "author_id": 1225211537,
        "paper_id": 15718873,
        "signature_id": "3059",
        "author_info": {
            "given_block": "j collins",
            "block": "j collins",
            "position": 1,
            "first": "John",
            "middle": null,
            "last": "Collins",
            "suffix": null,
            "affiliations": [
                "University of Minnesota"
            ],
            "email": null
        }
    }
```