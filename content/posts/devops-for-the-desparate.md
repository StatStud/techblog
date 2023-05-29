---
title: "Devops for the Desperate"
date: 2023-05-27T11:10:41-04:00
draft: false
tags: ['books']
ShowToc: true
cover:
    image: devops-for-the-desperate.png
    alt: ""
    caption: ""
---


# PART I: INFRASTRUCTURE AS CODE, CONFIGURATION MANAGEMENT, SECURITY, AND ADMINISTRATION
# Chapter 1: Setting Up a Virtual Machine

Infrastructure as Code (IaC) and Configuration Management (CM).

IaC is the process of using code to describe and manage infrastructure (VMs, network switches, and cloud resources like AWS). The benefit of IaC is the ease of deployment because applications are built and tested the same way in every delivery pipeline. The drawbacks of IaC is that provisioning can take some time and organization, which may not be needed if you're doing simple code tests on your local machine; it's a tradeoff between deployment and creating scrappy MVPs

CM is the process of configuring those resources for a specific purpose in a predictable and repeatable manner.

Vagrant and Ansible are two examples of IaC and CM, respectively. Please note that Vagrant itself is not a VM, but rather a framework for managing VMs--there's a difference.

## Modifications to this chapter

Because I'm using an Apple Silicon computer as my host machine, VirtualBox is not an option. Apple Silicon’s CPU is based off the ARM architecture, and VirtualBox only works on x86. :(

    

# Chapter 2: Using Ansible to Manage Passwords, Users, and Groups
# Chapter 3: Using Ansible to Configure SSH
# Chapter 4: Controlling User Commands with sudo
# Chapter 5: Automating and Testing a Host-Based Firewall
# PART II: CONTAINERIZATION AND DEPLOYING MODERN APPLICATIONS
# Chapter 6: Containerizing an Application with Docker
# Chapter 7: Orchestrating with Kubernetes
# Chapter 8: Deploying Code
# PART III: OBSERVABILITY AND TROUBLESHOOTING
# Chapter 9: Observability
# Chapter 10: Troubleshooting Hosts