---
title: "Using GPT for Automatic Database Querying and Code Execution"
date: 2023-07-25T08:32:37-07:00
draft: false
tags: ['large-language-models']
ShowToc: true
cover:
    image: placeholder.png
    alt: ""
    caption: ""
ShowCodeCopyButtons: true
---

# Introduction

This post will show how to prompt GPT (or any language model) to answer a natural language query. Specifically:
- Take a human-written question
- write query statements to parse data tables based on human question
- return final result from database as answer to user's question

This code can be found in [this repo](https://github.com/StatStud/gpt-agent/tree/main).

# The Code

Without further adu, below is the code itself.

```python
import openai
import os
openai.api_key = os.environ["OPENAI_API_KEY"]
import time

query = "Feel like eating some good chinese food tonight."

prompt = f"""
VITALLY IMPORTANT: Ensure that your response is pure python, without any other non-python text.
I have the following tables (as a csv format). 

User_profile (file_tables/mock_data/user_profile.csv): 
user_id,user_name,user_preferences,max_budget,location_long,location_lat 
"U123456","John Doe","Italian, Mexican",30,-119.13142,46.23511 

Restaurants (file_tables/mock_data/user_profile.csv): 
store,location_long,location_lat,genre,price 
"Restaurant A",-119.1266,46.1923,"Italian",35 

Menus (file_tables/mock_data/menu.csv): 
store,genre,price,food_name,food_desc 
"Restaurant A","Italian",35,"Margherita Pizza","Traditional Neapolitan-style pizza topped with tomato sauce, mozzarella cheese, and fresh basil leaves." 

Write a python script that uses pandas 
(and other libraries as needed) to answer the question: 
{query}.

Avoid merging or joining tables when possible!!!

Your response should follow the class definition as follows:

class agent_query():
    def __init__(self):
        self.name = "yes"

    @staticmethod
    def run_query():
        ### < INSERT QUERY HERE >
        return <ANSWER HERE>

VITALLY IMPORTANT: Ensure that your response is pure python, without any other non-python text.
I REPEAT: Ensure that your response is pure python, DO NOT INCLUDE non-python text.
"""

def run_program():

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
    )
    response = response.choices[0].message.content

    def save_agent_response_to_file(string):
        with open("agent_code.py", 'w') as file:
            file.write(string)

    save_agent_response_to_file(response)

    from agent_code import agent_query

    try:
        result = agent_query.run_query()
        return result
    except Exception as e:
        print(f"Error encountered: {e}")
        print("Retrying...")
        time.sleep(2)  # Add a small delay before rerunning
        return run_program()

output = run_program()
print(output)
```

Notice how the bulk of this code is the prompt itself; this task is primarily dependent on the quality of the prompt. Let's look at this prompt to extract a few key things worth noting.

```python
query = "Feel like eating some good chinese food tonight."

prompt = f"""
VITALLY IMPORTANT: Ensure that your response is pure python, without any other non-python text.
I have the following tables (as a csv format). 

User_profile (file_tables/mock_data/user_profile.csv): 
user_id,user_name,user_preferences,max_budget,location_long,location_lat 
"U123456","John Doe","Italian, Mexican",30,-119.13142,46.23511 

Restaurants (file_tables/mock_data/user_profile.csv): 
store,location_long,location_lat,genre,price 
"Restaurant A",-119.1266,46.1923,"Italian",35 

Menus (file_tables/mock_data/menu.csv): 
store,genre,price,food_name,food_desc 
"Restaurant A","Italian",35,"Margherita Pizza","Traditional Neapolitan-style pizza topped with tomato sauce, mozzarella cheese, and fresh basil leaves." 

Write a python script that uses pandas 
(and other libraries as needed) to answer the question: 
{query}.

Avoid merging or joining tables when possible!!!

Your response should follow the class definition as follows:

class agent_query():
    def __init__(self):
        self.name = "yes"

    @staticmethod
    def run_query():
        ### < INSERT QUERY HERE >
        return <ANSWER HERE>

VITALLY IMPORTANT: Ensure that your response is pure python, without any other non-python text.
I REPEAT: Ensure that your response is pure python, DO NOT INCLUDE non-python text.
"""
```

Both at the start and end of the prompt, I heavily emphasize how the model's generated text should be pure python, without any additional text, explanations, or disclaimers. While this may still produce faulty code, it greatly minimizes the number of times the code returns an error due to unrecognized python characters.

To address the occasional bad generated code, I included a recursive return during the exception block here:

```python
    try:
        result = agent_query.run_query()
        return result
    except Exception as e:
        print(f"Error encountered: {e}")
        print("Retrying...")
        time.sleep(2)  # Add a small delay before rerunning
        return run_program()
```

This permits the main code to keep trying until it gets a successful return. And, because our prompting emphasizes python code, we don't often encounter expectations, but adding this makes our code more robust to errors (if an error occurs the first time, the next iteration is typically good enough to run without error).

Another thing to note about the prompt is the inclusion of database schema with examples. You may exclude examples if you include the data field types for each column--both methods work. This allows the model to form the right logic to answer the user's query.

Finally, the last important part, is the main method code structure I provide to the language model:

```python
# Your response should follow the class definition as follows:
class agent_query():
    def __init__(self):
        self.name = "yes"

    @staticmethod
    def run_query():
        ### < INSERT QUERY HERE >
        return <ANSWER HERE>
```

This part is important because when I try to run the script generated by the model, I have to make sure it follows a consistent import name so that I can actually run the generated script as an executable python file.

```python 
from agent_code import agent_query
result = agent_query.run_query()
print(result) #providing the user the answer
```

# The Results

So how well does this code do? Let me show you come generated responses!

## Example 1

Question: "I feel like eating some good chinese food tonight"

Answer:
```sh
          store  location_long  ...              food_name                                          food_desc
0  Restaurant C      -119.0879  ...  General Tso's Chicken  Crispy deep-fried chicken chunks glazed in a t...
1  Restaurant C      -119.0879  ...        Kung Pao Shrimp  Stir-fried succulent shrimp, peanuts, and vege...
2  Restaurant C      -119.0879  ...         Mongolian Beef  Tender slices of beef stir-fried with scallion...
3  Restaurant C      -119.0879  ...        Dim Sum Platter  Assortment of bite-sized steamed or fried dump...
4  Restaurant C      -119.0879  ...    Sweet and Sour Pork  Crispy deep-fried pork pieces in a tangy and s...
5  Restaurant C      -119.0879  ...              Mapo Tofu  Soft tofu cubes cooked in a spicy and flavorfu...
```

Explanation: The model not only identified the right restaurant that's sells Chinese food (Restaurant C) but also listed out the food items and descriptions (essentials the menu) for the restaurant.

Generated code:
```python
class agent_query():
    def __init__(self):
        self.name = "yes"
    
    @staticmethod
    def run_query():
        import pandas as pd
        
        # Read the user_profile.csv file into a DataFrame
        user_profile_df = pd.read_csv('file_tables/mock_data/user_profile.csv')
        
        # Read the restaurants.csv file into a DataFrame
        restaurants_df = pd.read_csv('file_tables/mock_data/restaurants.csv')
        
        # Read the menu.csv file into a DataFrame
        menus_df = pd.read_csv('file_tables/mock_data/menu.csv')
        
        # Filter restaurants for Chinese cuisine and within maximum budget
        chinese_restaurants = restaurants_df[(restaurants_df['genre'] == 'Chinese') & (restaurants_df['price'] <= user_profile_df['max_budget'][0])]
        
        # Filter menus for Chinese cuisine
        chinese_menus = menus_df[menus_df['genre'] == 'Chinese']
        
        # Merge the two DataFrames on the restaurant/store column
        merged_df = pd.merge(chinese_restaurants, chinese_menus, on='store')
        
        # Return the merged DataFrame
        return merged_df
```

## Example 2

Question: "I only have $20, where can I eat Mexican?"

Answer: "Restaurant B"

Explanation: Restaurant B is correct because it's a Mexican restaurant with menu items under $20.

Generated code:
```python
class agent_query():
    def __init__(self):
        self.name = "yes"

    @staticmethod
    def run_query():
        import pandas as pd

        # Read the user_profile table
        user_profile = pd.read_csv('file_tables/mock_data/user_profile.csv')

        # Read the restaurants table
        restaurants = pd.read_csv('file_tables/mock_data/restaurants.csv')

        # Filter the restaurants table based on genre and price
        filtered_restaurants = restaurants[(restaurants['genre'] == 'Mexican') & (restaurants['price'] <= 20)]

        # Get the store names
        store_names = filtered_restaurants['store']

        # Check if there are any matching stores
        if store_names.empty:
            return "No restaurants found"
        else:
            return store_names.tolist()
```

## Example 3

Question: 

Answer: "The nearest Italian restaurant to David Johnson is Restaurant A, 1.4106255158719745 miles away."

Expatiation: Not much to add here other than it's correct

Generated code:
```python
import pandas as pd
from geopy.distance import geodesic

class agent_query():
    def __init__(self):
        self.name = "yes"

    @staticmethod
    def run_query():
        user_profile = pd.read_csv('file_tables/mock_data/user_profile.csv')
        restaurants = pd.read_csv('file_tables/mock_data/restaurants.csv')

        user_name = "David Johnson"
        user_location = (user_profile.loc[user_profile['user_name'] == user_name, 'location_lat'].values[0],
                         user_profile.loc[user_profile['user_name'] == user_name, 'location_long'].values[0])

        italian_restaurants = restaurants.loc[restaurants['genre'] == 'Italian']
        italian_restaurants['distance'] = italian_restaurants.apply(
            lambda row: geodesic(user_location, (row['location_lat'], row['location_long'])).miles, axis=1)

        nearest_restaurant = italian_restaurants.loc[italian_restaurants['distance'].idxmin()]
        nearest_restaurant_name = nearest_restaurant['store']
        distance = nearest_restaurant['distance']

        return f"The nearest Italian restaurant to {user_name} is {nearest_restaurant_name}, {distance} miles away."
```