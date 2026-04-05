# IF ELSE  statements 
# we use conditional statements to check if a condition is true or false
# if the condition is true then the code inside the if block will be executed
# if the condition is false then the code inside the else block will be executed
# for example if we want to check if a number is even or odd
# we can use the modulus operator to check if the number is divisible by 2
# if the number is divisible by 2 then it is even
# if the number is not divisible by 2 then it is odd
a = input("enter a number -")
if int(a)%2 == 0:
    print("the number is even")
else:
    print("the number is odd")
#we also have elif statement which is used to check multiple conditions
# for example if we want to check if a number is positive, negative or zero
# we can use the if, elif and else statements
a = input("enter a number -")
if int(a) > 0:
    print("the number is positive")
elif int(a) < 0:
    print("the number is negative")
else:
    print("the number is zero")

