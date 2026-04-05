#enumerate function in python helps to iterate over a list and get the index of each element
# # for example a list named fruits can be used to hold the names of fruits
fruits = ["apple", "banana", "cherry"]
# we can use the enumerate() function to iterate over the list and get the index of each element
for index, fruit in enumerate(fruits):
    print(f"Index: {index}, Fruit: {fruit}")

#modules in python are used to organize code into separate files
#import modules using the import keyword they are used to encapsulate code that can be reused
import math 
# for example we can use the math module to perform mathematical operations
# we can use the sqrt() function to find the square root of a number
number = 16
sqrt_number = math.sqrt(number)
print(f"The square root of {number} is {sqrt_number}")
# we can also use the pow() function to find the power of a number
base = 2
exponent = 3
power_result = math.pow(base, exponent)
print(f"{base} raised to the power of {exponent} is {power_result}")
# we can also use math as m to shorten the module name
import math as m
# we can use the pi constant from the math module
pi_value = m.pi
#we can also import specific functions from a module using the from keyword
from math import factorial, gcd
# we can use the factorial() function to find the factorial of a number
factorial_result = factorial(5)
print(f"The factorial of 5 is {factorial_result}")
# we can use the gcd() function to find the greatest common divisor of two numbers
gcd_result = gcd(12, 15)
print(f"The greatest common divisor of 12 and 15 is {gcd_result}")

