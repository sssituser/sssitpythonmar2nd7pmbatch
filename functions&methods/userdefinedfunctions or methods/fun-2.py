'''
Write a program to find the reverse given number
'''

def reverse(num:int):
    rev = 0
    while num>0:
        rev  = rev*10+num%10
        num//=10
    return rev
x = reverse(123)
print(f'x values is : {x}')
print(reverse(234))
print(f'reverse number is : {reverse(678)}')