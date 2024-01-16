---
title: "Linux Distro Check"
date: 2023-05-26T12:41:49-07:00
draft: false
tags: ['linux']
ShowToc: true
cover:
    image: linux.png
    alt: ""
    caption: ""
ShowCodeCopyButtons: true
---

# TL;DR

There are 2 practical methods to check which linux distro your machine or remote server is using:

# Method 1

```sh
uname -a
```

This will produce something that looks like,

```sh
Darwin abc123 22.4.0 Darwin Kernel Version 22.4.0: Mon Mar  6 21:00:17 PST 2023; root:xnu-8796.101.5~3/RELEASE_X86_64 x86_64
```

The information suggests that we are using the Darwin operating system with a kernel version of 22.4.0. Darwin is the core operating system that serves as the foundation for macOS and iOS. It is based on the BSD Unix operating system. 

In other words, it's highly *likely* that we are running macOS on our system.

## Side Note

In addition to checking the distribution, you can also run the following to get the type of archeceture:

```sh
uname -m
```

This will output something like:

```sh
x86_64
```

Knowing this will be helpful when downloading certain software.

# Method 2

```sh
cat /etc/*-release
```

Here, we use the asterisk wildcard (*) to search for any file with the suffix "-release".
We're actually looking for a file named "os-release", but this may not have the same name across all devices.
Regardless, when such a file is found, the output will look something like this:


```sh
CentOS Linux release 7.8.2003 (Core)
DGX_NAME="DGX Server"
DGX_PRETTY_NAME="NVIDIA DGX Server"
DGX_OTA_VERSION="22.02-1"
DGX_OTA_DATE="Wed Apr  6 15:17:02 PDT 2022"
DGX_PLATFORM="DGX Server for H12DGO-6"
DGX_SERIAL_NUMBER=C438G0K05B10182
DGX_EL_SUPPORTED="7"
NAME="CentOS Linux"
VERSION="7 (Core)"
ID="centos"
ID_LIKE="rhel fedora"
VERSION_ID="7"
PRETTY_NAME="CentOS Linux 7 (Core)"
ANSI_COLOR="0;31"
CPE_NAME="cpe:/o:centos:centos:7"
HOME_URL="https://www.centos.org/"
BUG_REPORT_URL="https://bugs.centos.org/"

CENTOS_MANTISBT_PROJECT="CentOS-7"
CENTOS_MANTISBT_PROJECT_VERSION="7"
REDHAT_SUPPORT_PRODUCT="centos"
REDHAT_SUPPORT_PRODUCT_VERSION="7"

CentOS Linux release 7.8.2003 (Core)
CentOS Linux release 7.8.2003 (Core)
```

From this example, it is more clear to see that we are using CentOS (release 7.8.2003).

# Bonus: Hardware check.

To view the hardware specs of your device run "lscpu". To specifically get the number of cpu-cores of your machine, run "nproc".

lscpu will output something that looks like this:
```sh
Architecture:          x86_64
CPU op-mode(s):        32-bit, 64-bit
Byte Order:            Little Endian
CPU(s):                48
On-line CPU(s) list:   0-47
Thread(s) per core:    1
Core(s) per socket:    24
Socket(s):             2
NUMA node(s):          8
Vendor ID:             AuthenticAMD
CPU family:            25
Model:                 1
Model name:            AMD EPYC 7413 24-Core Processor
Stepping:              1
CPU MHz:               2650.000
CPU max MHz:           2650.0000
CPU min MHz:           1500.0000
BogoMIPS:              5290.52
Virtualization:        AMD-V
L1d cache:             32K
L1i cache:             32K
L2 cache:              512K
L3 cache:              32768K
NUMA node0 CPU(s):     0-5
NUMA node1 CPU(s):     6-11
NUMA node2 CPU(s):     12-17
NUMA node3 CPU(s):     18-23
NUMA node4 CPU(s):     24-29
NUMA node5 CPU(s):     30-35
NUMA node6 CPU(s):     36-41
NUMA node7 CPU(s):     42-47
```

This specific device has 48 cpu cores.

To get GPU count, run "lspci | grep -i nvidia" (this searches for nvidea specific GPUs). The output will look like this:

```sh
07:00.0 3D controller: NVIDIA Corporation Device 20b2 (rev a1)
0a:00.0 3D controller: NVIDIA Corporation Device 20b2 (rev a1)
45:00.0 3D controller: NVIDIA Corporation Device 20b2 (rev a1)
4b:00.0 3D controller: NVIDIA Corporation Device 20b2 (rev a1)
83:00.0 3D controller: NVIDIA Corporation Device 20b2 (rev a1)
89:00.0 3D controller: NVIDIA Corporation Device 20b2 (rev a1)
bf:00.0 3D controller: NVIDIA Corporation Device 20b2 (rev a1)
c2:00.0 3D controller: NVIDIA Corporation Device 20b2 (rev a1)
d1:00.0 Bridge: NVIDIA Corporation Device 1af1 (rev a1)
d2:00.0 Bridge: NVIDIA Corporation Device 1af1 (rev a1)
d3:00.0 Bridge: NVIDIA Corporation Device 1af1 (rev a1)
d4:00.0 Bridge: NVIDIA Corporation Device 1af1 (rev a1)
d5:00.0 Bridge: NVIDIA Corporation Device 1af1 (rev a1)
d6:00.0 Bridge: NVIDIA Corporation Device 1af1 (rev a1)
```

This specific machine has 8 GPUs available (3D controller).