---
title: "Hugo Static Site Generator"
date: 2023-08-11T13:52:18-04:00
draft: false
tags: ['webdev']
ShowToc: true
cover:
    image: hugo.png
    alt: ""
    caption: ""
ShowCodeCopyButtons: true
---

# TL;DR

This is where I pull put down what I learn as I become better at Hugo Static Site Generator

# Archetypes Folder

This is where you will create the template writing structure for your posts (e.g. the type of front matter for default values, the headings of each posts, etc).

To create a new templates, all you have to do is create a markdown file, and then save it--that's it!

So, if we create a test.md, that contains pre-defined front matter and headings, we can reference that template when we create a new blog post by using the "-k" argument (not using the -k argument will revert to whatever "default.md" is saved as).

```sh
hugo -k test new posts/deleteme.md
```
