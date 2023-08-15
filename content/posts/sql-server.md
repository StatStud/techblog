---
title: "Sql Server"
date: 2023-08-14T18:55:17-07:00
draft: false
tags: ['sql']
ShowToc: true
cover:
    image: placeholder.png
    alt: ""
    caption: ""
ShowCodeCopyButtons: true
---

Please note: many of these tricks are done from the perspective of a mac user.

# Locating the my.cnf file

Please note: the default location where mysql config files are stored for mac users under

```sh
/usr/local/etc/mysql
```

Instead of 

```sh
/etc/mysql
```

This is where you can change the bind-address = 127.0.0.1 to bind-address = 0.0.0.0, to allow all access, including from a remote server (important if you're working from a remote server).

# Accessing mysql from the cli

```sh
mysql -u root -p
```

# Restarting the sql server

This is helpful especially after you've made some changes to the users and/or configuration.

```sh
brew services restart mysql
```