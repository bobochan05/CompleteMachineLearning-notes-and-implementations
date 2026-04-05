#lists in python is a data structure that can hold multiple values
#for example a list named marks can be used to hold the marks of students
marks = [90, 80, 70, 60, 50]
# we can access the elements of the list using indexing
print("The first element in the list is:", marks[0])
# we can also use a for loop to iterate through the list
for mark in marks:
    print("The mark is:", mark)
# we can also use the len() function to find the length of the list
print("The length of the list is:", len(marks))
# we can also use the append() function to add an element to the list
marks.append(40)
# we can also use the insert() function to add an element at a specific index
marks.insert(2, 75)
# we can also use the remove() function to remove an element from the list
marks.remove(60)
# we can also use the pop() function to remove the last element from the list
marks.pop()
# we can also use the sort() function to sort the list in ascending order
marks.sort()
# we can also use the reverse() function to reverse the order of the list
marks.reverse()
# we can also use the index() function to find the index of an element in the list
print("The index of 80 in the list is:", marks.index(80))
# we can also use the count() function to count the number of occurrences of an element in the list
print("The number of occurrences of 80 in the list is:", marks.count(80))
# we can also use the copy() function to create a copy of the list
marks_copy = marks.copy()


