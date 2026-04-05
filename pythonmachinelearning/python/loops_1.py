#LOOPS
#for lopps are used to iterate over a sequence (list, tuple, dictionary, set, or string)
# we can use for loop to iterate over a string
# for example if we want to print each character of the string
# we can use for loop
name = input("enter your name -")
print ("your name is",name)
for i in name:
    print(i)

# we can use for loop to print n numbers 
# for example if we want to print 1 to 10
for i in range(11):
    print(i)
# we can use for loop to print even numbers
# for example if we want to print even numbers from 1 to 200000
for i in range(1,200):
    if i%2==0:
        print(i)

#WHILE LOOPS
# while loops are used to execute a block of code as long as the condition is true
# for example if we want to print 1 to 10
i = 1
while i <= 10:
    print(i)
    i=i+1
# we can use while loop to print even numbers
# for example if we want to print even numbers from 1 to 200000

i = 1
while i <= 200:
    if i%2==0:
        print(i)
    i += 1
