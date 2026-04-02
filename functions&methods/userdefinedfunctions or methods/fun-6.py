'''
find the factorial of a number

    4! is 24  1*2*3*4
    5! is 120 1*2*3*4*5
'''
def factorial(num:int): # num = 5
    fact = 1
    for i in range(1,num+1):
        fact = fact*i
    return fact
#--------------------------------
num = 5
print(f'{num}! is {factorial(num)}')

num = 4
print(f'{num}! is {factorial(num)}')

num = 8
print(f'{num}! is {factorial(num)}')

        
