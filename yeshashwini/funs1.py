'''
Write a program to find the sum two numers
Paramters : two integers
functionname : add
'''

# def add(num1:int,num2:int): # function definion
#     return num1+num2

# x = add(4,5) # function calling
# print(x)


# def sub(num1:int,num2:int):
#     return num1-num2
# print(sub(5,2))
''''
Write a program to find the reverse of a given number
parameters : num1
'''
# def reverse(num:int):
#     rev = 0
#     while num>0:
#         rev = rev * 10 + num%10
#         num = num//10
#     return rev
# print(reverse(123))

'''
Write a program to find the factorial of a given number 
example 
num = 4   4! = 24
num = 5   5! = 120
parameter : num
function name : factorial
'''
# def factorial(num:int):
#     fact = 1
#     for i in range(1,num+1):
#         fact = fact * i
#     return fact
# print(factorial(5))
        
'''
    Write a progam to check given number is Palindrome or not
    num = 123   rev = 321 
    parameters : int
    funtionname : ispalindrome
'''

# def ispalindrome(num):
#     res = str(num)
#     return res==res[::-1]
# print(ispalindrome(123))
# print(ispalindrome("abc"))
# print(ispalindrome("madam"))
# print(ispalindrome("eye"))
# num = 153   1cube+5cube+3cube   153  Armstrong number
# num = 1634  1pow4+6pow4+3pow4+4pow4  1634

def isamrstrong(num:int):
    pow = len(str(num))
    sum = 0
    copy = num 
    while num>0: # num = 153 num = 15>0 1>0 0>0
        digit = num%10 # digit = 153%10 digit = 3 digit = 15%10  digit = 5 digit = 1%10 digit = 1
        sum = sum + digit**pow # sum = 152 sum = 153
        num = num//10 # num = 153//10 num = 15//10  num = 1//10 num = 0
    return copy==sum
print(isamrstrong(153))
print(isamrstrong(123))
print(isamrstrong(1634))


    