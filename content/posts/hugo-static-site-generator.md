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

# Zero to Hero: Create a fully-functional site in 12 steps

## Step 0
Brew install hugo if you have not already done so

## Step 1
Create a new project with the following command:

```sh
hugo new site <project_name> -f yml
```

## Step 2

From the top-level project folder, git-clone the theme you desire
    - in my case, I'm using Papermod (“https://github.com/adityatelange/hugo-PaperMod/wiki/Installation”)
    - Whatever theme you choose, make sure you read the install instructions first

## Step 3
Copy the main config yml file from your previous project. Here is the basic layout that works for me:

```yaml
baseURL: ""
languageCode: en-us
title: Your-title-goes-here
theme: Your-theme-goes-here

outputs:
    home:
        - HTML
        - RSS
        - JSON 

params:
   ShowShareButtons: true
   ShowPostNavLinks: true
   fuseOpts:
        isCaseSensitive: false
        shouldSort: true
        location: 0
        distance: 1000
        threshold: 0.4
        minMatchCharLength: 0
        keys: ["title", "permalink", "summary", "content"]

menu:
        main:
                - identifier: posts
                  name: Posts
                  url: /posts/
                  weight: 10
                - identifier: archives
                  name: Archive
                  url: /archives/
                  weight: 20
                - identifier: search
                  name: Search
                  url: /search/
                  weight: 30
                - identifier: tags
                  name: Tags
                  url: /tags/
                  weight: 40

```
## Step 4

Now, within the "archetypes" folder, update the default post generator ("default.md") with whatever front matter and headings you desire. Here is an example:

```md
---
title: "{{ replace .Name "-" " " | title }}"
date: {{ .Date }}
draft: false
tags: ['life-update', 'practical-tips', 'what-i-learned','putting-it-to-the-test', 'observations-thoughts-opinions']
ShowToc: true
cover:
    image: placeholder.png
    alt: ""
    caption: ""
---

# TL;DR

# Whom am I speaking to? Who is this going to help?

# My Practical Experience

# My Mind Dump. 

# How does this opinion explain how the world really works in a way that accurate, wholistic, and realistic? 

# Given your thoughts and opinions, what practical actions can we take?

# Thanks for the advice, now how can I practically put this to use in a simple way for daily execution?

```

## Step 6
Within the "content" folder, create a subfolder called "posts". This is where all your md posts go.

Also within "content" folder, create the "archives.md" and "search.md" files, IF you are using hugo PaperMod theme.

Here is what archives.md looks like:

```md
---
title: Archive
layout: archives
url: /archives/
summary: archives
---
```

And here is what search.md looks like:

```md
title: "Search" # in any language you want
layout: "search" # is necessary
# url: "/archive"
# description: "Description for Search"
summary: "search"
placeholder: "search"
---
```

## Step 7

Add a top, introduction page by adding the "weight" field to one of the posts you create, like this:

```md
---
title: "About P&S"
date: 2023-04-23T15:10:31-04:00
draft: false
tags: []
ShowToc: true
TocOpen: true
cover:
    image: about1.png
    alt: ""
    caption: ""
weight: 999
---
```

## Step 8

Initialize git repo by running the following command from the top-level of the project folder:

```sh
git init
```

Followed by:

```sh
touch .gitmodules
```

within that .gitmodules file, type and save the following:

```txt
[submodule "themes/PaperMod"]
    path = themes/PaperMod
    url = "https://github.com/adityatelange/hugo-PaperMod.git"
```





# Misc

## Additional resources
- https://www.youtube.com/watch?v=hjD9jTi_DQ4

## Archetypes Folder

This is where you will create the template writing structure for your posts (e.g. the type of front matter for default values, the headings of each posts, etc).

To create a new templates, all you have to do is create a markdown file, and then save it--that's it!

So, if we create a test.md, that contains pre-defined front matter and headings, we can reference that template when we create a new blog post by using the "-k" argument (not using the -k argument will revert to whatever "default.md" is saved as).

```sh
hugo -k test new posts/deleteme.md
```
