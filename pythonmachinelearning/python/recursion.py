#recursion in python is a technique where a function calls itself to solve a problem
# for example if we want to find the factorial of a number using recursion
num=input("enter a number to find its factorial: ")
def factorial(n):
    """This function returns the factorial of a number."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
print(factorial(int(num)))

#WAP to find the fibonacci series using recursion 
print("Fibonacci series using recursion")
n= int(input("Enter the number of terms: "))
def fibonacci(n):
    """This function returns the Fibonacci series up to n terms."""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_series = fibonacci(n - 1)
        fib_series.append(fib_series[-1] + fib_series[-2])
        return fib_series
print(fibonacci(n))
