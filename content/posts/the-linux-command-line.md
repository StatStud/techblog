---
title: "The Linux Command Line"
date: 2023-05-25T17:54:12-04:00
draft: false
tags: []
ShowToc: true
cover:
    image: the-linux-command-line.png
    alt: ""
    caption: ""
---

# Table of Contents
## Part 1: Learning the Shell
### Chapter 1: What is the shell?
### Chapter 2: Navigation
### Chapter 3: Exploring the system
### Chapter 4: Manipulating Files and Directories
### Chapter 5: Working with Commands
### Chapter 6: Redirection

Chapter 6 was spicy. The chapter starts with the idea of I/O, or input/output redirection.

I learned the true and tried phrase of linux: "everything is a file".

In the context of linux, all inputs and outputs to the command line are files themselves.

For example, when you type commands, you're actually sending your inputs to a file called *standard input* (stdin)--stdin is, by default, attached to the keyboard.

On the other end, all output you see from the terminal screen is actually sent to a file called *standard output* (stdout).

What about status messages and errors? Yup, you guessed it: *standard error* (stderr).

I found this really cool, because these are actual files on your computer that you can look at, rather than some weird "black-box" magic that comes somewhere from the computer.

To redirect stdout to another file (let's say in the case you're running a machine learning model, and wish to save the output to a text file), you can type something like:

```sh
python model.py > results.txt
```

But let's say you already have a file on hand, and wish to *append* the results? Just use a double arrow:

```sh
python model.py > results.txt
```

To output both stdout and stderr, you can run:

```sh
python model.py > results.txt 2>&1 
```

Note that in the above example, I used "2"--this is a file descriptor, and linux has a reference for all three types of output: (0) standard input (1) standard output (2) standard error 

### Chapter 7: Seeing the world as the Shell sees it
### Chapter 8: Advance Keyboard Tricks
### Chapter 9: Permissions
### Chapter 10: Processes 
## Part 2: Configuration and the Environment
### Chapter 11: The environment
### Chapter 12: A gentle introduction to vi
### Chapter 13: Customizing the prompt
## Part 3: Common Tasks and Essential Tools
### Chapter 14: Package management
### Chapter 15: Storage Media
### Chapter 16: Networking
### Chapter 17: Searching for Files
### Chapter 18: Archiving and Backup
### Chapter 19: Regular Expressions
### Chapter 20: Text Processing
### Chapter 21: Formatting Output
### Chapter 22: Printing
### Chapter 23: Compiling Programs
## Part 4: Writing Shell Scripts
### Chapter 24: Writing your first script
### Chapter 25: Starting a project
### Chapter 26: Top-Down Design
### Chapter 27: Flow Control: Branching with IF
### Chapter 28: Reading keyboard inputs
### Chapter 29: Flow Control: Looping with while/until
### Chapter 30: Troubleshooting
### Chapter 31: Flow Control: Branching with case
### Chapter 32: Positional Parameters
### Chapter 33: Flow Control: Looping with For
### Chapter 34: Strings and Numbers
### Chapter 35: Arrays
### Chapter 36: Exotica



