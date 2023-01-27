# Recursion

Learn how to use recursion in Python.

The word recursion in Python describes the process of repeatedly calling a function within itself. In this article, we’ll cover how to use recursion with functions and why we use them.
A Recursive Function

Let’s take a look at what a recursive function looks like:
````
def factorial(num):
   if num == 1:
       return 1
   else:
       return num * factorial(num-1)
````
The above function factorial is a recursive function because it calls itself within the function. A recursive function contains two parts: recursive step and base case.
* Recursive Step

The line of code under the else statement is the recursive step, because it calls the function factorial().
Base Case

In the above function, the recursion stops when num == 1. This case is called the base case, which should be defined in every recursive function. Having a base case helps to avoid infinite recursions. The base case can be defined with an if statement like the function above. Without the base case in the factorial function above, the function would start calling factorial(0), factorial(-1) and so on.
How It Works

Taking the function factorial from above, let’s do a slight modification to implement a call stack that will help to visualize the recursion. Take a look at what happens if we call factorial(5):
````
def factorial(num):
   call_stack = []
   if num == 1:
       print('base case reached! Num is 1.')
       return 1
   else:
       call_stack.append({'input': num})
       print('call stack: ', call_stack)
       return num * factorial(num-1)
 
factorial(5)
 
# call stack:  [{'input': 5}]
# call stack:  [{'input': 4}]
# call stack:  [{'input': 3}]
# call stack:  [{'input': 2}]
# base case reached! Num is 1.
````

Notice the recursion stops when the base case (num = 1) is reached, and prints the final output.
Why Recurse?

There are a few advantages of using recursion:

*    It produces clear code, reducing the need to repeat code.
*    It can be used for advanced data structures problems.
*    It splits a complex task into smaller tasks.
