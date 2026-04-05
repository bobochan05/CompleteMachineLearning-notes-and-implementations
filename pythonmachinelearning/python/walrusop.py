#python 3.5 features
#walrus operator 
#the walrus operator allows you to assign values to a variable as a part of an expression 
#it is represented by := 
#example
if (n := len (input("enter your name"))) > 5:
    print(f"length of the string is {n} which is greater than 5 characters")
else:
    print(f"length of the string is {n} which is less than or equal to 5 characters")
#here we are assigning the length of the input string and using it in the if else condition 

#match case statement 
#it is used to match a value against a pattern
#it is similar to switch case statement in other languages
n=int (input("enter a number: "))
match n:
    case 1:
        print("you entered one")
    case 2:
        print("you entered two")
    case 3:
        print("you entered three")
    case _:
        print("you entered something else") #_ is used as a default case





