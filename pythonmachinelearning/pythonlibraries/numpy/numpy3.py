'''operations on array
like addition , multiplication ,etc 
and others '''
import numpy as np
arr=np.arange(0,10)
print(arr)
#we can add a number to each element of array 
print(arr+5)
#if we print arr+arr, each element gets added to itself 
print(arr+arr)
#if we print arr*arr, each element gets multiplied to itself 
print(arr*arr)
#division in numpy array is different  
print(arr/0)#0/0 is replaced by nan , scalar divided by 0 will be replaced by inf
#we can find the squareroot without importing math function 
print(np.sqrt(arr))
#we can also find the sin , cos values by using np.sin()
#the np.std() gives the standard deviation 
print(arr.sum())#this sums up every element of the array 
'''for a 2D array'''
ar=np.arange(0,25).reshape(5,5)
print(ar)
#now if we want the sum of each element then we normally use .sum()
#if we want sum along the coloumns
print(ar.sum(axis=0))#this adds the elements of each coloumn 
print(ar.sum(axis=1))#this adds the elements of each 




