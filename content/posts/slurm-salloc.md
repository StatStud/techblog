---
title: "Slurm Salloc"
date: 2023-04-19T10:24:28-04:00
draft: false
tags: ['SLURM','High-Performance-Computing']
ShowToc: true
cover:
    image: slurm.png
    alt: "Cover"
    caption: ""
ShowCodeCopyButtons: true
---

# Introduction

High-Performance Computing (HPC) is an essential tool for modern scientific research, allowing scientists and researchers to perform complex calculations and simulations at an unprecedented scale.

One of the most popular HPC job scheduling systems is **SLURM**, which stands for **S**imple **L**inux **U**tility for **R**esource **M**anagement.

In this blog post, we will focus on the salloc command, one of the most commonly used SLURM commands for requesting compute resources.

# The Salloc command

The salloc command allows users to request compute resources for *interactive* jobs. 

This command reserves resources on the HPC cluster for a certain amount of time and assigns them exclusively to the user. This can be useful for debugging or testing code, or for running jobs that require user interaction or visualizations.

Here's an example of how to use the salloc command:

```sh
salloc -N1 -p dlv -A project_a -t 120
```
Let's break down each of these options in more detail:
- **N1**: This option specifies the number of nodes requested for the job. In this case, we are requesting only one node.
- **-p dlv**: This option specifies the partition on which the job will run. Here, we are using the partition named "dlv", which corresponds to a specific computing resource such as "2xV100 GPUs"
- **-A project_a**: This option specifies the account or project to which the job belongs. 
- **-t 120**: This option specifies the duration of the job in minutes. In this example, we are requesting resources for 120 minutes.

Once we run the salloc command, we will see an output similar to the following:

# The srun command

Another command similar to salloc is srun:

```sh
srun -N 1 -p partition_name -t 02:00:00 --pty bash
```

- **srun**: This is the command used to submit parallel jobs for execution.

- **N 1**: This option specifies the number of nodes to be allocated for the job. In this case, it's requesting 1 node.

- **p**: The "-p" option is used to specify the partition or queue to which the job should be submitted. In this case, the partition is specified as "partition_name."

- **t**: The "-t" option specifies the maximum time (in HH:MM:SS format) the job is allowed to run. In this case, it's set to 2 hours.

- **pty bash**: This part of the command requests a pseudo-terminal (pty) and launches the "bash" shell. The "--pty" option is used to indicate that the job requires a pseudo-terminal for interactive use, and "bash" is the shell that will be started.



# Accessing Resources

```sh
salloc: Granted job allocation 123456
salloc: Waiting for resource configuration
salloc: Nodes cn001 are ready for job
```

Here's what this means:
- The first line indicates that the job allocation has been granted, and it provides a job ID (in this case, 123456)
- The second line indicates that the system is waiting for the resource configuration to be set up. 
- The third line indicates that the requested node (in this case, cn001) is ready for the job.

At this point, we can log into the allocated node using the ssh command and run our interactive job. Once we are finished, we can exit the node and the resources will be released automatically.

# Monitoring Resources

Another helpful command is squeue, which allows users to view the status of their jobs, as well as the jobs of other users on the cluster. 

By default, squeue shows *all* running and pending jobs on the cluster. However, users can use various options to filter the results by user, job ID, partition, or other criteria.

To view the status of your own jobs, you can use the -u option followed by your username. For example:

```sh
squeue -u username
```
This results in an output that may look similar to the one below:

```sh
JOBID     PARTITION     NAME         USER        ST   TIME_LEFT  NODES
123456    gpu           job1         johndoe     R    02:30:00   1
123457    gpu           job2         johndoe     PD   00:05:00   2
123458    cpu           job3         johndoe     R    00:45:00   1
```