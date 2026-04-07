'''
    Write Program to check given number is Adam
    Example :
    num = 12  square = 144
    num = 21  square = 441  reverse = 144
    
    
'''
def square(num:int):
    return num*num
def reverse(num:int):
    rev = 0
    while num>0:
        rev = rev*10+num%10
        num=num//10
    return rev
def isadam(num:int):
    return square(num)  == reverse(square(reverse(num)))

print(isadam(12))
print(isadam(10))
print(isadam(11))