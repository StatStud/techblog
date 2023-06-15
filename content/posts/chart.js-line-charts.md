---
title: "Chart.js Line Charts"
date: 2023-06-15T19:02:54-04:00
draft: false
tags: ['js','webdev']
ShowToc: true
cover:
    image: chart.js-line-plot.png
    alt: ""
    caption: ""
---

In this post, we will discuss using Chart.js for line plotting.

Examples from this post can be found in [this repo](https://github.com/StatStud/chart.js-line-plots).

# Reading data from a CSV file

Here the full function we use to read in the data:

```js
function parseCSV(csv) {
  const lines = csv.split("\n");
  const headers = lines[0].split(",");
  const data = {
    y_value: [],
    ym_value: []
  };

  for (let i = 1; i < lines.length; i++) {
    const currentLine = lines[i].split(",");
    data.y_value.push(parseFloat(currentLine[10])); //THIS IS WHERE we choose which column to display
    data.ym_value.push(parseFloat(currentLine[11]));
  }

  return data;
}
```

Let's dissect this a bit. We'll start with the first two lines:

```js
const lines = csv.split("\n");
const headers = lines[0].split(",");
```

As you might imagine, our csv files contains rows and columns; each record is separated by a new line in our file, while each element of the record is separated by a comma (comma-separated-values, or csv). Hence in the above context, we are simply defining the lines and headers for later use.

```js
  const data = {
    y_value: [],
    ym_value: []
  };
```

In this part, we are simply defining the structure of our data used for plotting. Since we are plotting two line values, we will store them as a dictionary of lists, where the first list we call "y_value" and the second "ym_value".

```js
  for (let i = 1; i < lines.length; i++) {
    const currentLine = lines[i].split(",");
    data.y_value.push(parseFloat(currentLine[10])); //THIS IS WHERE we choose which column to display
    data.ym_value.push(parseFloat(currentLine[11]));
  }

  return data;
```

Finally, we iterate over the total number of records (lines) from the csv file and extract the values we need. We use "data.y_value" to access the first list item of the data dictionary, from which we include ".push()" to append the specific column we desire. In the above case, for y_value, we're using the 10th column and appending all those values into that list. This process is then repeated for ym_value, but with the 11th column. In the end, once the look in finished, we return the entire data dictionary for later use in our script.
