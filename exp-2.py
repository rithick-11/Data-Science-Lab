#Working with Numpy arrays

#importing numpy
import numpy as np

print("Program 1:-", "\n")

# Creating array object 
arr = np.array( [[ 1, 2, 3], [ 4, 2, 5]] )

# Printing type of arr object
print("Array is of type: ", type(arr))

# Printing array dimensions (axes)
print("No. of dimensions: ", arr.ndim)

# Printing shape of array
print("Shape of array: ", arr.shape)

# Printing size (total number of elements) of array 
print("Size of array: ", arr.size)

# Printing type of elements in array
print("Array stores elements of type: ", arr.dtype)
print("----------------------------------------------------------------------------------")
print("")

print("Program 2:-")

# Creating array from list with type float
a = np.array([[1, 2, 4], [5, 8, 7]], dtype = 'float') 
print ("Array created using passed list:\n", a)

# Creating array from tuple 
b = np.array((1 , 3, 2))
print ("\nArray created using passed tuple:\n", b)

# Creating a 3X4 array with all zeros 
c = np.zeros((3, 4))
print ("\nAn array initialized with all zeros:\n", c)

# Create a constant value array of complex type 
d = np.full((3, 3), 6, dtype = 'complex')
print ("\nAn array initialized with all 6s. \nArray type is complex:\n", d)

# Create an array with random values 
e = np.random.random((2, 2))
print ("\nA random array:\n", e)

# Create an array with random values 
e = np.random.random((2, 2))
print ("\nA random array:\n", e)

# Create a sequence of integers 
# from 0 to 30 with steps of 5
f = np.arange(0, 30, 5)
print ("\nA sequential array with steps of 5:\n", f)

# Create a sequence of 10 values in range 0 to 5 
g = np.linspace(0, 5, 10)
print ("\nA sequential array with 10 values between 0 and 5:\n", g)

# Reshaping 3X4 array to 2X2X3 array 
arr = np.array([[1, 2, 3, 4], [5, 2, 4, 2], [1, 2, 0, 1]])
newarr = arr.reshape(2, 2, 3)
print ("\nOriginal array:\n", arr)
print ("Reshaped array:\n", newarr)

# Flatten array
arr = np.array([[1, 2, 3], [4, 5, 6]]) 
flarr = arr.flatten()
print ("\nOriginal array:\n", arr) 
print ("Fattened array:\n", flarr)
print("----------------------------------------------------------------------------------")
print("")

print("Program 3:-")

a = np.array([[1, 4, 2], [3, 4, 6], [0, -1, 5]])

# sorted array
print ("Array elements in sorted order:\n", 
np.sort(a, axis = None))

# sort array row-wise
print ("Row-wise sorted array:\n", 
np.sort(a, axis = 1))

# specify sort algorithm
print ("Column wise sort by applying merge-sort:\n", 
np.sort(a, axis = 0, kind = 'mergesort'))

# Example to show sorting ofstructured array 
# set alias names for dtypes
dtypes = [('name', 'S10'), ('grad_year', int), ('cgpa', float)]

# Values to be put in array
values = [('Hrithik', 2009, 8.5), ('Ajay', 2008, 8.7), ('Pankaj', 2008, 7.9), ('Aakash', 2009, 9.0)]

# Creating array
arr = np.array(values, dtype = dtypes) 
print ("\nArray sorted by names:\n", np.sort(arr, order = 'name'))
print ("Array sorted by graduation year and then cgpa:\n", np.sort(arr, order = ['grad_year', 'cgpa']))