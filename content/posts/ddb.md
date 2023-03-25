---
title: "DDB (Diseases Database)"
date: 2023-03-25T03:29:20-04:00
draft: false
tags: ['datasets','healthcare','webscraping']
ShowToc: true
---

# Introduction

One of the hardest parts of any data science project is gathering good data. Fortunately, many online data repositories exist for us to use!

The Diseases Database (DDB) is one such source. The Diseases Database, developed and maintained by Medical Object Oriented Software Enterprises LTD, is a cross-referenced index of human disease, medications, symptoms, signs, and abnormal investigation findings, intended for medical practitioners and students. Rather than in hierarchies of anatomical, physiological, or pathological systems, it serves as a way of classifying medical concepts along clinical axes, such as cause/effect, risk factors, interactions, etc. The content focuses on internal medicine, inherited disease, clinical biochemistry, and pharmacology, and is updated regularly, although its last update in the Metathesaurus was in 2001. For more information, consider checking out [the official site](http://www.diseasesdatabase.com/) of the data. Additionally, the Diseases Database is one of the sources of medical knowledge that contributes to the [UMLS](https://www.nlm.nih.gov/research/umls/sourcereleasedocs/current/DDB/index.html), which helps to provide a comprehensive and interoperable knowledge resource for the healthcare domain.

# Getting the Data

Unfortunately, DDB does not provide free download of the raw data nor an open API to interact with the data. It even says so on its website.

![](img1)

But that won't stop us in the name of data science! Web scraping allows us to interact with web pages to extact messy, textual data into clean, organized spreadsheets for our models!

Python has plenty of web scraping libraries to choose from; I personally enjoy working with [Selenium](https://selenium-python.readthedocs.io) because it's less prone to parsing issues common with Requests package. Additionally, you can interact with it on a live window, and it's pretty cool to watch!

## Web Scraping 101

If you have no idea how to create a custom web scraping file, don't worry! You only really need access to two peices of information:

1. Access to the web source code ("inspect" element on most web browsers)
2. Access to ChatGPT 

It's important to have an idea of how the site appears from a coding standpoint, because this will help guide your prompts for ChatGPT to help.


