#modules in python are as follows:
# math - for mathematical operations
# os - for operating system related operations
# sys - for system related operations
# random - for generating random numbers
# datetime - for working with dates and times
# json - for working with JSON data
# re - for regular expressions
# #functions in python , functions are used to encapsulate code that can be reused
#and so on
#creating a module is as simple as creating a python file with the .py extension
# and defining functions or classes in it
# for example we can create a module named mymodule.py with the following code
def greet(name):
    print(f"Hello, {name}!")
 # we can then import this module other python file and use the greet() function
import differentmodulesinpython as mymodule 
name=input("Enter your name: ")
mymodule.greet(name)



