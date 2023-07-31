---
title: "Aws Ec2 Port Forwarding"
date: 2023-07-31T12:38:08-07:00
draft: false
tags: ['cloud-computing','aws']
ShowToc: true
cover:
    image: placeholder.png
    alt: ""
    caption: ""
ShowCodeCopyButtons: true
---

Steps
	1. Pip install jupyter notebook (or make sure you have the right environment activated)
	2. Open a new terminal window, cd where you have your .pem key
	3. Then, on that new window, enter command:
		a. ssh -i ~/folder/folder/folder/aws/certs/pnnl_alejandro_michel.pem -L 8000:localhost:8888 ec2-user@url
	4. Go on browser and enter "localhost:8000"
	5. Done
		a. Side notes:
			i. Additional login steps may be required, but they're easy lifts
			ii. ssh -i ~/folder/folder/folder/aws/certs/pnnl_alejandro_michel.pem ec2-user@url
			iii. cd unknown_classifier
			iv. source env/bin/activate
jupyter notebook --no-browser --port=8888
