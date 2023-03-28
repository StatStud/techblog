---
title: "MedQA-USMLE"
date: 2023-03-27T18:09:23-04:00
draft: false
tags: ['datasets','healthcare']
ShowToc: true
cover:
    image: USMLElogo.png
    alt: "USMLE logo"
    caption: ""
---

# Introduction

This post will discuss the MedQA-USMLE dataset. For more details, check out the [original published paper](https://arxiv.org/pdf/2009.13081v1.pdf).

# What is USMLE?

The United States Medical Licensing Examination (USMLE) is simply a professional exam that all aspiring physicians must take in order to practice medicine in the United States.

The layout of the exam is involves 3 steps:
1. An 8-hour block consisting of 280 multiple-choice questions
2. (Day 1) A 9-hour block consisting of 316 multiple-choice questions (AKA, CK). (Day 2 and Day 3) A hands-on clinical skills assessment (AKA, CS)
3. (Day 1) A 7-hour block consisting of 233 multiple-choice questions (Day 2) A 7-hour block consisting of 180 multiple-choice questions and computer-based case simulations

For more info, check out the [official website](https://www.usmle.org/step-exams/step-1)

# What is MedQA-USMLE?
According to the paper, the MedQA dataset contains a total of 5,693 multiple-choice questions, which were collected from six different standardized medical exams, including the USMLE Step 1 and Step 2 exams. The questions cover a wide range of medical topics, including anatomy, physiology, pharmacology, and pathology.

It's worth noting that the MedQA dataset is just one of several medical QA datasets that have been developed in recent years and can be used to train and evaluate AI systems for medical QA tasks.

## Obtaining the MedQA-USMLE dataset

The paper includes an [official repo](https://github.com/jind11/MedQA) containing both the data and the experiment code. The data specifically lives in a [google drive folder](https://drive.google.com/file/d/1ImYUSLk9JbgHXOemfvyiDiirluZHPeQw/view?usp=sharing); this folder includes both the MedQA-USMLE dataset and the textbook data.

## How Many Questions does MedQA-USMLE have?

Upon downloading the zip file, we will see three .jonl files.
1. train.jonl, (10,180 questions)
2. test.jonl, (1,275 questions)
3. dev.jonl, (1,275 questions)
4. US_qbank.jonl (14,370 questions)

The "US_qbank.jsonl" files contain **all** data samples; all other files (train,test,dev) are the official random splits used in the experiments from the paper; users are free to have develop their own splitting variations

## What does a record from MedQA-USMLE look like?

Below is an example record from one of the files.

```json
{"question": "A 5-year-old girl is brought to the emergency department by her mother because of multiple episodes of nausea and vomiting that last about 2 hours. During this period, she has had 6–8 episodes of bilious vomiting and abdominal pain. The vomiting was preceded by fatigue. The girl feels well between these episodes. She has missed several days of school and has been hospitalized 2 times during the past 6 months for dehydration due to similar episodes of vomiting and nausea. The patient has lived with her mother since her parents divorced 8 months ago. Her immunizations are up-to-date. She is at the 60th percentile for height and 30th percentile for weight. She appears emaciated. Her temperature is 36.8°C (98.8°F), pulse is 99/min, and blood pressure is 82/52 mm Hg. Examination shows dry mucous membranes. The lungs are clear to auscultation. Abdominal examination shows a soft abdomen with mild diffuse tenderness with no guarding or rebound. The remainder of the physical examination shows no abnormalities. Which of the following is the most likely diagnosis?", 
"answer": "Cyclic vomiting syndrome", 
"options": {"A": "Cyclic vomiting syndrome", "B": "Gastroenteritis", "C": "Hypertrophic pyloric stenosis", "D": "Gastroesophageal reflux disease", "E": "Acute intermittent porphyria"}, 
"meta_info": "step2&3", 
"answer_idx": "A"}
```

## What else do we get from the download?

![](/medqa.png)

The folder is divided into two sections:
1. questions
2. textbooks

Questions are furthe divided into 3 langauges (English, Simplified Chinese, and Traditional Chinese). Within those folders, the file strucutre is the same.

Textbooks provides a corpus of relevant medical documents; these can be used to train any langauge model.


# Other datasets
For NLP operations, HuggingFace has [a dataset module](https://huggingface.co/datasets/medmcqa) that's ready to load with any transformer model.



