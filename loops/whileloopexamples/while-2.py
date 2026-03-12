'''
Write a program to generate the number from 1 to given number
num = 5             1 2 3 4 5
num = 7             1 2 3 4 5 6 7 
'''
num = int(input('Enter a number : '))
start = 1
end = num
while start <= end:
    print(start,end=" ")
    start = start+1
