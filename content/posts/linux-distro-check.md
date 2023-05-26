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

# Method 2

```sh
cat /etc/*-release
```

This will output something that looks like this:

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