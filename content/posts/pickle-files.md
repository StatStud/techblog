---
title: "Pickle Files"
date: 2023-09-20T13:55:47-07:00
draft: false
tags: []
ShowToc: true
cover:
    image: placeholder.png
    alt: ""
    caption: ""
ShowCodeCopyButtons: true
---

import pickle

# Open the file in binary write mode and save the object
```py
with open("pickle_filename.pickle", 'wb') as file:
    pickle.dump(my_list, file)
```

```py
with open("pickle_filename.pickle", 'rb') as file:
    loaded_object = pickle.load(file)
```

