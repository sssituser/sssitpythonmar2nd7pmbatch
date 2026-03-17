'''
Write program to find factors count of a given number
ex num = 8       8 has 3 factors
ex num = 12      12 has 5 factor
'''
num = int(input('Enter a number  : '))
count = 0
start = 1
end = num
while start<end:
    if num%start == 0:
        count+=1
    start+=1
print(f'{num} has {count} factors')