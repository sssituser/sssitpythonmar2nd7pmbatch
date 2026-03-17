'''
range(start,stop,step)

range(1,11)=>1,2,3,4,5..10 default step is one
range(10,0,-1)
'''
for i in range(1,11):
    print(i,end="  ")

for i in range(-10,0):
    print(i,end=" ")
print("\n")
for i in range(-1,-11,-1):
    print(i)