# a = 2
# b = 3
# print(f'a = {a}\tb = {b}')
# a,b = b,a
# print(f'a = {a}\tb = {b}')

# x = 10
# y = 20
# print(f'x = {x}\ty = {y}')
# temp = x
# x = y
# y = temp

# print(f'x = {x}\ty = {y}')

# a = 10
# b = 20
# print(f'a = {a}\tb = {b}')
# a = a+b
# b = a-b
# a = a-b
# print(f'a = {a}\tb = {b}')


li = [5,8,1,4,7]
print("Elements Before sorting")
print(li)
n = len(li)
for i in range(n): # 0,1,2,3,4
    for j in range(0,n-i-1): #0,4 ,0,3 ,0,2,0,1,0,0
        if li[j]>li[j+1]:
            li[j],li[j+1] = li[j+1],li[j]
print("Elements after sorting")
print(li)

'''
li = [5,8,1,4,7]
i = 0
j = 0
j = 0   j = 1
5>8 - F no swap
j = 1 j+1 = 2
8>1 -T swap
[5,1,8,4,7]
j = 2 j+1 = 3
8>4-> T swap
[5,1,4,8,7]
j = 3 j+1 = 4
8>7-Tswap
[5,1,4,7,8]
j = 0  j+1 = 1
5>1 - T swap
[1,5,4,7,8]
j = 1 j+1 = 2
5>4-T swap
[1,4,5,7,8]
j = 2 j+1=3
4>7-F no swap
j = 0 j+1 = 1
1>4-F no swap
j = 0 j+1 = 1
1>4-F now swap
'''




