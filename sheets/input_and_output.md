# Input and Output

Learn how to implement input and output in Python.

This article will cover different ways of implementing input and output in Python.
* Input

How do we ask for user input as a part of our program? Python has a built-in function called input() that takes in the user’s input. In the example below, we use the input() function to ask the user for their name:
````
input('What is your name?')
````
You can store user input as a variable to use later. For example, we can save the user’s response to “What is your name?” in the variable name like so:
````
name = input('What is your name?')
````
* Output

To display output, you can use Python’s built-in function print(). The following print() statement prints a simple sentence:
````
print('Very nice to meet you!')
````
Let’s say we want to print the user input we stored in the variable name from our last example. You could call the variable name in your print statement:
````
print('Very nice to meet you, ', name, '!')
````
You can also use multiple variables in the print statement:
````
name = 'Barbara'
age = '32'
 
print('Very nice to meet you! My name is', name, 'and I am', age, 'years old') 
````
You can also use + to concatenate variables and strings in the print() statement as long as your variables are strings:
````
print('Very nice to meet you! My name is ' + name, 'and I am ' + age + ' years old')
````
* Formatted String Literals

You could also use formatted string literals by starting the print argument with f and inserting a Python expression between { and }.
````
print(f'Very nice to meet you, {name}!')
````
This example would print the name in all uppercase:
````
print(f'Very nice to meet you, {name.upper()}!')
````
* str.format()

Python also has a built-in function called str.format() that can be used with the print() function.
````
print('Very nice to meet you, {}!'.format(name))
````