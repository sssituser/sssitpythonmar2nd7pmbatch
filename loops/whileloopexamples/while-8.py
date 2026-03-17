'''
Write a program  to find the factors of a given number
num = 8   factors = 1,2,4,8
'''
num = int(input('Enter number : '))
start = 1
end = num
while start<num:
    if num%start == 0:
        print(f'{start}',end=" ")
    start = start+1
