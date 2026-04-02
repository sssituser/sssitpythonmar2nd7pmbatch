'''
Write a program to check given number is Palidrome or not
num = 123   res : False
num = 121   res : True
'''
def reverse(num:int):
    rev = 0
    while num>0:
        rev = rev*10+num%10
        num//=10
    return rev
def ispalindrome(num:int):
    return num == reverse(num)

print(ispalindrome(122))
num = 121
print(f'{num} is Palindrome : {ispalindrome(num)}')
num = 123
print(f'{num} is Palindrome : {ispalindrome(num)}')