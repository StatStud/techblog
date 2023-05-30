---
title: "Instagram Scrape"
date: 2023-03-26T15:52:40-04:00
draft: false
tags: ['social-media','web-scraping','no-code']
ShowToc: true
cover:
    image: insta2.png
    alt: "Instagram"
    caption: ""
ShowCodeCopyButtons: true
---
# Introduction

Today we will be extracting a list of followers from social media.

While we could do this with web scraping, sometimes it's simply easier to do by using tools specifically made for this. After all, web scraping is all about the output, and less on *how* you scrape.

![](/insta1.gif)

# Extracting Followers 

![](/insta3.png)

For this demo, we will use [Donald Trump's account](https://www.instagram.com/realdonaldtrump/) to extract all of his followers into a spreadsheet. 

Specifically, we will be collecting the following data
- follower username
- follower name
- follower's page link

To accomplish this, we will use the [Bardeen Chrome Extension](https://chrome.google.com/webstore/detail/bardeen-automate-manual-w/ihhkmalpkhkoedlmcnilbbhhbhnicjga). This extension allows us to easily extract data specifically from instagram, and save the results automatically into a google sheet--all without any coding!

## Using Bardeen 

![](/insta4.png)
![](/insta7.png)

Once we have the extension installed, and selected the save instragram followers option, we may proceed with the scraping.

Make sure to have the "followers" tab open, on your browser. This will help Bardeen to extract the information that's already presented, and continue scrolling down the list.

Note: This process also works for "following" tab.

![](/insta6.png)

And that's in! It's as simple as that! When the extension is finished running, you may view the spreadsheet from your google sheets, as well as all of the attributes we outlined before.

# More Info

I found out about Bardeen when I tried creating a python Selenium script to do this same process, but Instragram prevents web drivers from access, which made the process much trickier to solve.

Then I found [this video](https://www.youtube.com/watch?v=9kgvVes6Ixs&t=296s), gave it a try, and was impressed with how easy it was! 

This is not a paid sponsorship--I simply share what I find useful, practical, and free. 

It seems like Bardeen also has a bunch of other use cases beyond Instragram, like [this video](https://www.youtube.com/watch?v=9kgvVes6Ixs&t=296s) shows.

Who knows, maybe Bardeen is simply one of many tools we have in our toolbox to collect data.

