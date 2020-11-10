import numpy as np
import pandas as pd


"""
General introduction and deep dive into Numpy

"""

# How to create arrays in Numpy

## Create array from Python lists

### 1. Same type
array = np.array([1,23,42,12])

### 2. Different data types (the data will be upcasted as much as possible)
data_types = np.array([3.31, 12, 1.11, 16]) 

### 3. Nested Lists
nested_type = np.array([range(i,i+3) for i in range(5)])


# Create arrays from scratch

### 1. Array filled with zeros
zero_array = np.zeros(10, dtype=int)

### 2. Nested array with ones
ones_array = np.ones((2,4), dtype=int)

### 3. Created an array with custom value
custom_array = np.full((2,3), 2.71, dtype=float)

# 4. 
### Create an array filled with a sequence
### Starting at 0, ending at 20, stepping by 2
### (this is similar to the built-in range() function)
np_array_sequence = np.arange(0, 20, 3)

# 5. 
### Create an array  filled with values evenly spaced between two numbers
np_spaced_array = np.linspace(0, 1, 5)

# 6. Create a 3x3 array of uniformly distributed(Each value has an equal chance of appearing even though there are infinite values) random values between 0 and 1
np_random_uniform_distribution = np.random.random((3, 3))

# 7. Create a 3x3 array with 0 mean and 1 standard deviation of normally distributed random values
### Normal distribution means that the data near to the mean is more likely to occur as compared to the data far from mean
np_random_mean_deviation = np.random.normal(0, 1, (3, 3))

# 8. Create a random int array between 5 and 15
np_randint = np.random.randint(5, 15, (3, 3))

# 9. Create a identity matrix of dimensions 3x3
np_identity = np.eye(3)


"""
How to check some of the attributes of an nd array using np

1. using the .ndim property to get the number of dimensions of the array
2. using the .size property to get the total number of elements in the array
3. using the .shape property to get the shape of the matrix formed
4. using the .dtype to get to know the data type of the elements inside the array

"""

alist = [1,2,3,4,5]
blist = [43, 123, 12321]
andarray = np.array(alist)
print(andarray)
print(np.ndim(andarray), "represents that it only has one dimension",andarray.ndim)
print(np.size(andarray), " represents that it only has 5 elements in it", andarray.size)
print(np.shape(andarray), "represents the shape of the ndarray ", andarray.shape)
print(" represents the data type inside the array", andarray.dtype)


"""
Accessing elements in the numpy array


"""

np.random.seed(0)
x1  = np.random.randint(0,10,size=(2,5))
x2 = np.random.randint(10, size=(5))
print(x1)
print(x2)
print(x1[0,1], "to access the element of row 0 and column 1")
print(x2[4], "To access the element at index 4")



"""
Array Slicing

To access a slice of an array x, 


x[start:stop:step] 


is the standard slicing syntax.

"""

x3 = np.random.random(size=(5))
x4 = np.arange(0, 10, 2)
print(x3)
print(x3[0:2])

# Multidimensional Subarray slicing

x5 = np.random.randint(0, 10, size=(3,3))
print(x5)
print(x5[0:2, 0:1], "Accessing the first two rows and first column would look like this")

# To reverse the order, we generally do array[::-1]

# reversing the row would look as follows:
print(x5[::-1,:])

# reversing the column would look as follows:
print(x5[:,::-1])

# reversing both row and column would be as follows:
print(x5[::-1,::-1])
print()
print()
print()



"""

How to create copies of the subarrays that are sliced out of the arrays?
We use the .copy() method to create the subarrays

"""

x6 = np.arange(1,10).reshape(3,3)
x7 = x6[:2,:2].copy()
print(x7)
x7[1,1] = 100
print(x6) # the original array doesn't get changed if we use the .copy() method while creating a subarray otherwise it does.
print(x7)
print()
print()
print()


"""
Reshaping the arrays

2 ways:
    a. .reshape(x,y) method
    b. slicing using np.newaxis method
"""


# Method a: Using the .reshape(x,y) method

x8 = np.arange(1,10)
print(x8)
x8 = x8.reshape((3,3))
print(x8)


# Method b: Slicing using np.newaxis method

x9 = np.arange(0,5)
print(x9.shape)
x9 = x9[np.newaxis, :]
print(x9.shape)
x_column =np.arange(0,5)
x_column = x_column[:, np.newaxis]
print(x_column)



"""
Array Concatenation and Splitting

"""

x10 = np.array([1, 2, 3, 4])
x11 = np.array([5, 6, 7, 8])

x12 = np.concatenate([x10, x11])
print(x12)

# It can also concatenate grids or multidimensional arrays

x13 = np.arange(1,10).reshape((3,3))
print(np.concatenate([x13, x13]))
print()
print(np.concatenate([x13, x13], axis=1))


# If we're working with arrays having different dimensions, then use vstack() and hstack()

x14 = np.arange(0,5)
x15 = np.arange(0,10).reshape((2,5))

print(np.vstack([x14, x15]))
print()
print(x14.shape, x15.shape)

x16 = np.arange(0,10).reshape((5,2))
x17 = np.arange(0,5)
x17 = x17[:, np.newaxis]
print(x17)
print(np.hstack([x16, x17]), ": this is the hstack implementation.")



# # Splitting of Arrays

x = [1, 2, 3, 99, 99, 3, 2, 1]

x1, x2, x3 = np.split(x, [3, 5])

print(x1)
print()
print(x2)
print()
print(x3)

grid = np.arange(16).reshape((4,4))

print(grid)

# To split it vertically
upper, lower = np.vsplit(grid, [2])


# To split it horizontally

left, right = np.hsplit(grid, [2])


v1 = np.arange(1,10).reshape((3, 3))
v2 = np.arange(0,3)
v2 = v2[np.newaxis, :]
print(np.add(v1, v2))

"""
Ufuncs are Universal functions. Just a fancy name for mathematical operations.
All the mathematical operations can be used interchangelby except ones with any form of aggregations. When aggregations are involved, 
the nunpy functions can be at least 100x faster as compared to the regular python functions

"""
"""
Comparisons, Masks, and Boolean Logic

"""

x = np.arange(0, 10)
print(x<6) # This is a boolean mask created that creates an array of True and False values for the condition speicified.
print(x[x<7])

# Comparison operators as Ufuncs(Universal Functions)

print(x < 6) # can also be <=

print(x > 6) # can also be >=

print(x == 6)

# It is also possible to do element by element comparison of two arrays

print((x *2) == (x<10))




# Counting Entries

print(np.count_nonzero(x < 6))

print(np.sum(x<6)) # this is the same as the above given function since it's a mask array which has only True and False values. It considers True as 1 and adds it and False as 0.

x = np.arange(1,10).reshape((3,3))

# It can also work for each row. Change the axis to 1

print(np.sum(x < 6, axis=1))


print(x[(x < 6) & (x % 2 == 0)])

"""
In the above expression, I've used an Ampersand instead of the traditional python 'and' operator. WHY?


Because, 'and' compares the two objects to determine these truth or falsehood and & compares the individual bits of these objects

when we say that x<10, it becomes a boolean array and having individual bits representing the information and hence use bitwise operators between these comparisons
"""