#this is strings in string if we want to print a part of string we write the starting index 
# then use ' :' and specify then n+1 th index
name = input("enter your name -")
print ("your name is",name)
print ("your name is",name[0:3])
print ("your name is",name[0:5])
# we use len function to find the length of string
print ("length of your name is",len(name))
# we can also use negative indexing to print the string from the end
print ("your name is",name[-1])
print ("your name is",name[-2])
print ("your name is",name[-3])
# we can also find the position of a character in the string using index function
# for example if we want to find the index of 'S' in the string
# we can use the index function
# but if the character is not present in the string it will give an error
print ("index of your name is" ,name.index("S"))
#revsersing a string
input_string = input("Enter a string to reverse: ")
reverse_string = input_string[::-1]


print("Reversed string:", reverse_string)
