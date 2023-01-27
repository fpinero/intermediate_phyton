# if, elif, else

Learn about conditional statements in Python.

This article will go over if, elif, and else statements, also known as conditional statements, which are used to execute a sequence of code based on the given boolean values.
* if Statements

An if statement evaluates whether the given expression is evaluated as True. If the condition evaluates to be True, the code is executed. If the condition evaluates to be False, the code does not execute.

For example, the if statement can be used to evaluate if the expression score >= 80 is True. If the variable score is set as 90, because it is greater than 80, it will execute the following code with the print statement:
````
score = 90
 
if score >= 80:
   print('You pass the course!')
````
If the variable score is changed to 40, the print() statement won’t be executed.

* else Statements

Adding an else statement after an if statement allows for another set of code to be ran if the if statement evaluates the expression to be False.
````
score = 70
 
if score >= 80:
   print('You pass the course!') 
else:
   print('You do not pass the course!')
````
The if statement here evaluates whether the variable score is greater than or equal to 80. Because the statement is False, the latter print() statement would be executed.
* elif Statements

An elif statement, which is short for else if, can be added between an if statement and an else statement to evaluate for another condition. The code under the elif statement will only execute if the preceding if statement evaluates to be False.
````
score = 70
 
if score >= 80:
   print('You pass the course with flying colors!')
 
elif score > 65:
   print('You pass the course! Talk to your instructor.')
 
else:
   print('You do not pass the course!')
````
Here, the initial if statement evaluates to be False, so the elif statement is evaluated. Because the elif statement evaluates to be True, the print() statement under elif is executed. 
