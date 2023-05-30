---
title: "Linux Commands: df"
date: 2023-05-10T02:47:58-04:00
draft: false
tags: ['tech-tips','linux']
ShowToc: true
cover:
    image: linux.png
    alt: ""
    caption: ""
ShowCodeCopyButtons: true
---

# Checking disk space

To check disk space on your machine or remote server, simply run:
```sh
df -h .
```

If you *include* the period, you make get an output that looks similar to this:
```sh
Filesystem     Size   Used  Avail Capacity iused     ifree %iused  Mounted on
/dev/disk3s5  228Gi  165Gi   44Gi    80% 2088008 457632960    0%   /System/Volumes/Data
```

If you do *not* include the period, your output may look something like this:

```sh
Filesystem       Size   Used  Avail Capacity iused      ifree %iused  Mounted on
/dev/disk3s1s1  228Gi   14Gi   44Gi    25%  501730  457632600    0%   /
devfs           208Ki  208Ki    0Bi   100%     718          0  100%   /dev
/dev/disk3s6    228Gi  4.0Gi   44Gi     9%       4  457632600    0%   /System/Volumes/VM
/dev/disk3s2    228Gi  138Mi   44Gi     1%     159  457632600    0%   /System/Volumes/Preboot
/dev/disk3s4    228Gi  656Ki   44Gi     1%      14  457632600    0%   /System/Volumes/Update
/dev/disk1s2    500Mi  6.0Mi  481Mi     2%       1    4928760    0%   /System/Volumes/xarts
/dev/disk1s1    500Mi  7.3Mi  481Mi     2%      21    4928760    0%   /System/Volumes/iSCPreboot
/dev/disk1s3    500Mi  588Ki  481Mi     1%      58    4928760    0%   /System/Volumes/Hardware
/dev/disk3s5    228Gi  165Gi   44Gi    80% 2088010  457632600    0%   /System/Volumes/Data
map auto_home     0Bi    0Bi    0Bi   100%       0          0  100%   /System/Volumes/Data/home
/dev/disk4s2     20Mi   15Mi  4.2Mi    79%     634 4294966645    0%   /Volumes/Disk Inventory X 1.3
/dev/disk5s1     29Mi  4.8Mi   24Mi    17%      66 4294967213    0%   /Volumes/Roblox
```

In both cases, the -h flag helps us see the storage in human-legible formats :)