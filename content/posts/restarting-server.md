---
title: "Restarting Server"
date: 2024-01-15T06:25:46-08:00
draft: false
tags: ['cloud']
ShowToc: true
cover:
    image: placeholder.png
    alt: ""
    caption: ""
ShowCodeCopyButtons: true
---

```sh
#!/bin/bash
cd ../main
ps -ef | grep 'python app.py' | grep -v grep | awk '{print \$2}' | xargs kill
git pull
rm nohup.out
nohup python app.py --save_session_data &
```

- the first line puts us into the main folder
- the second line kills any currently running python jobs (from out app)
- the third line pulls the repo for any updates
- the fourth line clears out the log file
- the last line runs the app.py python job in the background
Rinse and repeat whenever you make changes to the repo