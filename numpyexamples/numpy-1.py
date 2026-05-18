import numpy as numpy
array = numpy.array([10,20,30,40])
print(array)
print(type(array))

# Reading the elements from the array
print(f'Elements Present in the array : {len(array)}')
print(array[0])
print(array[1])
print(array[2])
print(array[3])

print(array[-1],array[-2],array[-3],array[-4])
print(f'Displaying the elements using for loop')
for element in array:
    print(element)