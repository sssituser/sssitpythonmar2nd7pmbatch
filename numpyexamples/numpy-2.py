import numpy as numpy
array = numpy.array([
    [10,20,30],
    [40,50,60]
]
)

print(array)
print(array[0][0],array[0][1],array[0][2])
print(array[1][0],array[1][1],array[1][2])

print("Array elements using rows cols")
for i in range(0,2): # rows 0,1
    for j in range(0,3):
        print(array[i][j],end="\t")
    print()








