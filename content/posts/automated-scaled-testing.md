---
title: "Automated Testing at Scale"
date: 2023-10-23T09:44:50-07:00
draft: false
tags: ['automated-testing']
ShowToc: true
cover:
    image: placeholder.png
    alt: ""
    caption: ""
ShowCodeCopyButtons: true
---


Today we will discuss how to run automated testing for a chatbot.

The elements of automated testing include:
1. **job status logging**: Keeping track on the testing progression
2. **caching**: storing looped indexes to avoid repeated testing
3. **Chat artifacts themselves**: Since this is for a chatbot, we will be storing all the chat logs for future analysis.
    - Each artifact should have a timestamp to verify with logging progression, as well as unique user ID to re-evaluate origin of simulation
    - Keep track of the number of API calls
