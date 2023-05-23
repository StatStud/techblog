---
title: "Managing Remote Repositories"
date: 2023-05-23T11:41:57-07:00
draft: false
tags: []
ShowToc: true
cover:
    image: placeholder.png
    alt: ""
    caption: ""
---

# Introduction

Did you know: You can manage your project by pushing it to different repos.

# Pushing to GitHub

What do I mean by this?

Say on our desktop, you have a project called "Hello.py". Let's say it's a basic python script that prints hello world.

```python
print("hello world")
```

Your options for uploading and saving this code is traditionally through github. So, when you're ready to upload your code, you may type:

```sh
git push origin main
```

or simply 

```sh
git push
```

if you've already configured your remote remote

# Pushing to GitLab, Bitbucket, Stash, or whatever the cool kids are using these days

What if you're team prefers to use gitlab instead, just because they're that cool. What do you do then?

simply *add* a new remote name with a remote url.

For example, say you want to push your code to stash, you'll type the following

```sh
git remote add stash <stash_remote_url>
```

Where <stash_remote_url> is simply the url of where, within stash, your code will reside.

Once that new remote name is added, pushing your code to Stash (instead of Github) is as simple as:

```sh
git push stash <branch_name>
```

Likewise, it does not matter what other repo hosting your teams use, this process will look the same when adding other remote repos.

For example, switching to gitlab would look like:

```sh
git remote add gitlab <gitlab_remote_url>
git push gitlab <branch_name>
```

Note: you only need to add "git remote add" once, when initializing a new remote name (rather than every time you wish to push something to a repo)

# Good Reads and References
- [GitGub Guide](https://docs.github.com/en/get-started/getting-started-with-git/managing-remote-repositories) (Note: this is a **GREAT** short and concise resource)