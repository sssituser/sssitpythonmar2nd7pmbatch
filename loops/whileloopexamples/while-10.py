'''
Write a program to find the sum of the factors of given number
num = 8   sum = 1+2+4  sum = 7
num = 12  sum = 1+2+3+4+6 sum = 16
'''
num = int(input('Enter number : ')) # 4
start = 1
end = num
sum = 0
while start<end: 
    if num%start == 0: 
        sum = sum + start 
    start = start+1
print(f'{num} factors sum is {sum}')
if num == sum:
    print(f'{num} is Perfect number')
else:
    print(f'{num} is not a Perfect number')