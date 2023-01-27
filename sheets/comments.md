# Comments

Learn why comments are important and how to make them in Python.

This article will go over the importance of comments and different ways to make them.
* What Are Comments?

In Python, comments are made with # to explain code at various points in the code. Comments are not executed as code and are used for documentation. There are two types of comments: inline comments and block comments.
Inline Comments

* Inline comments should be used when you have a short comment that you would like to include after a line of code.

````
minutes = seconds / 60  # calculating minutes from seconds
````
* Block Comments

Block comments are used when you have multiple lines of comments that you’d like to include with your code. Unlike most languages that have special syntax for multiple lines of comments, Python requires # on consecutive single lines.
````
def calculate_minutes(seconds):
   # This function calculates the time in minutes 
   # from given seconds.
   minutes = seconds / 60
   return minutes
````