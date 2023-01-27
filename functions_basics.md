# Function Basics

Learn how to create functions in Python.

A function in Python contains code that is executed when it is called. Functions make code reusable and repeatable. In this article, we’ll cover the following topics:

*    Creating a function
*    Using a function
*    Parameters
*    Arguments

Creating a Function

The following example shows the structure of a function in Python:
````
def add_three(num1, num2, num3):
   sum_three = num1 + num2 + num3
   return sum_three
````
Here is a breakdown of this function:

  *  def is the built-in keyword in Python that is used to declare functions.
  *  add_three is the name of the function.
  *  (num1, num2, num3) is the list of parameters needed for the function.
  *  : indicates the start of the function body.
  *  sum_three = num1 + num2 + num3’ is the code in the function body followed by the indentation.
  *  return is the built-in keyword that exits the function and returns the output sum_three.

** Using a Function

Functions can be used by calling the function name with parentheses. Let’s try to call the function add_three that we defined above, and assign it to the variable sum_output:
````
sum_output = add_three(2, 4, 6)
````
We can check the output by using the print() statement. This would return the output:
````
12
````
** Parameters

Functions can be built to include parameters. Parameters are treated as local variables within the body of the function. The function below has the parameter language.
````
def greetings(language):
   if language == 'Spanish':
       greeting = 'Hola'
 
   elif language == 'English':
       greeting = 'Hello'
 
   elif language == 'French':
       greeting = 'Bonjour'
 
   print(greeting)
````
** Arguments

Arguments are values that can be passed into the function and used as parameters. We can call the above function with the argument French like this:
````
greetings('French')
````
This would return the output:
````
'Bonjour'
````
