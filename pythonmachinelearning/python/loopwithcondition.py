#forloop with else in python  
for i in range(5):
    print("Current number is:", i)
else:
    print("Loop completed without break")
# The else block executes after the for loop completes normally, without a break statement.
# If a break statement is encountered, the else block will not execute.

#exception handling in python is used to handle errors and exceptions that may occur during the execution of a program
# it allows us to write code that can handle errors gracefully without crashing the program
#for example if we want to give the table of a number
a=input("Enter a number to print its table: ")
try:
    a=int(a)
    for i in range(1, 11):
        print(f"{a} x {i} = {a * i}")

except ValueError:
    print("Please enter a valid integer number.")
# The try block contains code that may raise an exception.
#finally block is used to execute code that should run regardless of whether an exception occurred or not
finally:
    print("Execution completed, whether or not an exception occurred.")
# The finally block is optional and can be used to clean up resources or perform final actions.
#rasing exceptions in python is used to raise an exception manually
# for example if we want to raise an exception if the user enters a negative number
def check_positive_number(num):
    """This function checks if the number is positive."""
    if num < 0:
        raise ValueError("The number must be positive.")
    return num
try:
    number = int(input("Enter a positive number: "))
    check_positive_number(number)
    print(f"You entered a valid positive number: {number}")
except ValueError as e:
    print(f"Error: {e}")
# The raise statement is used to raise an exception manually.

