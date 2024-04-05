---
title: "Php Sql Web"
date: 2023-09-16T20:10:09-04:00
draft: false
tags: ['php','webdev']
ShowToc: true
cover:
    image: placeholder.png
    alt: ""
    caption: ""
ShowCodeCopyButtons: true
---

Today I learned the following:
1. Create a database on hostgator via PHPMyAdmin
2. Create demo data for SQL table
3. Create PHP code to connect to database
4. Create HTML file to take user input and retrieve data from database
5. Create a subdomain for a single host plan
6. Add a git repo to that subdomain
7. ssh into my host plan, and use git to push updates
8. Writing SQL-Injection Resistant PHP Code
9. Using a non 'index.html' file as the default web page
10. Run python using PHP

# Setting up PHP for basic database query
The PHP code is quite simple:
```php
<?php
// Database connection parameters
$servername = "localhost";
$username = "user_name";
$password = "password";
$dbname = "database";

// Create a connection to the database
$conn = new mysqli($servername, $username, $password, $dbname);

// Check the connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Get the minimum and maximum prices from the form
$minPrice = $_POST["minPrice"];
$maxPrice = $_POST["maxPrice"];

// Construct the SQL query
$sql = "SELECT * FROM menu_items WHERE price BETWEEN $minPrice AND $maxPrice";

// Execute the query
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    // Output the data from the query
    while ($row = $result->fetch_assoc()) {
        echo "Product Name: " . $row["item_name"] . " - Price: $" . $row["price"] . "<br>";
    }
} else {
    echo "No products found within the specified price range.";
}

// Close the database connection
$conn->close();
?>
```

And here is the html code I used to run the code:
```html
<!DOCTYPE html>
<html>
<head>
    <title>Price Range Search</title>
</head>
<body>
    <h1>Search Products by Price Range</h1>
    <form method="post" action="test.php">
        <label for="minPrice">Minimum Price:</label>
        <input type="number" name="minPrice" id="minPrice" required>
        <br>
        <label for="maxPrice">Maximum Price:</label>
        <input type="number" name="maxPrice" id="maxPrice" required>
        <br>
        <input type="submit" value="Search">
    </form>
</body>
</html>
```

Putting these two together, the result was super easy!

The user can input a range of values for the price, and get the correct food items that match his or her budget.

I now have confidence to build a web app that can query from a database.

# Creating a subdomain for a single host plan

Why do we want to create a subdomain for a single host plan? 

Three reasons:
1. costs
2. organization
3. git

Cost-wise, rather than paying for x-number of hosting plans for x-number of different web-dev ideas, you can instead host (theoretically) an unlimited number of subdomains all using the same host plan. I say theoretically because there's of course a disk and memory limit to your hosting plan, but nevertheless the ideas are limitless!

Organization-wise, creating a subdomain on hostgator gives you a dedicated folder within your existing folder structure for your new site; you would not want to mix one website content (html, css, and php files, plus static elements) with a another, so having the separation really helps.

Finally, from a git-repo standpoint, having a dedicated folder for your subdomain makes it easier to git push and save your changes for one specific web idea. Each subdomian can have its own dedicated git-repo.

# Creating a database on hostgator via PHPMyAdmin

To create a new database (which will contain new data tables), checkout [this video](https://www.youtube.com/watch?v=4bnmnUsb7IU&t=240s).

To create the database tables for a specific database, you can import from an existing database or manually create demo data. You can also ingest from a csv. The options are yours

# Adding a git repo to a subdomain

Hostgator has recently changed their approach to this and now it's much easier than before!

1. Launch CPanel
2. Under "Files" section, click on "Git Version Control"
3. Click "Create"
4. Under "Clone URL", paste the github url to the repo
5. Click on "Create"

And that's it!

Alternatively, and this is my preference, you can "git clone" from the command line by ssh-ing into your website.

NOTE: You get to do a "git pull" anytime you update your repo, otherwise your website will not render the changes.

Double NOTE: Once you push your changes to the repo **AND** do a git pull on the remote server, you should see the changes **INSTANTLY** on the website. Otherwise, you probably forgot to do a git pull from the server side :) (or there's a bug in your code).

Triple NOTE: Github updated their security on pushing updates that does not permit password authentication; you instead use a personal access token to authenticate (if using https). See [this video](https://www.youtube.com/watch?v=kHkQnuYzwoo) on where to get tokens (hint: it's under developer settings in github).


Quadruple NOTE: For automatic git pulls (meaning, you push a change to the repo, and you want your server to automatically git pull that change in), use two things (1) webhooks (2) php script like the one below:

```php
<?php shell_exec('git pull'); ?>
```

Update the webhook to point to the endpoint that has this php script (so it would look something like "http://www.website.com/pull.php").

For more details, see [this blog post](https://medium.com/@tecfare/how-to-automate-your-pull-from-git-repo-to-cpanel-web-hosting-7c45ab1a8cc2).

# SSH-ing into website

```sh
ssh host_gator_username@website.com
```

**NOTE:** This is assuming you've already added your rsa_id key to hostgator. Make sure you do that.

After typing this, you will be prompted with a password entry; go ahead and enter your hostgator plan password that you'd normally use to login.


# Writing SQL-Injection Resistant PHP Code

Here are the elements of SQL-Injection Resistant PHP Code:
1. Prepared statements
2. whitelisting
3. typecasting
4. escaping

Credit to [Vickie Li Dev's video](https://www.youtube.com/watch?v=WONbg6ZjiXk) for such an amazing recap of the above concepts.

# Using a non 'index.html' file as the default web page

This is a simple fix on hostgator.

On the project folder for your website, look for the .htaccess file and change it to the following format:
```txt
DirectoryIndex index.php
```

With this update, "index.php" is now the main file.

# Run python using PHP
This is simple; you'll need two/three things:
1. html code
2. php code (could be combined with 1)
3. python script

Here is a simple example that uses all three, instead of combining:

html:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Square Calculator</title>
</head>
<body>
    <h1>Square Calculator</h1>
    <form action="calculate_square.php" method="post">
        <label for="number">Enter a number:</label>
        <input type="number" id="number" name="number" required>
        <input type="submit" value="Calculate">
    </form>
</body>
</html>
```

The important part of the above is the snippet of code:
```html
<form action="calculate_square.php" method="post">
```

Next, we have our php script:

```php
<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Get the number from the form
    $number = $_POST["number"];
    
    // Execute the Python script to calculate the square
    $output = shell_exec("python square.py $number");

    // Print the result
    echo "<h2>The square of $number is $output</h2>";
}
?>
```

The important snippet in this code is here:

```php
$output = shell_exec("python square.py $number");
```

Finally, here is our python script:

```python
import sys

def square(num):
    return num * num

if __name__ == "__main__":
    num = int(sys.argv[1])
    result = square(num)
    print(result)
```

And that's it! If you run these three scripts together, it will work as intended!

## Bonus

Take it a step further. The previous attempt would *redirect* us to a different page. Here's how we would go about it, by showing results on the same page.

The main difference is that we use AJAX over post method (if ($_SERVER["REQUEST_METHOD"] == "POST"))

Here would be your html script:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Square Calculator</title>
    <script src="https://code.jquery.com/jquery-3.7.1.min.js"></script>
</head>
<body>
    <h1>Square Calculator</h1>
    <a href="index.php">return home</a>
    <br>
    <label for="num">Enter a number:</label>
    <input type="number" id="num" name="num">
    <button onclick="calculateSquare()">Calculate</button>
    <div id="result"></div>
    <script>
        function calculateSquare() {
            var num = document.getElementById("num").value;
            $("#result").text("Calculating..."); // Print message indicating calculation is in progress
            $.ajax({
                type: "GET",
                url: "calculate_square.php",
                data: { num: num },
                dataType: "json",
                success: function(response) {
                    $("#result").text("The square of " + num + " is " + response.result);
                }
            });
        }
    </script>
</body>
</html>

```

And here is your php:

```php
<?php
// run_python_script.php
$num = $_GET['num']; // Get input number from AJAX request
$command = "python square.py $num";
$output = shell_exec($command);
echo json_encode(array('result' => $output));
?>
```

One of the main differences is in the php code; we are **not** using the following snippet at the top (or anywhere, for that matter):

```php
if ($_SERVER["REQUEST_METHOD"] == "POST")
```