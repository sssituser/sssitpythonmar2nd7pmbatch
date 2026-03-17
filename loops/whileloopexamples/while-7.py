'''
Write program to check given number strong or not
num = 145       1!+4!+5!=>1+24+120=> 145
'''
num = 145
copy = num
fsum = 0
while num>0:
    digit = num%10 
    start = 1
    end = digit
    fact = 1
    while start <= end: 
        fact = fact*start 
        start = start+1 
    fsum = fsum+fact 
    num=num//10 
    if copy==fsum:
        print(f'{copy} is Strong number')
    else:
        print(f'{copy} is not strong number')