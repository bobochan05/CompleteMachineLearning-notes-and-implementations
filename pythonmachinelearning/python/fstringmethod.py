#fstring in python is a way to format strings using curly braces {}
# # for example if we want to print the name and age of a student
name = "Alice"
age = 22
print(f"The student's name is {name} and age is {age}")
# fstrings can also be used to format numbers
pi = 3.14159
print(f"The value of pi is approximately {pi:.2f}")
# fstrings can also be used to format dates
# from datetime import datetime
# today = datetime.now()
#docstring in python is a way to document the code
# for example if we want to document a function that finds the square of a number
def square(num):
    """This function returns the square of a number."""
    print(num**2)
print(square.__doc__)

