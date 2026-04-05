#numpy , it is a python library to create n dimensional arrays 
#ability to quickly broadcast functions and inbuilt capabilities 
import numpy as np
#how to create a numpy array 
my_matrix=[[1,2,3],[4,5,6],[7,8,9]]
print(np.array(my_matrix))
#how to create a 1d array using numpy 
x=np.arange(0,10)
#we can also pass a 3rd argument which is called the step size or how much it will increment 
y=np.arange(0,10,2)
print(x)
print(y)
#the np.zeros is used to create an array of given shape and size with filled zeroes
a=np.zeros(5)
b=np.zeros((3,3))
print(a)
print(b)
#same can be done for ones 
print(np.ones(( 2,2)))
#we can use np.linspace to create evenly spread arrays
print(np.linspace(0,10,3))#the 3rd argument means the output will be 3 evenly spread numbers
#we can also create an identity matrix using the eye function 
print(np.eye(3))
#generating random numbers using numpy random function 
#the random.rand function generates random numbers in a given shape
#Create an array of the given shape and populate it with random samples from a uniform distribution over [0, 1).
#we pass the number of rows followed by the number of coloumns
print(np.random.rand(2,3)) 
#we use the function random.randn to to populate it with random samples from a uniform distribution over any range 
print(np.random.randn(2,3))#the number close to 0 have higher likelyhood of being selected
#we can also use the random.randint to get integer numbers 
print(np.random.randint(0,100,(4,4)))#the first argument is the lower threshold , the 2nd is the upper threshold
#3rd argument is the number of numbers we need or also pass the shape of matrix
print(np.random.seed(42))
print(np.random.rand(4))

arr=np.arange(0,25)
print(arr)
#we can use reshape function to reshape the array
print(arr.reshape(5,5))
#let there be an array of random elements 
rand_arr=np.random.randint(0,100,10)
print(rand_arr)
print(rand_arr.max())#returns the max value 
print(rand_arr.min())#returns the minimum value 
print(rand_arr.argmax())#returns the index of the max value
print(rand_arr.argmin())#returns the index of the min value 
# we can also use the shape function to know the shape of the array 

