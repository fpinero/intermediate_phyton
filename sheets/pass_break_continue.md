# Pass, Break, Continue

Learn how to control for and while loops in Python.

This article will cover the three keywords, pass, break and continue which are used to control or disrupt loops.
* pass

The pass keyword is mostly used as a placeholder in a loop. Nothing gets executed when pass is placed under a condition.

````
names = ['Joyce', 'Hannah', 'Manny', 'Manoj', 'Ezekiel']
 
for name in names:
   if 'j' in name.lower():
       pass
   else:
       print(name)
````
The example above iterates through the list names to print each element name, but ignores elements that contain the letter j. This is the output:
````
Hannah
Manny
Ezekiel
````
* break

The break keyword terminates a loop. break statements are typically found within conditional statements. If a certain condition is met, the loop stops iterating and breaks at that point.
````
names = ['Joyce', 'Hannah', 'Manny', 'Manoj', 'Ezekiel']
 
for name in names:
  if 'h' in name.lower():
      break
  else:
      print(name)
````
The code above iterates through the list names to print each name, but breaks when the letter h is found in name. This is the output:
````
Joyce
````
* continue

The continue keyword skips over an iteration if the condition is met and goes onto the next iteration. The difference between the continue keyword and pass is that continue goes onto the next iteration while pass simply does not do anything.
````
names = ['Joyce', 'Hannah', 'Manny', 'Manoj', 'Ezekiel']
 
for name in names:
  if 'm' in name.lower():
      continue
  else:
      print(name)
````
The code above iterates through the list names to print each element name, but skips over any elements that contain the letter m.

The output is:
````
Joyce
Hannah
Ezekiel
````