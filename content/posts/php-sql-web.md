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