---
title: "Argparse"
date: 2024-01-16T10:16:48-08:00
draft: false
tags: []
ShowToc: true
cover:
    image: placeholder.png
    alt: ""
    caption: ""
ShowCodeCopyButtons: true
---

```python
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    
    parser.add_argument("--gen_template", action='store_true',
                        help="Generate template file for adding a new user.")
    parser.add_argument("--init_user", default=77,
                        help="Initialize user-specific files and data directories.")
    parser.add_argument("--user_json", type=str, required=False,
                        help="Path to JSON file completed from template (required with --init_user).")

    args = parser.parse_args()

    main(args)
```
