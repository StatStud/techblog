---
title: "Port Forwarding for Jupyter Notebook"
date: 2023-03-28T11:08:20-04:00
draft: false
tags: ['tech-tips']
ShowToc: true
cover:
    image: port_forward.png
    alt: "Port Forwarding"
    caption: ""
ShowCodeCopyButtons: true
---

# Port forwarding onto a single remote server

1. ssh into remote server
2. run "jupyter notebook --no-browser --port=**port-forwarding**
    - note: the **port-forwarding**  can take on almost any value; 8888 is the commonly used port for jupyter port forwarding
3. open a new shell
4. run "ssh -L **local-port**:localhost:**port-forwarding** username@remove-server"
    - note: **local-port** can take on any value and is the port we use to access localhost jupyter notebook instance. Often, many people use 8000 for jupyter notebook
    - note: **port-forwarding** must match the value we specified in step 2
5. That's it! Open your browser and type localhost:**local-port**

# Port forwarding into a remote server, within another remote server

## Why might we do this?

In HPC settings, we may need to access a first remote server that gives us access to compute clusters; we may then ssh into a given cluster, thus creating another remote server from which we need to run jupyter notebook. 

## How do we do this?

Fortunately, the steps are quite similar to the case with a single remote server:

1. ssh into remote server
2. run "jupyter notebook --no-browser --port=**port-forwarding**
3. open a new shell
4. run "ssh -L **local-port**:localhost:**port-forwarding** username@remove-server-1"
    - note: pay attention that we are ssh-ing into the outer remote server here (remove-server-1)
5. Within that same second shell, run "ssh -L **port-forwarding**:localhost:**port-forwarding** username@remove-server-2"
    - note: pay attention that we are ssh-ing into the inner remote server here (remove-server-2)
    - also note that we use **port-forwarding** twice, instead of once
6. That's it! Open your browser and type localhost:**local-port**
