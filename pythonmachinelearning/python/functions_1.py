#functions in python , functions are used to encapsulate code that can be reused
# functions are defined using the def keyword
#for example if we want to create a function that finds the geometric mean of 2 numbers 
def gmean(a, b):
    geomean =(a*b)/(a+b)
    print("the geometric mean of",a,"and",b,"is",gmean)
# we can call the function by passing the arguments
gmean(4, 16)
# we can also use functions to find the arithmetic mean of 2 numbers
def amean(a, b):
    amean = (a + b) / 2
    print("the arithmetic mean of", a, "and", b, "is", amean)
# we can call the function by passing the arguments
amean(4, 16)
# there are also built in functions in python that can be used anytime 
