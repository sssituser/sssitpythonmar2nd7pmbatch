'''
Write a program to generate number from 1 to given number , in the below given order
num = 10    1 3 5 7 9
num = 15    1 4 7 10 13 
'''
num =int(input('Enter a number : '))
start = 1
end = num
while start <=end:
    print(start,end=" ")
    start = start+2
print('\n-------------------')
start = 1
while start<=end:
    print(start,end=" ")
    start = start+3    
    