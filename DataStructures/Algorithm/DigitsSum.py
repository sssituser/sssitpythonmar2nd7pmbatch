'''
    Write a program to find the sum of the digits of given number
    Example :
    num = 123   sum = 1+2+3  sum = 6
    num = 456   sum = 4+5+6  sum =15
    Algorithm:
    1.input number : num
    2.Separate the digits : %10 repeatedly
    3.sum = 0, Add the digits to the sum = 0
    4.Reduce number num//10
    
    
'''
num = 123
sum = 0
while num>0: # 123>0 -T 12>0-T 1>0-T 0>0-F
    digit = num%10 # digit = 123%10 digit = 3 digit = 12%10 digit = 2 digit 1%10 digit = 1
    sum = sum+digit # sum = 3 sum = 5 sum = 6
    num = num//10 # num = 123//10 num = 12//10 num = 1//10 num = 0
print(f'Sum of the digit of a given number : {sum}')
    