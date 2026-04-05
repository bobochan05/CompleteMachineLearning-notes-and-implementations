'''indexing and selection 
grabbing single element 
grabbing a slice of elements 
broadcasting selections 
indexing and selection in 2 dimension 
conditional search'''
import numpy as np
arr=np.arange(0,10)
print(arr)
#now we can use any method applicable to arrays 
#reassigning values to a particular section
arr[0:5]=100
print(arr)
#reversing 
ar=arr[::-1]
print(ar)
#2d array method
ar2d=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(ar2d)
#we can access each row by indexing 
print(ar2d[0],ar2d[1],ar2d[2])
print(ar2d[0,2])
#conditional search in array 
arr=np.arange(1,16)
#lets search the array for elements above 5
print(arr>5)
dice_rolls = np.array([3, 1, 5, 2, 5, 1, 1, 5, 1, 4, 2, 1, 4, 5, 3, 4, 5, 2, 4, 2, 6, 6, 3, 6, 2, 3, 5, 6, 5])

# total_rolls_over_two = # This should be a single integer

print(len(dice_rolls))
boolean=(dice_rolls>2)
print(boolean)
print(dice_rolls[boolean])


