#map , filter and reduce in python are inbuilt function in python that allows us to 
#apply a function to a sequence of elements to transform them or filter them based on a condition
#map function applies a given function to all items in an iterable (like a list) and returns a map object
#map function can be used to square all elements in a list
#eg we can use map to square all elements in a list
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x * x, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]

#filter function filters elements from an iterable based on a condition
#eg we can use filter to get all even numbers from a list
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4]

#reduce function is used to apply a rolling computation to sequential pairs of values in an iterable
#reduce is not a built-in function in Python 3, so we need to import it from functools
from functools import reduce
#eg we can use reduce to find the sum of all elements in a list
sum_of_numbers = reduce(lambda x, y: x + y, numbers)
print(sum_of_numbers)  # Output: 15
