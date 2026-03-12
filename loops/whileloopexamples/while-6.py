'''
Write a program to check given number is Armstrong
num = 153   1cube+5cube+3cube = 153
digits 1,5,3
count digit = 3
num = 1634  1pow4+6pow4+3pow4+4pow4
digits 1,6,3,4
count : 4

1.countdigits
2.separte the digits and find sum powervalues
3.compare number with sum of the  powervalues
'''
num = int(input('Enter number : '))
copy = num 
count = 0
while num>0: 
    digit = num%10 
    count += 1 
    num //= 10 
num = copy 
sum = 0
while num>0: 
    digit = num%10 
    sum += digit**count 
    num //= 10 
if copy==sum:
    print(f'{copy} is an Armstrong number')
else:
    print(f'{copy} is not an Armsrong number' )
