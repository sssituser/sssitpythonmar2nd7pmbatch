import numpy as numpy
matrix1 = numpy.array([
    [10,20],
    [30,40]
])

matrix2 = numpy.array([
    [11,22],
    [33,44]
])

print('============Matrix-1=====================')
for i in range(2):
    for j in range(2):
        print(matrix1[i][j],end="\t")
    print("\n")
print('=====================Matrix-2=========')
for i in range(2):
    for j in range(2):
        print(matrix2[i][j],end="\t")
    print("\n")
print('==========Sum of Matrix-1 and Matrix-2================')
for i in range(2):
    for j in range(2):
        print(matrix1[i][j]+matrix2[i][j],end="\t")
    print("\n")