# Variables

Learn more about variables in Python.

Variables are used to name, store and reference data. This article will cover the following topics:

 *   Declaring a Variable
 *   Casting
 *   Printing the Data Type of a Variable

** Declaring a Variable

You can declare a variable using the following syntax:
````
name = 'Grace'
````
This line of code stores the string ’Grace’ in the variable name. You can change the value stored in the variable by using the same syntax but assigning the variable to the new value.
````
name = 'Ari'
````
Note that you can store other data types in a variable, not just strings. For example, storing a number would look like this:
````
temperature = 97.5
````
You can also store results of expressions as a variable:
````
sum_of_two_numbers = 4 + 2
````
** Casting

You may sometimes want to specify the type of the variable using built-in data types in Python. For example, I may want to store a numerical value as a string, which can be done by using the constructor function str() like this:
````
temperature = str(97.5)
````
The function str() takes a value and converts it into a string. There are other functions such as int(), float() and bool() which we will cover in our next article.

** Printing the Data Type

If you need to access the data type of a variable, you can simply use the built-in function type() to print the variable’s type.
````
temperature = str(97.5)
type(temperature) # prints str
````