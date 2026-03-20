'''
A
B   C
D   E   F
G   H   I   J
K   L   M   N   O
P   Q   R   S
T   U   V
W   X
Y
'''
num = 5
k = 1
for i in range(1,num+1):
    for j in range(1,i+1):
        print(f'{chr(96+k)}',end="\t")
        k+=1
    print()
for i in range(num-1,0,-1):
    for j in range(1,i+1):
        print(f'{chr(96+k)}',end="\t")
        k+=1
    print()
