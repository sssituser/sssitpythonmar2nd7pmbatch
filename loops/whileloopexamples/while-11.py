'''
Write a program to check the given number is prime or not
num =7   7 is a Prime number
num = 8  8 is not a Prime number
'''
num = int(input('Enter a number  : '))
start = 1
end = num
count = 0
while start<=num:
    if num%start == 0:
        count +=1
    start = start+1
if count == 2:
    print(f'{num} is Prime number')
else:
    print(f'{num} is not a Prime number')
