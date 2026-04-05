#sets in python # sets are a data structure that can hold multiple values
# sets are unordered collections of unique elements
#sets are defined using curly braces and they dont allow duplicate elements
# for example a set named fruits can be used to hold the names of fruits
fruits = {"apple", "banana", "cherry"}
# we can access the elements of the set using a for loop
for fruit in fruits:
    print("The fruit is:", fruit)
# we can also use the len() function to find the length of the set
print("The length of the set is:", len(fruits))
# we can also use the add() function to add an element to the set
fruits.add("orange")
# we can also use the remove() function to remove an element from the set
fruits.remove("banana")
# we can also use the discard() function to remove an element from the set without raising an error if the element is not found
fruits.discard("grape")  # won't raise an error if "grape" is not in the set
#union of two sets can be done using the union() function or the | operator
fruits2 = {"kiwi", "mango"}
# union using the union() function
union_fruits = fruits.union(fruits2)



