#dictionaries in python are a data structure that can hold key-value pairs
# dictionaries are defined using curly braces and they allow duplicate keys
# for example a dictionary named student can be used to hold the name and age of a student
student = {"name": "John", "age": 20, "marks": 85}
# we can access the elements of the dictionary using the key
print("The name of the student is:", student["name"])
# we can also use the get() function to access the elements of the dictionary
print("The age of the student is:", student.get("age"))
#by using get() we wont get an error if the key is not found
# we can also use a for loop to iterate through the dictionary
for key, value in student.items():
    print(f"The {key} of the student is: {value}")
# we can also use the len() function to find the length of the dictionary
print("The length of the dictionary is:", len(student))
#we can also update the value of a key in the dictionary n add 2 dictionaries 
marks1= {"math": 90, "science": 85}
marks2 = {"english": 88, "history": 92}
marks1.update(marks2)
print("Updated marks dictionary:", marks1)
#we can use the del keyword to remove a key-value pair from the dictionary
del student["marks"]
print("Dictionary after deleting marks:", student)


