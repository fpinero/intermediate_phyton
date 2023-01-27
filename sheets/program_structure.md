# Program Structure

Learn about the basic structure of a Python program.

Let’s do a quick overview of what a Python program looks like.
* Hello World

You are probably familiar with the phrase “Hello World!” if you’ve learned other programming languages in the past. This is a simple Python program named greetings.py that prints “Hello World!” to the output:

```
def main():
    print('Hello World!')
 
if __name__ == '__main__':
    main()

The main() Function
```
Curious why we used a main function to create the program? In Python, we frequently use the main() function to define the starting point of our program. Including the main() function allows us to import and run this program in another script.

Placing the if statement in our program basically checks whether the program is being run independently as the primary module or as a library in another script. If you run the current greetings.py program on its own in the terminal, it will print “Hello World!”:
````
$ python greetings.py
Hello World! 
````
